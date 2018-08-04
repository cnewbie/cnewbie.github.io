#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'cnewbie'
SITENAME = "cnewbie's Blog"
SITEURL = 'https://cnewbie.github.io'

PATH = 'content'


# basic config
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Tech'
IGNORE_FILES = ['.#*', '.*' ]
# MARKDOWN = {
#     'extension_configs': {
#         'markdown.extensions.codehilite': {'css_class': 'highlight'},
#         'markdown.extensions.extra': {},
#         'markdown.extensions.meta': {},
#         'markdown.extensions.toc': {},
#     },
#     'output_format': 'html5',
#     'lazy_ol': False,  # See: https://pythonhosted.org/Markdown/reference.html#lazy_ol
# }


# path config
ARTICLE_PATHS = ['blog']
PLUGIN_PATHS = ['plugins']
STATIC_PATHS = ['images', 'static',]
PLUGINS = ['i18n_subsites',
            'tag_cloud',
            'sitemap',
            'tipue_search',
#            'render_math',
            'readtime',
            'pandoc_reader',
            ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n', ],
}
PANDOC_ARGS = [
  '--standalone',
  '--mathjax',
  '--toc',
  '--toc-depth=2',
#  '--number-sections',
]

PANDOC_EXTENSIONS = [
  '+smart',
  '+hard_line_breaks',
  '-citations',
#  '+mmd_title_block',
  '+tex_math_dollars',
]

# URL config
INDEX_STRING = 'index.html'
BLOG_URL = 'blog/'
ARCHIVES_URL = 'blog/'
CATEGORIES_URL = 'categories/'
TAGS_URL = 'tags/'

ARTICLE_URL = BLOG_URL + '{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + INDEX_STRING
ARTICLE_LANG_URL = BLOG_URL + '{date:%Y}/{slug}-{lang}/'
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL + INDEX_STRING
DRAFT_URL = 'drafts/{slug}/'
DRAFT_SAVE_AS = DRAFT_URL + INDEX_STRING
DRAFT_LANG_URL = 'drafts/{slug}-{lang}/'
DRAFT_LANG_SAVE_AS = DRAFT_LANG_URL + INDEX_STRING
#PAGE_URL = 'pages/{slug}/'
#PAGE_SAVE_AS = PAGE_URL + INDEX_STRING
#PAGE_LANG_URL = 'pages/{slug}-{lang}/'
#PAGE_LANG_SAVE_AS = PAGE_LANG_URL + INDEX_STRING
CATEGORY_URL = CATEGORIES_URL + '{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + INDEX_STRING
TAG_URL = TAGS_URL + '{slug}/'
TAG_SAVE_AS = TAG_URL + INDEX_STRING

AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
YEAR_ARCHIVE_SAVE_AS = BLOG_URL + '{date:%Y}/' + INDEX_STRING
ARCHIVES_SAVE_AS = BLOG_URL + INDEX_STRING
CATEGORIES_SAVE_AS = CATEGORIES_URL + INDEX_STRING
TAGS_SAVE_AS = TAGS_URL + INDEX_STRING



# locale config
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'zh'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%Y %b %d'
DIRECT_TEMPLATES = ['index', 'tags',
                    'categories',
                    'archives',
                    'search',
                    ]
# metadate config
EXTRA_PATH_METADATA = {'images/favicon.ico': {'path': 'favicon.ico'},
	'static/robots.txt': {'path': 'robots.txt'},
}



# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Pagination config
DEFAULT_PAGINATION = 10


# Themes

#THEME = 'themes/pelican-twitchy'
THEME = 'themes/pelican-bootstrap3'
SHOW_DATE_MODIFIED = True
#PYGMENTS_STYLE = 'solarizeddark'
USE_PAGER = True
SIDEBAR_ON_LEFT = True
#DISPLAY_TOC_ON_SIDEBAR = True
#SEARCH_URL = '/pages/search.html'
#MAIN_MENU = True
#MENUITEMS = (
#            ('Archives', '/' + ARCHIVES_URL),
#            ('Categories','/' + CATEGORIES_URL),
#             ('Tags','/' + TAGS_URL),
#            )

GITHUB_URL = 'https://github.com/cnewbie'
# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/cnewbie'),)


CC_LICENSE = 'CC-BY-SA'
SITEMAP = {
    'format': 'xml',
}
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
