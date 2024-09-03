from abc import ABC, abstractmethod

from iftg.noises.noise import Noise, Image


class NoiseAdder(ABC):
    """
    An abstract base class for adding noise to images. Subclasses must implement the methods 
    for applying noise, adding noises, saving images, and transforming images.

    Attributes:
        identifier (str): 
            A unique identifier for the noise adder instance.
        img_formats (list[str]): 
            A list of image formats for saving the processed images.
        noises (list[Noise]): 
            A list of noise objects to be applied to the images.
    """

    def __init__(self, 
                 noises: list[Noise],
                 identifier: str,
                 img_formats: list[str],
                ):
        self.identifier = identifier
        self.img_formats = img_formats
        self.noises = noises

    
    @abstractmethod
    def _apply_noises(self, image: Image) -> tuple[Image.Image, str, str]:
        pass


    @abstractmethod
    def add_noises(self) -> list[tuple[Image.Image, str, str]]:
        pass

    
    @abstractmethod
    def save_image(self, img_info: tuple[Image.Image, str, str]) -> None:
        pass

    
    @abstractmethod
    def transform_images(self) -> None:
        pass