import cv2
import numpy as np
from iftg.noises.noise import Noise, Image

class ErodeNoise(Noise):


    def __init__(self,
                 kernel_size: float = 3,
                 iterations: float = 1,
                ):
        
        self.kernel_size = kernel_size
        self.iterations = iterations


    def add_noise(self, image: Image) -> Image:
        return self._erode_noise(image)


    def _erode_noise(self, image: Image) -> Image:
        img_array = np.array(image)
        
        kernel = np.ones((self.kernel_size, self.kernel_size), np.uint8)
        noisy_img_array = cv2.erode(img_array, kernel, iterations=self.iterations)

        dilated_image = Image.fromarray(noisy_img_array)
        
        return dilated_image
