import os
import glob
import itertools
from functools import reduce

from iftg.adders.noise_adder import NoiseAdder
from iftg.noises.noise import Noise, Image


class DirectoryNoiseAdder(NoiseAdder):
    """
    A class for adding noise to images in a directory and saving the noisy images to a specified output path.
    Inherits from `NoiseAdder` and provides functionality for processing multiple images in a directory.

    Attributes:
        dir_path (str): 
            The path to the directory containing images to be processed.
        output_path (str): 
            The path where the processed images will be saved.
        noises (list[Noise]): 
            A list of noise objects to be applied to the images.
        identifier (str): 
            A unique identifier to append to the filenames of the processed images.
        img_formats (list[str]): 
            A list of image formats to be considered for processing.
        
    """

    
    def __init__(self, 
                 dir_path: str = '',
                 output_path: str = '',
                 noises: list[Noise] = [],
                 identifier: str = 'noisy',
                 img_formats: list[str] = ['jpg', 'png', 'tif'],
                ):
        
        super().__init__(noises, 
                         identifier, 
                         img_formats, 
                        )

        try:
            self.dir_path = dir_path
        except:
            raise FileNotFoundError('The directory does not exist.')
        
        if output_path == '':
            self.output_path = dir_path
        else:
            self.output_path = output_path

        self.images_pathes = list(itertools.chain.from_iterable(
                            glob.iglob(os.path.join(dir_path, f'*.{fmt}')) for fmt in self.img_formats
                            ))
        self._count = 0
    

    def _apply_noises(self, image: Image) -> tuple[Image.Image, str, str]:
        """
        Applies the specified noises to a given image.

        Parameters:
            image (Image): 
                The image to which noises will be applied.

        Returns:
            tuple:
                A tuple containing the noisy image, the base name of the image (without extension), and the image format (including the dot).
        """
        base_name = os.path.basename(self.images_pathes[self._count])
        img_name, img_format = os.path.splitext(base_name)
        noisy_image = reduce(lambda img, noise: noise.add_noise(img), self.noises, image)
        noisy_image.info['dpi'] = image.info['dpi']
        self._count += 1

        return noisy_image, img_name, img_format
        

    def add_noises(self) -> list[tuple[Image.Image, str, str]]:
        """
        Applies noises to all images in the directory.

        Returns:
            list:
                A list of tuples, each containing a noisy image, the base name of the image, and the image format.
        """
        images = [Image.open(img_path) for img_path in self.images_pathes]
        noisy_images = reduce(lambda acc, img: acc + [self._apply_noises(img)], images, [])

        return noisy_images
    

    def save_image(self, img_info: tuple[Image.Image, str, str]) -> None:
        """
        Saves a noisy image to the output path.

        Parameters:
            img_info (tuple[Image, str, str]): 
                A tuple containing the noisy image, the base name of the image, and the image format.
        """
        image, img_name, img_format = img_info
        img_final_name = f'{img_name}_{self.identifier}{img_format}'
        image.save(os.path.join(self.output_path, img_final_name), dpi=image.info['dpi'])


    def transform_images(self) -> None:
        """
        Applies noises to all images and saves the resulting noisy images to the output path.
        """
        transformed_images = self.add_noises()
        # Save images
        list(map(self.save_image, transformed_images))
