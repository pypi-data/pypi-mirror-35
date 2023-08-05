from setuptools import setup
import sys

VERSION = '0.2.1'

LONG_DESCRIPTION="""
A duplicate of PythonPusherClient (https://github.com/ekulyk/PythonPusherClient) for
use with the Gryphon trading framework. All credit to the original author.
"""

if sys.version_info >= (3,):
    requirements = ['websocket-client-py3']
else:
    requirements = ['websocket-client']

setup(
    name='gryphon-pusherclient',
    version=VERSION,
    description='Pusher websocket client for python',
    long_description=LONG_DESCRIPTION,
    author='MacLeod & Robinson',
    author_email='hello@tinkercoin.com',
    url='https://github.com/TinkerWork/PythonPusherClient',
    install_requires=requirements,
    packages=['pusherclient'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
    ]
)
