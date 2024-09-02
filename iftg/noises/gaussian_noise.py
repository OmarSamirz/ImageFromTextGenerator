import numpy as np

from iftg.noises.noise import Noise, Image


class GaussianNoise(Noise):
    """
    A class to apply Gaussian noise to an image. Gaussian noise is added by generating noise from a normal distribution and adding it to the image.

    Attributes:
        mean (float): 
            The mean of the Gaussian noise distribution.
        sigma (float): 
            The standard deviation of the Gaussian noise distribution.
    """
  

    def __init__(self,
                 mean: float = 0,
                 sigma: float = 40,
                ):
        
        self.mean = mean
        self.sigma = sigma

    def add_noise(self, image: Image) -> Image:
        """
        Applies Gaussian noise to the image.

        Args:
            image (Image): 
                The image to which noise will be applied.

        Returns:
            Image: 
                The image with Gaussian noise applied.
        """

        return self._gaussian_noise(image)


    def _gaussian_noise(self, image: Image) -> Image:
        
        img_array = np.array(image)

        noise = np.random.normal(self.mean, self.sigma, img_array.shape)
        noisy_img_array = img_array + noise
        noisy_img_array = np.clip(noisy_img_array, 0, 255).astype(np.uint8)

        noisy_image = Image.fromarray(noisy_img_array)
        
        return noisy_image
    

class RandomGaussianNoise(GaussianNoise):
    """
    A class to apply random Gaussian noise to an image. The mean and sigma for the Gaussian distribution are chosen randomly within specified ranges.

    Attributes:
        mean_range (tuple[float, float]): 
            The range for random selection of the mean of the Gaussian noise distribution. 
        sigma_range (tuple[float, float]): 
            The range for random selection of the standard deviation of the Gaussian noise distribution.
    """

    def __init__(self,
                 mean_range: tuple[float, float] = (0, 1),
                 sigma_range: tuple[float, float] = (40, 70),
                ):
        
        self.mean_range = mean_range
        self.sigma_range = sigma_range

    def add_noise(self, image: Image) -> Image:
        """
        Applies random Gaussian noise to the image by selecting a random mean and sigma within the specified ranges.

        Parameters:
            image (Image): 
                The image to which noise will be applied.

        Returns:
            Image: 
                The image with random Gaussian noise applied.
        """

        self.mean = np.random.uniform(*self.mean_range)
        self.sigma = np.random.uniform(*self.sigma_range)
        
        return super().add_noise(image)