from PIL import Image, ImageDraw
import numpy as np

from iftg.noises.noise import Noise, Image


class ShadowNoise(Noise):


    def __init__(self,
                 num_points: int = 5,
                 shadow_intensity: float = 0.5,
                ):
        if num_points < 2:
            raise ValueError('num_points should be atleast 2.')
        
        self.num_points = num_points
        self.shadow_intensity = shadow_intensity


    def add_noise(self, image: Image) -> Image:
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


    def __init__(self,
                 num_points_range: tuple[int, int] = (5, 10),
                 shadow_intensity_range: tuple[float, float] = (0.3, 0.7),
                ):
        self.num_points_range = num_points_range
        self.shadow_intensity_range = shadow_intensity_range


    def add_noise(self, image: Image) -> Image:
        self.num_points = np.random.randint(*self.num_points_range)
        self.shadow_intensity = np.random.uniform(*self.shadow_intensity_range)

        return super().add_noise(image)