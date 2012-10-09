SITEURL = 'http://code.mindmeldr.com/blog'

AUTHOR = 'Saravanan'
#AUTHOR_SAVE_AS = False

SITENAME = 'code.mindmeldr.com/blog'
TIMEZONE = 'America/Chicago'
DEFAULT_DATE_FORMAT = '%b %d, %Y'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

DEFAULT_CATEGORY = 'general'
OUTPUT_PATH = 'blog'
DELETE_OUTPUT_DIRECTORY = True
ARTICLE_EXCLUDES = ("blog", "images", "pages")
STATIC_PATHS = ["images"]

REVERSE_ARCHIVE_ORDER = True
#THEME = '../pelican-themes/tuxlite_tbs'

#TYPOGRIFY = True
LINKS = [ #('Mindmeldr blog', 'http://blog.mindmeldr.com'),
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
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_RSS = None

TWITTER_USERNAME = 'rsarava'
