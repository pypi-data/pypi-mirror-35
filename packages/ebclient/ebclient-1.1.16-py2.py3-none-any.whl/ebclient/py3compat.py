#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Enigma Bridge Ltd'

from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError


def parse_url(url):
    return urlparse(url)