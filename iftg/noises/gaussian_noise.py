import numpy as np

from iftg.noises.noise import Noise, Image


class GaussianNoise(Noise):

    def __init__(self,
                 mean: float = 0,
                 sigma: float = 40,
                ):
        
        self.mean = mean
        self.sigma = sigma

    def add_noise(self, image: Image) -> Image:
        return self._gaussian_noise(image)


    def _gaussian_noise(self, image: Image) -> Image:
        
        img_array = np.array(image)

        noise = np.random.normal(self.mean, self.sigma, img_array.shape)
        noisy_img_array = img_array + noise
        noisy_img_array = np.clip(noisy_img_array, 0, 255).astype(np.uint8)

        noisy_image = Image.fromarray(noisy_img_array)
        
        return noisy_image
    

class RandomGaussianNoise(GaussianNoise):

    def __init__(self,
                 mean_range: tuple[float, float] = (0, 1),
                 sigma_range: tuple[float, float] = (40, 70),
                ):
        
        self.mean_range = mean_range
        self.sigma_range = sigma_range

    def add_noise(self, image: Image) -> Image:
        self.mean = np.random.uniform(*self.mean_range)
        self.sigma = np.random.uniform(*self.sigma_range)
        
        return super().add_noise(image)