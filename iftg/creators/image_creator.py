import numpy as np
from PIL import Image, ImageFont, ImageDraw

from functools import reduce

from iftg.noises.noise import Noise
from iftg.creators.creator import Creator
from iftg.image_font_manager import ImageFontManager


class ImageCreator(Creator):
    """ 
    A class that extends the `Creator` base class to generate images with customizable text, noise, 
    blur, rotation, and other visual effects. This class is particularly useful for creating images 
    with text and applying various transformations for data creation and augmentation.
    """
    
    @classmethod
    def _create_base_image(cls, 
                           text: str,                            
                           font: ImageFont, 
                           background_color: str,
                           margins: tuple[int, int, int, int],
                           background_img: Image
                          ) -> tuple[Image.Image, int]:
        """
        Creates a base image with the specified background color and dimensions, 
        and optionally adds a background image.

        Parameters:
            text (str):
                The text to be added to the image.
            font (ImageFont):
                The font used for the text.
            background_color (str):
                The background color of the image.
            margins (tuple[int, int, int, int]):
                Margins for the image (left, top, right, bottom).
            background_img (Image):
                An optional background image to be used as a base.

        Returns:
            tuple[Image.Image, int]:
                A tuple containing the generated image and the top margin adjustment.
        """

        text_dimensions = cls.get_text_dimensions(text, font)
        image_width, image_height = cls.get_image_dimensions(margins, text_dimensions)

        image = Image.new('RGB', 
                          (image_width, image_height+text_dimensions[1]),
                          color=background_color
                         )
        
        # add a background image to the text
        if background_img != None:
            bg_width, bg_height = background_img.size

            x1 = np.random.randint(0, bg_width - image_width)
            y1 = np.random.randint(0, bg_height - image_height)
            x2 = x1 + image_width * 2
            y2 = y1 + image_height * 2

            random_bg_part = background_img.crop((x1, y1, x2, y2))

            image.paste(random_bg_part)
        
        return image, text_dimensions[1]

    
    @classmethod
    def _apply_noise(cls,
                     text: str,
                     top: int,
                     font: ImageFont,
                     noises: list[Noise],
                     font_color: str,
                     margins: tuple[int, int, int, int],
                     image: Image,
                    ) -> Image:
        
        """
        Applies text, noise, blur, and rotation effects to the base image.

        Parameters:
            text (str):
                The text to be drawn on the image.
            top (int):
                The top margin adjustment for the text placement.
            font (ImageFont):
                The font used for the text.
            noises (list[Noise]):
                A list of noise objects to apply to the image.
            font_color (str):
                The color of the text.
            margins (tuple[int, int, int, int]):
                Margins for text placement on the image (left, top, right, bottom).
            image (Image.Image):
                The base image to which effects will be applied.

        Returns:
            Image: The image with the applied text, noise, blur, and rotation effects.
        """

        # Draw the text on the image
        draw = ImageDraw.Draw(image)
        draw.text((margins[0], -top+margins[1]), text, font=font, fill=font_color)
        
        # Loop through all given noises and add them to the image
        image = reduce(lambda img, noise: noise.add_noise(img), noises, image)
            
        return image

    
    @classmethod
    def create_image(cls,
                     text: str,
                     font_path: str,
                     noises: list[Noise] = [],
                     font_size: float = 40.0,
                     font_color: str = 'black',
                     background_color: str = 'white',
                     margins: tuple[int, int, int, int] = (5, 5, 5, 5),
                     dpi: tuple[float, float] = (300.0, 300.0),
                     background_img: Image = None,
                     clear_font: bool = True
                    ):
        """
        Creates an image with the specified text, applying optional noise, blur, and rotation effects.

        Parameters:
            text (str): 
                The text to be drawn on the image.
            noises (list[Noise], optional): 
                A list of noise objects to apply to the image. Defaults to an empty list.
            font_path (str, optional):
                The file path to the font. Defaults to 'iftg/fonts/Arial.ttf'.
            font_size (float, optional): 
                The size of the font. Defaults to 40.0.
            font_color (str, optional):
                The color of the text. Defaults to 'black'.
            background_color (str, optional):
                The background color of the image. Defaults to 'white'.
            margins (tuple[int, int, int, int], optional):
                Margins for text placement on the image (left, top, right, bottom). Defaults to (5, 5, 5, 5).
            dpi (tuple[float, float], optional):
                The resolution of the image (dots per inch). Defaults to (300, 300).
            background_img (Image, optional):
                An optional background image to be used as a base. Defaults to None.
            clear_fonts (bool, optional): 
                Whether to clear the font cache after creating the image. Defaults to True.

        Returns:
            Image: 
                The generated image with the applied text and effects.
        """
        
        font = ImageFontManager.get_font(font_path, font_size)

        image, top = cls._create_base_image(text, font, background_color, margins, background_img)

        image = cls._apply_noise(text, top, font, noises, font_color, margins, image)
        image.info['dpi'] = dpi
        
        if clear_font:
            ImageFontManager.clear()

        return image