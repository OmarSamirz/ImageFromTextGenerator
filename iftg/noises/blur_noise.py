import numpy as np
from PIL import Image, ImageFilter

from iftg.noises.noise import Noise

class BlurNoise(Noise):
    def __init__(self, blur_radius: float = 2.0):
        self.blur_radius = blur_radius
    

    def add_noise(self, image: Image) -> Image:
        return self._blur_noise(image)


    def _blur_noise(self, image: Image) -> Image:
        gaussian_filter = ImageFilter.GaussianBlur(radius=self.blur_radius)
            
        blured_image = image.filter(gaussian_filter)

        return blured_image


class RandomBlurNoise(BlurNoise):
    def __init__(self, 
                 blur_radius_range: tuple[float, float] = (1.0, 3.0)
                ):
        self.blur_radius_range = blur_radius_range
    

    def add_noise(self, image: Image) -> Image:
        self.blur_radius = np.random.uniform(*self.blur_radius_range)
        
        return super().add_noise(image)

