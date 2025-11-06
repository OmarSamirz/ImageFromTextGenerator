from PIL import Image

from iftg.noises.noise import Noise


class MyNoise(Noise):

    def __init__(self):
        ...

    def add_noise(self, image: Image.Image) -> Image.Image:
        ...

    def _my_noise_function(self, image: Image.Image) -> Image.Image:
        ...
