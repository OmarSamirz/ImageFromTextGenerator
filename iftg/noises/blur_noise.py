import numpy as np
from PIL import Image, ImageFilter

from iftg.noises.noise import Noise

class BlurNoise(Noise):
    """
    A class to apply Gaussian blur noise to an image.

    Attributes:
        blur_radius (float): 
            The radius of the Gaussian blur to be applied. 
            A higher value results in a more blurred image.
    """


    def __init__(self, 
                 blur_radius: float = 2.0
                ):
        self.blur_radius = blur_radius
    

    def add_noise(self, image: Image) -> Image:
        """
        Applies Gaussian blur noise to the input image.

        Parameters:
            image (Image): 
                The input image to which noise will be added.

        Returns:
            Image:
                The image with Gaussian blur applied.
        """

        return self._blur_noise(image)


    def _blur_noise(self, image: Image) -> Image:
        gaussian_filter = ImageFilter.GaussianBlur(radius=self.blur_radius)
            
        blured_image = image.filter(gaussian_filter)

        return blured_image


class RandomBlurNoise(BlurNoise):
    """
    A class to apply Gaussian blur noise with a random blur radius to an image.

    Attributes:
        blur_radius_range : tuple[float, float]
            A tuple representing the range within which the blur radius will be randomly selected.
    """

    def __init__(self, 
                 blur_radius_range: tuple[float, float] = (1.0, 3.0)
                ):
        self.blur_radius_range = blur_radius_range
    

    def add_noise(self, image: Image) -> Image:
        """
        Applies Gaussian blur noise with a random radius to the input image.

        Parameters:
            image (Image): 
                The input image to which noise will be added.

        Returns:
            Image:
                The image with random Gaussian blur applied.
        """

        self.blur_radius = np.random.uniform(*self.blur_radius_range)
        
        return super().add_noise(image)

