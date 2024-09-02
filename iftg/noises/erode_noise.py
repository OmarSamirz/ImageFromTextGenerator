import cv2
import numpy as np
from iftg.noises.noise import Noise, Image

class ErodeNoise(Noise):
    """
    A class to apply erosion noise to an image. Erosion noise shrinks the white regions of the image
    by applying morphological erosion using a structuring element (kernel).

    Attributes:
        kernel_size (int): 
            The size of the structuring element (kernel) used for erosion.
        iterations (int): 
            The number of times the erosion operation is applied.
    """

    def __init__(self,
                 kernel_size: int = 3,
                 iterations: int = 1,
                ):
        
        self.kernel_size = kernel_size
        self.iterations = iterations


    def add_noise(self, image: Image) -> Image:
        """
        Applies erosion noise to the image.

        Parameters:
            image (Image): 
                The image to which noise will be applied.

        Returns:
            Image: 
                The image with erosion noise applied.
        """
        return self._erode_noise(image)


    def _erode_noise(self, image: Image) -> Image:
        img_array = np.array(image)
        
        kernel = np.ones((self.kernel_size, self.kernel_size), np.uint8)
        noisy_img_array = cv2.erode(img_array, kernel, iterations=self.iterations)

        eroded_image = Image.fromarray(noisy_img_array)
        
        return eroded_image



class RandomErodeNoise(ErodeNoise):
    """
    A class to apply random erosion noise to an image. The kernel size and number of iterations
    are chosen randomly within specified ranges.

    Attributes:
        kernel_size_range (tuple[int, int]): 
            The range of kernel sizes to choose from for erosion.
        iterations_range (tuple[int, int]): 
            The range of iteration counts to choose from for erosion.
    """

    def __init__(self,
                 kernel_size_range: tuple[int, int] = (3, 5),
                 iterations_range: tuple[int, int] = (1, 2),
                ):
        
        self.kernel_size_range = kernel_size_range
        self.iterations_range = iterations_range


    def add_noise(self, image: Image) -> Image:
        """
        Applies random erosion noise to the image by selecting random kernel size and number of iterations.

        Parameters:
            image (Image): 
                The image to which noise will be applied.

        Returns:
            Image: 
                The image with random erosion noise applied.
        """
                
        self.kernel_size = np.random.randint(*self.kernel_size_range)
        self.iterations = np.random.randint(*self.iterations_range)
        
        return super().add_noise(image)
