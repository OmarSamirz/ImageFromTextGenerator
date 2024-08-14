import numpy as np
import albumentations as A

from iftg.noises.noise import Noise, Image


class ShadowNoise(Noise):


    def __init__(self,):
        pass


    def add_noise(self, image: Image) -> Image:
        return self._shadow_noise(image)


    def _shadow_noise(self, image: Image) -> Image:
        img = np.asarray(image)
          
        transform = A.Compose([
            A.RandomShadow(p=1),
        ])
        img = transform(image=img)['image']  
          
        image = Image.fromarray(img)
          
        return image


class RandomShadowNoise(Noise):


    def __init__(self,):
        pass


    def add_noise(self, image: Image) -> Image:
        return self._random_shadow_noise(image)


    def _random_shadow_noise(self, image: Image) -> Image:
        img = np.asarray(image)
          
        transform = A.Compose([
            A.RandomShadow(p=1),
        ])
        img = transform(image=img)['image']  
          
        image = Image.fromarray(img)
          
        return image
