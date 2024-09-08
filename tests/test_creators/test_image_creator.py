import pytest
from PIL import Image, ImageFont

from unittest.mock import patch, MagicMock

from iftg.creators import ImageCreator
from iftg.noises import BlurNoise
from iftg.image_font_manager import ImageFontManager


# Fixture to create a dummy font path and mock the font retrieval
@pytest.fixture
def mock_font():
    font = ImageFontManager.get_font('tests/Arial.ttf', 12)
    return font


# Fixture to return a mock image
@pytest.fixture
def mock_image():
    image = MagicMock(spec=Image.Image)
    image.size = (500, 500)
    return image


# Fixture to return a list of noise objects
@pytest.fixture
def noise_list():
    return [BlurNoise(blur_radius=2.0), BlurNoise(blur_radius=5.0)]


# Test cases for _create_base_image method
@pytest.mark.parametrize(
    "text, margins, bg_color, expected_size",
    [
        ("Sample Text", (5, 5, 5, 5), "white", (500, 500)),  # Example with some dimensions
        ("Another Text", (10, 10, 10, 10), "black", (500, 500)),  # Another example
    ]
)
def test_create_base_image(mock_font, mock_image, text, margins, bg_color, expected_size):
    with patch('PIL.Image.new', return_value=mock_image):
        image, top = ImageCreator._create_base_image(text, mock_font, bg_color, margins, None)

        assert image == mock_image
        assert image.size == expected_size  # Mocked size
        assert isinstance(image, Image.Image)


# Test exception when invalid font path is given
def test_invalid_font_path():
    with patch('iftg.image_font_manager.ImageFontManager.get_font', side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            ImageCreator.create_image(
                text="Test",
                font_path="invalid_path",
                font_size=40
            )
