# **<a href='#flipnoise-module' style="text-decoration: underline;">FlipNoise</a> & <a href='#randomflipnoise-module' style="text-decoration: underline;">RandomFlipNoise</a> Modules**

!!! Note 
    - Inheritance Structure: 
        - <a href='../noise/#noise-module' style="text-decoration: underline;">`Noise`</a> (Abstract Base Class) 
        - <a href='#flipnoise-module' style="text-decoration: underline;">`FlipNoise`</a> (Concrete Implementation) 
        - <a href='#randomflipnoise-module' style="text-decoration: underline;">`RandomFlipNoise`</a> (Extends FlipNoise with randomness)

## **FlipNoise Module**
The <a href='#flipnoise-module' style="text-decoration: underline;">`FlipNoise`</a> class applies flipping noise to an image, mirroring it along a specified axis.

### **Attributes**
- **flip_type : `int`**

    Specifies the type of flip operation to be applied. It supports two types of flips:

    `0`: Flip the image horizontally (mirror along the vertical axis).
    
    `1`: Flip the image vertically (mirror along the horizontal axis).

### **Methods**
#### **`add_noise()`**
```py
add_noise(self, image: Image) -> Image:
```
Public method that applies `flipping` noise to the input image by mirroring it along a specified axis.

- **Parameters:**

    - **image : `Image`**

        The input image to which flipping noise will be added.

- **Returns:**

    - `Image`:

        The image with flipping noise applied.

#### **`_flip_noise()`**
```py
_flip_noise(self, image: Image) -> Image:
```
Internal method that performs the actual flip operation based on the specified <a href='#attributes' style="text-decoration: underline;">`flip_type`</a>.

- **Parameters:**

    - **image : `Image`**

        The image to which the flip will be applied.

- **Returns:**

    - `Image`:

        The flipped image.

### **Usage Example**
```py
from PIL import Image
from iftg.noises import FlipNoise

# Open an image
image = Image.open('path/to/image.tif')

# Create a FlipNoise object to flip the image horizontally (default)
flip_noise = FlipNoise(flip_type=0)

# Apply flipping noise to the image
flipped_image = flip_noise.add_noise(image)

# Save the flipped image
flipped_image.save('path/to/flipped_image.tif')
```

<br>

## **RandomFlipNoise Module**
The <a href='#randomflipnoise-module' style="text-decoration: underline;">`RandomFlipNoise`</a> class extends the functionality of <a href='#flipnoise-module' style="text-decoration: underline;">`FlipNoise`</a> by randomly selecting the flip type (either horizontal or vertical) for each image, adding variability to the flipping operation.

### **Attributes**
This class inherits the attributes of <a href='#flipnoise-module' style="text-decoration: underline;">`FlipNoise`</a> but chooses the <a href='#attributes' style="text-decoration: underline;">`flip_type`</a> randomly during the application of noise.

### **Methods**
#### **`add_noise()`**
!!! Note 
    Each call to `add_noise()` results in a different flip type (horizontal or vertical), adding randomness to the flipping operation. This feature is particularly useful when augmenting datasets with random image transformations.

```py
add_noise(self, image: Image) -> Image:
```
Public method that applies random `flipping` noise by selecting a random flip_type (horizontal or vertical).

- **Parameters:**

    - **image : `Image`**

        The input image to which random flipping noise will be applied.

- **Returns:**

    - `Image`:

        The image with random flipping noise applied.

### **Usage Example**
```py
from PIL import Image
from iftg.noises import RandomFlipNoise

# Open an image
image = Image.open('path/to/image.tif')

# Create a RandomFlipNoise object
random_flip_noise = RandomFlipNoise()

# Apply random flipping noise to the image
random_flipped_image = random_flip_noise.add_noise(image)

# Save the randomly flipped image
random_flipped_image.save('path/to/random_flipped_image.tif')
```