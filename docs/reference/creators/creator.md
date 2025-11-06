# **<a href='#creator-module' style="text-decoration: underline;">`Creator`</a> Module**
!!! warning
    This module is considered internal.

The <a href='#creator-module' style="text-decoration: underline;">`Creator`</a> class is an abstract base class designed for generating images with text and applying various transformations such as noise. Subclasses must implement several abstract methods to define specific behavior for creating base images. The class supports the generation of images with customizable text, background, font, margins, and optional background images.

## **Attributes**

The <a href='#creator-module' style="text-decoration: underline;">`Creator`</a>  class doesn’t have instance attributes but provides class-level methods for creating images. Subclasses will implement these methods to generate images based on the provided parameters.


## **Methods**

### **`_create_base_image()`**
```py
_create_base_image(cls,
                   text: str,
                   font: ImageFont,
                   font_color: Tuple[int, int, int],
                   background_color: str,
                   margins: Tuple[int, int, int, int],
                   background_img: Image
                   ) -> Image.Image:
```

This method is responsible for creating the base image with the specified text and background. It is an abstract method that must be implemented by subclasses.

- **Parameters:**
    - **text : `str`** 

        The text to be added to the image.

    - **font : `ImageFont`**

        The font object used to render the text.

    - **font_color : `Tuple[int, int, int]`**
        
        The color of the text to be added.

    - **background_color : `str`**

        The color of the image background, given as a hex code or color name.

    - **margins : `Tuple[int, int, int, int]`**
        
        The margins `(left, top, right, bottom)` around the text in the image.

    - **background_img : `Image`** 
        
        An optional background image over which the text will be placed.

- **Returns:**

    The generated `Image`.

### **`get_text_dimensions()`**

```py
get_text_dimensions(cls, 
                    text: str, 
                    font: ImageFont
                    ) -> Tuple[float, float, float, float]
```

This method calculates the dimensions (bounding box) of the given text using the provided font.

- **Parameters:**

    - **text : `str`** 

        The text to measure.

    - **font : `ImageFont`** 

        The font object used to render the text.

- **Returns:**

- A `tuple` containing four floating-point values representing the bounding box of the text:
    - **left : `float`**

         The left boundary of the text.

    - **top : `float`** 
        
        The top boundary of the text.

    - **right : `float`**
        
        The right boundary of the text.

    - **bottom : `float`** 
        
        The bottom boundary of the text.

### **`get_image_dimensions()`**

```py
get_image_dimensions(cls, 
                     margins: Tuple[int, int, int, int],
                     text_dimensions: Tuple[float, float, float, float]
                     ) -> Tuple[int, int]
```

This method calculates the width and height of the image based on the text dimensions and the provided margins.

- **Parameters:**

    - **margins : `Tuple[int, int, int, int]`**
        
        The margins (left, top, right, bottom) around the text.

    - **text_dimensions : `Tuple[float, float, float, float]`**

        The bounding box of the text (left, top, right, bottom) calculated using <a href='#get_text_dimensions' style="text-decoration: underline;">`get_text_dimensions()`</a>.

- **Returns:**

    - A `tuple` containing the width and height of the image as integers:
        - image_width : `int`

            The total width of the image, including the margins.

        - image_height : `int`
            
            The total height of the image, including the margins and text area.

### **`_apply_noise()`**

```py
_apply_noise(cls, noises: List[Noise], image: Image) -> Image:
```

This method applies noise to the image, altering the appearance of the text or background based on the noise objects.

- **Parameters:**

    - **noises : `List[Noise]`**
        
        A list of Noise objects to apply to the image.

    - **image : `Image`**
        
        The image object where the text will be placed and noise applied.

- **Returns:**
    
    The modified `Image` object after the noise has been applied.


### **`_blend_colors()`**

```py
_blend_colors(cls, bg_color: str, text_color: str, font_opacity: float) -> Tuple[float, float, float]:
```

The `_blend_colors` method is an abstract class method intended to blend a text color with a background color based on a specified opacity level. Subclasses must implement this method to compute the blended RGB values and return them as a tuple.

- **Parameters:**

    
    - **bg_color : `str`**
        
        The background color specified in any valid `PIL` color format.
    
    - **text_color : `str`**
        
        The text color specified in any valid `PIL` color format.
    
    - **font_opacity : `float`**
        
        The opacity level of the text color to blend with the background color.

- **Returns:**

    `tuple`: A tuple representing the blended color in RGB format `(R, G, B)`


### **`create_image()`**

```py
create_image(cls,
             text: str,
             font_path: str,
             noises: List[Noise],
             font_size: float,
             font_color: str,
             font_opacity: float,
             background_color: str,
             margins: Tuple[int, int, int, int],
             dpi: Tuple[float, float],
             background_img: Image,
             clear_font: bool,
             ) -> Image:
```

This is the main method responsible for creating the final image with text, background, and optional noise.

- **Parameters:**

    
    - **text : `str`**
        
        The text to be rendered in the image.
    
    - **font_path : `str`**
        
        The path to the font file used to render the text.
    
    - **noises : `List[Noise]`**
        
        A list of Noise objects to be applied to the image.
    
    - **font_size : `float`** 

        The size of the font.
    
    - **font_color : `str`**
        
        The color of the font text.
    
    - **font_opacity : `float`**

        The opacity of the text, where 1.0 is fully opaque and 0.0 is fully transparent.

    - **background_color : `str`**
        
        The background color of the image.
    
    - **margins : `Tuple[int, int, int, int]`**
        
        The margins (left, top, right, bottom) around the text.
    
    - **dpi : `Tuple[float, float]`**
        
        The DPI (dots per inch) resolution for the image.
    
    - **background_img : `Image`** 
        
        An optional background image to be used instead of a plain color.
    
    - **clear_font : `bool`** 
        
        If `True`, the font will be rendered without noise. If `False`, the font will also have noise applied.
    


- **Returns:**

    The final `Image` object containing the text, background, and applied noise.