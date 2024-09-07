# **<a href='#brightnessnoise-module' style="text-decoration: underline;">`BrightnessNoise`</a> & <a href='#randombrightnessnoise-module' style="text-decoration: underline;">`RandomBrightnessNoise`</a> Modules**

!!! Note
    - **Inheritance Structure:**
        - <a href='../noise/#noise-module' style="text-decoration: underline;">`Noise`</a> (Abstract Base Class)
        - <a href='#brightnessnoise-module' style="text-decoration: underline;">`BrightnessNoise`</a> (Concrete Implementation)
        - <a href='#randombrightnessnoise-module' style="text-decoration: underline;">`RandomBrightnessNoise`</a> (Extends BlurNoise with randomness)

## **BrightnessNoise Module**
The <a href='#brightnessnoise-module' style="text-decoration: underline;">`BrightnessNoise`</a> class is designed to adjust the brightness of an image by scaling its pixel values with a fixed brightness factor. It inherits from the abstract base class <a href='../noise/#noise-module' style="text-decoration: underline;">`Noise`</a> and provides a mechanism for systematically applying brightness noise to images.

### **Attributes**

- **brightness_factor : `float`**
    
    The factor by which the brightness of the image will be scaled. A value less than 1.0 darkens the image, while a value greater than 1.0 brightens it.

### **Methods**

#### **`add_noise()`**
```py
add_noise(self, image: Image) -> Image:
```
Applies the `brightness` noise to the input image.

- **Parameters:**

    - **image : `Image`** 
        
        The input image to which brightness noise will be added.

- **Returns:**

    - `Image`: 
        
        The image with adjusted brightness.

#### **`_brightness_noise()`**
```py
_brightness_noise(self, image: Image) -> Image:
```
An internal method that performs the `brightness` adjustment.

- **Parameters:**
    - **image : `Image`** 
        
        The image whose brightness will be adjusted.

- **Returns:**
    - `Image`: 
        
        The image with adjusted brightness.

#### Usage Example
```py
from PIL import Image
from iftg.noises import BrightnessNoise

# Open an image
image = Image.open('path/to/image.tif')

# Create a BrightnessNoise object with a brightness factor of 0.7
brightness_noise = BrightnessNoise(brightness_factor=0.7)

# Apply brightness noise to the image
brightened_image = brightness_noise.add_noise(image)

# Save the brightened image
brightened_image.save('path/to/brightened_image.tif')

```


<br>

## **RandomBrightnessNoise Module**
The <a href='#randombrightnessnoise-module' style="text-decoration: underline;">`RandomBrightnessNoise`</a> class extends <a href='#brightnessnoise-module' style="text-decoration: underline;">`BrightnessNoise`</a> by introducing randomness to the brightness adjustment. Instead of using a fixed brightness factor, a random factor is selected from a specified range each time the noise is applied. This class is useful when you want to introduce variability in brightness adjustments across images.


### **Attributes**

- **brightness_factor_range : `tuple[float, float]`**

    The range of brightness factors to choose from. A random factor is selected within this range for each.

### **Methods**

#### **`add_noise()`** 
!!! Note
    Each call to `add_noise()` results in a different brightness factor, adding variability to the brightness adjustment. This is particularly useful when processing multiple images to introduce diverse brightness levels.
```py
add_noise(self, image: Image) -> Image:
```
Applies a `random brightness` adjustment to the input image by selecting a random brightness factor from the specified range.


- **Parameters:**

    - **image : `Image`** 
        
        The input image to which brightness noise will be added.

- **Returns:**

    - `Image`: 
        
        The image with random brightness adjustment.

#### Usage Example
```py
from PIL import Image
from iftg.noises import RandomBrightnessNoise

# Open an image
image = Image.open('path/to/image.jpg')

# Create a RandomBrightnessNoise object with a brightness factor range of (0.6, 1.2)
random_brightness_noise = RandomBrightnessNoise(brightness_factor_range=(0.6, 1.2))

# Apply random brightness noise to the image
random_brightened_image = random_brightness_noise.add_noise(image)

# Save the randomly brightened image
random_brightened_image.save('path/to/random_brightened_image.jpg')
```