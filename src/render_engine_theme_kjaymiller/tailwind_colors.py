import dataclasses

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

    def __init__(self, name:str, value:int):
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