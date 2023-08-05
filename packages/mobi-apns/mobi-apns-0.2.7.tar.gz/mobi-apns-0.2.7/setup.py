from setuptools import setup
from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name = 'mobi-apns',
    packages = [
        'mobi',
        'mobi.apns'
    ],
    python_requires='>=3.5',
    version = '0.2.7',
    description = 'A library for interacting with APNs using HTTP/2 and token-based authentication.',
    long_description=readme,
    long_description_content_type='text/x-rst',
    license=license,
    author = 'Sören Busch, Gene Sluder',
    author_email = 'sbusch@mobivention.com',
    url = 'https://bitbucket.org/mobivention/mobi-apns/',
    download_url = 'https://bitbucket.org/mobivention/mobi-apns/get/0.2.7.zip',
    keywords = [
        'apns',
        'push notifications',
    ],
    classifiers = [],
    install_requires=[
        'cryptography',
        'hyper',
        'pyjwt',
    ],
    project_urls={  # Optional
        'Bug Reports': 'https://bitbucket.org/mobivention/mobi-apns/issues',
        'Source': 'https://bitbucket.org/mobivention/mobi-apns/',
        'Company Home': 'https://www.mobivention.com'
    }
)
