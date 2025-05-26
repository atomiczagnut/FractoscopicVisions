AUTHOR = 'Colin Trierweiler'
SITENAME = 'Fractoscopic Visions'
SITEURL = "http://localhost:8000"

PATH = "content"
THEME = "themes/my-theme"

TIMEZONE = 'America/Phoenix'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = True

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

PLUGINS = ['sitemap', 'neighbors']
SITEMAP = {
    'format': 'xml',
    'priorities': {'pages': 0.7, 'indexes': 0.5},
    'changefreqs': {'pages': 'weekly', 'indexes': 'weekly'}
}

CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True

PAGE_EXCLUDES = ['pages/404.md']
STATIC_PATHS = ['pages/404.md']
EXTRA_PATH_METADATA = {
    'pages/404.md': {'path': 'fractoscopic/404.html'}
}
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
