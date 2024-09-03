
from PIL import Image
from iftg.noises.noise import Noise

class MyNoise(Noise):

    def __init__(self):
        pass


    def add_noise(self, image: Image) -> Image:
        pass


    def _my_noise_function(self, image: Image) -> Image:
        pass