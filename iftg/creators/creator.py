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
                           margins: tuple[int, int, int, int],
                           background_img: Image
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
                     top: int,
                     font: ImageFont,
                     noises: list[Noise],
                     font_color: str,
                     margins: tuple[int, int, int, int],
                     image: Image,
                    ) -> Image:
        pass


    @classmethod
    @abstractmethod
    def create_image(cls,
                     text: str,
                     font_path: str,
                     noises: list[Noise],
                     font_size: float,
                     font_color: str,
                     background_color: str ,
                     margins: tuple[int, int, int, int],
                     dpi: tuple[float, float],
                     background_img: Image,
                     clear_font: bool
                    ):
        pass


