import numpy as np
from functools import reduce
from iftg.noises.noise import Noise
from iftg.creators.creator import Creator
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from iftg.utils.image_font_manager import ImageFontManager
from iftg.utils import get_text_dimensions, get_image_dimensions

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
                           is_multiline: bool,
                           background_color: str,
                           margins: tuple[int, int, int, int]
                          ) -> tuple[Image.Image, int]:
        """
        Creates a base image with the specified background color and dimensions calculated based on the text.

        Args:
            text (str): The text to be added to the image.
            font (ImageFont): The font used for the text.
            is_multiline (bool): Indicates if the text contains multiple lines.
            background_color (str): The background color of the image.
            margins (tuple[int, int, int, int]): Margins for the image (left, top, right, bottom).

        Returns:
            tuple: 
            A tuple containing the generated image and the top margin adjustment.

        """

        _, top, right, bottom = get_text_dimensions(text, font, is_multiline)
        image_width, image_height = get_image_dimensions(right, top, bottom, margins)

        image = Image.new('RGB', 
                          (image_width, image_height-top if is_multiline else image_height+top),
                          color=background_color
                         )
        
        return image, top

    
    @classmethod
    def _apply_noise(cls,
                     text: str,
                     top: int,
                     font: ImageFont,
                     noises: list[Noise],
                     blur_radius: float ,
                     random_blur: bool,
                     min_blur: float,
                     max_blur: float,
                     rotation_angle: float,
                     random_rotation: bool,
                     min_rotation: float,
                     max_rotation: float,
                     font_color: str,
                     background_color: str,
                     margins: tuple[int, int, int, int],
                     image: Image,
                    ) -> Image:
        
        """
        Applies text, noise, blur, and rotation effects to the base image.

        Args:
            text (str): The text to be drawn on the image.
            top (int): The top margin adjustment for the text placement.
            font (ImageFont): The font used for the text.
            noises (list[Noise]): A list of noise objects to apply to the image.
            blur_radius (float): The radius for Gaussian blur; applied if greater than 0.
            random_blur (bool): Whether to apply a random blur within a specified range.
            min_blur (float): The minimum blur radius for random blur.
            max_blur (float): The maximum blur radius for random blur.
            rotation_angle (float): The fixed rotation angle for the image.
            random_rotation (bool): Whether to apply a random rotation within a specified range.
            min_rotation (float): The minimum rotation angle for random rotation.
            max_rotation (float): The maximum rotation angle for random rotation.
            font_color (str): The color of the text.
            background_color (str): The background color used when rotating the image.
            margins (tuple[int, int, int, int]): Margins for text placement on the image (left, top, right, bottom).
            image (Image.Image): The base image to which effects will be applied.

        Returns:
            Image.Image: The image with the applied text, noise, blur, and rotation effects.
        """

        # Draw the text on the image
        draw = ImageDraw.Draw(image)

        draw.text((margins[0], -top+margins[1]), text, font=font, fill=font_color)
        

        # Add blur to the image if blur_radius is greater than 0
        if blur_radius > 0 or random_blur == True:
            gaussian_filter = ImageFilter.GaussianBlur(
                                                        radius=blur_radius if not random_blur 
                                                        else np.random.uniform(min_blur, max_blur)
                                                      )
            
            image = image.filter(gaussian_filter)
        
        # Add rotation to the image if rotate is greater than 0
        if rotation_angle != 0 or random_rotation == True:
            image = image.rotate(angle=rotation_angle if not random_rotation 
                                 else np.random.uniform(min_rotation, max_rotation),
                                 resample=Image.Resampling.BICUBIC, 
                                 fillcolor=background_color,
                                 expand=True
                                )
        
        # Loop through all given noises and add them to the image
        image = reduce(lambda img, noise: noise.add_noise(img), noises, image)
            
        return image

    
    @classmethod
    def create_image(cls,
                     text: str,
                     noises: list[Noise] = [],
                     blur_radius: float = 0.0,
                     random_blur: bool = False,
                     min_blur: float = 1.0,
                     max_blur: float = 4.0,
                     rotation_angle: float = 0.0,
                     random_rotation: bool = False,
                     min_rotation: float = -50.0,
                     max_rotation: float = 50.0,
                     font_path: str = 'iftg/fonts/Arial.ttf',
                     font_size: float = 40.0,
                     font_color: str = 'black',
                     background_color: str = 'white',
                     margins: tuple[int, int, int, int] = (5, 5, 5, 5),
                     clear_fonts: bool = True
                    ):
        """
        Creates an image with the specified text, applying optional noise, blur, and rotation effects.

        Args:
            text (str): The text to be drawn on the image.
            noises (list[Noise], optional): A list of noise objects to apply to the image. Defaults to an empty list.
            blur_radius (float, optional): The radius for Gaussian blur. Defaults to 0.0.
            random_blur (bool, optional): Whether to apply a random blur within a specified range. Defaults to False.
            min_blur (float, optional): The minimum blur radius for random blur. Defaults to 1.0.
            max_blur (float, optional): The maximum blur radius for random blur. Defaults to 4.0.
            rotation_angle (float, optional): The fixed rotation angle for the image. Defaults to 0.0.
            random_rotation (bool, optional): Whether to apply a random rotation within a specified range. Defaults to False.
            min_rotation (float, optional): The minimum rotation angle for random rotation. Defaults to -50.0.
            max_rotation (float, optional): The maximum rotation angle for random rotation. Defaults to 50.0.
            font_path (str, optional): The file path to the font. Defaults to 'iftg/fonts/Arial.ttf'.
            font_size (float, optional): The size of the font. Defaults to 40.0.
            font_color (str, optional): The color of the text. Defaults to 'black'.
            background_color (str, optional): The background color of the image. Defaults to 'white'.
            margins (tuple[int, int, int, int], optional): Margins for text placement on the image (left, top, right, bottom). Defaults to (5, 5, 5, 5).
            clear_fonts (bool, optional): Whether to clear the font cache after creating the image. Defaults to True.

        Returns:
            Image.Image: The generated image with the applied text and effects.
        """
        
        font = ImageFontManager.get_font(font_path, font_size)
        is_multiline = True if len(text.splitlines()) > 1 else False

        image, top = cls._create_base_image(text, font, is_multiline, background_color, margins)

        image = cls._apply_noise(text, top, font, noises, blur_radius, random_blur, min_blur, max_blur,
                                  rotation_angle, random_rotation, min_rotation, max_rotation, 
                                  font_color, background_color, margins, image)
        
        if clear_fonts:
            ImageFontManager.clear()

        return image