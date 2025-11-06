from PIL import Image

from typing_extensions import override

from iftg.noises.noise import Noise


class SkewNoise(Noise):

    def __init__(self) -> None:
        ...

    @override
    def add_noise(self, image: Image.Image) -> Image.Image:
        return self._skew_noise(image)

    def _skew_noise(self, image: Image.Image) -> Image.Image:
        ...


class RandomSkewNoise(SkewNoise):

    def __init__(self) -> None:
        ...

    @override
    def add_noise(self, image: Image.Image) -> Image.Image:
        return super().add_noise(image)
