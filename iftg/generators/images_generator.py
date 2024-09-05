from PIL import Image

import os

from iftg.noises.noise import Noise
from iftg.image_font_manager import ImageFontManager
from iftg.creators.image_creator import ImageCreator
from iftg.generators.generator import Generator


class ImagesGenerator(Generator):
    """
    A generator class for creating a sequence of images with varying text, noise effects.
    Inherits from `Generator` and provides functionality to iterate over the generated images.

    Attributes:
        texts (list[str]): 
            A list of texts to be used for image creation.
        font_path (str):
            The file path to the font used in the images.
        noises (list[Noise]):
            A list of noise objects to be applied to the images.
        font_size (float):
            The size of the font used in the images.
        font_color (str):
            The color of the text in the images.
        background_color (str):
            The background color of the images.
        margins (tuple[int, int, int, int]):
            Margins for text placement on the images.
        dpi (tuple[float, float]):
            The DPI (dots per inch) settings for the images.
        img_name (str):
            The base name for the output image files.
        img_format (str):
            The file format for the output images.
        img_output_path (str):
            The directory where the generated images will be saved.
        txt_name (str):
            The base name for the output text files containing the image labels.
        txt_format (str):
            The file format for the output text files.
        txt_output_path (str):
            The directory where the generated text files will be saved.
        auto_remove_font (bool):
            A flag indicating whether to automatically remove the font from the cache after image generation.
        background_image_path (str):
            The file path to the background image, if any.
    """
    
    
    def __init__(self, 
                 texts: list[str],
                 font_path: str,
                 noises: list[Noise] = [],
                 font_size: float = 40.0,
                 font_color: str = 'black',
                 background_color: str = 'white',
                 margins: tuple[int, int, int, int] = (5, 5, 5, 5),
                 dpi: tuple[float, float] = (300.0, 300.0),
                 img_name: str = 'img',
                 img_format: str = '.tif',
                 img_output_path: str = 'output',
                 txt_name: str = 'text',
                 txt_format: str = '.txt',
                 txt_output_path: str = 'output',
                 auto_remove_font: bool = True,
                 background_image_path: str = '',
                ):
        
        self.auto_remove_font = auto_remove_font
        self.background_img = None

        if os.path.exists(font_path) == False:
            raise FileNotFoundError("The font does not exist.")

        if background_image_path != '':
            try:
                self.background_img = Image.open(background_image_path)
            except:
                raise FileNotFoundError("The background image does not exist")

        super().__init__(texts, 
                         font_path,
                         noises, 
                         font_size,
                         font_color,
                         background_color,
                         margins,
                         dpi,
                         img_name,
                         img_format,
                         img_output_path,
                         txt_name,
                         txt_format,
                         txt_output_path,
                         background_image_path
                        )

    
    def _generate_next(self) -> tuple[Image.Image, str]:
        """
        Generates the next image in the sequence.

        Returns:
            tuple: A tuple containing the generated image and the text used for the image.
        
        Raises:
            StopIteration: When all images have been generated and the font cache is cleared.
        """
        if self._count >= self._texts_len:
            if self.auto_remove_font:
                ImageFontManager.remove_font(self.font_path, self.font_size)

            raise StopIteration

        img_info = (ImageCreator.create_image(self.texts[self._count],
                                             self.font_path,
                                             self.noises,
                                             self.font_size,
                                             self.font_color,
                                             self.background_color,
                                             self.margins,
                                             self.dpi,
                                             self.background_img,
                                             False,
                                            ), self.texts[self._count], self._count)
        
        self._count += 1
        return img_info


    def _save_image(self, img: Image, i: int) -> None:
        """
        Saves the image to output path.
        """
        img_path = os.path.join(self.img_output_path, self.img_name + f'_{i}' + self.img_format)
        img.save(img_path, **img.info)


    def _save_image_and_text(self, img_info: tuple[Image.Image, str, int]) -> None:
            """
            Saves the image and the corresponding text to their respective output paths.
            """
            img, lbl, i = img_info
            
            self._save_image(img, i)

            text_path = os.path.join(self.txt_output_path, self.txt_name + f'_{i}' + self.txt_format)
            with open(text_path, 'w') as text_file:
                text_file.write(lbl)


    def generate_images(self) -> None:
        """
        Generates and saves images to the specified output directory.

        Creates the output directory if it doesn't exist, and saves each generated image 
        with the specified name and format.
        """
        if os.path.isdir(self.img_output_path) == False:
            os.mkdir(self.img_output_path)

        for img, _, i in self:
            self._save_image(img, i)

    
    def generate_images_with_text(self) -> None:
        """
        Generates images and saves both the images and their corresponding texts to the specified directories.

        Creates the output directories if they don't exist. Saves each generated image and its label
        to their respective paths.
        """
        if os.path.isdir(self.img_output_path) == False:
            os.mkdir(self.img_output_path)
        if os.path.isdir(self.txt_output_path) == False:
            os.mkdir(self.txt_output_path)

        for img_info in self:
            self._save_image_and_text(img_info)
        