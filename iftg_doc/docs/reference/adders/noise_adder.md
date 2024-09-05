# **<a href='#noiseadder-module' style="text-decoration: underline;">`NoiseAdder`/a> Module**
!!! warning
    This module is considered internal.

<a href='#noiseadder-module style="text-decoration: underline;"'>`NoiseAdder`</a> is an abstract base class designed to handle the application of noise to images. Subclasses inheriting from <a href='#noiseadder-module' style="text-decoration: underline;">`NoiseAdder`</a> must implement its abstract methods to define specific noise-adding behaviors.

## **Attributes**

- **identifier : str**

    A unique identifier for the noise adder instance. This is used to distinguish between different noise adders or configurations.

- **img_formats : list[str]**

    A list of image formats in which the processed images will be saved. These formats are typically strings like `'TIF'`, `'JPEG'`, etc.

- **noises : list[Noise]**

    A list of Noise objects that represent different noise types to be applied to the images. Each Noise object should adhere to the structure and behavior defined by the Noise class from the iftg.noises module.

## **Methods**

### **`_apply_noises()`**

```py   
_apply_noises(<p style="color: blue;">self</p>, image: Image) 
-> tuple[Image.Image, str, str]
```

This method applies the specified noises to an image.
It is an abstract method that must be implemented by any subclass.

- **Parameters:**

    - **image : Image**

        The image object to which noises will be applied.

- **Returns:**

    - **A tuple containing:**
        - The transformed `Image` object (after applying noise),
        - A `str` representing the name or format of the image,
        - A `str` representing the extension or format for saving the image (e.g., `.tif`, `.jpg`).

### **`add_noises()`**

```py
add_noises(self) -> list[tuple[Image.Image, str, str]]
```

This method generates a list of images with noises applied.
Subclasses must implement this method to handle batch noise application to multiple images.

- **Returns:**

    - **A list of tuples where each tuple contains:**
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

    - **img_info : tuple[Image.Image, str, str]**
        
        The tuple representing the image and its saving information.

- **Returns:**
    - None

### **`transform_images()`**

```py
transform_images(self) -> None
```

This method triggers the entire process of transforming and saving images by applying noise.
It is abstract and should be implemented by subclasses to manage the full transformation workflow.

- **Returns:**
    - None