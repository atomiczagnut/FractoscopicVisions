# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://fractoscopicvisions.com"
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

THEME = 'themes/my-theme'
STATIC_PATHS = ['pages/404.md', '.htaccess', 'robots.txt', 'img']
EXTRA_PATH_METADATA = {
    'pages/404.md': {'path': 'fractoscopic/404.html'},
    '.htaccess': {'path': 'fractoscopic/.htaccess'},
    'robots.txt': {'path': 'fractoscopic/robots.txt'}
}

