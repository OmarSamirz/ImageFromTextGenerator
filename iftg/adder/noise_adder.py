from abc import ABC, abstractmethod

from iftg.noises.noise import Noise, Image


class NoiseAdder(ABC):
    

    def __init__(self, 
                 noises: list[Noise],
                 identifier: str,
                 img_formats: list[str],
                ):
        self.identifier = identifier
        self.img_formats = img_formats
        self.noises = noises

    
    @abstractmethod
    def _apply_noises(self, image: Image) -> list[Image.Image]:
        pass


    @abstractmethod
    def _add_noises(self):
        pass

    
    @abstractmethod
    def _save_images(self):
        pass

    
    @abstractmethod
    def transform_images(self):
        pass