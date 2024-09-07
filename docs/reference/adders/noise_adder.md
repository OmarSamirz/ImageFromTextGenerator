# **<a href='#noiseadder-module' style="text-decoration: underline;">`NoiseAdder`</a> Module**

!!! warning
    This module is considered internal.

<a href="#noiseadder-module" style="text-decoration: underline;">`NoiseAdder`</a> is an abstract base class designed to handle the application of noise to images. Subclasses inheriting from <a href='#noiseadder-module' style="text-decoration: underline;">`NoiseAdder`</a> must implement its abstract methods to define specific noise-adding behaviors.

## **Attributes**

- **noises : `list[Noise]`**

    A list of <a href='../../noises/noise/#noise-module' style="text-decoration: underline;">`Noise`</a> objects that represent different noise types to be applied to the images. Each <a href='../../noises/noise/#noise-module' style="text-decoration: underline;">`Noise`</a> object should adhere to the structure and behavior defined by the <a href='../../noises/noise/#noise-module' style="text-decoration: underline;">`Noise`</a> class from the iftg.noises module.

- **output_path : `str`**

    The path where the processed image will be saved.

- **identifier : `str`**

    A unique identifier for the noise adder instance. This is used to distinguish between different noise adders or configurations.


## **Methods**

### **`_apply_noises()`**

```py   
_apply_noises(self, image: Image) 
-> tuple[Image.Image, str, str]
```

This method applies the specified noises to an image.
It is an abstract method that must be implemented by any subclass.

- **Parameters:**

    - **image : `Image`**

        The image object to which noises will be applied.

- **Returns:**

    - **A `tuple` containing:**
        - The transformed `Image` object (after applying noise),
        - A `str` representing the name or format of the image,
        - A `str` representing the extension or format for saving the image (e.g., `.tif`, `.jpg`).

### **`add_noises()`**

```py
add_noises(self) -> tuple[Image.Image, str, str] | list[tuple[Image.Image, str, str]]
```

This method generates a list of images or a single image with noises applied.
Subclasses must implement this method to handle batch noise application to multiple images.

- **Returns:**

    - **A `list[tuple]` where each tuple contains:**
        - The transformed `Image`,
        - The image name `str`,
        - The image format or extension `str`.


### **`save_image()`**

```py
save_image(self, img_info: tuple[Image.Image, str, str]) -> None
```

This method saves an image after noises have been applied.
It takes a tuple containing the image, name, and format and saves the image to the corresponding file.

- **Parameters:**

    - **img_info : `tuple[Image.Image, str, str]`**
        
        The tuple representing the image and its saving information.

- **Returns:**
    - `None`
