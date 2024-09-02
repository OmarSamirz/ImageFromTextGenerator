import numpy as np


from iftg.noises.noise import Noise, Image


class FlipNoise(Noise):

    def __init__(self, 
                 flip_type: int = 0
                ):
        self.flip_type = flip_type
        

    
    def add_noise(self, image: Image) -> Image.Image:
        return self._flip_noise(image)
    

    def _flip_noise(self, image: Image) -> Image.Image:

        flipped_img = image.transpose(self.flip_type)

        return flipped_img
    

class RandomFlipNoise(FlipNoise):

    def __init__(self):
        super().__init__()

    
    def add_noise(self, image: Image) -> Image.Image:
        self.flip_type = np.random.randint(0, 2)

        return super().add_noise(image)
    