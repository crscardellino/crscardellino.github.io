#!/usr/bin/env python
"""Duty tasks for the project."""

import shutil
from pathlib import Path

from duty import duty, tools
from duty.context import Context
from pelican import main as pelican_main
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file("pelicanconf.py")
SETTINGS.update(LOCAL_SETTINGS)

OUTPUT_DIRECTORY = SETTINGS.get("OUTPUT_DIRECTORY", "_site")

run_pelican = tools.lazy(pelican_main, name="pelican.main")


@duty(capture=False)
def build(ctx: Context) -> None:
    """Build the site."""
    ctx.run(run_pelican(["-s", "pelicanconf.py", "-o", OUTPUT_DIRECTORY]))


@duty
def clean(ctx: Context) -> None:
    """Clean the _site directory."""
    site_dir = Path("output")
    if site_dir.is_dir():
        shutil.rmtree(site_dir)


@duty(capture=False)
def devserver(ctx: Context, port: int = 4000) -> None:
    """Start dev server with autoreload"""
    ctx.run(
        run_pelican(["-s", "pelicanconf.py", "-o", OUTPUT_DIRECTORY, "-r", "-l", "-p", f"{port}"])
    )
