import pytest
from PIL import Image

import os

from iftg.noises import BlurNoise
from iftg.image_font_manager import ImageFontManager
from iftg.generators import BatchesImagesGenerator, ImagesGenerator


@pytest.fixture
def valid_texts():
    return [["Text1", "Text2"], ["Text3", "Text4"]]

@pytest.fixture
def valid_noises():
    return [[BlurNoise()], [BlurNoise()]]

@pytest.fixture
def valid_font_paths():
    return [os.path.join("tests", "Arial.ttf"), os.path.join("tests", "Arial.ttf")]

@pytest.fixture
def valid_batch_params(valid_texts, valid_noises, valid_font_paths):
    return {
        "texts": valid_texts,
        "font_paths": valid_font_paths,
        "noises": valid_noises,
        "font_sizes": [40.0, 45.0],
        "font_colors": ["black", "blue"],
        "background_colors": ["white", "gray"],
        "margins": [(5, 5, 5, 5), (10, 10, 10, 10)],
        "dpi": [(300, 300), (72, 72)],
        "img_names": ["batch1", "batch2"],
        "img_formats": [".png", ".jpeg"],
        "img_output_paths": ["output1", "output2"],
        "txt_names": ["label1", "label2"],
        "txt_formats": [".txt", ".md"],
        "txt_output_paths": ["output1", "output2"],
        "background_image_paths": ["", ""],
    }

@pytest.fixture
def batch_generator(valid_batch_params):
    return BatchesImagesGenerator(**valid_batch_params)


@pytest.mark.parametrize("with_label", [True, False])
def test_generate_batches(batch_generator, with_label, mocker):
    mock_generate_images = mocker.patch.object(ImagesGenerator, 'generate_images')
    mock_generate_images_with_text = mocker.patch.object(ImagesGenerator, 'generate_images_with_text')

    batch_generator.generate_batches(is_with_label=with_label)

    if with_label:
        assert mock_generate_images_with_text.call_count == 2
    else:
        assert mock_generate_images.call_count == 2


def test_stop_iteration(batch_generator):
    """
    Test that StopIteration is raised when all batches are processed.
    """
    # Generate all batches
    for _ in batch_generator:
        pass
    
    # Ensure StopIteration is raised on the next call
    with pytest.raises(StopIteration):
        next(batch_generator)


def test_mismatched_lengths():
    """
    Test that the constructor handles mismatched input lengths by extending lists.
    """
    texts = [["Text1", "Text2"]]
    font_paths = [os.path.join("tests", "Arial.ttf")]
    noises = [[BlurNoise()]]
    batch_gen = BatchesImagesGenerator(texts=texts, font_paths=font_paths, noises=noises)

    assert len(batch_gen.texts) == len(batch_gen.font_path) == len(batch_gen.noises) == 1


def test_missing_font_raises_error():
    """
    Test that a FileNotFoundError is raised if the font file doesn't exist.
    """
    texts = [["Text1", "Text2"]]
    font_paths = ["invalid_font_path.ttf"]
    with pytest.raises(FileNotFoundError):
        batch_generator = BatchesImagesGenerator(texts=texts, font_paths=font_paths)
        batch_generator.generate_batches()


def test_batch_extension(batch_generator):
    """
    Test that shorter input lists are extended properly to match the longest list.
    """
    assert len(batch_generator.font_size) == len(batch_generator.font_color)
    assert len(batch_generator.img_name) == len(batch_generator.txt_format)


@pytest.mark.parametrize("is_with_label", [True, False])
def test_output_directories_created(batch_generator, is_with_label):

    batch_generator.generate_batches(is_with_label=is_with_label)

    assert os.path.exists('output1') == True
    assert os.path.exists('output2') == True
