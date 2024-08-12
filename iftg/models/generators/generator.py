from PIL import Image
from abc import abstractmethod
from iftg.models.base_model import BaseModel

class Generator(BaseModel):
    
    def __init__(self, 
                 texts,
                 noises,
                 blur_radius,
                 random_blur,
                 min_blur,
                 max_blur,
                 rotation_angle,
                 random_rotation,
                 min_rotation,
                 max_rotation,
                 font_path,
                 font_size,
                 font_color,
                 background_color,
                 margins,
                 clear_fonts
                 ):
        super().__init__(noises, 
                         blur_radius,
                         random_blur,
                         min_blur,
                         max_blur,
                         rotation_angle,
                         random_rotation,
                         min_rotation,
                         max_rotation,
                         font_path,
                         font_size,
                         font_color,
                         background_color,
                         margins,
                         clear_fonts
                        )
        
        self.texts = texts
        self._texts_len = len(texts)
        self._count = 0


    def __iter__(self):
        return self


    def __next__(self):
        return self.next()


    @abstractmethod
    def _generate_next_image(self) -> tuple[Image.Image, str]:
        pass


    @abstractmethod
    def _generate_images(self) -> tuple[Image.Image, str]:
        pass



    