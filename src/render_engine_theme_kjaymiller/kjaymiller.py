
from jinja2 import PackageLoader
from render_engine.utils.themes import Theme

kjaymiller = Theme(
    name="kjaymiller",
    template_loader=PackageLoader("render_engine_theme_kjaymiller", "templates"),
    static_loader=PackageLoader("render_engine_theme_kjaymiller", "static"),
)