import numpy as np
from PIL import Image

from iftg.noises.noise import Noise


class PixelateNoise(Noise):
    """
    A class to apply pixelation noise to an image.
    The image is divided into blocks and each block is replaced with its average color.

    Attributes:
        noise_intensity (int):
            The size of pixelation blocks. Larger values create more pronounced pixelation.
    """

    def __init__(self, noise_intensity: int = 2):
        self.noise_intensity = noise_intensity

    def add_noise(self, image: Image) -> Image:
        """
        Applies pixelation noise to the image.

        Parameters:
            image (Image):
                The image to which noise will be applied.

        Returns:
            Image:
                The pixelated version of the input image.

        Raises:
            ValueError: If noise_intensity is less than 1.
        """
        return self._pixelate_noise(image)

    def _pixelate_noise(self, image: Image) -> Image:
        if self.noise_intensity < 1:
            raise ValueError("Window size must be positive")

        img = np.array(image)
        orig_height, orig_width = img.shape[:2]

        pad_height = (self.noise_intensity - (orig_height %
                      self.noise_intensity)) % self.noise_intensity
        pad_width = (self.noise_intensity - (orig_width %
                     self.noise_intensity)) % self.noise_intensity

        if pad_height > 0 or pad_width > 0:
            padding = ((0, pad_height), (0, pad_width), (0, 0))
            img = np.pad(img, padding, mode='edge')

        # Get new dimensions after padding
        n, m, c = img.shape
        reshaped = img.reshape(n//self.noise_intensity, self.noise_intensity,
                               m//self.noise_intensity, self.noise_intensity, c)
        means = reshaped.mean(axis=(1, 3))

        pixelated = np.repeat(
            np.repeat(means, self.noise_intensity, axis=0), self.noise_intensity, axis=1)
        pixelated = pixelated[:orig_height, :orig_width].astype(np.uint8)

        return Image.fromarray(pixelated)


class RandomPixelateNoise(PixelateNoise):
    """
    A class to apply random pixelation noise to an image.
    The pixelation intensity is chosen randomly within a specified range.

    Attributes:
        noise_intensity_range (tuple[int, int]):
            The range within which the pixelation intensity will be randomly selected.
    """

    def __init__(self, noise_intensity_range: tuple[int, int] = (2, 5)):
        self.noise_intensity_range = noise_intensity_range

    def add_noise(self, image: Image) -> Image:
        """
        Applies random pixelation noise to the image by selecting a random intensity within the specified range.

        Parameters:
            image (Image):
                The image to which noise will be applied.

        Returns:
            Image:
                The image pixelated with a random intensity within the specified range.
        """
        self.noise_intensity = np.random.randint(*self.noise_intensity_range)

        return super().add_noise(image)
