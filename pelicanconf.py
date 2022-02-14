#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import sys, os
syspath = syspath =  ["E:/Projects/pelican_dev",
                      "E:/Projects/pelican_dev/pelican-jupyter",
                      "E:/Projects/pelican_dev/liquid-tags/pelican/plugins"]
sys.path.extend(syspath)


AUTHOR = 'duydl'
SITENAME = 'π-Radiant Archive'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Japan'

DEFAULT_LANG = 'en'

# OUTPUT_PATH = 'duydl.github.io/'
STATIC_PATHS = []

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
THEME = 'themes/pelican-bootstrap3' # 'themes/pelican-attila'
DEFAULT_PAGINATION = False
PROGRESSBAR_COLOR = "blue"

# Plugins Settings

# PLUGIN_PATHS = ['plugins']
import liquid_tags
from pelican_jupyter import liquid as nb_liquid
from plugins import render_math, i18n_subsites


PLUGINS = [ nb_liquid, 
           liquid_tags, 
           i18n_subsites, 
           render_math, 
           ]

MARKUP = ("md", "ipynb")
IPYNB_MARKUP_USE_FIRST_CELL = True
IGNORE_FILES = [".ipynb_checkpoints"]

LIQUID_CONFIGS = (("IPYNB_FIX_CSS", "False", ""), 
                  ("IPYNB_SKIP_CSS", "False", ""), 
                  ("IPYNB_EXPORT_TEMPLATE", "base", ""),)


JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

MATHJAX = {'process_summary': True, }


MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
# DIRECT_TEMPLATES = (('index', 'blog', 'tags', 'categories', 'archives'))
# PAGINATED_DIRECT_TEMPLATES = (('blog',))

