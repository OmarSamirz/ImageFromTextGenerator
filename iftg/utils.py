import numpy as np
from PIL import ImageFont


def get_text_dimensions(text: str,
                        font: ImageFont
                        ) -> tuple[float, float, float, float]:

    left, top, right, bottom = font.getbbox(text)

    return left, top, right, bottom


def get_image_dimensions(right: int, 
                         bottom: int, 
                         margins: tuple[int, int, int, int] = (0, 0, 0, 0)
                         ) -> tuple[int, int]:
    
    left_margin, top_margin, right_margin, bottom_margin = margins

    image_width = right + left_margin + right_margin
    image_height = bottom + top_margin + bottom_margin

    return image_width, image_height
    