#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup


VERSION = '0.3.1'
URL = 'https://github.com/operasoftware/twisted-gcmclient'
DOWNLOAD_URL = URL + '/tarball/' + VERSION


setup(
  name='twisted-gcmclient',
  packages=['gcmclient'],
  version=VERSION,
  description='Twisted client for Google Cloud Messaging (GCM)',
  author='Michał Łowicki',
  author_email='mlowicki@opera.com',
  url=URL,
  download_url=DOWNLOAD_URL,
  keywords=['twisted', 'gcm', 'fcm'],
  classifiers=[],
  install_requires=['Twisted', 'treq']
)
