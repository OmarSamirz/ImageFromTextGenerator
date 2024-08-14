import cv2
import numpy as np

from iftg.noises.noise import Noise, Image


class DilateNoise(Noise):


    def __init__(self,
                 kernel_size: int = 3,
                 iterations: int = 1,
                ):
        
        self.kernel_size = kernel_size
        self.iterations = iterations


    def add_noise(self, image: Image) -> Image:
        return self._dilate_noise(image)


    def _dilate_noise(self, image: Image) -> Image:
        img_array = np.array(image)
        
        kernel = np.ones((self.kernel_size, self.kernel_size), np.uint8)
        noisy_img_array = cv2.dilate(img_array, kernel, iterations=self.iterations)

        dilated_image = Image.fromarray(noisy_img_array)
        
        return dilated_image
    

class RandomDilateNoise(Noise):

    def __init__(self,
                 kernel_size_range: tuple[int, int] = (2, 5),
                 iterations_range: tuple[int, int] = (1, 1),
                ):
        
        self.kernel_size_range = kernel_size_range
        self.iterations_range = iterations_range


    def add_noise(self, image: Image) -> Image:
        return self._random_dilate_noise(image)


    def _random_dilate_noise(self, image: Image) -> Image:
        img_array = np.array(image)
        
        kernel_size = np.random.randint(self.kernel_size_range[0], self.kernel_size_range[1])
        iterations = np.random.randint(self.iterations_range[0], self.iterations_range[1])

        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        noisy_img_array = cv2.dilate(img_array, kernel, iterations=iterations)

        dilated_image = Image.fromarray(noisy_img_array)
        
        return dilated_image