from PIL import Image, ImageDraw
import numpy as np

from iftg.noises.noise import Noise, Image


class ShadowNoise(Noise):
    """
    A class to apply shadow noise to an image. The shadow is applied based on a polygon drawn on a mask image.
    
    Attributes:
        num_points (int): 
            The number of points used to create the polygon for the shadow mask. Must be at least 2.
        shadow_intensity (float): 
            The intensity of the shadow applied to the image. Ranges from 0 to 1.
    """
 

    def __init__(self,
                 num_points: int = 5,
                 shadow_intensity: float = 0.5,
                ):
        if num_points < 2:
            raise ValueError('num_points should be atleast 2.')
        
        self.num_points = num_points
        self.shadow_intensity = shadow_intensity


    def add_noise(self, image: Image) -> Image:
        """
        Applies shadow noise to the image.

        Parameters:
            image (Image):
                The image to which shadow noise will be applied.

        Returns:
            Image:
                The image with the shadow noise applied.
        """
                
        return self._shadow_noise(image)


    def _shadow_noise(self, image: Image) -> Image:
        width, height = image.size
        mask = Image.new('L', (width, height), 0)
        
        points = [(np.random.randint(0, width-1), np.random.randint(0, height-1)) for _ in range(self.num_points)]
        ImageDraw.Draw(mask).polygon(points, fill=255)
        
        img_array = np.array(image)
        mask_array = np.array(mask)
        
        shadow = img_array * (1 - (mask_array[:,:,np.newaxis] / 255.0) * self.shadow_intensity)
        shadow = np.clip(shadow, 0, 255).astype(img_array.dtype)
        noisy_image = Image.fromarray(shadow, 'RGB')
        
        return noisy_image
        

class RandomShadowNoise(ShadowNoise):
    """
    A class to apply random shadow noise to an image. The number of points and shadow intensity are randomly chosen within specified ranges.

    Attributes:
        num_points_range (tuple[int, int]):
            The range of the number of points used to create the polygon for the shadow mask.
        shadow_intensity_range (tuple[float, float]):
            The range of shadow intensity values.
    """
   

    def __init__(self,
                 num_points_range: tuple[int, int] = (5, 10),
                 shadow_intensity_range: tuple[float, float] = (0.3, 0.7),
                ):
        self.num_points_range = num_points_range
        self.shadow_intensity_range = shadow_intensity_range


    def add_noise(self, image: Image) -> Image:
        """
        Applies random shadow noise to the image by selecting a random number of points and shadow intensity.

        Parameters:
            image (Image): 
                The image to which random shadow noise will be applied.

        Returns:
            Image: 
                The image with the random shadow noise applied.
        """
        
        self.num_points = np.random.randint(*self.num_points_range)
        self.shadow_intensity = np.random.uniform(*self.shadow_intensity_range)

        return super().add_noise(image)