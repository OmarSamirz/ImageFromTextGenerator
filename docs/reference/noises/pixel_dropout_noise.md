# **<a href='#pixeldropoutnoise-module' style="text-decoration: underline;">`PixelDropoutNoise`</a> & <a href='#randompixeldropoutnoise-module' style="text-decoration: underline;">`RandomPixelDropoutNoise`</a> Modules**

!!! Note 
    - **Inheritance Structure:** 
    - <a href='../noise/#noise-module' style="text-decoration: underline;">`Noise`</a> (Abstract Base Class) 
    - <a href='#pixeldropoutnoise-module' style="text-decoration: underline;">`PixelDropoutNoise`</a> (Concrete Implementation) 
    - <a href='#randompixeldropoutnoise-module' style="text-decoration: underline;">`RandomPixelDropoutNoise`</a> (Extends PixelDropoutNoise with randomness)

## **PixelDropoutNoise Module**
The <a href='#pixeldropoutnoise-module' style="text-decoration: underline;">`PixelDropoutNoise`</a> class applies pixel dropout noise to an image by randomly dropping out pixels based on a specified probability, simulating the removal of pixels.

### **Attributes**
- **dropout_prob : `float`**

    The probability of a pixel being dropped out. A higher value leads to more pixels being dropped.

- **pixel_dimensions : `tuple[float, float]`**

    The dimensions of the dropout pixels (width, height), controlling how many pixels are removed in blocks.

- **pixel_color : `str`**

    The color of the dropped-out pixels, specified as a hex color code (e.g., `#FFFFFF` for `white`).

### **Methods**
#### **`add_noise()`**
```py
add_noise(self, image: Image) -> Image:
```
Public method that applies `pixel dropout` noise to the input image by dropping out pixels according to the specified probability, dimensions, and color.

- **Parameters:**

    - **image : `Image`**

        The input image to which pixel dropout noise will be added.

- **Returns:**

    - `Image`:

        The image with pixel dropout noise applied.

#### **`_pixeldropout_noise()`**
```py
_pixeldropout_noise(self, image: Image) -> Image:
```
Internal method that creates a dropout mask, randomly selects pixels for removal, and applies the dropout to the image.

- **Parameters:**

    - **image : `Image`**

        The image to which pixel dropout noise will be applied.

- **Returns:**

    - `Image`:

        The noisy image with pixel dropout applied.

### **Usage Example**
```py
from PIL import Image
from iftg.noises import PixelDropoutNoise

# Open an image
image = Image.open('path/to/image.tif')

# Create a PixelDropoutNoise object with a dropout probability of 0.2 and pixel dimensions of (5, 5)
pixel_dropout_noise = PixelDropoutNoise(dropout_prob=0.2, pixel_dimensions=(5, 5), pixel_color='#FF0000')

# Apply pixel dropout noise to the image
noisy_image = pixel_dropout_noise.add_noise(image)

# Save the noisy image
noisy_image.save('path/to/noisy_image.tif')
```

<br>

## **RandomPixelDropoutNoise Module**
The <a href='#randompixeldropoutnoise-module' style="text-decoration: underline;">`RandomPixelDropoutNoise`</a> class extends the functionality of <a href='#pixeldropoutnoise-module' style="text-decoration: underline;">`PixelDropoutNoise`</a> by allowing random selection of the dropout probability and pixel dimensions from specified ranges.

### **Attributes**
- **dropout_prob_range : `tuple[float, float]`**

    The range for random selection of the dropout probability. This controls the likelihood of pixels being dropped out.

- **pixel_dimensions_range : `tuple[float, float]`**

    The range for random selection of the pixel dimensions (width, height). Larger ranges will result in larger dropout blocks.

- **pixel_color : `str`**

    The color of the dropped-out pixels, specified as a hex color code (e.g., `#FFFFFF` for `white`).

### **Methods**
#### **`add_noise()`**
!!! Note 
    Each call to `add_noise()` results in a different dropout pattern by selecting random values for the dropout probability and pixel dimensions, introducing variability into the noise application.

```py
add_noise(self, image: Image) -> Image:
```
Public method that applies `random pixel dropout` noise to the input image by selecting random dropout probability and pixel dimensions within the specified ranges.

- **Parameters:**

    - **image : `Image`**

        The input image to which random pixel dropout noise will be added.

- **Returns:**

    - `Image`:

        The image with random pixel dropout noise applied.

### **Usage Example**
```py
from PIL import Image
from iftg.noises import RandomPixelDropoutNoise

# Open an image
image = Image.open('path/to/image.tif')

# Create a RandomPixelDropoutNoise object with dropout probability range (0.1, 0.3) and pixel dimensions range (3, 6)
random_pixel_dropout_noise = RandomPixelDropoutNoise(dropout_prob_range=(0.1, 0.3), pixel_dimensions_range=(3, 6), pixel_color='#00FF00')

# Apply random pixel dropout noise to the image
random_noisy_image = random_pixel_dropout_noise.add_noise(image)

# Save the randomly noisy image
random_noisy_image.save('path/to/random_noisy_image.tif')
```