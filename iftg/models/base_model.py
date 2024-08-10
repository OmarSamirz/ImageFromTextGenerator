from abc import ABC
from iftg.noises.noise import Noise

class BaseModel(ABC):
    def __init__(self,
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
                ):
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
        self.clear_fonts = clear_fonts