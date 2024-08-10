from PIL import ImageFont


class ImageFontManager:
    _fonts = {}


    @property
    def fonts(cls):
        return cls._fonts


    @classmethod
    @fonts.setter
    def fonts(cls):
        return cls._fonts


    @classmethod
    def clear(cls):
        cls._fonts.clear()


    @classmethod
    def get_font(cls, font_path, font_size):
        if (font_path, font_size) not in cls._fonts:
            cls._fonts[(font_path, font_size)] = ImageFont.truetype(font_path, font_size)
        
        return cls._fonts[(font_path, font_size)]
    
    

    



    