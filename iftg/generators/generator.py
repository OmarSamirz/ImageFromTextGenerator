import numpy as np
from functools import reduce
from abc import ABC, abstractmethod
from iftg.noises.noise import Noise
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from iftg.utils import get_text_dimensions, get_image_dimensions

class Generator(ABC):
    
    def __init__(self, 
                 texts: list[str] = [],
                 texts_len: int = 0, 
                 noises: list[Noise] = [],
                 blur_radius: float = 0.0,
                 random_blur: bool = False,
                 min_blur: float = 1.0,
                 max_blur: float = 4.0,
                 rotation_angle: float = 0.0,
                 random_rotation: bool = False,
                 min_rotation: float = -50.0,
                 max_rotation: float = 50.0,
                 font_path: str = "arial.ttf",
                 font_size: int = 40,
                 font_color: str = 'black',
                 background_color: str = 'white',
                 margins: tuple[int, int, int, int] = (0, 0, 0, 0)
                 ):
        self.texts = texts
        self.texts_len = texts_len
        self.noises = noises
        self.blur_radius = blur_radius
        self.random_blur = random_blur
        self.min_blur = min_blur
        self.max_blur = max_blur
        self.rotation_angle = rotation_angle
        self.random_rotation = random_rotation
        self.min_rotation = min_rotation
        self.max_rotation = max_rotation
        self.font_path = font_path
        self.font_size = font_size
        self.font_color = font_color
        self.background_color = background_color
        self.margins = margins
        self._count = 0
        self._font = ImageFont.truetype(self.font_path, self.font_size)

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def _create_image(self, text: str) -> Image:
        """
            This function creates an image with the background color the user specify
            after calculating the text dimensions and image dimensions

            
        """
        _, top, right, bottom = get_text_dimensions(text, self._font)
        image_width, image_height = get_image_dimensions(right, bottom, self.margins)

        image = Image.new('RGB', (image_width+2, image_height+top), color=self.background_color)

        return image

    @abstractmethod
    def _apply_noise(self, text: str, image: Image) -> Image:
        # Draw the text on the image
        draw = ImageDraw.Draw(image)
        draw.text((0+self.margins[0], 0+self.margins[1]), text, font=self._font, fill=self.font_color)

        # Add blur to the image if blur_radius is greater than 0
        if self.blur_radius > 0 or self.random_blur == True:
            gaussian_filter = ImageFilter.GaussianBlur(
                                                        radius=self.blur_radius if not self.random_blur 
                                                        else np.random.uniform(self.min_blur, self.max_blur)
                                                      )
            
            image = image.filter(gaussian_filter)
        
        # Add rotation to the image if rotate is greater than 0
        if self.rotation_angle != 0 or self.random_rotation == True:
            image = image.rotate(angle=self.rotation_angle if not self.random_rotation 
                                 else np.random.uniform(self.min_rotation, self.max_rotation),
                                 resample=Image.Resampling.BICUBIC, 
                                 fillcolor=self.background_color,
                                 expand=True
                                )
        
        # Loop through all given noises and add them to the image
        image = reduce(lambda img, noise: noise.add_noise(img), self.noises, image)
            
        return image

    @abstractmethod
    def _generate_image(self) -> Image:
        pass

    


    