# **<a href='#imagefontmanager-module' style="text-decoration: underline;">`ImageFontManager`</a> Module**
!!! warning
    This module is considered internal.

<a href='#imagefontmanager-module' style="text-decoration: underline;">`ImageFontManager`</a> is a utility class designed to manage font objects created using the Pillow library's ImageFont module. This class provides functionality to cache fonts, retrieve them efficiently, and clear the font cache as needed. The primary goal is to avoid repeatedly loading the same font, thereby improving performance and resource management.

## **Class Attributes**

- **_fonts : `dict`**

    A private class-level dictionary that caches font objects. The keys are tuples of (font_path, font_size), and the values are `ImageFont` objects.

## **Class Methods**

### **`clear()`**

```py
clear(cls) -> None:
```
Clears the font cache by removing all stored fonts from the internal dictionary.

- **Returns:**
    - `None`

### **`remove_font`**

```py
remove_font(cls, font_path: str, font_size: int) -> None:
```
Removes a specific font from the cache based on its path and size.

- **Parameters:**
    - **font_path : `str`**
        
        The file path to the font that needs to be removed.

    - **font_size : `int`**
        
        The size of the font that needs to be removed.

- **Raises:**

    - `KeyError`: 
        
        If the specified font is not found in the cache. The exception message will indicate that the key does not exist in the ImageFontManager.

### **`get_font`**

```py
get_font(cls, font_path: str, font_size: int) -> ImageFont:
```
Retrieves a font from the cache or loads it if it is not already cached.

- **Parameters:**

    - **font_path : `str`**
    
        The file path to the font to retrieve.

    - **font_size : `int`** 
        
        The size of the font to retrieve.

- **Returns:**
    - `ImageFont`: 
    
        The ImageFont object corresponding to the specified font path and size.
