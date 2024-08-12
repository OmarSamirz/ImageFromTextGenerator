from PIL import Image, ImageFont
from iftg.noises.noise import Noise
from abc import ABC, abstractmethod

class Creator(ABC):


    @abstractmethod
    def _create_base_image(cls, 
                           text: str, 
                           font: ImageFont, 
                           background_color: str,
                           margins: tuple[int, int, int, int]
                          ) -> Image:
        pass


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
                     clear_fonts: bool = True
                    ):
        pass


