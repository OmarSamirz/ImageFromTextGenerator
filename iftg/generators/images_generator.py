from iftg.noises.noise import Noise
from iftg.utils.image_font_manager import ImageFontManager
from iftg.creators.image_creator import ImageCreator
from iftg.generators.generator import Generator, Image


class ImagesGenerator(Generator):
    """
    A generator class for creating a sequence of images with varying text, noise, blur, rotation, and other effects.
    Inherits from `Generator` and provides functionality to iterate over the generated images.

    Attributes:
        texts (list[str]): A list of texts to be used for image creation.
        noises (list[Noise]): A list of noise objects to be applied to the images.
        blur_radius (float): The radius for Gaussian blur applied to the images.
        random_blur (bool): Whether to apply a random blur within a specified range.
        min_blur (float): The minimum blur radius for random blur. 
        max_blur (float): The maximum blur radius for random blur.
        rotation_angle (float): The fixed rotation angle for the images. 
        random_rotation (bool): Whether to apply a random rotation within a specified range.
        min_rotation (float): The minimum rotation angle for random rotation.
        max_rotation (float): The maximum rotation angle for random rotation.
        font_path (str): The file path to the font used in the images.
        font_size (float): The size of the font used in the images.
        font_color (str): The color of the text in the images.
        background_color (str): The background color of the images.
        margins (tuple[int, int, int, int]): Margins for text placement on the images.
        clear_fonts (bool): Whether to clear the font cache after generating images.
    """
    
    
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
                 margins: tuple[int, int, int, int] = (5, 5, 5, 5),
                 clear_fonts: bool = False,
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
        return self._generate_next_image()

    
    def _generate_next_image(self) -> tuple[Image.Image, str]:
        """
        Generates the next image in the sequence.

        Returns:
            tuple: A tuple containing the generated image and the text used for the image.
        
        Raises:
            StopIteration: When all images have been generated and the font cache is cleared.
        """
        if self._count >= self._texts_len:
            ImageFontManager.remove_font(self.font_path, self.font_size)
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


    def _generate_images(self) -> tuple[Image.Image, str]:
        pass
        