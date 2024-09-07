# **<a href='#blurnoise-module' style="text-decoration: underline;">`BlurNoise`</a> & <a href='#randomblurnoise-module' style="text-decoration: underline;">`RandomBlurNoise`</a> Modules**

!!! Note
    - **Inheritance Structure:**
        - <a href='../noise/#noise-module' style="text-decoration: underline;">`Noise`</a> (Abstract Base Class)
        - <a href='#blurnoise-module' style="text-decoration: underline;">`BlurNoise`</a> (Concrete Implementation)
        - <a href='#randomblurnoise-module' style="text-decoration: underline;">`RandomBlurNoise`</a> (Extends BlurNoise with randomness)

## **BlurNoise Module**
The <a href='#blurnoise-module' style="text-decoration: underline;">`BlurNoise`</a> class is designed to apply `Gaussian blur` noise to images using the Pillow library. It inherits from the abstract base class <a href='../noise/#noise-module' style="text-decoration: underline;">`Noise`</a> and implements the add_noise method.


### **Attributes**
- **blur_radius : `float`**

    The radius of the Gaussian blur to be applied. A higher value results in a more blurred image.

### **Methods**

#### **`add_noise()`**

```py
add_noise(self, image: Image) -> Image:
```
Applies `Gaussian blur` noise to the input image.

- **Parameters:**

    - **image : `Image`**
        
         The input image to which the noise will be added.

- **Returns:**

    - `Image`:  
        
        The image with Gaussian blur applied.

#### **`_blur_noise`**
```py
_blur_noise(self, image: Image) -> Image:
```
An internal method that applies the `Gaussian blur` to the image.

- **Parameters:**

    - **image : `Image`** 
            
        The image to which the Gaussian blur will be applied.

- **Returns:**
    - `Image`: 
    
        The blurred image.

### Usage Example
```py
from PIL import Image
from iftg.noises import BlurNoise

# Open an image
image = Image.open('path/to/image.tif')

# Create a BlurNoise object with a specific blur radius
blur_noise = BlurNoise(blur_radius=5.0)

# Apply the blur noise to the image
blurred_image = blur_noise.add_noise(image)

# Save the blurred image
blurred_image.save('path/to/blurred_image.tif')
```

<br>
## **RandomBlurNoise Module**
The <a href='#randomblurnoise-module' style="text-decoration: underline;">`RandomBlurNoise`</a> class extends <a href='#blurnoise-module' style="text-decoration: underline;">`BlurNoise`</a> by introducing randomness to the blur radius. Instead of using a fixed blur radius, it selects a random value within a specified range each time the noise is applied.


### **Attributes**
- **blur_radius_range : `tuple[float, float]`**

    A tuple representing the minimum and maximum values between which the blur radius will be randomly selected.

### **Methods**

#### **`add_noise()`**
!!! Note
    Each call to `add_noise()` results in a different blur radius, adding variability to the blur effect. This is particularly useful when processing multiple images to prevent uniform blur across all images.

```py
add_noise(self, image: Image) -> Image:
```
Applies `Gaussian blur` noise with a `random` radius to the input image.


- **Parameters:**
    - **image : `Image`**
        
        The input image to which the noise will be added.

- **Returns:**

    - `Image`: 
        
        The image with random Gaussian blur applied.


#### Usage Example
```py
from PIL import Image
from iftg.noises import RandomBlurNoise

# Open an image
image = Image.open('path/to/image.tif')

# Create a RandomBlurNoise object with a blur radius range
random_blur_noise = RandomBlurNoise(blur_radius_range=(2.0, 6.0))

# Apply random blur noise to the image
random_blurred_image = random_blur_noise.add_noise(image)

# Save the randomly blurred image
random_blurred_image.save('path/to/random_blurred_image.tif')

```