import os
import glob
import itertools
from functools import reduce

from iftg.adder.noise_adder import NoiseAdder
from iftg.noises.noise import Noise, Image


class DirectoryNoiseAdder(NoiseAdder):

    
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
        self.count = 0
    

    def _apply_noises(self, image: Image) -> tuple[Image.Image, str, str]:
        base_name = os.path.basename(self.images_pathes[self.count])
        img_name, img_format = os.path.splitext(base_name)

        self.count += 1
        return (reduce(lambda img, noise: noise.add_noise(img), self.noises, image), img_name, img_format)
        

    def _add_noises(self) -> list[tuple[Image.Image, str, str]]:
        images = [Image.open(img_path) for img_path in self.images_pathes]
        noisy_images = reduce(lambda acc, img: acc + [self._apply_noises(img)], images, [])

        return noisy_images
    

    def _save_images(self, img_info: tuple[Image.Image, str, str]) -> None:
        image, img_name, img_format = img_info
        img_final_name = f'{img_name}_{self.identifier}{img_format}'
        image.save(os.path.join(self.output_path, img_final_name))            
        

    def transform_images(self) -> None:
        transformed_images = self._add_noises()
        # Save images
        list(map(self._save_images, transformed_images))        




