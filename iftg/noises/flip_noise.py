import numpy as np


from iftg.noises.noise import Noise, Image


class FlipNoise(Noise):

    def __init__(self, flip_type: str = 'horizontal'):
        self.flip_type = flip_type

        if flip_type != 'horizontal' and flip_type != 'vertical':
            raise TypeError('You need to input (horizontal or vertical)')
        

    
    def add_noise(self, image: Image) -> Image.Image:
        return self._flip_noise(image)
    

    def _flip_noise(self, image: Image) -> Image.Image:
        flipped_img = image.transpose(Image.FLIP_LEFT_RIGHT if self.flip_type == 'horizontal' 
                                      else Image.FLIP_TOP_BOTTOM
                                     )

        return flipped_img
    

class RandomFlipNoise(Noise):

    def __init__(self):
        super().__init__()

    
    def add_noise(self, image: Image) -> Image.Image:
        return self._random_flip_noise(image)
    

    def _random_flip_noise(self, image: Image) -> Image.Image:
        flip = np.random.randint(0, 2)
        flipped_img = image.transpose(flip)

        return flipped_img