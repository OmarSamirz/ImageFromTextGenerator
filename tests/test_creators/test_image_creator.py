import pytest
from PIL import Image, ImageFont
from unittest.mock import patch, MagicMock

from iftg.creators import ImageCreator
from iftg.noises import BlurNoise
from iftg.image_font_manager import ImageFontManager


@pytest.fixture
def mock_font():
    font = ImageFontManager.get_font('tests/Arial.ttf', 12)
    return font


@pytest.fixture
def mock_image():
    image = MagicMock(spec=Image.Image)
    # Add required attributes and methods for ImageDraw
    image.size = (500, 500)
    image.readonly = False
    image.getdraw = MagicMock()
    # Mock the drawing context
    draw_context = MagicMock()
    image.getdraw.return_value = draw_context
    return image


@pytest.fixture
def noise_list():
    return [BlurNoise(blur_radius=2.0), BlurNoise(blur_radius=5.0)]


@pytest.mark.parametrize(
    "text, margins, bg_color, font_color, expected_size",
    [
        ("Sample Text", (5, 5, 5, 5), "white", (255, 255, 255), (500, 500)),
        ("Another Text", (10, 10, 10, 10), "black", (255, 255, 255), (500, 500)),
    ]
)
def test_create_base_image(mock_font, mock_image, text, margins, bg_color, font_color, expected_size):
    with patch('PIL.Image.new', return_value=mock_image):
        image = ImageCreator._create_base_image(
            text, mock_font, font_color, bg_color, margins, None)

        assert image == mock_image
        assert image.size == expected_size
        assert isinstance(image, MagicMock)  # Changed from Image.Image since we're using a mock


def test_invalid_font_path():
    with patch('iftg.image_font_manager.ImageFontManager.get_font', side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            ImageCreator.create_image(
                text="Test",
                font_path="invalid_path",
                font_size=40
            )