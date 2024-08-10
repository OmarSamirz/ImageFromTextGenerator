from iftg.noises.noise import Noise
from iftg.models.image_font_manager import ImageFontManager
from iftg.models.creators.image_creator import ImageCreator
from iftg.models.generators.generator import Generator, Image

class ImagesGenerator(Generator):
    
    
    def __init__(self, 
                 texts: list[str],
                 noises: list[Noise] = [],
                 blur_radius: float = 0.0,
                 random_blur: bool = False,
                 min_blur: float = 1.0,
                 max_blur: float = 4.0,
                 rotation_angle: float = 0.0,
                 random_rotation: bool = False,
                 min_rotation: float = -50.0,
                 max_rotation: float = 50.0,
                 font_path: str = "iftg/fonts/Arial.ttf",
                 font_size: float = 40.0,
                 font_color: str = 'black',
                 background_color: str = 'white',
                 margins: tuple[int, int, int, int] = (0, 0, 0, 0),
                 clear_fonts: bool = False
                 ):
        super().__init__(texts, 
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
                        )
        

    def __iter__(self):
        return self


    def __next__(self):
        return self._generate_images()


    
    def _next(self) -> tuple[Image.Image, str]:
        if self._count == self._texts_len:
            raise StopIteration

        self._count += 1
        return (ImageCreator.create_image(
            self.texts[self._count-1],
            self.noises,
            self.blur_radius,
            self.random_blur,
            self.min_blur,
            self.max_blur,
            self.rotation_angle,
            self.random_rotation,
            self.min_rotation,
            self.max_rotation,
            self.font_path,
            self.font_size,
            self.font_color,
            self.background_color,
            self.margins,
            self.clear_fonts
        ), self.texts[self._count-1])


    
    def _generate_images(self) -> Image:
        result = self._next()
        ImageFontManager.clear()

        return result





