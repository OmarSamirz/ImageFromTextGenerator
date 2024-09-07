# **<a href='#dilatenoise-module' style="text-decoration: underline;">`DilateNoise`</a> & <a href='#randomdilatenoise-module' style="text-decoration: underline;">`RandomDilateNoise`</a> Modules**

!!! Note
    - **Inheritance Structure:**
        - <a href='../noise/#noise-module' style="text-decoration: underline;">`Noise`</a> (Abstract Base Class)
        - <a href='#dilatenoise-module' style="text-decoration: underline;">`DilateNoise`</a> (Concrete Implementation)
        - <a href='#randomdilatenoise-module' style="text-decoration: underline;">`RandomDilateNoise`</a> (Extends DilateNoise with randomness)

## **DilateNoise**
The <a href='#dilatenoise-module' style="text-decoration: underline;">`DilateNoise`</a> class is designed to apply dilation noise to an image by using a morphological dilation operation. The dilation process enlarges the white regions in the image, which can be useful for data augmentation and creating specific visual effects. 

### **Attributes**
- **kernel_size : `int`**
    
    The size of the structuring element (kernel) used for dilation. A larger kernel size results in more pronounced dilation effects.

- **iterations : `int`**
    
    The number of times the dilation operation is applied. More iterations produce stronger dilation effects.

### **Methods**

#### **`add_noise()`**
```py
add_noise(self, image: Image) -> Image:
```
Applies `dilation` noise to the input image by enlarging white regions using a structuring element.

- **Parameters:**

    - **image : `Image`** 
        
        The input image to which dilation noise will be added.

- **Returns:**

    - `Image`: 
        
        The image with dilation noise applied.


#### **`_dilate_noise()`**
```py
_dilate_noise(self, image: Image) -> Image:
```
An internal method that performs the dilation operation on the image.

- **Parameters:**

    - **image : `Image`**

        The image to which dilation will be applied.

- **Returns:**
    - `Image`: 
        
        The image with the dilation effect applied.

### Usage Example
```py
from PIL import Image
from iftg.noises import DilateNoise

# Open an image
image = Image.open('path/to/image.tif')

# Create a DilateNoise object with a kernel size of 4 and 2 iterations
dilate_noise = DilateNoise(kernel_size=4, iterations=2)

# Apply dilation noise to the image
dilated_image = dilate_noise.add_noise(image)

# Save the dilated image
dilated_image.save('path/to/dilated_image.tif')

```

## **RandomDilateNoise**
The <a href='#randomdilatenoise-module' style="text-decoration: underline;">`RandomDilateNoise`</a>  class extends <a href='#dilatenoise-module' style="text-decoration: underline;">`DilateNoise`</a> by introducing randomness in both the size of the structuring element (kernel) and the number of iterations for dilation. This adds variability to the dilation noise applied to different images.

### **Attributes**
- **kernel_size_range : `tuple[int, int]`**
    
    A tuple representing the range of possible kernel sizes to randomly select from. The first element is the minimum size, and the second is the maximum size.

- **iterations_range : `tuple[int, int]`**
    
    A tuple representing the range of possible iteration counts to randomly select from.

### **Methods**

#### **`add_noise()`**
!!! Note
    Each call to `add_noise()` results in a different dilate noises, adding variability to the dilation adjustment. This is particularly useful when processing multiple images to introduce diverse dilate levels.

```py
add_noise(self, image: Image) -> Image:
```
Applies `random dilation` noise to the input image by selecting a random kernel size and a random number of iterations within the specified ranges.

- **Parameters:**

    - **image : `Image`** 
        
        The input image to which random dilation noise will be applied.

- **Returns:**

    - `Image`: 
        
        The image with random dilation noise applied.


### Usage Example
```py
from PIL import Image
from iftg.noises import RandomDilateNoise

# Open an image
image = Image.open('path/to/image.tif')

# Create a RandomDilateNoise object with a kernel size range of (3, 6) and iterations range of (1, 3)
random_dilate_noise = RandomDilateNoise(kernel_size_range=(3, 6), iterations_range=(1, 3))

# Apply random dilation noise to the image
random_dilated_image = random_dilate_noise.add_noise(image)

# Save the randomly dilated image
random_dilated_image.save('path/to/random_dilated_image.tif')
```

