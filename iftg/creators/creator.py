from PIL import Image, ImageFont
from abc import ABC, abstractmethod

from iftg.noises.noise import Noise


class Creator(ABC):
    """
    An abstract base class that defines the interface for image creation classes.
    This class provides the basic structure and required methods for creating images
    with text and various effects.
    """

    @classmethod
    @abstractmethod
    def _create_base_image(cls,
                           text: str,
                           font: ImageFont,
                           font_color: tuple[int, int, int],
                           font_opacity: float,
                           background_color: str,
                           margins: tuple[int, int, int, int],
                           background_img: Image
                           ) -> Image.Image:
        pass

    @classmethod
    @abstractmethod
    def get_text_dimensions(cls, text: str, font: ImageFont) -> tuple[float, float, float, float]:
        """
        Gets the dimensions of text when rendered with a specific font.

        Parameters:
            text (str): The text to measure.
            font (ImageFont): The font to use for measurement.

        Returns:
            tuple[float, float, float, float]: The text dimensions as (left, top, right, bottom).
        """
        left, top, right, bottom = font.getbbox(text)

        return left, top, right, bottom

    @classmethod
    @abstractmethod
    def get_image_dimensions(cls,
                             margins: tuple[int, int, int, int],
                             text_dimensions: tuple[float, float, float, float],
                             ) -> tuple[int, int]:
        """
        Calculates the dimensions of the image based on the text dimensions and margins.

        Parameters:
            margins (tuple[int, int, int, int]): Margins for the image (left, top, right, bottom).
            text_dimensions (tuple[float, float, float, float]): The dimensions of the text.

        Returns:
            tuple[int, int]: The image dimensions as (width, height).
        """
        _, top, right, bottom = text_dimensions
        left_margin, top_margin, right_margin, bottom_margin = margins

        image_width = right + left_margin + right_margin
        image_height = bottom - (top * 2) + top_margin + bottom_margin

        return image_width, image_height

    @classmethod
    @abstractmethod
    def _apply_noise(cls, noises: list[Noise], image: Image) -> Image:
        pass

    @classmethod
    @abstractmethod
    def _blend_colors(cls, bg_color: str, text_color: str, font_opacity: float) -> tuple[int, int, int]:
        pass

    @classmethod
    @abstractmethod
    def create_image(cls,
                     text: str,
                     font_path: str,
                     noises: list[Noise],
                     font_size: float,
                     font_opacity: float,
                     font_color: str,
                     background_color: str,
                     margins: tuple[int, int, int, int],
                     dpi: tuple[float, float],
                     background_img: Image,
                     clear_font: bool,
                     ) -> Image:
        pass
