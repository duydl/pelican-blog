#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'duydl'
SITENAME = 'π-Radiant Archive'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Japan'

DEFAULT_LANG = 'en'

# OUTPUT_PATH = 'duydl.github.io/'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
USE_FOLDER_AS_CATEGORY = True
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git", "README.md"]
USE_CDN = True

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# Appearance
THEME = '_custom_theme'
DEFAULT_PAGINATION = False
PROGRESSBAR_COLOR = "blue"
# Plugins Settings

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    # 'neighbors',
    'render_math',
    'summary',
]


# DIRECT_TEMPLATES = (('index', 'blog', 'tags', 'categories', 'archives'))
# PAGINATED_DIRECT_TEMPLATES = (('blog',))