# **Tutorial: To be continued**

Welcome to the IFTG (Image From Text Generator) package tutorial. This guide will walk you through the key modules and functionalities provided by the package, allowing you to create robust datasets for OCR (Optical Character Recognition) models. Whether you're augmenting images with noise, generating text-based images, or creating batches of data, this tutorial will guide you step-by-step.


## **Adders**


### **<a href='../../reference/adders/image_noise_adder' style="text-decoration: underline;">`ImageNoiseAdder`</a> Module**
<a href='../../reference/adders/image_noise_adder' style="text-decoration: underline;">`ImageNoiseAdder`</a> is a class used to apply various noise effects to an image and save the resulting noisy image to a specified directory. It extends the <a href='../../reference/adders/noise_adder', style="text-decoration: underline;">`NoiseAdder`</a> class, leveraging its functionality.

#### **How to use `ImageNoiseAdder`**
```py
iftg.adders import ImageNoiseAdder
from iftg.noises import PixelDropoutNoise, RandomGaussianNoise

# Initialize ImageNoiseAdder with the specified parameters
result = ImageNoiseAdder(img_path='path/to/image.tif',  # Path to the input image file.
                            output_path='',    #  Directory where the noisy image will be saved. Default is an empty string.
                            noises=[PixelDropoutNoise(), RandomGaussianNoise()],  # List of noise objects to be applied to the image.
                            identifier='noisy' # Identifier for the noisy image file.
                        )

# Apply the specified noises and save the transformed images
result.transform_image()
```

### **<a href='../../reference/adders/directory_noise_adder' style="text-decoration: underline;">`DirectoryNoiseAdder`</a> Module**
The <a href='../../reference/adders/directory_noise_adder' style="text-decoration: underline;">`DirectoryNoiseAdder`</a> class is an extension of the abstract base class <a href='../../reference/adders/noise_adder', style="text-decoration: underline;">`NoiseAdder`</a>. It provides functionality for applying noise to multiple images located in a directory and saving the resulting noisy images to a specified output path. This class is ideal for batch image processing tasks where noise needs to be added to a collection of images.

#### **How to use `DirectoryNoiseAdder`**
```py
from iftg.adders import DirectoryNoiseAdder
from iftg.noises import (GaussianNoise, PixelDropoutNoise, RotationNoise, ShadowNoise)

# Initialize DirectoryNoiseAdder with the specified parameters
results = DirectoryNoiseAdder(dir_path='path/to/directory', # The path to the directory containing images to be processed.
                                output_path='path/to/output/directory',   # The path where the processed images will be saved.
                                noises=[RotationNoise(), # A list of noise objects to be applied to the images.
                                        GaussianNoise(),
                                        PixelDropoutNoise(),
                                        ShadowNoise()
                                        ],
                                identifier='noisy',   # A unique identifier to append to the filenames of the processed images.
                                img_formats=['jpg', 'png'],   # A list of image formats to be considered for processing.
                                )

# Apply the specified noises and save the transformed images
results.transform_images()
```

<br>
<br>

## **Creators**

### **<a href='../../reference/creators/image_creator' style="text-decoration: underline;">`ImageCreator`</a> Module**
The <a href='../../reference/creators/image_creator' style="text-decoration: underline;">`ImageCreator`</a> class extends the <a href="../../reference/creators/creator" style="text-decoration: underline;">`Creator`</a>
base class to provide functionality for generating images with customizable text, noise, and visual effects. This class is particularly useful for creating synthetic data by augmenting text-based images with noise or other transformations.

#### **How to use `ImageCreator`**
```py
from PIL import Image
from iftg.creators import ImageCreator

# Define the text
text = 'Hello, World!'


# Create an image with specified parameters
image = ImageCreator.create_image(text=text,    # The text to be drawn on the image.
                                    font_path='path/to/the/font', # The file path to the font.
                                    noises=[],    # A list of noise objects to apply to the image.
                                    font_size=50, # The size of the font.
                                    font_color='black',   # The color of the text. It can be text or hexadecimal
                                    background_color='white', # The background color of the image. It can be text or hexadecimal
                                    margins=(5, 5, 5, 5), # Margins for text placement on the image (left, top, right, bottom). 
                                    dpi=(300, 300),   # The resolution of the image (dots per inch). 
                                    background_img=Image.open('path/to/background/image'),   # An optional background image to be used as a base.
                                    clear_font=True, # Whether to clear the font cache after creating the image.
                                    )


# Save the created image to a file
image.save('image.tif', **image.info)
```

<br>
<br>


## **Generators**

### **<a href='../../reference/generators/images_generator' style="text-decoration: underline;">`ImagesGenerator`</a> Module**

The <a href='../../reference/generators/images_generator' style="text-decoration: underline;">`ImagesGenerator`</a> class extends the <a href='../../reference/generators/generator' style="text-decoration: underline;">`Generator`</a> class to create a sequence of images with varying text and noise effects. It handles the generation of images based on the provided configuration and includes functionality to save both images and their corresponding text labels.

#### **How to use `ImagesGenerator`**
```py
from iftg.generators import ImagesGenerator
from iftg.noises import (BlurNoise, BrightnessNoise, DilateNoise)

texts = ['Hello, World!']

results = ImagesGenerator(texts=texts,  # A list of texts to be used for image creation.
                          font_path= "path/to/the/font",    # The file path to the font used in the images.
                          noises=[BlurNoise(),  # A list of noise objects to be applied to the images.
                                  BrightnessNoise(),
                                  DilateNoise()
                                 ],    
                          font_size= 40,    # The size of the font used in the images.
                          font_color= 'black',  # The color of the text in the images.
                          background_color= 'white',    # The background color of the images.
                          margins= (5, 5, 5, 5),    # Margins for text placement on the images.
                          dpi= (300, 300),  # The DPI (dots per inch) settings for the images.
                          img_name='img',   # The base name for the output image files.
                          img_format='.tif',    # The file format for the output images.
                          img_output_path='output', # The directory where the generated images will be saved.
                          txt_name='text',  # The base name for the output text files containing the image labels.
                          txt_format='.txt',    # The file format for the output text files.
                          txt_output_path='output', # The directory where the generated text files will be saved.
                          auto_remove_font=True,    # A flag indicating whether to automatically remove the font from the cache after image generation.
                          background_image_path='', # The file path to the background image, if any.
                         )

# Generate and save the images without labels
results.generate_images()

# OR

# Generate and save images with labels
results.generate_images_with_text()

# OR

# You can use for-loop to further modify your images or do something else
for img, lbl, i in results:
    img.save(f'img_{i}.tif', **img.info)
```


### **<a href='../../reference/generators/batches_images_generator' style="text-decoration: underline;">`BatchesImagesGenerator`</a> Module**

<a href='../../reference/generators/batches_images_generator' style="text-decoration: underline;">`BatchesImagesGenerator`</a> is a class designed to generate images in batches, where each batch can have its own unique settings such as font, noise, background color, and margins. It inherits from the <a href='../../reference/generators/generator/' style="text-decoration: underline;">`Generator`</a> class and provides functionality to create and iterate over different batches of images.


#### **How to use `BatchesImagesGenerator`**
```py
from iftg.generators import ImagesGenerator
from iftg.noises import (BlurNoise, BrightnessNoise, DilateNoise)

texts = ['Hello, World!']

results = ImagesGenerator(texts=texts,  # A list of texts to be used for image creation.
                          font_path= "path/to/the/font",    # The file path to the font used in the images.
                          noises=[BlurNoise(),  # A list of noise objects to be applied to the images.
                                  BrightnessNoise(),
                                  DilateNoise()
                                 ],    
                          font_size= 40,    # The size of the font used in the images.
                          font_color= 'black',  # The color of the text in the images.
                          background_color= 'white',    # The background color of the images.
                          margins= (5, 5, 5, 5),    # Margins for text placement on the images.
                          dpi= (300, 300),  # The DPI (dots per inch) settings for the images.
                          img_name='img',   # The base name for the output image files.
                          img_format='.tif',    # The file format for the output images.
                          img_output_path='output', # The directory where the generated images will be saved.
                          txt_name='text',  # The base name for the output text files containing the image labels.
                          txt_format='.txt',    # The file format for the output text files.
                          txt_output_path='output', # The directory where the generated text files will be saved.
                          auto_remove_font=True,    # A flag indicating whether to automatically remove the font from the cache after image generation.
                          background_image_path='', # The file path to the background image, if any.
                         )

# Generate and save the images without labels
results.generate_images()

# OR

# Generate and save images with labels
results.generate_images_with_text()

# OR

# You can use for-loop to further modify your images or do something else
for img, lbl, i in results:
    img.save(f'img_{i}.tif', **img.info)
from iftg.generators import BatchesImagesGenerator
from iftg.noises import (ElasticNoise, ErodeNoise, FlipNoise)

# Define the texts for each batch
texts = [['Hello, World!'], ['Hello, World!']]

# Initialize the BatchesImagesGenerator with the specified parameters
results = BatchesImagesGenerator(texts=texts,   # A list of lists of texts, where each inner list contains texts for one batch of images.
                                 font_paths=["path/to/the/font"],   # A list of font file paths, where each font corresponds to a batch of images.
                                 noises=[   # A list of lists of noise objects, where each inner list contains noises to be applied to one batch of images.
                                        [ElasticNoise(), FlipNoise()],
                                        [ErodeNoise(), FlipNoise]
                                        ],
                                 font_sizes=[40],   # A list of font sizes, where each size corresponds to a batch of images.
                                 font_colors=['black'], # A list of font colors, where each color corresponds to a batch of images.
                                 background_colors=['white'],   # A list of background colors, where each color corresponds to a batch of images.
                                 margins=[(5, 5, 5, 5)],    # A list of margin tuples (left, top, right, bottom) for text placement, where each margin corresponds to a batch of images.
                                 dpi=[(300, 300)],  # A list of DPI (dots per inch) settings, where each DPI value corresponds to a batch of images.
                                 img_names=['img'], # A list of base names for the output image files, where each name corresponds to a batch of images.
                                 img_formats=['.tif'],  # A list of file formats for the output images, where each format corresponds to a batch of images.
                                 img_output_paths=[''], # A list of directories where the generated images will be saved, where each directory corresponds to a batch of images.
                                 txt_names=['text'],    # A list of base names for the output text files containing image labels, where each name corresponds to a batch of images.
                                 txt_formats=['.txt'],  # A list of file formats for the output text files, where each format corresponds to a batch of images.
                                 txt_output_paths=[''], # A list of directories where the generated text files will be saved, where each directory corresponds to a batch of images.
                                 background_image_paths=['']    # A list of file paths to the background image, if any.
                                )

# Generate and save the images without labels
results.generate_batches(is_with_label=True) # Set to False to generate images without labels
```

