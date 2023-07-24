
from jinja2 import PackageLoader
from render_engine.utils.themes import Theme

kjaymiller = Theme(
    themeLoader = PackageLoader('render_engine_theme_kjaymiller', 'templates')
)