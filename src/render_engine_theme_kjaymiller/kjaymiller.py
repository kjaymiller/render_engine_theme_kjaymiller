
from jinja2 import PackageLoader
from render_engine.utils.themes import Theme

kjaymiller = Theme(
    loader=PackageLoader("render_engine_theme_kjaymiller", "templates"),
    static_dir= __file__.parent / "static",
)