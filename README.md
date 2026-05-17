# Cristian Cardellino — Blog

Personal blog and notes of a Computer Scientist, built with [Pelican](https://getpelican.com/), a static site generator powered by Python. Deployed to [GitHub Pages](https://pages.github.com/).

## Tech Stack

- **Static Site Generator**: [Pelican](https://getpelican.com/)
- **Template Engine**: [Jinja2](https://jinja.palletsprojects.com/)
- **Markdown Processor**: [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/) with [Pygments](https://pygments.org/)
- **Math Rendering**: [MathJax](https://www.mathjax.org/)
- **Dependency Management**: [uv](https://docs.astral.sh/uv/)
- **Task Runner**: [duty](https://github.com/pawamoy/duty)
- **Python Linting/Formatting**: [Ruff](https://docs.astral.sh/ruff/)
- **CI/CD**: GitHub Actions

## Requirements

- Python >= 3.13
- [uv](https://docs.astral.sh/uv/) package manager

## Installation

```bash
# Clone the repository
git clone https://github.com/crscardellino/crscardellino.github.io.git
cd crscardellino.github.io

# Install dependencies
uv sync
```

## Development

### Quick Start

```bash
# Build the site
uv run duty build

# Start dev server with autoreload on http://localhost:4000
uv run duty devserver

# Clean build output
uv run duty clean
```

### Linting & Formatting

```bash
uv run duty lint
```

### Publishing

```bash
# Full pipeline: lint, build, verify, push
uv run duty push

# Build with production config (publishconf.py) - Run on Github Action
uv run duty publish
```

## Project Structure

```
.
├── content/                    # Source content
│   ├── posts/                  # Blog posts (Markdown)
│   ├── pages/                  # Static pages
│   ├── assets/                 # Images, PDFs, misc assets
│   ├── extra/                  # Extra static files (e.g., CNAME)
│   └── drafts/                 # Draft posts (not published)
├── themes/
│   └── crscardellino/          # Custom theme
│       ├── templates/          # Jinja2 templates
│       └── static/             # Static assets (CSS, JS, fonts)
│           ├── css/
│           ├── js/
│           ├── img/
│           ├── webfonts/
│           └── mathjax/
├── output/                     # Build output (gitignored)
├── pelicanconf.py              # Development configuration
├── publishconf.py              # Production configuration
├── pyproject.toml              # Python dependencies & tool config
├── duties.py                   # Task runner definitions
├── TODO.md                     # Refactoring plan
└── .github/workflows/
    └── pelican.yml             # GitHub Actions CI/CD
```

## Configuration

### Development vs Production

The project uses two separate configuration files:

| File | Purpose | `RELATIVE_URLS` | `DELETE_OUTPUT_DIRECTORY` | Plugins |
|------|---------|-----------------|---------------------------|---------|
| `pelicanconf.py` | Local development | `True` | `False` | Core plugins only |
| `publishconf.py` | Production builds | `False` | `True` | All plugins (sitemap, etc.) |

`publishconf.py` imports from `pelicanconf.py` and overrides production-specific settings.

### Key Settings

| Setting | Development | Production | Description |
|---------|-------------|------------|-------------|
| `SITEURL` | `https://crscardellino.net` | `https://crscardellino.net` | Base URL of the site |
| `PATH` | `content` | `content` | Source content directory |
| `OUTPUT_DIRECTORY` | `output` | `output` | Build output directory |
| `THEME` | `themes/crscardellino` | `themes/crscardellino` | Theme directory |
| `TIMEZONE` | `America/Argentina/Cordoba` | `America/Argentina/Cordoba` | Article date timezone |
| `RELATIVE_URLS` | `True` | `False` | Document-relative vs absolute URLs |
| `DELETE_OUTPUT_DIRECTORY` | `False` | `True` | Clean output before build |

### Markdown Extensions

The site uses PyMdown Extensions with the following features:

- **highlight**: Pygments syntax highlighting for code blocks
- **superfences**: Fenced code blocks with tabbed interfaces
- **arithmatex**: MathJax rendering for inline (`$...$`) and block (`$$...$$`) math
- **inlinehilite**: Inline code highlighting
- **mark**, **smartsymbols**, **tilde**, **saneheaders**, **keys**, **emoji**, **extra**: Standard text enhancements

### Plugins

| Plugin | Purpose | Configuration |
|--------|---------|---------------|
| `minchin.pelican.plugins.summary` | Article excerpts | `SUMMARY_END_MARKER`, `SUMMARY_MAX_PARAGRAPHS` |
| `neighbors` | Previous/next article navigation | Automatic |
| `readtime` | Reading time estimation | `READTIME_WPM = 180` |
| `tag_cloud` | Visual tag cloud | `TAG_CLOUD_STEPS = 4`, `TAG_CLOUD_SORTING = "alphabetically"` |
| `yaml_metadata` | YAML-style metadata in Markdown | Automatic |
| `sitemap` | XML sitemap generation | `SITEMAP` config (production only) |

### URL Patterns

| Content Type | URL Pattern | Output Path |
|--------------|-------------|-------------|
| Articles | `/{date:%Y}/{date:%m}/{date:%d}/{slug}` | `/{date:%Y}/{date:%m}/{date:%d}/{slug}.html` |
| Pages | `/{slug}` | `/{slug}/index.html` |
| Categories | `archive/category/{slug}/` | `archive/category/{slug}/index.html` |
| Tags | `archive/tag/{slug}/` | `archive/tag/{slug}/index.html` |
| Archives | `archive/` | `archive/index.html` |
| Yearly Archives | `archive/{date:%Y}/` | `archive/{date:%Y}/index.html` |
| Monthly Archives | `archive/{date:%Y}/{date:%m}/` | `archive/{date:%Y}/{date:%m}/index.html` |

## Writing Posts

### Post Metadata

Posts use Markdown with metadata at the top of the file:

```markdown
title: My Post Title
date: 2024-01-15 10:00
category: tech
tags:
  - python
  - pelican
```

### Excerpts

Use `<!-- more -->` to split the post into an excerpt and full content:

```markdown
This is the excerpt that appears on the homepage.

<!-- more -->

This is the full post content that only appears on the article page.
```

### Code Blocks

Use fenced code blocks with language tags for syntax highlighting:

````markdown
```python
print("Hello, world!")
```

```scala
object Main extends App {
  println("Hello, world!")
}
```
````

### Math

Use `$...$` for inline math and `$$...$$` for block math:

```markdown
The equation $E = mc^2$ is famous.

$$\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}$$
```

## Deployment

The site is automatically deployed to GitHub Pages via GitHub Actions when changes are pushed to the `master` branch.

### Manual Deploy

```bash
uv run duty push
```

This task:
1. Runs format and lint checks
2. Builds the site with `publishconf.py` for verification
3. Verifies the working tree is clean
4. Verifies the current branch is `main`
5. Pushes to the remote repository

### CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/pelican.yml`):
1. Checks out the repository
2. Sets up Python 3.13 and uv
3. Installs dependencies
4. Runs `uv run duty publish`
5. Deploys the `output/` directory to GitHub Pages

## Licensing

- **Code & Configuration**: All configuration files, build scripts, and custom themes in this repository are licensed under the [GNU Affero General Public License v3.0](LICENSE).
- **Content**: All written articles within the `content/` directory are licensed under the [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org) License. For any other content not created by the Blog's Author (Cristian Cardellino), refer to the source.

## Credits

- Built with [Pelican](https://getpelican.com/)
- Theme based on [Minima](https://github.com/jekyll/minima) (Jekyll)
- Icons from [Font Awesome](https://fontawesome.com/)
- Fonts: [Inconsolata](https://fonts.google.com/specimen/Inconsolata)
