"""
Tests the color spec logic of the templates
"""

import pytest
from render_engine_theme_kjaymiller.tailwind_colors import TailwindCSSColorSpec

def tests_theme_check_raises_error():
    """Test that the theme is properly configured"""
    with pytest.raises(ValueError):
        TailwindCSSColorSpec("not-a-color", 50)

    with pytest.raises(ValueError):
        TailwindCSSColorSpec("red", 1000)