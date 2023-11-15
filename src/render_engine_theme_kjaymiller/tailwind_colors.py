import dataclasses
import re

VALID_TAILWINDCSS_COLOR_RANGE = (
    50,
    100,
    200,
    300,
    400,
    500,
    600,
    700,
    800,
    900,
    950,
)

VALID_TAILWINDCSS_COLORS = (
    "slate",
    "gray",
    "zinc",
    "neutral",
    "stone",
    "red",
    "orange",
    "amber",
    "yellow",
    "lime",
    "green",
    "emerald",
    "teal",
    "cyan",
    "sky",
    "blue",
    "indigo",
    "violet",
    "purple",
    "fuchsia",
    "pink",
    "rose",
)


@dataclasses.dataclass
class TailwindCSSColorSpec:
    """#TODO: Validate name and range to valid colors"""

    name: str
    value: int

    def __init__(self, name: str, value: int):
        if name.lower() not in VALID_TAILWINDCSS_COLORS:
            raise ValueError(f"{name} is not a recognized tailwind color")
        else:
            self.name = name.lower()

        if value not in VALID_TAILWINDCSS_COLOR_RANGE:
            raise ValueError(f"{value} is not a recognized tailwind value")
        else:
            self.value = value

    def __str__(self):
        return f"{self.name}-{self.value}"


def to_theme_object(theme_color: str) -> TailwindCSSColorSpec:
    """Split a string based on the tailwind spec"""
    match = re.match(r"([a-z]+)-(\d{2,3})", theme_color)
    return TailwindCSSColorSpec(match.group(1), int(match.group(2)))


def get_color_string_value(theme_color: str) -> int:
    """Split a string based on the tailwind spec"""
    color = to_theme_object(theme_color)
    return color.value


# Filters for the engine
def get_theme_gradient_to(base_value: str, increment_value: int) -> str:
    color = to_theme_object(base_value)
    if color.value == 50 and increment_value != 50:
        increment_value += 50
    color.value += increment_value
    if color.value > 950:
        color.value = 950
    if color.value < 50:
        color.value = 50
    return f"to-{str(color)}"
