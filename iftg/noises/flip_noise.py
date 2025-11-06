import numpy as np

from typing_extensions import override

from iftg.noises.noise import Noise, Image


class FlipNoise(Noise):
    """
    A class to apply flipping noise to an image. Flipping noise mirrors the image along a specified axis.

    Attributes:
        flip_type (int): 
            The type of flip operation to be applied. 
            - 0: Flip horizontally
            - 1: Flip vertically
    """

    def __init__(
        self,
        flip_type: int = 0
    ) -> None:
        self.flip_type = flip_type

    @override
    def add_noise(self, image: Image.Image) -> Image.Image:
        """
        Applies flipping noise to the image.

        Parameters:
            image (Image): 
                The image to which noise will be applied.

        Returns:
            Image:
                The image with flipping noise applied.
        """
        return self._flip_noise(image)

    def _flip_noise(self, image: Image.Image) -> Image.Image:

        flipped_img = image.transpose(self.flip_type)

        return flipped_img


class RandomFlipNoise(FlipNoise):
    """
    Initializes the RandomFlipNoise. Inherits from FlipNoise with a default flip type.
    """

    def __init__(self) -> None:
        super().__init__()

    @override
    def add_noise(self, image: Image.Image) -> Image.Image:
        """
        Applies random flipping noise to the image by selecting a random flip type.

        Parameters:
            image (Image):
                The image to which noise will be applied.

        Returns:
            Image: 
                The image with random flipping noise applied.
        """

        self.flip_type = np.random.randint(0, 2)

        return super().add_noise(image)
