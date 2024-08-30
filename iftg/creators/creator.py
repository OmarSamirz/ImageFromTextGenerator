from PIL import Image, ImageFont
from abc import ABC, abstractmethod

from iftg.noises.noise import Noise

class Creator(ABC):


    @classmethod
    @abstractmethod
    def _create_base_image(cls, 
                           text: str, 
                           font: ImageFont, 
                           background_color: str,
                           margins: tuple[int, int, int, int]
                          ) -> Image:
        pass
    
    
    @classmethod
    @abstractmethod
    def get_text_dimensions(cls, text: str, font: ImageFont) -> tuple[float, float, float, float]:
        left, top, right, bottom = font.getbbox(text)

        return left, top, right, bottom


    @classmethod
    @abstractmethod
    def get_image_dimensions(cls,
                             margins: tuple[int, int, int, int],
                             text_dimensions: tuple[float, float, float, float],
                            ) -> tuple[int, int]:
        
        _, top, right, bottom = text_dimensions
        left_margin, top_margin, right_margin, bottom_margin = margins

        image_width = right + left_margin + right_margin
        image_height = bottom - (top * 2) + top_margin + bottom_margin

        return image_width, image_height


    @classmethod
    @abstractmethod
    def _apply_noise(cls,
                     text: str,
                     font: ImageFont,
                     noises: list[Noise],
                     blur_radius: float ,
                     random_blur: bool,
                     min_blur: float,
                     max_blur: float,
                     rotation_angle: float,
                     random_rotation: bool,
                     min_rotation: float,
                     max_rotation: float,
                     font_color: str,
                     background_color: str,
                     margins: tuple[int, int, int, int],
                     image: Image,
                    ) -> Image:
        pass


    @classmethod
    @abstractmethod
    def create_image(cls,
                     text: str,
                     noises: list[Noise] = [],
                     blur_radius: float = 0.0,
                     random_blur: bool = False,
                     min_blur: float = 1.0,
                     max_blur: float = 4.0,
                     rotation_angle: float = 0.0,
                     random_rotation: bool = False,
                     min_rotation: float = -50.0,
                     max_rotation: float = 50.0,
                     font_path: str = "iftg/fonts/Arial.ttf",
                     font_size: int = 40,
                     font_color: str = 'black',
                     background_color: str = 'white',
                     margins: tuple[int, int, int, int] = (5, 5, 5, 5),
                     dpi: tuple[int, int] = (300, 300),
                     background_image_path: str = '',
                     clear_fonts: bool = True
                    ):
        pass


