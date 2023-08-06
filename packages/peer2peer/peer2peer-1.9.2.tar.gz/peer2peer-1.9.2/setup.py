#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
setup(name='peer2peer',
      version='1.9.2',
      description='peer 2 peer',
      py_modules=['peer2peer'],
      url='https://bitbucket.org/val314159/peer2peer.git',
      scripts=['peer2peer.py'],
      license='MIT',
      platforms='any',
      install_requires=[
          'websocket-client',
          'gevent-websocket',
          'gevent','future','docopt'
          ],
)
