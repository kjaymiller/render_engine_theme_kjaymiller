"""
Tests the generation logic of the templates
"""

from typing import Literal
import pytest
from render_engine_theme_kjaymiller.kjaymiller import (
    TailwindCSSColorSpec,
    get_color_string_value,
    get_theme_gradient_to,
    to_theme_object,
)


def test_to_theme_object():
    """Tests color string creates TailwindCSSColorSpec object"""
    color = to_theme_object("red-200")
    assert isinstance(color, TailwindCSSColorSpec)
    assert color.name == "red"
    assert color.value == 200

def test_get_color_string_value():
    """Tests color string creates TailwindCSSColorSpec object"""
    color = get_color_string_value("red-200")
    assert color == 200

@pytest.mark.parametrize(
        "increment_value, end_result",
        [
            (100, "300"), # Test Positive Increment
            (-100, "100"), # Test Negative Increment
        ]
)
def test_get_theme_gradient_to(increment_value: Literal[100, -100] | None, end_result: Literal['300', '100']):
    """Tests color string creates TailwindCSSColorSpec object"""
    color = get_theme_gradient_to("red-200", increment_value)
    assert color == f"to-red-{end_result}"

@pytest.mark.parametrize(
    "starting_value, increment_value, end_result",
    [
        (900, 100, "950"), # Test Max Value is 950
        (100, -100, "50"), # Test Min Value is 50
    ]
)
def test_get_theme_gradient_to_max_min(starting_value: Literal[900, 100], increment_value: Literal[100, -100], end_result: Literal['950', '50']):
    """Tests color string creates TailwindCSSColorSpec object"""
    color = get_theme_gradient_to(f"red-{starting_value}", increment_value)
    assert color == f"to-red-{end_result}"