import pytest
import os
import glob
from unittest.mock import patch, MagicMock
from PIL import Image
from iftg.adders import DirectoryNoiseAdder
from iftg.noises import BlurNoise

# Fixture to return a valid directory path with images
@pytest.fixture
def valid_dir_path(tmp_path):
    img_formats = ['jpg', 'png', 'tif']
    img_dir = tmp_path / "images"
    img_dir.mkdir()

    # Create dummy images
    for fmt in img_formats:
        img_path = img_dir / f"test_image.{fmt}"
        img = Image.new('RGB', (100, 100))
        img.save(img_path)
    
    return str(img_dir)

@pytest.fixture
def invalid_dir_path():
    # Return a non-existing directory path
    return "non_existent_directory"

@pytest.fixture
def blur_noises():
    return [BlurNoise(blur_radius=2.0), BlurNoise(blur_radius=5.0)]

@pytest.fixture
def mock_image():
    mock_img = MagicMock(spec=Image.Image)
    mock_img.info = {'dpi': (72, 72)}
    return mock_img

### TEST CASES:

# Test successful initialization with a valid directory path
def test_init_valid_directory(valid_dir_path, blur_noises):
    adder = DirectoryNoiseAdder(valid_dir_path, noises=blur_noises)
    assert adder.dir_path == valid_dir_path
    assert len(adder.images_pathes) == 3  # Three images

# Test initialization failure with an invalid directory path
def test_init_invalid_directory(invalid_dir_path, blur_noises):
    with pytest.raises(FileNotFoundError):
        DirectoryNoiseAdder(invalid_dir_path, noises=blur_noises)

# Test noise application on a directory
def test_add_noises_directory(valid_dir_path, blur_noises):
    adder = DirectoryNoiseAdder(valid_dir_path, noises=blur_noises)

    with patch('PIL.Image.open') as mock_open:
        image = Image.new('RGB', (100, 100))  # Create a new image
        mock_open.return_value = image
        
        noisy_images = adder.add_noises()

        assert len(noisy_images) == 3  # Two images processed
        for noisy_image, img_name, img_format in noisy_images:
            assert isinstance(noisy_image, Image.Image)
            assert img_format in ['.jpg', '.png', '.tif']

# Test image transformation and saving with BlurNoise on a directory
@patch('iftg.adders.DirectoryNoiseAdder.save_image')
def test_transform_images(mock_save_image, valid_dir_path, blur_noises):
    adder = DirectoryNoiseAdder(valid_dir_path, noises=blur_noises)

    with patch('PIL.Image.open') as mock_open:
        image = Image.new('RGB', (100, 100))
        mock_open.return_value = image

        adder.transform_images()
    
    assert mock_save_image.call_count == 3  # Two images saved
