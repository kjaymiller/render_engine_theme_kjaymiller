import dataclasses


@dataclasses.dataclass
class Stylesheet:
    href: str

    def __str__(self):
        return f'<link rel="stylesheet" href="{self.href}" />'
