import importlib
import json
import jwt
import time
import uuid

from collections import namedtuple
from contextlib import closing
from hyper import HTTP20Connection
from typing import Optional, List, Mapping
from .exceptions import (
    InternalException,
    ImproperlyConfigured,
    PayloadTooLarge,
    BadDeviceToken,
    PartialBulkMessage
)

from .utils import validate_private_key, wrap_private_key


ALGORITHM = 'ES256'
SANDBOX_HOST = 'api.development.push.apple.com:443'
PRODUCTION_HOST = 'api.push.apple.com:443'
MAX_NOTIFICATION_SIZE = 4096

APNS_RESPONSE_CODES = {
    'Success': 200,
    'BadRequest': 400,
    'TokenError': 403,
    'MethodNotAllowed': 405,
    'TokenInactive': 410,
    'PayloadTooLarge': 413,
    'TooManyRequests': 429,
    'InternalServerError': 500,
    'ServerUnavailable': 503,
}
APNSResponseStruct = namedtuple('APNSResponseStruct', ' '.join(APNS_RESPONSE_CODES.keys()))
APNSResponse = APNSResponseStruct(**APNS_RESPONSE_CODES)

class APNsMessage:
    
    alert = "" # type: str
    badge = None # type: Optional[int]
    sound = None # type: Optional[str]
    category = None # type: Optional[str]
    content_available = None # type: Optional[bool]
    mutable_content = None # type: Optional[bool]
    action_loc_key = None # type: Optional[str]
    loc_key = None # type: Optional[str]
    loc_args = [] # type: List[str]
    extra = {} # type: dict
    identifier = None # type: Optional[str]
    expiration = None # type: Optional[int]
    priority = 10 # type: int

    def __init__(self,
                 alert: str,
                 badge: Optional[int] = None,
                 sound: Optional[str] = None,
                 category: Optional[str] = None,
                 content_available: Optional[bool] = False,
                 mutable_content: Optional[bool] = False,
                 action_loc_key: Optional[str] = None,
                 loc_key: Optional[str] = None,
                 loc_args: List[str] = [],
                 extra: dict = {},
                 identifier: Optional[str] = None,
                 expiration: Optional[int] = None,
                 priority: int = 10):

        self.alert = alert
        self.badge = badge
        self.sound = sound
        self.category = category
        self.content_available = content_available
        self.mutable_content = mutable_content
        self.action_loc_key = action_loc_key
        self.loc_key = loc_key
        self.loc_args = loc_args
        self.extra = extra
        self.identifier = identifier
        self.expiration = expiration
        self.priority = priority

class APNsClient(object):

    def __init__(self,
                 team_id: str,
                 auth_key_id: str,
                 auth_key: Optional[str] = None,
                 auth_key_filepath: Optional[str] = None,
                 bundle_id: Optional[str] = None,
                 use_sandbox: bool = False,
                 force_proto: Optional[bool] = None,
                 wrap_key: bool = False
                 ):

        if not (auth_key_filepath or auth_key):
            raise ImproperlyConfigured(
                'You must provide either an auth key or a path to a file containing the auth key'
            )

        if not auth_key:
            try:
                with open(auth_key_filepath, "r") as f:
                    auth_key = f.read()

            except Exception as e:
                raise ImproperlyConfigured("The APNS auth key file at %r is not readable: %s" % (auth_key_filepath, e))

        validate_private_key(auth_key)
        if wrap_key:
            auth_key = wrap_private_key(auth_key) # Some have had issues with keys that aren't wrappd to 64 lines

        self.team_id = team_id
        self.bundle_id = bundle_id
        self.auth_key = auth_key
        self.auth_key_id = auth_key_id
        self.force_proto = force_proto
        self.host = SANDBOX_HOST if use_sandbox else PRODUCTION_HOST

    def send_message(self,
                     registration_id: str,
                     message: APNsMessage,
                     topic: Optional[str] = None,
                     bundle_id: Optional[str] = None
                     ):
        if not (topic or bundle_id or self.bundle_id):
            raise ImproperlyConfigured(
                'You must provide your bundle_id if you do not specify a topic'
            )

        json_data = self._create_json_payload(message)

        request_headers = self._create_headers(bundle_id, topic, message)
        return self._send_message(registration_id, json_data, request_headers)

    def send_bulk_message(self,
                          registration_ids: List[str],
                          message: APNsMessage,
                          topic: Optional[str] = None,
                          bundle_id: Optional[str] = None
                          ):
        if not (topic or bundle_id or self.bundle_id):
            raise ImproperlyConfigured(
                'You must provide your bundle_id if you do not specify a topic'
            )

        json_data = self._create_json_payload(message)

        request_headers = self._create_headers(bundle_id, topic, message)
        good_registration_ids = []
        bad_registration_ids = []

        res = None
        with closing(self._create_connection()) as connection:
            for registration_id in registration_ids:
                try:
                    res = self._send_message(registration_id, json_data, request_headers, connection=connection)
                    good_registration_ids.append(registration_id)
                except:
                    bad_registration_ids.append(registration_id)

        if not bad_registration_ids:
            return res

        if not good_registration_ids:
            raise BadDeviceToken("None of the registration ids were accepted"
                                 "Rerun individual ids with ``send_message()``"
                                 "to get more details about why")

        if bad_registration_ids and good_registration_ids:
            raise PartialBulkMessage(
                "Some of the registration ids were accepted. Rerun individual "
                "ids with ``send_message()`` to get more details about why. "
                "The ones that failed: \n:"
                "{bad_string}\n"
                "The ones that were pushed successfully: \n:"
                "{good_string}\n".format(
                    bad_string="\n".join(bad_registration_ids),
                    good_string = "\n".join(good_registration_ids)
                ),
                bad_registration_ids
            )

    def _create_connection(self) -> HTTP20Connection:
        return HTTP20Connection(self.host, force_proto=self.force_proto)

    def _create_token(self):
        token = jwt.encode(
            {
                'iss': self.team_id,
                'iat': time.time()
            },
            self.auth_key,
            algorithm= ALGORITHM,
            headers={
                'alg': ALGORITHM,
                'kid': self.auth_key_id,
            }
        )
        return token.decode('ascii')

    def _send_message(self,
                      registration_id: str,
                      json_payload: str,
                      request_headers: Mapping[str, str],
                      connection: Optional[HTTP20Connection] = None):
        if connection:
            response = self._send_push_request(connection, registration_id, json_payload, request_headers)
        else:
            with closing(self._create_connection()) as connection:
                response = self._send_push_request(connection, registration_id, json_payload, request_headers)

        return response

    def _create_headers(self,
                        bundle_id: Optional[str],
                        topic: Optional[str],
                        message: APNsMessage) -> Mapping[str, str]:
        # If expiration isn't specified use 1 month from now
        expiration_time = message.expiration if message.expiration is not None else int(time.time()) + 2592000
        auth_token = self._create_token()
        if not topic:
            topic = bundle_id if bundle_id else self.bundle_id
        request_headers = {
            'apns-expiration': str(expiration_time),
            'apns-priority': str(message.priority),
            'apns-topic': topic,
            'authorization': 'bearer {0}'.format(auth_token)
        }
        if not message.identifier:
            message.identifier = uuid.uuid4()
        request_headers['apns-id'] = str(message.identifier)
        return request_headers

    def _create_json_payload(self, message: APNsMessage) -> str:
        data = {}
        aps_data = {}
        if message.action_loc_key or message.loc_key or message.loc_args:
            alert = {"body": message.alert} if message.alert else {}
            if message.action_loc_key:
                alert["action-loc-key"] = message.action_loc_key
            if message.loc_key:
                alert["loc-key"] = message.loc_key
            if message.loc_args:
                alert["loc-args"] = message.loc_args
        if message.alert is not None:
            aps_data["alert"] = message.alert
        if message.badge is not None:
            aps_data["badge"] = message.badge
        if message.sound is not None:
            aps_data["sound"] = message.sound
        if message.category is not None:
            aps_data["category"] = message.category
        if message.content_available:
            aps_data["content-available"] = 1
        if message.mutable_content:
            aps_data["mutable-content"] = 1
        data["aps"] = aps_data
        data.update(message.extra)
        # Convert to json, avoiding unnecessary whitespace with separators (keys sorted for tests)
        json_data = json.dumps(data, separators=(",", ":"), sort_keys=True).encode("utf-8")

        if len(json_data) > MAX_NOTIFICATION_SIZE:
            raise PayloadTooLarge("Notification body cannot exceed %i bytes" % (MAX_NOTIFICATION_SIZE))

        return json_data

    def _send_push_request(self,
                           connection: HTTP20Connection,
                           registration_id: str,
                           json_data: str,
                           request_headers: Mapping[str, str]):
        connection.request(
            'POST',
            '/3/device/{0}'.format(registration_id),
            json_data,
            headers=request_headers
        )
        response = connection.get_response()

        if response.status != APNSResponse.Success:
            identifier = response.headers['apns-id']
            body = json.loads(response.read().decode('utf-8'))
            reason = body["reason"] if "reason" in body else None

            if reason:
                exceptions_module = importlib.import_module("mobi.apns.exceptions")
                ExceptionClass = None
                try:
                    ExceptionClass = getattr(exceptions_module, reason)
                except AttributeError:
                    ExceptionClass = InternalException
                raise ExceptionClass()

        return True

