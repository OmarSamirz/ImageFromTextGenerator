import cv2
import numpy as np

from iftg.noises.noise import Noise, Image


class DilateNoise(Noise):
    """
    A class to apply dilation noise to an image. Dilation noise enlarges the white regions of the image
    by applying morphological dilation using a structuring element (kernel).

    Attributes:
        kernel_size (int): 
            The size of the structuring element (kernel) used for dilation.
        iterations (int): 
            The number of times the dilation operation is applied.
    """


    def __init__(self,
                 kernel_size: int = 3,
                 iterations: int = 1,
                ):
        
        self.kernel_size = kernel_size
        self.iterations = iterations


    def add_noise(self, image: Image) -> Image:
        """
        Applies dilation noise to the image.

        Parameters:
            image (Image): 
                The image to which noise will be applied.

        Returns:
            Image: 
                The image with dilation noise applied.
        """
        return self._dilate_noise(image)


    def _dilate_noise(self, image: Image) -> Image:
        img_array = np.array(image)
        
        kernel = np.ones((self.kernel_size, self.kernel_size), np.uint8)
        noisy_img_array = cv2.dilate(img_array, kernel, iterations=self.iterations)

        dilated_image = Image.fromarray(noisy_img_array)
        
        return dilated_image
    

class RandomDilateNoise(DilateNoise):   
    """
    A class to apply random dilation noise to an image. The kernel size and number of iterations
    are chosen randomly within specified ranges.

    Attributes:
        kernel_size_range (tuple[int, int]): 
            The range of kernel sizes to choose from for dilation.
        iterations_range (tuple[int, int]): 
            The range of iteration counts to choose from for dilation.
    """


    def __init__(self,
                 kernel_size_range: tuple[int, int] = (2, 5),
                 iterations_range: tuple[int, int] = (1, 1),
                ):
        
        self.kernel_size_range = kernel_size_range
        self.iterations_range = iterations_range


    def add_noise(self, image: Image) -> Image:
        """
        Applies random dilation noise to the image by selecting random kernel size and number of iterations.

        Parameters:
            image (Image): 
                The image to which noise will be applied.

        Returns:
            Image: 
                The image with random dilation noise applied.
        """
        self.kernel_size = np.random.randint(self.kernel_size_range[0], self.kernel_size_range[1])
        self.iterations = np.random.randint(self.iterations_range[0], self.iterations_range[1])
        
        return super().add_noise(image)