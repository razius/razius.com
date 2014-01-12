#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site settings.
AUTHOR = u'Silviu Tantos'
AUTHOR_EMAIL = u'me@razius.com'
SITENAME = u'Silviu Tantos (razius)'
TAGLINE = 'Toying with the idea of becoming a useful member of society.'
SITEURL = 'http://localhost:8000'
DEFAULT_DATE_FORMAT = ('%d-%m-%Y')

TIMEZONE = 'Europe/Copenhagen'

DEFAULT_LANG = u'en'
DEFAULT_METADATA = (
)

DELETE_OUTPUT_DIRECTORY = True

# Blogroll
LINKS = (
    ('asda', 'http://razius.com'),
)

# Social widget.
SOCIAL = (
    ('Github', 'http://github.com/razius'),
    ('Last.fm', 'http://last.fm/user/razius'),
    ('Twitter', 'http://twitter.com/razius'),
    ('PLUS', 'https://plus.google.com/+SilviuTantos?rel=author'),
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
    'files/github/.nojekyll': {'path': '.nojekyll'},
    'files/github/CNAME': {'path': 'CNAME'},
    'files/github/404.html': {'path': '404.html'},
    'files/github/README.md': {'path': 'README.md'},
    'files/robots.txt': {'path': 'robots.txt'},
    'images/favicon.ico': {'path': 'favicon.ico'},
}

# URL settings
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)
ARTICLE_URL = ('articles/{slug}/')
ARTICLE_SAVE_AS = ('articles/{slug}/index.html')
PAGE_URL = ('pages/{slug}/')
PAGE_SAVE_AS = ('pages/{slug}/index.html')
PAGE_LANG_SAVE_AS = False
TAG_URL = ('tag/{slug}/')
TAG_SAVE_AS = ('tag/{slug}/index.html')
TAGS_URL = ('tags/')
TAGS_SAVE_AS = None
CATEGORY_URL = ('category/{slug}/')
CATEGORY_SAVE_AS = ('category/{slug}/index.html')
AUTHOR_SAVE_AS = False

# Feed.
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None

# Theme.
THEME = 'theme'
# COVER_IMG_URL = '/images/cover.jpg'
COVER_BG_COLOR = '#375152'
TYPOGRIFY = True
DEFAULT_PAGINATION = 10

# Plugin.
PLUGIN_PATH = 'plugins'
PLUGINS = ['gzip_cache', 'assets', 'optimize_images', 'sitemap', 'gravatar', 'pelican_youtube']
PYGMENTS_RST_OPTIONS = {'cssclass': 'codehilite', 'linenos': 'table'}

# Sitemap.
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'pages': 0.9,
        'indexes': 0.8,
    },
    'changefreqs': {
        'indexes': 'daily',
        'articles': 'daily',
        'pages': 'weekly'
    }
}

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = False
