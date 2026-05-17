#!/usr/bin/env python
# -*- coding: utf-8 -*-

AUTHOR = "Cristian Cardellino"
SITENAME = "Cristian Cardellino"
SITEDESCRIPTION = "Notes of a Computer Scientist"
SITEURL = "https://crscardellino.net"

PATH = "content"

DEFAULT_LANG = "en"

# Feed generation
FEED_ALL_RSS = "feed.xml"
RSS_FEED_SUMMARY_ONLY = True

# URL settings
ARTICLE_URL = "/{date:%Y}/{date:%m}/{date:%d}/{slug}"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
PAGE_URL = "/{slug}"
PAGE_SAVE_AS = "{slug}/index.html"

# Archiving
ARCHIVES_SAVE_AS = "archive/index.html"
YEAR_ARCHIVE_SAVE_AS = "archive/{date:%Y}/index.html"
MONTH_ARCHIVE_SAVE_AS = "archive/{date:%Y}/{date:%m}/index.html"

CATEGORY_URL = "archive/category/{slug}/"
CATEGORY_SAVE_AS = "archive/category/{slug}/index.html"
CATEGORIES_SAVE_AS = "archive/categories/index.html"

TAG_URL = "archive/tag/{slug}/"
TAG_SAVE_AS = "archive/tag/{slug}/index.html"
TAGS_SAVE_AS = "archive/tags/index.html"


DIRECT_TEMPLATES = ["index", "categories", "archives", "tags", "404"]

AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DATE_FORMATS = {"en": "%b %d, %Y"}
TIMEZONE = "America/Argentina/Cordoba"

# Theme
THEME = "themes/crscardellino"
THEME_STATIC_DIR = "assets"

# Markdown extensions
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
    ],
    "output_format": "html5",
}

# Static files
STATIC_PATHS = ["assets", "extra/CNAME"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}

# Social links
MASTODON_HANDLE = "@crscardellino@mastodon.social"
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

# Delete output directory before building
OUTPUT_DIRECTORY = "output"
DELETE_OUTPUT_DIRECTORY = True

# Logo float
FLOAT_LOGO = True

# Plugins
PLUGINS = [
    "minchin.pelican.plugins.summary",
    "neighbors",
    "readtime",
    "sitemap",
    "tag_cloud",
    "yaml_metadata",
]

# Read Time
READTIME_WPM = 180

# Summary
SUMMARY_END_MARKER = "<!-- more -->"
SUMMARY_MAX_LENGTH = None
SUMMARY_MAX_PARAGRAPHS = 2

# Sitemap config
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.8,
        "indexes": 0.3,
        "pages": 0.5,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "monthly",
        "pages": "monthly",
    },
}

# Tag Cloud
TAG_CLOUD_STEPS = 4
TAG_CLOUD_SORTING = "alphabetically"
TAG_CLOUD_BADGE = False
