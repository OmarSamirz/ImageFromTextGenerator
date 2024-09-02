import cv2
import numpy as np
from iftg.noises.noise import Noise, Image

class ErodeNoise(Noise):


    def __init__(self,
                 kernel_size: int = 3,
                 iterations: int = 1,
                ):
        
        self.kernel_size = kernel_size
        self.iterations = iterations


    def add_noise(self, image: Image) -> Image:
        return self._erode_noise(image)


    def _erode_noise(self, image: Image) -> Image:
        img_array = np.array(image)
        
        kernel = np.ones((self.kernel_size, self.kernel_size), np.uint8)
        noisy_img_array = cv2.erode(img_array, kernel, iterations=self.iterations)

        eroded_image = Image.fromarray(noisy_img_array)
        
        return eroded_image



class RandomErodeNoise(ErodeNoise):


    def __init__(self,
                 kernel_size_range: tuple[int, int] = (3, 5),
                 iterations_range: tuple[int, int] = (1, 1),
                ):
        
        self.kernel_size_range = kernel_size_range
        self.iterations_range = iterations_range


    def add_noise(self, image: Image) -> Image:
        self.kernel_size = np.random.randint(self.kernel_size_range[0], self.kernel_size_range[1])
        self.iterations = np.random.randint(self.iterations_range[0], self.iterations_range[1])
        
        return super().add_noise(image)
