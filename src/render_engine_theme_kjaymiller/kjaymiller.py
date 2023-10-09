import pathlib
import re

from jinja2 import PackageLoader
from render_engine.utils.themes import Theme
from render_engine_tailwindcss import TailwindCSS

from .tailwind_colors import TailwindCSSColorSpec


def to_theme_object(theme_color:str) -> TailwindCSSColorSpec:
    """Split a string based on the tailwind spec"""
    match = re.match(r"([a-z]+)-(\d{2,3})", theme_color)
    return TailwindCSSColorSpec(match.group(1), int(match.group(2)))

def get_color_string_value(theme_color:str) -> int:
    """Split a string based on the tailwind spec"""
    color = to_theme_object(theme_color)
    return color.value

# Filters for the engine
def get_theme_gradient_to(base_value:str, increment_value:int) -> str:
    color = to_theme_object(base_value)
    if color.value == 50 and increment_value != 50:
        increment_value += 50
    color.value += increment_value
    if color.value > 950:
        color.value = 950
    if color.value < 50:
        color.value = 50
    return f"to-{str(color)}"

kjaymiller = Theme(
    loader=PackageLoader("render_engine_theme_kjaymiller", "templates"),
    static_dir= pathlib.Path(__file__).parent / "static",
    plugins = [TailwindCSS],
    filters = {
        "theme_gradient_to": get_theme_gradient_to,
        "theme_color_value": get_color_string_value,
        },
)