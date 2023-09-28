---
title: Theme Settings
---

This theme supports embeds for many different tools.

## Site Settings

There are some values that are not in the settings that will be optionally used in the theme.

### SITE_AUTHOR

The author is used in the footer and in the meta tags. Be sure that the Author format is correct.

```
SITE_AUTHOR = {
    "name": "Jay Miller",
    "email": "kjaymiller@gmail.com",
}
```

## Adding theme settings

Here is an example settings for this theme:

```json
"theme": {
    "favicon": "https:fav.farm/☕",
    "fontawesome": "abcd1234",
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
    }
```

## Settings

In this theme all settings are optional.

### colors

#### main1 (default: gray-600)

The primary color used in the site. This is present in the header and as some accents.

_This must be a valid tailwind color._

`purple-500` ✅
`#9333ea` ❌
`rgb(147 51 234)` ❌

```json

Since this is tailwind you can modify the css color by modifying the tailwind config.

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        'main1': 'rgb(147 51 234)',
      }
    }
  }
}
```

#### header_gradient_interval (default: 100)

The strength of the gradient used in the header. This can be an increment of 100 between (+-)100 and (+-)800. you can also use in increment of (-)50 and (+)50 when trying to get to the 50 and 950 color values.

### favicon (default: <https://fav.farm/👨🏾‍💻>)

This is a path/url to a favicon.

### fontawesome (optional)

This is a fontawesome key. You can get one from [fontawesome](https://fontawesome.com/).

> **Warning**
> This is not required but if you do not provide one you will not be able to use any of the fontawesome icons in social.

### social (optional)

This is a dictionary of social links. You can use any of the following keys:

- youtube
- x_twitter
- linkedin
- github
- mastodon

Social links not provided will not be shown.
