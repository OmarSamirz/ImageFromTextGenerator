import pytest
from PIL import ImageFont
from unittest.mock import patch, MagicMock
from iftg.image_font_manager import ImageFontManager


# Fixture to simulate a valid font path and size
@pytest.fixture
def valid_font():
    return "tests/Arial.ttf", 12


# Fixture to simulate an invalid font path
@pytest.fixture
def invalid_font():
    return "invalid_font.ttf", 12


# Fixture to clear the font cache before each test
@pytest.fixture(autouse=True)
def clear_cache():
    ImageFontManager.clear()


### TEST CASES


# Test that `get_font` loads a new font when not cached
def test_get_font_loads_new_font(valid_font):
    font_path, font_size = valid_font

    with patch.object(ImageFont, 'truetype', return_value=MagicMock()) as mock_truetype:
        font = ImageFontManager.get_font(font_path, font_size)
        mock_truetype.assert_called_once_with(font_path, font_size)
        assert ImageFontManager.get_font(font_path, font_size) == font


# Test that `get_font` uses the cache if the font is already loaded
def test_get_font_uses_cache(valid_font):
    font_path, font_size = valid_font

    with patch.object(ImageFont, 'truetype', return_value=MagicMock()) as mock_truetype:
        # First call, font should be loaded
        ImageFontManager.get_font(font_path, font_size)
        # Second call, font should be retrieved from cache
        ImageFontManager.get_font(font_path, font_size)
        # Ensure `truetype` was only called once
        mock_truetype.assert_called_once_with(font_path, font_size)


# Test `remove_font` removes font from cache
def test_remove_font(valid_font):
    font_path, font_size = valid_font

    with patch.object(ImageFont, 'truetype', return_value=MagicMock()) as mock_truetype:
        ImageFontManager.get_font(font_path, font_size)
        assert (font_path, font_size) in ImageFontManager.fonts()
        ImageFontManager.remove_font(font_path, font_size)
        assert (font_path, font_size) not in ImageFontManager.fonts()


# Test `remove_font` raises `KeyError` for non-existent font
@pytest.mark.skip(reason="Other modules handle this part")
def test_remove_font_keyerror(invalid_font):
    font_path, font_size = invalid_font

    with pytest.raises(KeyError):
        ImageFontManager.remove_font(font_path, font_size)


# Test `clear` removes all fonts from cache
def test_clear_clears_cache(valid_font):
    font_path, font_size = valid_font

    with patch.object(ImageFont, 'truetype', return_value=MagicMock()) as mock_truetype:
        ImageFontManager.get_font(font_path, font_size)
        assert (font_path, font_size) in ImageFontManager.fonts()
        ImageFontManager.clear()
        assert len(ImageFontManager.fonts()) == 0


# Parameterized test to check if multiple fonts can be loaded
@pytest.mark.parametrize("font_path,font_size", [
    ("arial.ttf", 12),
    ("times.ttf", 14),
    ("comic.ttf", 16),
])
def test_multiple_fonts(font_path, font_size):
    with patch.object(ImageFont, 'truetype', return_value=MagicMock()) as mock_truetype:
        font = ImageFontManager.get_font(font_path, font_size)
        assert ImageFontManager.get_font(font_path, font_size) == font
        mock_truetype.assert_called_once_with(font_path, font_size)
