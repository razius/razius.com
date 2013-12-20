#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site settings.
AUTHOR = u'Silviu Tantos'
AUTHOR_EMAIL = u'me@razius.com'
SITENAME = u'Silviu Tantos (razius)'
TAGLINE = 'Toying with the idea of becoming a useful member of society.'
SITEURL = ''
DEFAULT_DATE_FORMAT = ('%d-%m-%Y')

TIMEZONE = 'Europe/Copenhagen'

DEFAULT_LANG = u'en'
DEFAULT_METADATA = (
)

DELETE_OUTPUT_DIRECTORY = True

# Blogroll
LINKS =  (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('You can modify those links in your config file', '#'),
)

# Social widget.
SOCIAL = (
    ('Github', 'http://github.com/razius'),
    ('Last.fm', 'http://last.fm/user/razius'),
    ('Twitter', 'http://twitter.com/razius'),
    ('RSS', 'http://feeds.feedburner.com/razius'),
)

MENUITEMS = (
)

# Content path.
PATH = 'content'
PAGE_DIR = 'pages'
ARTICLE_DIR = 'articles'
STATIC_PATHS = ['images', 'files']
EXTRA_PATH_METADATA = {
    'robots.txt': {'path': 'robots.txt'},
}

# URL settings
ARTICLE_URL = ('articles/{slug}.html')
ARTICLE_SAVE_AS = ('articles/{slug}.html')
PAGE_URL = ('pages/{slug}.html')
PAGE_SAVE_AS = ('pages/{slug}.html')
# PAGINATION_PATTERNS = (
#     (1, '{base_name}/', '{base_name}/index.html'),
#     (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
# )
AUTHOR_SAVE_AS = False
PAGE_LANG_SAVE_AS = False

# Feed.
FEED_DOMAIN = SITEURL
# FEED_ALL_RSS = 'feeds/all.rss.xml'
# FEED_ALL_ATOM = 'feeds/all.atom.xml'

# Theme.
THEME = 'theme'
COVER_IMG_URL = '/images/cover.jpg'
DISQUS_SITENAME = 'razius'
TYPOGRIFY = True
# GOOGLE_ANALYTICS
DEFAULT_PAGINATION = 5

# Plugin.
PLUGIN_PATH = 'plugins'
PLUGINS = ['sitemap', 'gravatar']
PYGMENTS_RST_OPTIONS = {'cssclass': 'codehilite', 'linenos': 'table'}
