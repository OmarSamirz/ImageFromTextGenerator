import numpy as np

from iftg.noises.noise import Noise, Image


class BrightnessNoise(Noise):
    """
    A class to apply a brightness adjustment to an image. The brightness is scaled by a fixed factor.

    Attributes:
        brightness_factor (float): 
            The factor by which the brightness of the image will be scaled.
    """


    def __init__(self, 
                 birghtness_factor: float = 0.8
                ):
        self.brightness_factor = birghtness_factor


    def add_noise(self, image: Image) -> Image:
        """
        Applies the brightness noise to the image.

        Parameters:
            image (Image):
                The image to which noise will be applied.

        Returns:
            Image: 
                The image with brightness noise applied.
        """
        return self._brightness_noise(image)

    
    def _brightness_noise(self, image: Image) -> Image:
        noisy_image = image.point(lambda p: min(255, int(p * self.brightness_factor)))

        return noisy_image



class RandomBrightnessNoise(BrightnessNoise):
    """
    A class to apply a random brightness adjustment to an image. The brightness is scaled by a factor 
    selected from a specified range.

    Attributes:
        brightness_factor_range (tuple[float, float]): 
            The range of brightness factors to choose from randomly.
    """

    def __init__(self, 
                 brightness_factor_range: tuple[float, float] = (0.5, 1.0)
                ):
        self.brightness_factor_range = brightness_factor_range


    def add_noise(self, image: Image) -> Image:
        """
        Applies a random brightness noise to the image by selecting a brightness factor from the specified range.

        Parameters:
            image (Image):
                The image to which noise will be applied.

        Returns:
            Image: 
                The image with random brightness noise applied.
        """
        self.brightness_factor = np.random.uniform(*self.brightness_factor_range)

        return super().add_noise(image)
