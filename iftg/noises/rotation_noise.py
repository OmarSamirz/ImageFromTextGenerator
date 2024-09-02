import numpy as np
from PIL import Image, ImageFilter

from iftg.noises.noise import Noise

class RotationNoise(Noise):
    """
    A class to apply rotation noise to an image. 
    The image is rotated by a fixed angle, with options for background color and resampling.

    Attributes:
        rotation_angle (float): 
            The angle by which the image will be rotated.
        background_color (str): 
            The color to use for the background after rotation.
    """


    def __init__(self,
                 rotation_angle: float = 30.0,
                 background_color: str = 'white',
                ):
        self.rotation_angle = rotation_angle
        self.background_color = background_color
    

    def add_noise(self, image: Image) -> Image:
        """
        Applies rotation noise to the image.

        Parameters:
            image (Image): 
                The image to which noise will be applied.

        Returns:
            Image: 
                The rotated image with the applied background color.
        """
        return self._rotation_noise(image)


    def _rotation_noise(self, image: Image) -> Image:
        rotated_image = image.rotate(angle=self.rotation_angle,
                                     resample=Image.Resampling.BICUBIC, 
                                     fillcolor=self.background_color,
                                     expand=True
                                    )

        return rotated_image


class RandomRotationNoise(RotationNoise):
    """
    A class to apply random rotation noise to an image. 
    The rotation angle is chosen randomly within a specified range.

    Attributes:
        rotation_angle_range (tuple[float, float]): 
            The range within which the rotation angle will be randomly selected.
        background_color (str): 
            The color to use for the background after rotation.
    """


    def __init__(self, 
                 rotation_angle_range: tuple[float, float] = (-50.0, 50.0),
                 background_color: str = 'white',
                ):
        self.rotation_angle_range = rotation_angle_range
        self.background_color = background_color
    

    def add_noise(self, image: Image) -> Image:
        """
        Applies random rotation noise to the image by selecting a random angle within the specified range.

        Parameters:
            image (Image): 
                The image to which noise will be applied.

        Returns:
            Image: 
                The image rotated by a random angle within the specified range.
        """
        
        self.rotation_angle = np.random.uniform(*self.rotation_angle_range)

        return super().add_noise(image)

