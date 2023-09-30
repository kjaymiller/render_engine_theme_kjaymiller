# KJayMiller Render Engine Theme

[![Github Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fkjaymiller%2Frender_engine_theme_kjaymiller%2Fbadge%3Fref%3Dmain&style=flat-square)](https://actions-badge.atrox.dev/kjaymiller/render_engine_theme_kjaymiller/goto?ref=main)

This is a theme based on the early development of render-engine for kjaymiller.com.

It relies on Tailwind CSS with support for icons via fontawesome and embeds for analytics, and newsletters.

## Quickstart

1. Install this theme through pip:

```bash
pip install kjaymiller-render-engine-theme
```

2. Import and register your theme:

```python
from render_engine import Site
from kjaymiller_render_engine_theme import theme

app = Site()
app.register_themes(theme)
```

3. Add configuration file

This theme supports styling through [TailwindCSS](https://tailwindcss.com/). To add your own configuration, create a `tailwind.config.js` file in your project root and add your configuration there. You will need the following information in your config:

```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['output/**/*.{html, js}'],
  plugins: [require('@tailwindcss/typography')]
}
```

4. Add your theme settings

This theme supports embeds for many different tools as well as configurations for your tailwindcss settings. Here is a basic example of what your site's theme settings might look like:

```python

settings = {
    ... # settings for other plugins and your site
    "theme" : {
        "colors": {
          "main1": "rose-800", # You can use any valid tailwindcss color here
        }
        "favicon": "https:fav.farm/☕", # url to your favicon
        "fontawesome": "12345abcde", # fontawesome license key
        "buttondown": "kjaymiller", # newsletter id for embed
        "colors": {
            "main1": "purple-500",
            "header_gradient_interval": 100,
        },
        "social": {
            "youtube": "https://www.youtube.com/kjaymiller",
            "twitter": "https://twitter.com/kjaymiller",
            "linkedin": "https://linkedin.com/in/kjaymiller",
            "github": "https://github.com/kjaymiller",
            "mastodon": "https://mastodon.social/@kjaymiller",
        },
    }
}

```

5. Build your site
