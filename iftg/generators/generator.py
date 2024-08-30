from abc import ABC, abstractmethod

from iftg.noises.noise import Noise

class Generator(ABC):
    
    def __init__(self,
                 texts: list[str] | list[list[str]],
                 noises: list[Noise] | list[list[Noise]],
                 font_path: str | list[str],
                 font_size: float | list[float],
                 font_color: str | list[str],
                 background_color: str | list[str],
                 margins: tuple[int, int, int, int] | list[tuple[int, int, int, int]],
                 dpi: tuple[int, int] | list[tuple[int, int]],
                 img_name: str | list[str],
                 img_format: str | list[str],
                 img_output_path: str | list[str],
                 txt_name: str | list[str],
                 txt_format: str | list[str],
                 txt_output_path: str | list[str],
                 background_image_path: str | list[str],
                ):
        self.texts = texts
        self.noises = noises
        self.font_path = font_path
        self.font_size = font_size
        self.font_color = font_color
        self.background_color = background_color
        self.margins = margins
        self.dpi = dpi
        self.img_name = img_name
        self.img_format = img_format
        self.img_output_path = img_output_path
        self.txt_name = txt_name
        self.txt_format = txt_format
        self.txt_output_path = txt_output_path
        self.background_image_path = background_image_path

        self._texts_len = len(texts)
        self._count = 0

        
    def __iter__(self):
        return self


    def __next__(self):
        return self._generate_next()
    

    def _generate_next():
        pass