# **<a href='#rotationnoise-module' style="text-decoration: underline;">`RotationNoise`</a> & <a href='#randomrotationnoise-module' style="text-decoration: underline;">`RandomRotationNoise`</a> Modules**

!!! Note 
    - **Inheritance Structure:** 
        - <a href='../noise/#noise-module' style="text-decoration: underline;">`Noise`</a> (Abstract Base Class) 
        - <a href='#rotationnoise-module' style="text-decoration: underline;">`RotationNoise`</a> (Concrete Implementation) 
        - <a href='#randomrotationnoise-module' style="text-decoration: underline;">`RandomRotationNoise`</a> (Extends RotationNoise with randomness)

## **RotationNoise Module**
The <a href='#rotationnoise-module' style="text-decoration: underline;">`RotationNoise`</a> class applies rotation noise to an image by rotating the image by a fixed angle. The background color and resampling method can be specified to fill the empty space after rotation.

### **Attributes**
- **rotation_angle : `float`**

    The angle (in degrees) by which the image will be rotated. A positive value rotates the image clockwise, while a negative value rotates it counterclockwise.

- **background_color : `str`**

    The color of the background that fills in the empty spaces after rotation. Specified as a string (e.g., `#FFFFFF` for `white`).

### **Methods**
#### **`add_noise()`**
```py
add_noise(self, image: Image) -> Image:
```
Public method that applies `rotation` noise to the input image by rotating it according to the specified angle and background color.

- **Parameters:**

    - **image : `Image`**

        The input image to which rotation noise will be added.

- **Returns:**

    - `Image`:

        The rotated image with the specified background color.

#### **`_rotation_noise()`**
```py
_rotation_noise(self, image: Image) -> Image:
```
Internal method that performs the actual `rotation` of the image using the specified angle and resampling method.

- **Parameters:**

    - **image : `Image`**

        The image to which rotation noise will be applied.

- **Returns:**

    - `Image`:

        The rotated image with the applied background color.

### **Usage Example**
```py
from PIL import Image
from iftg.noises import RotationNoise

# Open an image
image = Image.open('path/to/image.tif')

# Create a RotationNoise object with a rotation angle of 45 degrees and background color 'black'
rotation_noise = RotationNoise(rotation_angle=45.0, background_color='black')

# Apply rotation noise to the image
rotated_image = rotation_noise.add_noise(image)

# Save the rotated image
rotated_image.save('path/to/rotated_image.tif')
```

<br>

## **RandomRotationNoise Module**
The <a href='#randomrotationnoise-module' style="text-decoration: underline;">`RandomRotationNoise`</a> class extends the functionality of <a href='#rotationnoise-module' style="text-decoration: underline;">`RotationNoise`</a> by selecting a random rotation angle from a specified range.

### **Attributes**
- **rotation_angle_range : `tuple[float, float]`**

    The range within which the rotation angle will be randomly selected. The lower bound defines the maximum counterclockwise rotation, while the upper bound defines the maximum clockwise rotation.

- **background_color : `str`**

    The color of the background that fills in the empty spaces after rotation. Specified as a string (e.g., `#FFFFFF` for `white`).

### **Methods**
#### **`add_noise()`**
!!! Note 
    Each call to `add_noise()` results in a different rotation by selecting a random angle within the specified range.

```py
add_noise(self, image: Image) -> Image:
```
Public method that applies `random rotation` noise to the input image by selecting a random rotation angle within the specified range.

- **Parameters:**

    - **image : `Image`**

        The input image to which random rotation noise will be added.

- **Returns:**

    - `Image`:

        The rotated image with the randomly selected angle and background color.

### **Usage Example**
```py
from PIL import Image
from iftg.noises import RandomRotationNoise

# Open an image
image = Image.open('path/to/image.tif')

# Create a RandomRotationNoise object with a rotation angle range of (-30, 30) and background color 'red'
random_rotation_noise = RandomRotationNoise(rotation_angle_range=(-30.0, 30.0), background_color='red')

# Apply random rotation noise to the image
random_rotated_image = random_rotation_noise.add_noise(image)

# Save the randomly rotated image
random_rotated_image.save('path/to/random_rotated_image.tif')
```