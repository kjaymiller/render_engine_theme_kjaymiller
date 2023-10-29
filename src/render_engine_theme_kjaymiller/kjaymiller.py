import pathlib
import re

from jinja2 import PackageLoader
from render_engine.utils.themes import Theme
from render_engine_tailwindcss import TailwindCSS

from .tailwind_colors import (
    get_color_string_value,
    get_theme_gradient_to,
)
from .utils import Stylesheet

kjaymiller = Theme(
    loader=PackageLoader("render_engine_theme_kjaymiller", "templates"),
    static_dir= pathlib.Path(__file__).parent / "static",
    plugins = [TailwindCSS],
    filters = {
        "theme_gradient_to": get_theme_gradient_to,
        "theme_color_value": get_color_string_value,
        },
    template_globals = {
        "head": ["kjaymiller_com/_head.html"],
        "body_class": "dark:bg-slate-800 dark:text-slate-100",
        "page_title_class": "text-2xl font-bold text-slate-900 dark:text-slate-100",
    },
)