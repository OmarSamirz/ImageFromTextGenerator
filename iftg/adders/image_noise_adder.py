
import os
from functools import reduce

from iftg.adders.noise_adder import NoiseAdder
from iftg.noises.noise import Noise, Image


class ImageNoiseAdder(NoiseAdder):
    """
    A class to add noise to an image and save the noisy image to a specified output path.

    Attributes:
        img_path (str): 
            Path to the input image file.
        output_path (str): 
            Directory where the noisy image will be saved. Default is an empty string.
        noises (list[Noise]):
            List of noise objects to be applied to the image.
        identifier (str):
            Identifier for the noisy image file. Default is 'noisy'.
    """
    
    def __init__(self,
                 img_path: str,
                 output_path: str = '',
                 noises: list[Noise] = [],
                 identifier: str = 'noisy',
                ):
        
        if os.path.exists(img_path) == True:
            self.img_path = img_path
        else:
            raise FileNotFoundError('The image does not exist.')

        if output_path == '':
            output_path = os.path.dirname(img_path)
        

        super().__init__(noises,
                         output_path,
                         identifier,
                        )
        
    
    def _apply_noises(self, image: Noise) -> tuple[Image.Image, str, str]:
        """
        Applies the specified noises to a given image.

        Parameters:
            image (Image): 
                The image to which noises will be applied.

        Returns:
            tuple:
                A tuple containing the noisy image, the base name of the image (without extension), and the image format (including the dot).
        """
        base_name = os.path.basename(self.img_path)
        img_name, img_format = os.path.splitext(base_name)

        noisy_image = reduce(lambda img, noise: noise.add_noise(img), self.noises, image)

        if 'dpi' in image.info:
            noisy_image.info['dpi'] = image.info['dpi']
        else:
            noisy_image.info['dpi'] = (300, 300)

        return noisy_image, img_name, img_format


    def add_noises(self) -> tuple[Image.Image, str, str]:
        """
        Applies noises to the image specified by the image path.

        Returns:
            list:
                A list of tuples, each containing a noisy image, the base name of the image, and the image format.
        """
        image = Image.open(self.img_path)

        noisy_image = self._apply_noises(image)

        return noisy_image


    def save_image(self, img_info: tuple[Image.Image, str, str]) -> None:
        """
        Saves a noisy image to the output path.

        Parameters:
            img_info (tuple[Image, str, str]): 
                A tuple containing the noisy image, the base name of the image, and the image format.
        """
        super().save_image(img_info)

    
    def transform_image(self) -> None:
        """
        Applies noises to image and saves the resulting noisy image to the output path.
        """

        transformed_image = self.add_noises()

        self.save_image(transformed_image)


        