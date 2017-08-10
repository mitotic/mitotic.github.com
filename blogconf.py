SITEURL = 'https://mitotic.github.io/blog'

AUTHOR = 'Saravanan'
#AUTHOR_SAVE_AS = False

SITENAME = 'mitotic.github.io/blog'
TIMEZONE = 'America/Chicago'
DEFAULT_DATE_FORMAT = '%b %d, %Y'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

DEFAULT_CATEGORY = 'general'
OUTPUT_PATH = 'blog'
DELETE_OUTPUT_DIRECTORY = True
ARTICLE_EXCLUDES = ("blog", "images", "pages", "static")
STATIC_PATHS = ["images", "static"]

REVERSE_ARCHIVE_ORDER = True
#THEME = '../pelican-themes/tuxlite_tbs'

#TYPOGRIFY = True
LINKS = [ #('Mitotic blog', 'http://blog.mitotic.org'),
        ]

DEFAULT_PAGINATION = 10
#FILES_TO_COPY = [('extra/CNAME', 'CNAME'), ('extra/robots.txt', 'robots.txt')]

DISQUS_SITENAME = 'codemindmeldr'
GOOGLE_ANALYTICS = 'UA-35342722-1'

SOCIAL = (
    ('GitHub', 'http://github.com/mitotic'),
    ('Twitter', 'http://twitter.com/rsarava'),
)

FEED_DOMAIN = SITEURL
TAG_FEED_ATOM = None
TAG_FEED_RSS = None

TWITTER_USERNAME = 'rsarava'
