from pelicanconf import *  # noqa: F403

# =============================================================================
# Production Overrides
# =============================================================================

# Use absolute URLs in production
RELATIVE_URLS = False

# Ignore drafts
IGNORE_FILES = IGNORE_FILES + ["drafts"]  # noqa: F405

# Enable RSS feed for production
FEED_ALL_RSS = "feed.xml"

# Enable sitemap plugin for production (includes sitemap in PLUGINS)
PLUGINS = PLUGINS + ["sitemap"]  # noqa: F405

# Delete output directory before production build
DELETE_OUTPUT_DIRECTORY = True

# =============================================================================
# Sitemap Plugin Configuration (production only)
# =============================================================================

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
