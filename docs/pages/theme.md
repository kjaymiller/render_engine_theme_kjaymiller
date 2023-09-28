---
title: Theme
---

The theme is built on Tailwind CSS with support from fontawesome.

## Install theme

You can install the theme via pip.

```shell
python -m pip install kjaymiller-render-engine-theme
```

## Register theme

This theme is installed through the site's `register_themes` method.

```python
from render_engine import Site
from kjaymiller_render_engine_theme import kjaymiller

app = Site()
app.register_themes(kjaymiller)
```

## Theme Filters

This theme does add some filters but they are for building the site and not intended for use by the user.
