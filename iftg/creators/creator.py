from PIL import Image, ImageFont

from typing import Tuple, List
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
    def _create_base_image(
        cls,
        text: str,
        font: ImageFont.ImageFont,
        font_color: Tuple[int, int, int],
        font_opacity: float,
        background_color: str,
        margins: Tuple[int, int, int, int],
        background_img: Image.Image
    ) -> Image.Image:
        ...

    @classmethod
    @abstractmethod
    def get_text_dimensions(cls, text: str, font: ImageFont.ImageFont) -> Tuple[int, int]:
        """
        Gets the dimensions of text when rendered with a specific font.

        Parameters:
            text (str): The text to measure.
            font (ImageFont): The font to use for measurement.

        Returns:
            Tuple[int, int]: The text dimensions as (max_width, total_height).
        """
        lines = text.splitlines() or [""]

        bboxes = [
            font.getbbox("A") if not line.strip() else font.getbbox(line)
            for line in lines
        ]

        max_width = max(right for _, _, right, _ in bboxes)
        bottom_sum = sum(bottom for _, _, _, bottom in bboxes)
        max_top = max(top for _, top, _, _ in bboxes)
        total_height = bottom_sum + max_top

        return max_width, total_height

    @classmethod
    @abstractmethod
    def get_image_dimensions(
        cls,
        margins: Tuple[int, int, int, int],
        text_dimensions: Tuple[float, float, float, float],
    ) -> Tuple[int, int]:
        """
        Calculates the dimensions of the image based on the text dimensions and margins.

        Parameters:
            margins (Tuple[int, int, int, int]): Margins for the image (left, top, right, bottom).
            text_dimensions (Tuple[float, float, float, float]): The dimensions of the text.

        Returns:
            Tuple[int, int]: The image dimensions as (width, height).
        """
        max_width, max_height = text_dimensions
        left_margin, top_margin, right_margin, bottom_margin = margins

        image_width = max_width + left_margin + right_margin
        image_height = max_height + top_margin + bottom_margin

        return image_width, image_height

    @classmethod
    @abstractmethod
    def _apply_noise(cls, noises: List[Noise], image: Image.Image) -> Image.Image:
        ...

    @classmethod
    @abstractmethod
    def _blend_colors(cls, bg_color: str, text_color: str, font_opacity: float) -> Tuple[int, int, int]:
        ...

    @classmethod
    @abstractmethod
    def create_image(
        cls,
        text: str,
        font_path: str,
        noises: List[Noise],
        font_size: float,
        font_opacity: float,
        font_color: str,
        background_color: str,
        margins: Tuple[int, int, int, int],
        dpi: Tuple[float, float],
        background_img: Image.Image,
        clear_font: bool,
    ) -> Image.Image:
        ...
