from PIL import Image
from abc import ABC, abstractmethod

class Generator(ABC):
    
    def __init__(self,
                 texts,
                 noises,
                 font_path,
                 font_size,
                 font_color,
                 background_color,
                 margins,
                 img_name,
                 img_format,
                 img_output_path,
                 txt_name,
                 txt_format,
                 txt_output_path,
                 clear_fonts
                ):
        self.texts = texts
        self.noises = noises
        self.font_path = font_path
        self.font_size = font_size
        self.font_color = font_color
        self.background_color = background_color
        self.margins = margins
        self.img_name = img_name
        self.img_format = img_format
        self.img_output_path = img_output_path
        self.txt_name = txt_name
        self.txt_format = txt_format
        self.txt_output_path = txt_output_path
        self.clear_fonts = clear_fonts
        
        self._texts_len = len(texts)
        self._count = 0


    def __iter__(self):
        return self


    def __next__(self):
        return self.next()


    @abstractmethod
    def generate_images(self) -> bool:
        pass

    
    @abstractmethod
    def generate_images_with_text(self) -> bool:
        pass



    