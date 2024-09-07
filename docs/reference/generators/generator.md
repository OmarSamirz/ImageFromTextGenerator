# **<a href='#generator-module' style="text-decoration: underline;">`Generator`</a> Module**
!!! warning
    This module is considered internal.


The <a href='#generator-module' style="text-decoration: underline;">`Generator`</a> class is an abstract base class designed for creating image generators that apply various effects, such as noise and text, to images. It serves as a template for subclasses that define specific image generation methods and manage different parameters for text, font, noise, and image properties.


## **Attributes**

- **texts : `list[str]` or `list[list[str]]`**
        
    A list of texts or a list of lists of texts to be used for generating images. The text(s) will be applied to the images as part of the generation process.

- **font_path : `str` or `list[str]`**
        
    The path(s) to the font file(s) used for rendering text on the images. This can be a single path or multiple paths if different fonts are used.

- **noises : `list[Noise]` or `list[list[Noise]]`**
    
    A list of noise objects or a list of lists of noise objects to apply to the images. These noises will be used to add variations and effects to the images.

- **font_size : `float` or `list[float]`**
        
    The size(s) of the font(s) used. This can be a single size or multiple sizes depending on the number of fonts.

- **font_color : `str` or `list[str]`**
        
    The color(s) of the text in the images. This can be a single color or a list of colors if different colors are applied to different images.

- **background_color : `str` or `list[str]`**
        
    The background color(s) of the images. This can be a single color or multiple colors if different backgrounds are used.

- **margins : tuple[int, int, int, int] or list[tuple[int, int, int, int]] **
        
    Margins for text placement on the images. This can be a single tuple defining margins (left, top, right, bottom) or a list of such tuples.

- **dpi : `tuple[float, float]` or `list[tuple[float, float]]`**
        
    The DPI (dots per inch) settings for the images. This can be a single DPI setting or a list of settings for different images.

- **img_name : `str` or `list[str]`**
    The base name(s) for the output image files. This can be a single name or a list of names if multiple images are generated.

- **img_format : `str` or `list[str]`**
        
    The file format(s) for the output images (e.g., `'tif'`, `'png'`). This can be a single format or a list of formats.

- **img_output_path : `str` or `list[str]`**
    
    The directory or directories where the generated images will be saved. This can be a single directory path or a list of paths.

- **txt_name : `str` or `list[str]`**
        
    The base name(s) for the output text files that will contain image labels. This can be a single name or a list of names.

- **txt_format : `str` or `list[str]`**
        
    The file format(s) for the output text files (e.g., `'txt'`). This can be a single format or a list of formats.

- **txt_output_path : `str` or `list[str]`**
        
    The directory or directories where the generated text files will be saved. This can be a single directory path or a list of paths.

- **background_image_path : `str` or `list[str]`**
        
    The file path(s) to the background image(s) to be used in the images. This can be a single path or multiple paths if different backgrounds are used.

## **Methods**

### **`__iter__()`**

```py
__iter__(self)
```

Returns the generator object itself, making it iterable.

- **Returns:**
    - `Generator`:
         The generator object.

### **`__next__()`**

```py
__next__(self)
```

Generates the next image by calling the <a href='#_generate_next' style="text-decoration: underline;">`_generate_next`</a> method.

- **Returns:**
    - <a href='#imagesgenerator-module' style="text-decoration: underline;">`ImagesGenerator`</a> or `tuple[Image.Image, str, int]`
        - If the subclass returns an image, a tuple is expected containing:
            - `Image.Image`: The generated image.
            - `str`: A label or related information for the image.
            - `int`: An additional identifier or index for the image.

- **Raises:**
    - `StopIteration`:
        
        When there are no more images to generate.

### **`_generate_next()`**

```py
_generate_next(self) -> ImagesGenerator | tuple[Image.Image, str, int]:
```

An abstract method that should be implemented by subclasses to define how each image is generated. This method is called by <a href='#__next__'>`__next__`</a>.

- **Returns:**
    - <a href='#imagesgenerator-module' style="text-decoration: underline;">`ImagesGenerator`</a> or `tuple[Image.Image, str, int]`
        - If the subclass returns an image, a tuple is expected containing:
            - `Image.Image`: The generated image.
            - `str`: A label or related information for the image.
            - `int`: An additional identifier or index for the image.