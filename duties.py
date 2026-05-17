#!/usr/bin/env python
"""Duty tasks for the project."""

import shutil
from pathlib import Path

from duty import duty, tools, Context
from pelican import main as pelican_main
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file("pelicanconf.py")
SETTINGS.update(LOCAL_SETTINGS)

OUTPUT_DIRECTORY = SETTINGS.get("OUTPUT_DIRECTORY", "output")

run_pelican = tools.lazy(pelican_main, name="pelican.main")


@duty(capture=False)
def build(ctx: Context) -> None:
    """Run the site linting, and builds it"""
    clean(ctx)
    ctx.run(["ruff", "format", "--check", "."])
    ctx.run(["ruff", "check", "."])
    ctx.run(run_pelican(["-s", "pelicanconf.py", "-o", OUTPUT_DIRECTORY]))


@duty(capture=False)
def clean(ctx: Context) -> None:
    """Clean the _site directory."""
    site_dir = Path(OUTPUT_DIRECTORY)
    if site_dir.is_dir():
        shutil.rmtree(site_dir)


@duty(capture=False)
def devserver(ctx: Context) -> None:
    """Start dev server with autoreload"""
    ctx.run(run_pelican(["-s", "pelicanconf.py", "-o", OUTPUT_DIRECTORY, "-r", "-l", "-p", "4000"]))


@duty(capture=False)
def lint(ctx: Context) -> None:
    """Run formating and linting for fixing"""
    ctx.run(["ruff", "format", "."])
    ctx.run(["ruff", "check", "--fix", "."])


@duty
def pygments(ctx: Context, style: str = "tango") -> None:
    """Generates the correct pygments"""
    with open("./themes/crscardellino/static/css/pygments.css", "wt") as fh:
        css = ctx.run(["pygmentize", "-S", style, "-f", "html", "-a", ".highlight"])
        fh.write(css)
    ctx.run(
        "sed -i "
        rf"""'s/"pygments_style":\s*"[^"]*",/"pygments_style": "{style}",/' """
        "./pelicanconf.py"
    )
