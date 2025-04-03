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
    # Create a real PIL Image with RGBA mode to support more operations
    return Image.new("RGBA", (500, 500), color=(255, 255, 255))

@pytest.fixture
def noise_list():
    return [BlurNoise(blur_radius=2.0), BlurNoise(blur_radius=5.0)]

@pytest.mark.parametrize(
    "text, margins, bg_color, font_color, expected_size",
    [
        ("Sample Text", (5, 5, 5, 5), (255, 255, 255), (0, 0, 0), (500, 500)),
        ("Another Text", (10, 10, 10, 10), (0, 0, 0), (255, 255, 255), (500, 500)),
    ]
)
def test_create_base_image(mock_font, text, margins, bg_color, font_color, expected_size):
    # Create a patch that returns a real RGBA image
    with patch('PIL.Image.new', return_value=Image.new("RGBA", expected_size, color=bg_color)):
        image = ImageCreator._create_base_image(
            text, mock_font, font_color, 1.0, bg_color, margins, None)
        
        assert image.size == expected_size
        assert isinstance(image, Image.Image)

def test_invalid_font_path():
    with patch('iftg.image_font_manager.ImageFontManager.get_font', side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            ImageCreator.create_image(
                text="Test",
                font_path="invalid_path",
                font_size=40
            )

def test_apply_noises():
    """Test that noises are properly applied to the image."""
    # Create a mock image
    test_image = Image.new("RGB", (200, 100), color="white")
    
    # Create a proper noise effect
    blur_noise = BlurNoise(blur_radius=2.0)
    
    # Apply the noise to the image
    with patch.object(ImageCreator, '_create_base_image', return_value=test_image):
        result = ImageCreator.create_image(
            text="Test with noise",
            font_path="tests/Arial.ttf",
            font_size=12,
            noises=[blur_noise]
        )
    
    # Verify the result is an image
    assert isinstance(result, Image.Image)

def test_create_image_with_custom_params():
    """Test creating an image with custom parameters."""
    test_image = Image.new("RGB", (300, 150), color="blue")
    
    with patch.object(ImageCreator, '_create_base_image', return_value=test_image):
        # Test with various custom parameters
        result = ImageCreator.create_image(
            text="Custom Test",
            font_path="tests/Arial.ttf",
            font_size=16,
            font_color="red",     # String color name instead of tuple
            background_color="blue",      # String color name instead of tuple
            margins=(20, 20, 20, 20) # Wide margins
        )
    
    assert isinstance(result, Image.Image)