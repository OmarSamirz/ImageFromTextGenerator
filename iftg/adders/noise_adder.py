from PIL import Image

import os
from abc import ABC, abstractmethod
from typing import List, Tuple, Union

from iftg.noises.noise import Noise


class NoiseAdder(ABC):
    """
    An abstract base class for adding noise to images. Subclasses must implement the methods 
    for applying noise, adding noises, saving images, and transforming images.

    Attributes:
        noises (List[Noise]): 
            A list of noise objects to be applied to the images.
        output_path (str): 
            The path where the processed images will be saved.
        identifier (str): 
            A unique identifier to append to the filenames of the processed images.
    """

    def __init__(
        self,
        noises: List[Noise],
        output_path: str,
        identifier: str,
    ) -> None:
        self.noises = noises
        self.output_path = output_path
        self.identifier = identifier
        if os.path.exists(self.output_path) == False:
            os.makedirs(self.output_path, exist_ok=True)

    @abstractmethod
    def _apply_noises(self, image: Image.Image) -> Tuple[Image.Image, str, str]:
        ...

    @abstractmethod
    def add_noises(self) -> Union[Tuple[Image.Image, str, str], List[Tuple[Image.Image, str, str]]]:
        ...

    @abstractmethod
    def save_image(self, img_info: Tuple[Image.Image, str, str]) -> None:
        image, img_name, img_format = img_info
        img_final_name = f'{img_name}_{self.identifier}{img_format}'
        image.save(
            os.path.join(self.output_path, img_final_name),
            dpi=image.info['dpi']
        )
