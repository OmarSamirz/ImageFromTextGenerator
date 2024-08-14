import numpy as np
from PIL import Image, ImageFilter

from iftg.noises.noise import Noise

class RotationNoise(Noise):
    def __init__(self,
                 rotation_angle: float = 30.0,
                 background_color: str = 'white',
                ):
        self.rotation_angle = rotation_angle
        self.background_color = background_color
    

    def add_noise(self, image: Image) -> Image:
        return self._rotation_noise(image)


    def _rotation_noise(self, image: Image) -> Image:
        rotated_image = image.rotate(angle=self.rotation_angle,
                                     resample=Image.Resampling.BICUBIC, 
                                     fillcolor=self.background_color,
                                     expand=True
                                    )

        return rotated_image


class RandomRotationNoise(Noise):


    def __init__(self, 
                 rotation_angle_range: tuple[float, float] = (-50.0, 50.0),
                 background_color: str = 'white',
                ):
        self.rotation_angle_range = rotation_angle_range
        self.background_color = background_color
    

    def add_noise(self, image: Image) -> Image:
        return self._rotation_noise(image)


    def _rotation_noise(self, image: Image) -> Image:
        rotation_angle = np.random.uniform(*self.rotation_angle_range)

        rotated_image = image.rotate(angle=rotation_angle,
                                     resample=Image.Resampling.BICUBIC, 
                                     fillcolor=self.background_color,
                                     expand=True
                                    )

        return rotated_image

