# **<a href='#imagenoiseadder-module' style="text-decoration: underline;">`ImageNoiseAdder`</a> Module**

<a href='#imagenoiseadder-module' style="text-decoration: underline;">`ImageNoiseAdder`</a> is a class used to apply various noise effects to an image and save the resulting noisy image to a specified directory. It extends the <a href='../noise_adder/#noiseadder-module' style="text-decoration: underline;">`NoiseAdder`</a> class, leveraging its functionality.


## **Attributes**

- **img_path : `str`**
    
    The file path to the input image that will have noise applied to it.

- **output_path : `str`**
    
    The directory where the noisy image will be saved. Defaults to an empty string.
    !!! Note
        If left empty, the image will be saved in the same directory as the input image.



- **noises : `list[Noise]`**
    
    A list of noise objects that will be applied to the image. These should be instances of <a href='../../noises/noise/#noise-module' style="text-decoration: underline;">`Noise`</a> or its subclasses.

- **identifier : `str`**
    
    An identifier for the noisy image file. Defaults to 'noisy'.

## **Methods**

### **`_apply_noises()`**
```py
_apply_noises(self, image: Noise) -> tuple[Image.Image, str, str]:
```
This method applies the list of noise objects to the provided image.

- **Parameters:**
    - **image : `Image`**
        
        The image to which noises will be applied. This should be an instance of Image.

- **Returns:**
    - `tuple`: A tuple containing:

        - The noisy image `Image`.
        - The base name of the image file (excluding extension) `str`.
        - The image format (including the dot) `str`.

### **`add_noises()`**
This method opens the image from the specified file path <a href='#attributes' style="text-decoration: underline;">`img_path`</a>, applies the list of noises to it, and returns the noisy image along with its base name and format.

```py
def add_noises(self) -> tuple[Image.Image, str, str]:
```

- **Returns:**
    - `tuple`: A tuple containing:
        - The noisy image `Image`.
        - The base name of the image file (excluding extension) `str`.
        - The image format (including the dot) `str`.


### **`save_image()`**

```py
save_image(self, img_info: tuple[Image.Image, str, str]) -> None:
```
This method saves the noisy image to the specified output directory <a href='#attributes' style="text-decoration: underline;">`output_path`</a> using the file name and format provided.

- **Parameters:**

    - img_info `tuple` containing:
        - The noisy image `Image.Image`.
        - The base name of the image file (without extension).
        - The image format (e.g., `.tif`, `.png`).

- **Returns:**
    - `None`

### **`transform_image()`**

```py
transform_image(self) -> None:
```
This method orchestrates the entire process of applying noises to the image and saving the result.

- **Returns:**
    - `None`

## Usage Example

```py
from iftg.adders import ImageNoiseAdder
from iftg.noises import BlurNoise, GaussianNoise

# Create noise objects (assumes Noise is a valid class and instantiated correctly)
noise_list = [BlurNoise(), GaussianNoise()]

# Instantiate the ImageNoiseAdder
noise_adder = ImageNoiseAdder(
    img_path='path/to/image.jpg',
    output_path='path/to/output',
    noises=noise_list,
    identifier='noisy'
)

# Apply noise and save the noisy image
noise_adder.transform_image()
```

In this example, we demonstrate how to use the <a href='#imagenoiseadder-module' style="text-decoration: underline;">`ImageNoiseAdder`</a> class to apply noise effects to an image and save the result in a specified directory.

!!! Notes
    1. **Error Handling:**

        The constructor checks if the provided <a href='#attributes' style="text-decoration: underline;">`img_path`</a> exists. If it does not, a `FileNotFoundError` is raised. Ensure the path to the image is correct to avoid runtime errors.

    
    2. **Flexible Output:**
        
        The <a href='#attributes' style="text-decoration: underline;">`output_path`</a> allows specifying where the noisy image will be saved. If no path is provided (empty string), it will use the inputed image.

    3. **Identifier and File Naming:**
        
        The <a href='#attributes' style="text-decoration: underline;">`identifier`</a> helps distinguish the noisy images from the original ones. The saved image will include the identifier in its file name, followed by the batch or image number.

