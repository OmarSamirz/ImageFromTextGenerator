import numpy as np
from functools import reduce
from iftg.noises.noise import Noise
from iftg.models.creators.creator import Creator
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from iftg.models.image_font_manager import ImageFontManager
from iftg.utils import get_text_dimensions, get_image_dimensions

class ImageCreator(Creator):
        
    
    @classmethod
    def _create_base_image(cls, 
                           text: str, 
                           font: ImageFont, 
                           background_color: str,
                           margins: tuple[int, int, int, int]
                          ) -> Image:
        """
            This function creates an image with the background color the user specify
            after calculating the text dimensions and image dimensions

            
        """
        _, top, right, bottom = get_text_dimensions(text, font)
        image_width, image_height = get_image_dimensions(right, bottom, margins)

        image = Image.new('RGB', (image_width+2, image_height+top), color=background_color)

        return image

    
    @classmethod
    def _apply_noise(cls,
                     text: str,
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
        # Draw the text on the image
        draw = ImageDraw.Draw(image)
        draw.text((0+margins[0], 0+margins[1]), text, font=font, fill=font_color)

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
                     margins: tuple[int, int, int, int] = (0, 0, 0, 0),
                     clear_fonts: bool = True
                    ):

        font = ImageFontManager.get_font(font_path, font_size)

        image = cls._create_base_image(text, font, background_color, margins)

        image = cls._apply_noise(text, font, noises, blur_radius, random_blur, min_blur, max_blur,
                                  rotation_angle, random_rotation, min_rotation, max_rotation, 
                                  font_color, background_color, margins, image)
        
        if clear_fonts:
            ImageFontManager.clear()

        return image