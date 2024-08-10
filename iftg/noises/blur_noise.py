import numpy as np
import albumentations as A
from iftg.noises.noise import Noise, Image


class BlurNoise(Noise):

    def __init__(self, blur_limit: float = 2.0):
        self.blur_limit = blur_limit

    def add_noise(self, image: Image) -> Image:
        return self._blur_noise(image)


    def _blur_noise(self, image: Image) -> Image:
        img_array = np.array(image)     #convert to numpy
        transform = A.Compose([A.Blur(blur_limit=self.blur_limit, p=1)])
        
        img_array = transform(image=img_array)['image']  
        image = Image.fromarray(img_array)   
        
        return image



