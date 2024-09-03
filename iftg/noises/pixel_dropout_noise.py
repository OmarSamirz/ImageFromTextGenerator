import numpy as np
from PIL import Image, ImageColor

from iftg.noises.noise import Noise


class PixelDropoutNoise(Noise):
    """
    A class to apply pixel dropout noise to an image. 
    Pixel dropout noise simulates the effect of randomly "dropping out" pixels in the image.

    Attributes:
        dropout_prob (float): 
            The probability of a pixel being dropped out.
        pixel_dimensions (tuple[float, float]): 
            The dimensions of the dropout pixels (width, height).
        pixel_color (str): 
            The color of the dropped-out pixels.
    """


    def __init__(self, 
                 dropout_prob: float = 0.1, 
                 pixel_dimensions: tuple[float, float] = (1, 1),
                 pixel_color: str = '#FFFFFF'
                ):
        self.dropout_prob = dropout_prob
        self.pixel_dimensions = pixel_dimensions
        self.pixel_color = pixel_color
        


    def add_noise(self, image: Image) -> Image:
        """
        Applies pixel dropout noise to the image.

        Parameters:
            image (Image):
                The image to which noise will be applied.

        Returns:
            Image: 
                The image with pixel dropout noise applied.
        """
                
        return self._pixeldropout_noise(image)
    

    def _pixeldropout_noise(self, image: Image) -> Image:
        pixel_width, pixel_height = self.pixel_dimensions
        
        image_array = np.array(image)
        
        mask_height = (image_array.shape[0] + pixel_height - 1) // pixel_height
        mask_width = (image_array.shape[1] + pixel_width - 1) // pixel_width
        
        drop_mask = np.random.rand(mask_height, mask_width) < self.dropout_prob
        
        expanded_mask = np.repeat(np.repeat(drop_mask, pixel_height, axis=0), pixel_width, axis=1)
        expanded_mask = expanded_mask[:image_array.shape[0], :image_array.shape[1]]
        
        image_array[expanded_mask] = ImageColor.getrgb(self.pixel_color)
        noisy_img = Image.fromarray(image_array)
        
        return noisy_img
    


class RandomPixelDropoutNoise(PixelDropoutNoise):
    """
    A class to apply random pixel dropout noise to an image. 
    The dropout probability and pixel dimensions are chosen randomly within specified ranges.

    Attributes:
        dropout_prob_range (tuple[float, float]): 
            The range for random selection of the dropout probability.
        pixel_dimensions_range (tuple[float, float]): 
            The range for random selection of pixel dimensions (width, height).
        pixel_color (str): 
            The color of the dropped-out pixels.
    """

    def __init__(self, 
                 dropout_prob_range: tuple[float, float] = (0.1, 0.3), 
                 pixel_dimensions_range: tuple[float, float] = (5, 10),
                 pixel_color: str = '#FFFFFF'
                ):
        self.dropout_prob_range = dropout_prob_range
        self.pixel_dimensions_range = pixel_dimensions_range
        self.pixel_color = pixel_color
        


    def add_noise(self, image: Image) -> Image:
        """
        Applies random pixel dropout noise to the image by selecting a random dropout probability and pixel dimensions.

        Parameters:
            image (Image):
                The image to which noise will be applied.

        Returns:
            Image:
                The image with random pixel dropout noise applied.
        """
                
        self.dropout_prob = np.random.uniform(*self.dropout_prob_range)
        self.pixel_dimensions = (np.random.randint(*self.pixel_dimensions_range), np.random.randint(*self.pixel_dimensions_range))
        
        return super().add_noise(image)