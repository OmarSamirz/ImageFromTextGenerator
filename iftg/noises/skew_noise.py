

from iftg.noises.noise import Noise, Image


class SkewNoise(Noise):


    def __init__(self):
        pass


    def add_noise(self, image: Image) -> Image:
        return self._skew_noise(image)


    def _skew_noise(self, image: Image) -> Image:
        pass


class RandomSkewNoise(SkewNoise):


    def __init__(self):
        pass


    def add_noise(self, image: Image) -> Image:

        return super().add_noise(image)