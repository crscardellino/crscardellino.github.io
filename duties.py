#!/usr/bin/env python
"""Duty tasks for the project."""

from duty import duty, tools, Context
from pelican import main as pelican_main
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file("pelicanconf.py")
SETTINGS.update(LOCAL_SETTINGS)

OUTPUT_DIRECTORY = SETTINGS.get("OUTPUT_DIRECTORY", "output")

run_pelican = tools.lazy(pelican_main, name="pelican.main")


def _clean(ctx: Context) -> None:
    ctx.run(["rm", "-rf", OUTPUT_DIRECTORY])


def _ruff_format(ctx: Context, fix: bool = False) -> None:
    command = ["ruff", "format", "."]
    if not fix:
        command.append("--check")
    ctx.run(command)


def _ruff_lint(ctx: Context, fix: bool = False) -> None:
    command = ["ruff", "check", "."]
    if fix:
        command.append("--fix")
    ctx.run(command)


@tools.lazy(name="duty.setup")
def setup(ctx: Context, fix: bool = False) -> None:
    _clean(ctx)
    _ruff_format(ctx, fix)
    _ruff_lint(ctx, fix)


@duty(capture=False)
def build(ctx: Context) -> None:
    """Run the site linting, and builds it"""
    ctx.run(setup(ctx, False), silent=True)
    ctx.run(run_pelican(["-s", "pelicanconf.py", "-o", OUTPUT_DIRECTORY]))


@duty(capture=False)
def clean(ctx: Context) -> None:
    """Clean output directory"""
    _clean(ctx)


@duty(capture=False)
def devserver(ctx: Context) -> None:
    """Start dev server with autoreload"""
    ctx.run(setup(ctx, True), silent=True)
    ctx.run(run_pelican(["-s", "pelicanconf.py", "-o", OUTPUT_DIRECTORY, "-r", "-l", "-p", "4000"]))


@duty(capture=False)
def lint(ctx: Context) -> None:
    """Run formating and linting for fixing"""
    ctx.run(setup(ctx, True), silent=True)


@duty(capture=False)
def publish(ctx: Context) -> None:
    ctx.run(setup(ctx, False), silent=True)
    ctx.run(run_pelican(["-s", "publishconf.py", "-o", OUTPUT_DIRECTORY]))


@duty(capture=False)
def push(ctx: Context) -> None:
    """Checks everything is working and pushes changes"""
    ctx.run(setup(ctx, False), silent=True)
    ctx.run(run_pelican(["-s", "publishconf.py", "-o", OUTPUT_DIRECTORY]))
    ctx.run(r"""[ -z "$(git status --porcelain -uno)" ]""")
    ctx.run(["git", "push"])


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
