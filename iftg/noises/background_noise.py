

from iftg.noises.noise import Noise, Image


class BackgroundNoise(Noise):


    def __init__(self):
        pass


    def add_noise(self, image: Image) -> Image.Image:
        return self._background_noise(image)
    
    def _background_noise(self, image: Image) -> Image.Image:
        pass