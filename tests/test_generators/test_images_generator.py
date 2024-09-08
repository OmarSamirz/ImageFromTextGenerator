import pytest
from PIL import Image

import os
from unittest.mock import MagicMock, patch

from iftg.noises import GaussianNoise
from iftg.generators import ImagesGenerator
from iftg.image_font_manager import ImageFontManager


# Fixture to simulate valid input parameters
@pytest.fixture
def valid_texts():

    return ["Hello", "World"]

@pytest.fixture
def valid_font_path():
    return "tests/Arial.ttf"


@pytest.fixture
def valid_output_path(tmpdir):
    return str(tmpdir)


@pytest.fixture
def valid_background_image_path():
    return "background.jpg"


# Fixture to create a mock noise object
@pytest.fixture
def mock_noise():
    noise = MagicMock(spec=GaussianNoise())
    return noise


### TEST CASES


# Test the constructor when valid paths are provided
def test_images_generator_init(valid_texts, valid_font_path, valid_output_path):
    with patch("os.path.exists", return_value=True):
        generator = ImagesGenerator(
            texts=valid_texts, 
            font_path=valid_font_path, 
            img_output_path=valid_output_path
        )
        assert generator.texts == valid_texts
        assert generator.font_path == valid_font_path
        assert generator.img_output_path == valid_output_path


# Test the constructor raises FileNotFoundError if font path doesn't exist
def test_images_generator_invalid_font_path(valid_texts, valid_output_path):
    with pytest.raises(FileNotFoundError):
        ImagesGenerator(
            texts=valid_texts, 
            font_path="invalid_font.ttf", 
            img_output_path=valid_output_path
        )


# Test the constructor raises FileNotFoundError if background image doesn't exist
def test_images_generator_invalid_background_image(valid_texts, valid_font_path, valid_output_path):
    with patch("os.path.exists", side_effect=[True, False]):
        with pytest.raises(FileNotFoundError):
            ImagesGenerator(
                texts=valid_texts, 
                font_path=valid_font_path, 
                img_output_path=valid_output_path, 
                background_image_path="invalid_image.jpg"
            )


# Test _generate_next returns the correct image and text tuple
def test_generate_next(valid_texts, valid_font_path, mock_noise, valid_output_path):
    with patch("os.path.exists", return_value=True):
        generator = ImagesGenerator(
            texts=valid_texts, 
            font_path=valid_font_path, 
            noises=[mock_noise], 
            img_output_path=valid_output_path
        )
        
        generator._generate_next()
        assert len(ImageFontManager.fonts()) == 1


# Test that StopIteration is raised after all images are generated
def test_generate_next_stop_iteration(valid_texts, valid_font_path, valid_output_path):
    with patch("os.path.exists", return_value=True):
        generator = ImagesGenerator(
            texts=valid_texts, 
            font_path=valid_font_path, 
            img_output_path=valid_output_path
        )

        generator._count = len(valid_texts) + 1 # Set the counter beyond the texts length

        with pytest.raises(StopIteration):
                generator._generate_next()
                ImageFontManager.clear()


# Test save_image saves the image to the correct path
def test_save_image(valid_texts, valid_font_path, valid_output_path):
    with patch("os.path.exists", return_value=True):
        generator = ImagesGenerator(
            texts=valid_texts, 
            font_path=valid_font_path, 
            img_output_path=valid_output_path
        )
        img = Image.new('RGB', (100, 100))
        generator._save_image(img, 0)

        img_path = os.path.join(valid_output_path, "img_0.tif")
        assert os.path.exists(img_path)


# Test generate_images creates images and saves them in the output directory
def test_generate_images(valid_texts, valid_font_path, valid_output_path, mock_noise):
    with patch("os.path.exists", return_value=True):
        generator = ImagesGenerator(
            texts=valid_texts, 
            font_path=valid_font_path, 
            noises=[mock_noise], 
            img_output_path=valid_output_path
        )

        
        generator.generate_images()

        for i, text in enumerate(valid_texts):
            img_path = os.path.join(valid_output_path, f"img_{i}.tif")
            assert os.path.exists(img_path)


# Test generate_images_with_text creates images and corresponding text files
def test_generate_images_with_text(valid_texts, valid_font_path, valid_output_path, mock_noise):
    with patch("os.path.exists", return_value=True):
        generator = ImagesGenerator(
            texts=valid_texts, 
            font_path=valid_font_path, 
            noises=[mock_noise], 
            img_output_path=valid_output_path,
            txt_output_path=valid_output_path
        )

        generator.generate_images_with_text()

        for i, text in enumerate(valid_texts):
            img_path = os.path.join(valid_output_path, f"img_{i}.tif")
            txt_path = os.path.join(valid_output_path, f"text_{i}.txt")
            assert os.path.exists(img_path)
            assert os.path.exists(txt_path)
            with open(txt_path, 'r') as f:
                assert f.read() == text
