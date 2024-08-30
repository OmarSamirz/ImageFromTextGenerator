import numpy as np
from scipy.ndimage import gaussian_filter, map_coordinates

from iftg.noises.noise import Noise, Image


class ElasticNoise(Noise):
    

    def __init__(self,
                 alpha: float = 10.0,
                 sigma: float = 2.0,
                ):
        self.alpha = alpha
        self.sigma = sigma


    def add_noise(self, image: Image) -> Image.Image:
        return self._elastic_noise(image)
    

    def _elastic_noise(self, image: Image) -> Image.Image:

        shape = np.array(image).shape
        dx = gaussian_filter((np.random.RandomState(None).rand(*shape[:2]) * 2 - 1), self.sigma) * self.alpha
        dy = gaussian_filter((np.random.RandomState(None).rand(*shape[:2]) * 2 - 1), self.sigma) * self.alpha

        x, y = np.meshgrid(np.arange(shape[1]), np.arange(shape[0]))
        indices = np.reshape(y+dy, (-1, 1)), np.reshape(x+dx, (-1, 1))

        distorted = np.array(image)
        if len(shape) == 3:
            for c in range(shape[2]):
                distorted[:,:,c] = map_coordinates(distorted[:,:,c], indices, order=1, mode='reflect').reshape(shape[:2])
        else:
            distorted = map_coordinates(distorted, indices, order=1, mode='reflect').reshape(shape[:2])

        return Image.fromarray(np.clip(distorted, 0, 255).astype(np.uint8))
    

class RandomElasticNoise(ElasticNoise):
    
    
    def __init__(self,
                 alpha_range: tuple[float, float] = (10.0, 20.0),
                 sigma_range: tuple[float, float] = (2.0, 4.0),
                ):
        self.alpha_range = alpha_range
        self.sigma_range = sigma_range


    def add_noise(self, image: Image) -> Image.Image:
        self.alpha = np.random.uniform(*self.alpha_range)
        self.sigma = np.random.uniform(*self.sigma_range)
        
        return super().add_noise(image)
