#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#site&information setting configuration
AUTHOR = u'cnewbie'
SITENAME = u"cnewbie's 	 blog"
SITEURL = 'https://cnewbie.github.io'
SITEMAP_SAVE_AS = 'sitemap.xml'
#DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
##date&lang related configuration
TIMEZONE = 'Asia/Hong_Kong'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%Y %B %d %a'
DEFAULT_LANG = u'zh'

## url & save location configuration

#input folder
PATH = 'content'
ARTICLE_PATHS = ['blog']
#article
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_URL = 'posts/{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}-{lang}.html'

#drafts
DRAFT_URL = 'drafts/{date:%Y}/{date:%m}/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{date:%Y}/{date:%m}/{slug}.html'
DRAFT_LANG_URL = 'drafts/{date:%Y}/{date:%m}/{slug}-{lang}.html'
DRAFT_LANG_SAVE_AS = 'drafts/{date:%Y}/{date:%m}/{slug}-{lang}.html'

#page
PAGE_URL = 'others/pages/{slug}.html'
PAGE_SAVE_AS = 'others/pages/{slug}.html'
PAGE_LANG_URL = 'others/pages/{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = 'others/pages/{slug}-{lang}.html'

#categroy
CATEGORIES_SAVE_AS ='others/category/index.html'
CATEGORY_URL = 'others/category/{slug}.html'
CATEGORY_SAVE_AS = 'others/category/{slug}.html'

#archives
ARCHIVES_URL = 'posts/index.html'
ARCHIVES_SAVE_AS = 'posts/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

#author
AUTHORS_SAVE_AS = 'others/author/index.html'
AUTHOR_URL = 'others/author/{slug}.html'
AUTHOR_SAVE_AS = 'others/author/{slug}.html'

#tags
TAGS_SAVE_AS = 'others/tag/index.html'
TAG_URL = 'others/tag/{slug}.html'
TAG_SAVE_AS = 'others/tag/{slug}.html'

#TEMPLATE_PAGES = {'src/books.html': 'dest/books.html',}


## menuitems configuration
#DISPLAY_CATEGORIES_ON_MENU = False
#DISPLAY_PAGES_ON_MENU = False
#menu items

#MENUITEMS = (('Home', '/index.html'),('About', '/pages/about.html'),)




#static path configuration
STATIC_PATHS = ['images', 'extra/robots.txt']
STATIC_EXCLUDES = ['.DS_Store']

EXTRA_PATH_METADATA = {'images/favicon.ico': {'path': 'favicon.ico'},
	'extra/robots.txt': {'path': 'robots.txt'},
}

#plugin configuration
PLUGIN_PATHS = ['plugins']
PLUGINS = [ 'liquid_tags','i18n_subsites', 'tag_cloud', 'assets',
'footer_insert','related_posts','sitemap','render_math']
#JINJA_EXTENSIONS = ['jinja2.ext.i18n']
JINJA_ENVIRONMENT = {'extensions':['jinja2.ext.i18n']}
SITEMAP = {
    'format': 'xml',
}
#MATH_JAX = {'color':'blue','align':left}

##theme configuration
THEME = 'themes/pelican-bootstrap3'
#THEME = 'themes/voidy-bootstrap'
GITHUB_URL = 'https://github.com/cnewbie'
OUTPUT_RETENTION = [".git", ".bzr"]
##pelican-bootstrap3
#RELATED_POSTS_SKIP_SAME_CATEGORY = True
#RELATED_POSTS_MAX = 10
CC_LICENSE = 'CC-BY-SA'
##voidy-bootstrap
#SITESUBTITLE ='Coding Life'
#SITETAG = "Text that's displayed in the title on the home page."
#CUSTOM_ARTICLE_FOOTERS = ("taglist.html", )
#CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
#CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"
#SIDEBAR = "sidebar.html"
#STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css",)
#CUSTOM_SIDEBAR_MIDDLES = ( "sb_tagcloud.html",)
#CUSTOM_SIDEBAR_MIDDLES = ( "sb_taglist.html",)
#TAG_CLOUD_BADGE = 'True'
#SOCIAL = (('GitHub', 'http://github.com/cnewbie','fa fa-github-square fa-fw fa-lg'),)



# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),       )

# Social widget
SOCIAL = (('Github', 'https://github.com/cnewbie'),  )


# Feed generation is usually not desired when developing

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
