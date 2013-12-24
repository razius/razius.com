#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://razius.com'
FEED_DOMAIN = SITEURL
RELATIVE_URLS = False

ARTICLE_EXCLUDES = ('drafts',)

# Following items are often useful when publishing

DISQUS_SITENAME = 'razius'
GOOGLE_ANALYTICS = 'UA-29024708-1'
