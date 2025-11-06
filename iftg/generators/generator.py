
from abc import ABC, abstractmethod
from typing import List, Tuple, Union

from iftg.noises.noise import Noise


class Generator(ABC):
    """
    An abstract base class for creating image generators that apply various effects, 
    such as noise and text, to images. Subclasses should implement the `_generate_next` method 
    to define how each image is generated.

    Attributes:
        texts (List[str] | List[List[str]]): 
            A list of texts or a list of lists of texts for generating images.
        font_path (str | List[str]): 
            The file path(s) to the font(s) used in the images.
        noises (List[Noise] | List[List[Noise]]): 
            A list of noise objects or a list of lists of noise objects to be applied to the images.
        font_size (float | List[float]): 
            The size(s) of the font(s) used in the images.
        font_color (str | List[str]): 
            The color(s) of the text in the images.
        font_opacity (float | List[float]):
            The opacity level(s) of the text, where 1.0 is fully opaque and 0.0 is fully transparent.
        background_color (str | List[str]): 
            The background color(s) of the images.
        margins (Tuple[int, int, int, int] | List[Tuple[int, int, int, int]]): 
            Margins for text placement on the images, either as a single tuple or a list of tuples.
        dpi (Tuple[float, float] | List[Tuple[float, float]]): 
            The DPI (dots per inch) settings for the images, either as a single tuple or a list of tuples.
        img_name (str | List[str]): 
            The base name(s) for the output image files.
        img_format (str | List[str]): 
            The file format(s) for the output images.
        img_output_path (str | List[str]): 
            The directory or directories where the generated images will be saved.
        txt_name (str | List[str]): 
            The base name(s) for the output text files containing image labels.
        txt_format (str | List[str]): 
            The file format(s) for the output text files.
        txt_output_path (str | List[str]): 
            The directory or directories where the generated text files will be saved.
        background_image_path (str | List[str]): 
            The file path(s) to the background image(s) to be used in the images.
    """

    def __init__(
        self,
        texts: Union[List[str], List[List[str]]],
        font_path: Union[str, List[str]],
        noises: Union[List[Noise], List[List[Noise]]],
        font_size: Union[float, List[float]],
        font_color: Union[str, List[str]],
        font_opacity: Union[float, List[float]],
        background_color: Union[str, List[str]],
        margins: Union[Tuple[int, int, int, int], List[Tuple[int, int, int, int]]],
        dpi: Union[Tuple[float, float], List[Tuple[float, float]]],
        img_name: Union[str, List[str]],
        img_format: Union[str, List[str]],
        img_output_path: Union[str, List[str]],
        txt_name: Union[str, List[str]],
        txt_format: Union[str, List[str]],
        txt_output_path: Union[str, List[str]],
        background_image_path: Union[str, List[str]],
    ) -> None:
        self.texts = texts
        self.font_path = font_path
        self.noises = noises
        self.font_size = font_size
        self.font_color = font_color
        self.font_opacity = font_opacity
        self.background_color = background_color
        self.margins = margins
        self.dpi = dpi
        self.img_name = img_name
        self.img_format = img_format
        self.img_output_path = img_output_path
        self.txt_name = txt_name
        self.txt_format = txt_format
        self.txt_output_path = txt_output_path
        self.background_image_path = background_image_path
        self._texts_len = len(texts)
        self._count = 0
        
    def __len__(self):
        return len(self.texts)

    def __iter__(self):
        """
        Returns the generator object itself.

        Returns:
            Generator:
                The generator object.
        """
        return self

    def __next__(self):
        """
        Returns the next generated image by calling the `_generate_next` method.

        Returns:
        ImagesGenerator | Tuple[Image.Image, str, int]:
            - If the subclass returns an image, a tuple is expected containing:
                - `Image.Image`: The generated image.
                - `str`: A label or related information for the image.
                - `int`: An additional identifier or index for the image.
            - Alternatively, a custom subclass may return an instance of `ImagesGenerator`.

        Raises:
            StopIteration:
                When there are no more images to generate.
        """

        return self._generate_next()

    @abstractmethod
    def _generate_next(self):
        """
        Abstract method that defines how the next image in the sequence is generated.
        This method must be implemented by subclasses.

        Returns:
            ImagesGenerator | Tuple[Image.Image, str, int]:
                - If returning an image directly, a tuple containing:
                    - The generated image
                    - A label or text associated with the image
                    - An index or identifier for the image
                - Alternatively, an instance of ImagesGenerator for batch processing

        Raises:
            StopIteration: When there are no more images to generate
        """
        ...
