# **<a href='#imagecreator-module' style="text-decoration: underline;">`ImageCreator`</a> Module**

The <a href='#imagecreator-module' style="text-decoration: underline;">`ImageCreator`</a> class extends the <a href="../creator/#creator-module" style="text-decoration: underline;">`Creator`</a>
base class to provide functionality for generating images with customizable text, noise, and visual effects. This class is particularly useful for creating synthetic data by augmenting text-based images with noise or other transformations.

## **Attributes**

<a href='#imagecreator-module' style="text-decoration: underline;">`ImageCreator`</a> is a class-based implementation with class-level methods that generate images. The methods allow developers to create text images with optional visual transformations, background images, and noise effects.


## **Class Methods**

### **`_create_base_image()`**
```py
_create_base_image(cls,
                   text: str,
                   font: ImageFont,
                   font_color: Tuple[float, float, float],
                   background_color: str,
                   margins: Tuple[int, int, int, int],
                   background_img: Image
                   ) -> Image.Image:
```

Creates the base image with a specified background color, font, and text. Optionally, it can apply a background image over which the text will be rendered.

- **Parameters:**
    - **text : `str`** 

        The text to be added to the image.

    - **font : `ImageFont`**

        The font object used to render the text.

    - **font_color : `Tuple[float, float, float]`**
    
        The color of the text to be added.

    - **background_color : `str`**

        The color of the image background, given as a hex code or color name.

    - **margins : `Tuple[int, int, int, int]`**
        
        The margins `(left, top, right, bottom)` around the text in the image.

    - **background_img : `Image`** 
        
        An optional background image. If not <a href='../../noises' style="text-decoration: underline;">`Noise`</a>, this image will be used as a base.

- **Returns:**

    The generated `Image`.


### **`_apply_noise()`**

```py
_apply_noise(cls, noises: List[Noise], image: Image) -> Image:
```

This method applies noise to the image, altering the appearance of the text or background based on the noise objects.

- **Parameters:**

    - **noises : `List[Noise]`**
        
        A list of <a href='../../noises' style="text-decoration: underline;">`Noise`</a> objects that apply various noise transformations to the image.
    
    - **image : `Image`**
        
        The image object where the text will be placed and noise applied.

- **Returns:**
    
    The modified `Image` object after the noise has been applied.


### **`_blend_colors()`**

```py
_blend_colors(cls, bg_color: str, text_color: str, font_opacity: float) -> Tuple[float, float, float]:
```

The `_blend_colors` method blends a text color with a background color to achieve a transparency effect based on the provided opacity level. It calculates the blended RGB values and returns them as a `tuple`.

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
             noises: List[Noise] = [],
             font_size: float = 40.0,
             font_color: str = 'black',
             font_opacity: float = 1.0,
             background_color: str = 'white',
             margins: Tuple[int, int, int, int] = (5, 5, 5, 5),
             dpi: Tuple[float, float] = (300.0, 300.0),
             background_img: Image = None,
             clear_font: bool = True,
             ) -> Image:
```

The main method responsible for generating the final image with text and effects. It uses the helper methods <a href='#_create_base_image' style="text-decoration: underline;">`_create_base_image`</a> and <a href='#_apply_noise' style="text-decoration: underline;">`_apply_noise`</a> to construct the image, draw the text, and apply noise or transformations.

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

        The opacity of the text in the image.
    
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


## **Usage Example**

Here’s an example of how to use the <a href='imagecreator-module' style="text-decoration: underline;">`ImageCreator`</a> class to create an image with text and noise:

```py
from PIL import Image
from iftg.noises import GaussianNoise
from iftg.creators import ImageCreator

# Parameters
text = "Hello World"
font_path = "path/to/the/font"
font_size = 50
font_color = "black"
font_opacity = 1
background_color = "white"
margins = (10, 10, 10, 10)
dpi = (300, 300)

# Noise object
noises = [GaussianNoise(mean=0, sigma=40)]

# Load a background image
bg_img = Image.open('path/to/background/image')

# Create an image
image = ImageCreator.create_image(
    text=text,
    font_path=font_path,
    noises=noises,
    font_size=font_size,
    font_color=font_color,
    font_opacity=font_opacity,
    background_color=background_color,
    margins=margins,
    dpi=dpi,
    background_img=bg_img
)

# Save the generated image
image.save("generated_image.tif", **image.info)
```

!!! Notes

    1. **Background Image:**

        If you use a background image, it will randomly crop a portion of the background to use as the base. This allows for variability in background textures.

    2. **Noises:**

        The `noises` parameter accepts a list of <a href='../../noises' style="text-decoration: underline;">`Noise`</a> objects, allowing multiple types of noise to be applied to the image.