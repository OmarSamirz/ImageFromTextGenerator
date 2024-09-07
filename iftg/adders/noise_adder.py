
import os
from abc import ABC, abstractmethod


from iftg.noises.noise import Noise, Image


class NoiseAdder(ABC):
    """
    An abstract base class for adding noise to images. Subclasses must implement the methods 
    for applying noise, adding noises, saving images, and transforming images.

    Attributes:
        noises (list[Noise]): 
            A list of noise objects to be applied to the images.
        output_path (str): 
            The path where the processed images will be saved.
        identifier (str): 
            A unique identifier to append to the filenames of the processed images.
    """

    def __init__(self, 
                 noises: list[Noise],
                 output_path: str,
                 identifier: str,
                ):
        self.noises = noises
        self.output_path = output_path
        self.identifier = identifier

    
    @abstractmethod
    def _apply_noises(self, image: Image) -> tuple[Image.Image, str, str]:
        pass


    @abstractmethod
    def add_noises(self) -> tuple[Image.Image, str, str] | list[tuple[Image.Image, str, str]]:
        pass


    @abstractmethod
    def save_image(self, img_info: tuple[Image.Image, str, str]) -> None:
        image, img_name, img_format = img_info
        img_final_name = f'{img_name}_{self.identifier}{img_format}'
        image.save(os.path.join(self.output_path, img_final_name), dpi=image.info['dpi'])

    