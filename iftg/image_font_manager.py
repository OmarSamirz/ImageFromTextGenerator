from PIL import ImageFont


class ImageFontManager:
    """
    Manages font objects created using the PIL (Pillow) library's ImageFont module. 
    This class caches fonts to avoid loading the same font multiple times.
    """


    _fonts = {}


    @property
    def fonts(cls) -> dict:
        return cls._fonts


    @classmethod
    def clear(cls) -> None:
        """
        Clears the cache by removing all stored fonts from the internal dictionary.
        """
        cls._fonts.clear()


    @classmethod
    def remove_font(cls, font_path, font_size) -> None:
        """
        Removes a specific font from the cache based on its path and size.

        Args:
            font_path (str): The file path to the font.
            font_size (int): The size of the font.

        Raises:
            KeyError: If the specified font is not found in the cache.
        """
        try:
            del cls._fonts[(font_path, font_size)]
        except:
            raise KeyError("This key does not exist inside ImageFontManager")


    @classmethod
    def get_font(cls, font_path, font_size) -> ImageFont:
        """
        Retrieves a font from the cache or loads it if not already cached.

        Args:
            font_path (str): The file path to the font.
            font_size (int): The size of the font.

        Returns:
            ImageFont: The loaded ImageFont object.
        """
        if (font_path, font_size) not in cls._fonts:
            cls._fonts[(font_path, font_size)] = ImageFont.truetype(font_path, font_size)
        
        return cls._fonts[(font_path, font_size)]
    
