from PIL import Image
from abc import ABC, abstractmethod

class Noise(ABC):
    
    
    @abstractmethod
    def add_noise(self,
                  image: Image,
                  ) -> Image:
        pass
