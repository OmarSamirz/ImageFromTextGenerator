# **<a href='#erodenoise-module' style="text-decoration: underline;">ErodeNoise</a> & <a href='#randomerodenoise-module' style="text-decoration: underline;">RandomErodeNoise</a> Modules**

!!! Note 
    - Inheritance Structure: 
        - <a href='../noise/#noise-module' style="text-decoration: underline;">`Noise`</a> (Abstract Base Class) 
        - <a href='#erodenoise-module' style="text-decoration: underline;">`ErodeNoise`</a> (Concrete Implementation) 
        - <a href='#randomerodenoise-module' style="text-decoration: underline;">`RandomErodeNoise`</a> (Extends ErodeNoise with randomness)

## **ErodeNoise Module**
The <a href='#erodenoise-module' style="text-decoration: underline;">`ErodeNoise`</a> class applies erosion noise to an image, shrinking the white regions by performing morphological erosion using a structuring element (kernel).

### **Attributes**
- **kernel_size : `int`**

    The size of the structuring element (kernel) used for erosion. A larger kernel will erode more significant regions of the image.

- **iterations : `int`**

    The number of times the erosion operation is applied. Higher iteration counts will lead to more extensive erosion.

### **Methods**

#### **`add_noise()`**
```py
add_noise(self, image: Image) -> Image:
```
Public method that applies `erosion` noise to the input image by shrinking the white regions using a structuring element.

- **Parameters:**
    - **image : `Image`**

        The input image to which erosion noise will be added.

    - **Returns:**
        - `Image`:

            The image with erosion noise applied.


#### **`_erode_noise()`**
```py
_erode_noise(self, image: Image) -> Image:
```
Internal method that applies `erosion` by performing morphological operations using a structuring element (kernel).

- **Parameters:**
    - **image : `Image`**

        The image to which the erosion operation will be applied.

- **Returns:**

    - `Image`:

        The image with erosion noise applied.

### **Usage Example**
```py
from PIL import Image
from iftg.noises import ErodeNoise

# Open an image
image = Image.open('path/to/image.tif')

# Create an ErodeNoise object with kernel size 5 and 2 iterations
erode_noise = ErodeNoise(kernel_size=5, iterations=2)

# Apply erosion noise to the image
noisy_image = erode_noise.add_noise(image)

# Save the noisy image
noisy_image.save('path/to/noisy_image.tif')
```


<br>

## **RandomErodeNoise Module**

The <a href='#randomerodenoise-module' style="text-decoration: underline;">`RandomErodeNoise`</a> class extends the functionality of <a href='#erodenoise-module' style="text-decoration: underline;">`ErodeNoise`</a> by randomly selecting the kernel size and the number of iterations for the erosion operation within specified ranges. This adds more variation to the applied noise.

### **Attributes**
- **kernel_size_range : `tuple[int, int]`**

    The range of possible values for <a href='#attributes' style="text-decoration: underline;">`kernel_size`</a> (structuring element size).

- **iterations_range : `tuple[int, int]`**

    The range of possible values for <a href='#attributes' style="text-decoration: underline;">`iterations`</a> (number of iterations for the erosion operation).


### **Methods**
#### **`add_noise()`**
!!! Note 
    Each call to `add_noise()` results in a different erosion noise effect, as the kernel_size and iterations are chosen randomly from the specified ranges. This adds variability to the erosion process, which is especially useful for augmenting images with random noise.

```py
add_noise(self, image: Image) -> Image:
```
Public method that applies `erosion` noise with random kernel_size and iterations values to the input image.

- **Parameters:**

    - **image : `Image`**

        The input image to which random erosion noise will be applied.

- **Returns:**

    - `Image`:

        The image with random erosion noise applied.

### **Usage Example**
```py
from PIL import Image
from iftg.noises import RandomErodeNoise

# Open an image
image = Image.open('path/to/image.tif')

# Create a RandomErodeNoise object with kernel size range (3, 7) and iterations range (1, 3)
random_erode_noise = RandomErodeNoise(kernel_size_range=(3, 7), iterations_range=(1, 3))

# Apply random erosion noise to the image
random_noisy_image = random_erode_noise.add_noise(image)

# Save the randomly noisy image
random_noisy_image.save('path/to/random_noisy_image.tif')

```
