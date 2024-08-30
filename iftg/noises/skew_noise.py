

from iftg.noises.noise import Noise, Image


class SkewNoise(Noise):


    def __init__(self):
        pass


    def add_noise(self, image: Image) -> Image.Image:
        return self._skew_noise(image)


    def _skew_noise(self, image: Image) -> Image.Image:
        pass


class RandomSkewNoise(Noise):


    def __init__(self):
        pass


    def add_noise(self, image: Image) -> Image.Image:
        return self._random_skew_noise(image)


    def _random_skew_noise(self, image: Image) -> Image.Image:
        pass