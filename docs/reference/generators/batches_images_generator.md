# **<a href='#BatchesImagesGenerator-module' style="text-decoration: underline;">`BatchesImagesGenerator`</a> Module**

<a href='#BatchesImagesGenerator-module' style="text-decoration: underline;">`BatchesImagesGenerator`</a> is a class designed to generate images in batches, where each batch can have its own unique settings such as font, noise, background color, and margins. It inherits from the <a href='../generator/#generator-module' style="text-decoration: underline;">`Generator`</a> class and provides functionality to create and iterate over different batches of images.

Each batch generates multiple images based on a list of text strings, applying the specified style and noise settings. This class is useful when the user wants to create varied batches of images with different styles, formats, or noise effects.

## **Attributes:**

- **texts : `list[list[str]]`**

    A nested list where each inner list represents a batch of texts. Each batch of images will have texts from the corresponding inner list.

- **noises : `list[list[Noise]]`**

    A nested list of Noise objects to be applied to the images in each batch. Each batch of images will use the noise from the corresponding inner list.

- **font_paths : `list[str]`**
    
    A list of file paths to the fonts to be used for the text in each batch of images. Each batch will have its own font.

- **font_sizes : `list[float]`**
    
    A list of font sizes, where each value corresponds to the font size used in a batch of images.

- **font_colors : `list[str]`**
    
    A list of font colors, where each value corresponds to the font color used in a batch of images.

- **background_colors : `list[str]`**
    
    A list of background colors, where each value represents the background color of a batch of images.

- **margins : `list[tuple[int, int, int, int]]`**
    
    A list of margin tuples `(left, top, right, bottom)` to define text placement for each batch of images.

- **dpi : `list[tuple[float, float]]`**
    
    A list of DPI settings for each batch of images, where each tuple contains horizontal and vertical DPI values.

- **img_names : `list[str]`**
    
    A list of base names for the output image files, where each value corresponds to a batch of images.

- **img_formats : `list[str]`**
    
    A list of file formats for the output images, where each value represents the format of the images in the respective batch (e.g., `.tif`, `.png`).

- **img_output_paths : `list[str]`**
    
    A list of directory paths where the images of each batch will be saved. Each value corresponds to the output path for a batch.

- **txt_names : `list[str]`**
    
    A list of base names for the output text files that contain the image labels, where each value corresponds to a batch.

- **txt_formats : `list[str]`**
    
    A list of file formats for the output text files, where each value represents the format of the text file for the respective batch.

- **txt_output_paths : `list[str]`**
    
    A list of directory paths where the text files of each batch will be saved. Each value corresponds to a batch's output path for the text files.

- **background_image_paths : `list[str]`**
    
    A list of file paths for background images. Each batch can have its own background image.

## **Methods**
### **`_generate_next()`**

```py
_generate_next(self):
```

Generates the next batch of images using the specified settings for that batch.

- **Returns:**

    An instance of <a href='../images_generator/#imagegenerator-module' style="text-decoration: underline;">`ImagesGenerator`</a>, which is responsible for generating the images of the current batch.

- **Raises:**

    - `StopIteration`:
        
        When all batches have been generated. This method also clears the font cache for the last batch to avoid resource exhaustion.

### **`generate_batches()`**

```py
generate_batches(self, is_with_label: bool = True) -> None:
```

Generates and saves images for each batch. Optionally saves the corresponding text labels.

- **Parameters:**

    - **is_with_label : `bool`**
            
        If set to True, both images and their text labels are saved. If set to False, only images are saved without labels.
    
- **Returns:**
    - `None`


## **Usage Example**

```py

from iftg.noises import GaussianNoise, BlurNoise
from iftg.generators import BatchesImagesGenerator

texts = [["Hello World", "Batch 1"], ["Second Batch", "Text Here"]]
noises = [[GaussianNoise()], [BlurNoise()]]
font_paths = ["path/to/font1.ttf", "path/to/font2.ttf"]
font_sizes = [30, 40]
font_colors = ["blue", "green"]
background_colors = ["white", "gray"]
img_output_paths = ["output/batch1", "output/batch2"]
txt_output_paths = ["output/batch1", "output/batch2"]

batch_gen = BatchesImagesGenerator(
    texts=texts,
    font_paths=font_paths,
    noises=noises,
    font_sizes=font_sizes,
    font_colors=font_colors,
    background_colors=background_colors,
    img_output_paths=img_output_paths,
    txt_output_paths=txt_output_paths
)

# Generate batches with labels
batch_gen.generate_batches(is_with_label=True)
```

In the provided example, the <a href='#BatchesImagesGenerator-module' style="text-decoration: underline;">`BatchesImagesGenerator`</a> is used to generate two separate batches of images. Each batch has its own unique settings for text, font, noise effects, font size, font color, and background color. Additionally, the images are saved in two different output directories.

!!! Notes
    - **Handling Multiple Batches:**
        
        The <a href='#BatchesImagesGenerator-module' style="text-decoration: underline;">`BatchesImagesGenerator`</a> is designed to handle multiple batches of images, each with independent settings. The key benefit is the ability to define distinct properties like font, noise, and background for each batch, making it flexible for varied image creation tasks.

    - **Automatic List Extension:**
        
        The constructor automatically extends any shorter lists (e.g., `font_sizes`, `background_colors`) to match the longest list (in this case, `texts`). This ensures consistent generation across batches without the need for manually repeating settings.