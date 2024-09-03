from abc import ABC, abstractmethod

from iftg.noises.noise import Noise

class Generator(ABC):
    """
    An abstract base class for creating image generators that apply various effects, 
    such as noise and text, to images. Subclasses should implement the `_generate_next` method 
    to define how each image is generated.

    Attributes:
        texts (list[str] | list[list[str]]): 
            A list of texts or a list of lists of texts for generating images.
        font_path (str | list[str]): 
            The file path(s) to the font(s) used in the images.
        noises (list[Noise] | list[list[Noise]]): 
            A list of noise objects or a list of lists of noise objects to be applied to the images.
        font_size (float | list[float]): 
            The size(s) of the font(s) used in the images.
        font_color (str | list[str]): 
            The color(s) of the text in the images.
        background_color (str | list[str]): 
            The background color(s) of the images.
        margins (tuple[int, int, int, int] | list[tuple[int, int, int, int]]): 
            Margins for text placement on the images, either as a single tuple or a list of tuples.
        dpi (tuple[float, float] | list[tuple[float, float]]): 
            The DPI (dots per inch) settings for the images, either as a single tuple or a list of tuples.
        img_name (str | list[str]): 
            The base name(s) for the output image files.
        img_format (str | list[str]): 
            The file format(s) for the output images.
        img_output_path (str | list[str]): 
            The directory or directories where the generated images will be saved.
        txt_name (str | list[str]): 
            The base name(s) for the output text files containing image labels.
        txt_format (str | list[str]): 
            The file format(s) for the output text files.
        txt_output_path (str | list[str]): 
            The directory or directories where the generated text files will be saved.
        background_image_path (str | list[str]): 
            The file path(s) to the background image(s) to be used in the images.
    """
      

    def __init__(self,
                 texts: list[str] | list[list[str]],
                 font_path: str | list[str],
                 noises: list[Noise] | list[list[Noise]],
                 font_size: float | list[float],
                 font_color: str | list[str],
                 background_color: str | list[str],
                 margins: tuple[int, int, int, int] | list[tuple[int, int, int, int]],
                 dpi: tuple[float, float] | list[tuple[float, float]],
                 img_name: str | list[str],
                 img_format: str | list[str],
                 img_output_path: str | list[str],
                 txt_name: str | list[str],
                 txt_format: str | list[str],
                 txt_output_path: str | list[str],
                 background_image_path: str | list[str],
                ):
        self.texts = texts
        self.font_path = font_path
        self.noises = noises
        self.font_size = font_size
        self.font_color = font_color
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
            Object:
                The next generated image or relevant output, depending on the subclass implementation.

        Raises:
            StopIteration:
                When there are no more images to generate.
        """
        return self._generate_next()
    

    def _generate_next(self):
        pass