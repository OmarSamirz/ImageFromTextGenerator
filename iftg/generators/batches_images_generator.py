from PIL import Image

from iftg.noises.noise import Noise
from iftg.generators import ImagesGenerator
from iftg.generators.generator import Generator
from iftg.image_font_manager import ImageFontManager


class BatchesImagesGenerator(Generator):
    
    
    def __init__(self, 
                 texts: list[list[str]],
                 noises: list[list[Noise]] = [],
                 font_paths: list[str] = ["iftg/fonts/Arial.ttf"],
                 font_sizes: list[float] = [40.0],
                 font_colors: list[str] = ['black'],
                 background_colors: list[str] = ['white'],
                 margins: list[tuple[int, int, int, int]] = [(5, 5, 5, 5)],
                 img_names: list[str] = ['img'],
                 img_formats: list[str] = ['.tif'],
                 img_output_paths: list[str] = [''],
                 txt_names: list[str] = ['text'],
                 txt_formats: list[str] = ['.txt'],
                 txt_output_paths: list[str] = [''],
                ):
        super().__init__(texts, 
                         noises, 
                         font_paths,
                         font_sizes,
                         font_colors,
                         background_colors,
                         margins,
                         img_names,
                         img_formats,
                         img_output_paths,
                         txt_names,
                         txt_formats,
                         txt_output_paths,
                        )            


    def __iter__(self):
        return self
    
    
    def __next__(self):
        return self._generate_next_batch()
    

    def _generate_next_batch(self):
        if self._count >= self._texts_len:
            ImageFontManager.remove_font(self.font_path[self._count-1], self.font_size[self._count-1])
            raise StopIteration
        
        generator =  ImagesGenerator(self.texts[self._count], 
                                     self.noises[self._count],
                                     self.font_path[self._count],
                                     self.font_size[self._count],
                                     self.font_color[self._count],
                                     self.background_color[self._count],
                                     self.margins[self._count],
                                     self.img_name[self._count] + f'_{self._count}',
                                     self.img_format[self._count],
                                     self.img_output_path[self._count],
                                     self.txt_name[self._count] + f'_{self._count}',
                                     self.txt_format[self._count],
                                     self.txt_output_path[self._count],
                                     auto_remove_font=False,
                                    )
        
        self._count += 1
        return generator

    
    def generate_batches(self) -> bool:
        for generator in self:
            generator.generate_images()
        
        return True

    





