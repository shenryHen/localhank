#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hank Shen'
SITENAME = 'LocalHank'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# These correspond with article categories. Category and design svg must be the same name.
MENUITEMS = [
    ('memes', f"{SITEURL}/category/memes"),
    ('quote-lists', f"{SITEURL}/category/quote-lists"),
    ('designs', f"{SITEURL}/category/designs")
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('', ''))

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

THEME = 'scatter-plot'
THEME_STATIC_DIR = 'theme'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# For setting the favicon
STATIC_PATHS = [
    'extra',
]

EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'}}
