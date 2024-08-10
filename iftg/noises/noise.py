from abc import ABC, abstractmethod
from PIL import Image, ImageDraw, ImageFont

class Noise(ABC):
    
    
    @abstractmethod
    def add_noise(self,
                  image: Image,
                  ) -> Image:
        pass

