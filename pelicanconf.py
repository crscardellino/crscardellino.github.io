# =============================================================================
# Site Specific Configurations
# =============================================================================

# Site identity
AUTHOR = "Cristian Cardellino"
SITENAME = "Cristian Cardellino"
SITEDESCRIPTION = "Notes of a Computer Scientist"
SITEURL = "https://crscardellino.net"

# Fediverse
MASTODON_HANDLE = "@crscardellino@mastodon.social"

# Social media links
SOCIAL = (
    ("mastodon", "https://mastodon.social/@crscardellino"),
    ("bluesky", "https://bsky.app/profile/crscardellino.bsky.social"),
    ("github", "https://github.com/crscardellino/"),
    ("linkedin", "https://linkedin.com/in/crscardellino/"),
)

# Author info
AUTHOR_IMAGE = "/assets/img/me.jpg"
LOGO = "/assets/img/logo.png"
COVER = "/assets/img/cover.jpg"
FAVICON = "/assets/img/favicon.png"

# =============================================================================
# Pelican Specific Configuration
# =============================================================================

# Source and language
PATH = "content"
DEFAULT_LANG = "en"

# Feed generation (disabled in development, enabled in publishconf.py)
FEED_ALL_RSS = None
RSS_FEED_SUMMARY_ONLY = True
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Use relative URLs for local development (overridden to False in publishconf.py)
RELATIVE_URLS = True

# URL patterns
ARTICLE_URL = "/{date:%Y}/{date:%m}/{date:%d}/{slug}"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
PAGE_URL = "/{slug}"
PAGE_SAVE_AS = "{slug}/index.html"

# Archiving
ARCHIVES_SAVE_AS = "archive/index.html"
YEAR_ARCHIVE_SAVE_AS = "archive/{date:%Y}/index.html"
MONTH_ARCHIVE_SAVE_AS = "archive/{date:%Y}/{date:%m}/index.html"

# Categories
CATEGORY_URL = "archive/category/{slug}/"
CATEGORY_SAVE_AS = "archive/category/{slug}/index.html"
CATEGORIES_SAVE_AS = "archive/categories/index.html"

# Tags
TAG_URL = "archive/tag/{slug}/"
TAG_SAVE_AS = "archive/tag/{slug}/index.html"
TAGS_SAVE_AS = "archive/tags/index.html"

# Direct templates (pages generated without content files)
DIRECT_TEMPLATES = ["index", "categories", "archives", "tags", "404"]

# Date formatting
DATE_FORMATS = {"en": "%b %d, %Y"}
TIMEZONE = "America/Argentina/Cordoba"

IGNORE_FILES = ["*.bak"]

# Theme
THEME = "themes/crscardellino"
THEME_STATIC_DIR = "assets"

# Show floating logo in top-left corner
FLOAT_LOGO = True

# Markdown processor
MARKDOWN = {
    "extension_configs": {
        "pymdownx.highlight": {
            "use_pygments": True,
            "noclasses": False,
            "pygments_style": "tango",
        },
        "pymdownx.superfences": {},
        "pymdownx.inlinehilite": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.tables": {},
        "markdown.extensions.footnotes": {},
        "markdown.extensions.attr_list": {},
    },
    "extension_names": [
        "pymdownx.highlight",
        "pymdownx.inlinehilite",
        "pymdownx.superfences",
        "pymdownx.arithmatex",
        "pymdownx.mark",
        "pymdownx.smartsymbols",
        "pymdownx.tilde",
        "pymdownx.saneheaders",
        "pymdownx.keys",
        "pymdownx.emoji",
        "pymdownx.extra",
    ],
    "output_format": "html5",
}

# Static files
STATIC_PATHS = ["assets", "extra/CNAME"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}

# Build output (False in development to keep output for quick rebuilds)
OUTPUT_DIRECTORY = "output"
DELETE_OUTPUT_DIRECTORY = False

# =============================================================================
# Plugin Specific Configuration
# =============================================================================

# Active plugins (sitemap added in publishconf.py for production)
PLUGINS = [
    "minchin.pelican.plugins.summary",
    "neighbors",
    "readtime",
    "tag_cloud",
    "yaml_metadata",
]

# --- Summary Plugin ---
SUMMARY_END_MARKER = "<!-- more -->"
SUMMARY_MAX_LENGTH = None
SUMMARY_MAX_PARAGRAPHS = 2

# --- Read Time Plugin ---
READTIME_WPM = 180

# --- Tag Cloud Plugin ---
TAG_CLOUD_STEPS = 4
TAG_CLOUD_SORTING = "alphabetically"
TAG_CLOUD_BADGE = False
