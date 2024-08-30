import numpy as np

from iftg.noises.noise import Noise, Image


class BrightnessNoise(Noise):


    def __init__(self, 
                 birghtness_factor: float = 0.8
                ):
        self.brightness_factor = birghtness_factor


    def add_noise(self, image: Image) -> Image.Image:
        return self._brightness_noise(image)

    
    def _brightness_noise(self, image: Image) -> Image.Image:
        noisy_image = image.point(lambda p: min(255, int(p * self.brightness_factor)))

        return noisy_image



class RandomBrightnessNoise(Noise):


    def __init__(self, 
                 brightness_factor_range: tuple[float, float] = (0.5, 1.0)
                ):
        self.brightness_factor_range = brightness_factor_range


    def add_noise(self, image: Image) -> Image.Image:
        return self._random_brightness_noise(image)

    
    def _random_brightness_noise(self, image: Image) -> Image.Image:
        brightness_factor = np.random.uniform(*self.brightness_factor_range)

        noisy_image = image.point(lambda p: min(255, int(p * brightness_factor)))

        return noisy_image