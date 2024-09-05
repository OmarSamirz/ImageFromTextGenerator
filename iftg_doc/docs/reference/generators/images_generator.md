# **<a href='#imagesgenerator-module' style="text-decoration: underline;">`ImagesGenerator`</a> Module**


The <a href='#imagesgenerator-module' style="text-decoration: underline;">`ImagesGenerator`</a> class extends the <a href='../generator/#generator-module' style="text-decoration: underline;">`Generator`</a> class to create a sequence of images with varying text and noise effects. It handles the generation of images based on the provided configuration and includes functionality to save both images and their corresponding text labels.

## **Attributes**

- **texts : list[str]**

    A list of texts to be used for generating images. Each text in the list will be applied to a separate image.

- **font_path : str**

    The file path to the font used for rendering text on the images. The font must be accessible at this path.

- **noises : list[Noise]**

    A list of noise objects that will be applied to the images. These can be used to add random variations or effects to the images.

- **font_size : float**

    The size of the font used in the images. This value determines the text size.

- **font_color : str**

    The color of the text in the images. The color should be specified in a format supported by the image library (e.g., 'black', '#000000').

- **background_color : str**

    The background color of the images. This color will be used if no background image is specified.

- **margins : tuple[int, int, int, int]**

    Margins for text placement on the images. The tuple (left, top, right, bottom) specifies the margins around the text.

- **dpi : tuple[float, float]**

    The DPI (dots per inch) settings for the images. This tuple specifies the horizontal and vertical DPI.

- **img_name : str**

    The base name for the output image files. This name will be used as the prefix for generated image files.

- **img_format : str**

    The file format for the output images (e.g., '.png', '.jpg'). This format determines the image file type.

- **img_output_path : str**

    The directory where the generated images will be saved. This path must be accessible and writable.

- **txt_name : str**

    The base name for the output text files that will contain the image labels. Each text file will be named using this base name.

- **txt_format : str**

    The file format for the output text files (e.g., '.txt'). This format determines the text file type.

- **txt_output_path : str**

    The directory where the generated text files will be saved. This path must be accessible and writable.

- **auto_remove_font : bool**

    A flag indicating whether to automatically remove the font from the cache after image generation. If True, the font will be removed to free up memory.

- **background_image_path : str**

    The file path to the background image, if any. If specified, this image will be used as the background for the generated images.

## **Methods**

### **`_generate_next`**

```py
_generate_next(self) -> tuple[Image.Image, str]
```

Generates the next image in the sequence. This method is called by the <a href='../generator/#__next__' style="text-decoration: underline;">`__next__`</a> method.

- **Returns:**
    - **tuple:**

        A tuple containing the generated image `Image.Image`, the text used `str`, and the index `int`.

- **Raises:**
    - **StopIteration:**

        When all images have been generated and the font cache is cleared.


### **`_save_images()`**

```py
_save_image(self, img: Image, i: int) -> None
```

Saves the image to the specified output path.

- **Parameters:**
    - **img : Image**
    
        The image to be saved.

    - **i : int**
    
        The index to append to the image file name.

### **`_save_image_and_text()`**

```py
_save_image_and_text(self, img_info: tuple[Image.Image, str, int]) -> None
```

Saves both the image and the corresponding text to their respective output paths.

- **Parameters:**
    - **img_info : tuple[Image.Image, str, int]**
        
        A tuple containing the image `Image.Image`, the text `str`, and the index `int`.

### **`generate_images()`**

```py
generate_images(self) -> None
```

Generates and saves images to the specified output directory.

- **Creates:**

    The output directory if it does not exist.

- **Saves:**

    Each generated image to the specified output path using _save_image.

### **`generate_images_with_text`**

```py
generate_images_with_text(self) -> None
```

Generates images and saves both the images and their corresponding texts to the specified directories.

- **Creates:**

    The output directories if they do not exist.

- **Saves:**

    Each generated image and its label to their respective paths using _save_image_and_text.

## **Example Usage**
Here’s how you might use the <a href='#imagesgenerator-module' style="text-decoration: underline;">`ImagesGenerator`</a> class:

```py
from iftg.noises import GaussianNoise
from iftg.generators import ImagesGenerator

# Define configuration
generator = ImagesGenerator(
    texts=["Hello World", "Test Image"],
    font_path="path/to/the/font",
    noises=[GaussianNoise(mean=0, sigma=25)],
    font_size=40,
    font_color="black",
    background_color="white",
    margins=(10, 10, 10, 10),
    dpi=(300, 300),
    img_name="image",
    img_format=".png",
    img_output_path="./images",
    txt_name="label",
    txt_format=".txt",
    txt_output_path="./labels",
    background_image_path=""
)

# Generate and save images with text
generator.generate_images_with_text()
```