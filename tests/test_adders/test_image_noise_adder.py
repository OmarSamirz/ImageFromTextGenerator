import pytest
from PIL import Image as Image

from unittest.mock import patch, MagicMock

from iftg.adders import ImageNoiseAdder
from iftg.noises import BlurNoise

# Fixture to return a valid image path and mock image object
@pytest.fixture
def valid_image_path(tmp_path):
    # Create a valid temporary image file
    img_path = tmp_path / "test_image.png"
    img = Image.new('RGB', (100, 100))  # Create a blank image
    img.save(img_path)
    return str(img_path)


@pytest.fixture
def invalid_image_path():
    # Return a non-existing image path
    return "non_existent_image.png"

@pytest.fixture
def blur_noises():
    # Return a list of BlurNoise instances with different radii
    return [BlurNoise(blur_radius=2.0), BlurNoise(blur_radius=5.0)]


@pytest.fixture
def mock_image():
    mock_img = MagicMock(spec=Image.Image)
    mock_img.info = {'dpi': (72, 72)}
    return mock_img

### TEST CASES:

# Test successful initialization with a valid image path
def test_init_valid_image(valid_image_path, blur_noises):
    adder = ImageNoiseAdder(valid_image_path, noises=blur_noises)
    assert adder.img_path == valid_image_path

# Test initialization failure with an invalid image path
def test_init_invalid_image(invalid_image_path, blur_noises):
    with pytest.raises(FileNotFoundError):
        ImageNoiseAdder(invalid_image_path, noises=blur_noises)

# Test noise application with BlurNoise
def test_add_noises(valid_image_path, blur_noises):
    adder = ImageNoiseAdder(valid_image_path, noises=blur_noises)
    
    with patch('PIL.Image.open') as mock_open:
        image = Image.new('RGB', (100, 100))  # Create a new image
        mock_open.return_value = image
        
        noisy_image, img_name, img_format = adder.add_noises()

        assert isinstance(noisy_image, Image.Image)
        assert img_name == "test_image"
        assert img_format == ".png"

# Test image transformation and saving with BlurNoise
@patch('iftg.adders.image_noise_adder.ImageNoiseAdder.save_image')
def test_transform_image(mock_save_image, valid_image_path, blur_noises):
    adder = ImageNoiseAdder(valid_image_path, noises=blur_noises)
    
    adder.transform_image()
    
    mock_save_image.assert_called_once()
