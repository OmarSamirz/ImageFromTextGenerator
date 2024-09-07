# **<a href='#directorynoiseadder-module' style="text-decoration: underline;">`DirectoryNoiseAdder`</a> Module**

The <a href='#directorynoiseadder-module' style="text-decoration: underline;">`DirectoryNoiseAdder`</a> class is an extension of the abstract base class <a href='../noise_adder/#noiseadder-module', style="text-decoration: underline;">`NoiseAdder`</a>. It provides functionality for applying noise to multiple images located in a directory and saving the resulting noisy images to a specified output path. This class is ideal for batch image processing tasks where noise needs to be added to a collection of images.

## **Attributes**

- **dir_path : `str`**

    The path to the directory that contains the images to be processed.

- **output_path : `str`**

    The path where the processed images will be saved. 
    !!! Note
        If left empty, the images will be saved in the same directory as the source images.

- **noises : `list[Noise]`**

    A list of <a href='../../noises/noise/#noise-module' style="text-decoration: underline;">`Noise`</a> objects that represent different noise types to be applied to the images. Each <a href='../../noises/noise/#noise-module' style="text-decoration: underline;">`Noise`</a> object should adhere to the structure and behavior defined by the <a href='../../noises/noise/#noise-module' style="text-decoration: underline;">`Noise`</a> class from the `iftg.noises` module.

- **identifier : `str`**

    A unique identifier appended to the filenames of processed images. This is useful for distinguishing between original and processed images (e.g., an image named `example.tif` could become `example_noisy.tif`).

- **img_formats : `list[str]`**

    A list of image formats in which the processed images will be saved. These formats are typically strings like `'TIF'`, `'JPEG'`, etc.

## **Methods**

### **`_apply_noises()`**

```py
_apply_noises(self, image: Image) -> tuple[Image.Image, str, str]
```

This method applies the specified noise transformations to a given image.

- **Parameters:**

    - **image : `Image`** 

        The image object to which noises will be applied.

- **Returns:**

    - A `tuple` containing:
        - The transformed `Image` object (after applying noise),
        - The base name of the image file (without its extension),
        - The image file extension (with a dot, e.g., `.tif`).

### **`add_noises()`**

```py
add_noises(self) -> list[tuple[Image.Image, str, str]]
```

This method processes all the images in the directory by applying the specified noises.

- **Returns:**

    - A `list[tuple]`, where each tuple contains:
        - A noisy `Image.Image`,
        - The image's base name `str`,
        - The image's format or extension `str`.

### **`add_noises()`**

```py
add_noises(self) -> list[tuple[Image.Image, str, str]]
```

This method processes all the images in the directory by applying the specified noises.

- **Returns:**

    - A `list[tuple]`, where each tuple contains:
        - A noisy `Image.Image`,
        - The image's base name `str`,
        - The image's format or extension `str`.

### **`save_image()`**

```py
save_image(self, img_info: tuple[Image.Image, str, str]) -> None
```

This method saves a noisy image to the output path.

- **Parameters:**

    - **img_info : `tuple[Image.Image, str, str]`**
    
        A tuple containing the noisy image, the base name of the image, and the image format.

### **`transform_images()`**

```py
transform_images(self) -> None
```

This method triggers the entire process of transforming and saving images by applying noise.
It is abstract and should be implemented by subclasses to manage the full transformation workflow.

- **Returns:**
    - `None`

## **Usage Example**

```py
from iftg.noises import GaussianNoise
from iftg.adders import DirectoryNoiseAdder

# Define the noises to be applied
noises = [GaussianNoise(mean=0, sigma=25)]

# Create an instance of DirectoryNoiseAdder
dir_noise_adder = DirectoryNoiseAdder(
    dir_path='path/to/input_images',
    output_path='path/to/output_images',
    noises=noises,
    identifier='gaussian_noisy',
    img_formats=['jpg', 'png']
)

# Transform and save noisy images
dir_noise_adder.transform_images()
```

In this example, a list of <a href='../../noises' style="text-decoration: underline;">`Noise`</a> objects is created (in this case, a <a href='../../noises/gaussian_noise/' style="text-decoration: underline;">`GaussianNoise`</a> object), and the <a href='#directorynoiseadder-module'>`DirectoryNoiseAdder`</a> class is instantiated with the paths to input and output directories. It will apply the noise to all images in the directory and save the resulting noisy images.

!!! Notes
    1. **Image Formats:**
        
        The class supports reading and saving images in any format listed in the <a href='#attributes' style="text-decoration: underline;">`img_formats`</a>  attribute, making it flexible for various image file types.

    2. **Error Handling:**
        
        If the <a href='#attributes' style="text-decoration: underline;">`dir_path`</a> does not exist, the class raises a `FileNotFoundError`. Additionally, if no <a href='#attributes' style="text-decoration: underline;">`output_path`</a> is provided, the processed images will be saved in the original <a href='#attributes' style="text-decoration: underline;">`dir_path`</a>.

    3. **Efficiency:**
        
        The use of Python's `reduce` function allows for efficient chaining of noise transformations on each image. The class processes images in the order they are found, and can handle large directories by iterating over the images one by one.