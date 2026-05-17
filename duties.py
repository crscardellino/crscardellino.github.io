import sys

from datetime import datetime
from duty import duty, tools, Context
from pathlib import Path
from pelican import main as pelican_main
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file
from slugify import slugify
from zoneinfo import ZoneInfo

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
def new_post(
    ctx: Context, title: str, category: str | None = None, tags: str | None = None
) -> None:
    now = datetime.now(tz=ZoneInfo(SETTINGS.get("TIMEZONE", "UTC")))
    post_name = f"{now.strftime('%Y-%m-%d')}-{slugify(title)}.markdown"
    post_path = Path("./content/drafts") / post_name

    if post_path.exists():
        print(f"The file {post_path} exists. Refusing to overwrite.", file=sys.stderr)
        sys.exit(1)

    with open(post_path, "wt") as fh:
        print("---", file=fh)
        print(f"title: {title}", file=fh)
        print(f"date: {now.strftime('%Y-%m-%d %H:%M:%S %z')}", file=fh)

        if category:
            print(f"category: {category}", file=fh)

        if tags:
            tags = tags.split(",")
            print("tags:", file=fh)
            for tag in tags:
                print(f"  - {tag.strip()}", file=fh)

        print("---", file=fh)


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
