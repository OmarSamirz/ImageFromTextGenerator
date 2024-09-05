<div align="center">
  <img src="https://drive.google.com/uc?export=view&id=1ixdcGw8OQYGCCuwaMw3A0tJWgPhdqRRf" alt="Logo" width="60%">
  <h1>ImageFromTextGenerator</h1>
</div>

![PyPI - Version](https://img.shields.io/pypi/v/iftg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/iftg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/iftg)
![GitHub Release Date](https://img.shields.io/github/release-date/OmarSamirz/ImageFromTextGenerator)
![GitHub License](https://img.shields.io/github/license/OmarSamirz/ImageFromTextGenerator?logoColor=%230d7fc0)


IFTG is a powerful Python package designed to create high-quality datasets for Optical Character Recognition (OCR) models. By generating synthetic text images with various noise and augmentation techniques, IFTG enables researchers and developers to build robust and accurate OCR systems.

## Table of Contents

1. [Why IFTG](#why-iftg)
2. [Noises](#noises)
3. [Installation](#installation)
4. [Quick Start](#quick-start)
5. [Usage](#usage)
     - [Creators](#creators)
         - [ImageCreator](#imagecreator)
     - [Generators](#generators)
         - [ImagesGenerator](#imagesgenerator)
         - [BatchesImagesGenerator](#batchesimagesgenerator)
     - [Adders](#adders)
         - [DirectoryNoiseAdder](#directorynoiseadder)
6. [Planned Features](#planned-features)
        


## Why IFTG
IFTG is designed to simplify and accelerate the process of creating large and diverse OCR datasets. Here's why you should choose IFTG for your OCR model development:

- **Efficient Dataset Generation:** Create large-scale synthetic datasets for OCR models with minimal effort.
  
- **Rich Noise Library:** Access over 10 different noise types to simulate diverse real-world conditions.
  
- **Endless Noise Combinations:** Combine multiple noise types to generate highly varied datasets.
  
- **Custom Noise Integration:** Easily add custom noise types using the provided noise template, allowing for customized dataset creation.
  
- **Advanced Image Augmentation:** Apply augmentations such as rotations, blurring, distortions, and more to both newly generated and existing datasets.
  
- **Flexible Text and Font Options:** Generate images with customizable fonts, colors, sizes, and backgrounds.
  
- **Support for All Languages:** Generate text images in any language, as long as the correct font is provided.
  
- **Automated Dataset Creation:** Automate the process of generating and saving large datasets.
  
- **Distinctive Image Naming:** Automatically rename images with distinctive names to differentiate between original and augmented versions.
  
- **User-Friendly API:** Simple and intuitive API design for easy integration into your projects.

## Noises
IFTG offers a wide variety of noise effects that you can apply to your images to create robust and diverse datasets for OCR models. With more than 10 noise types available, you have the flexibility to use static noises or introduce randomness in your noise application.

- **Static Noises:** These noises apply consistent effects, making them useful when you want repeatable results across your dataset.
  
- **Random Noises:** These noises introduce variability, allowing you to generate different effects with each image, enhancing the robustness of your models.
  
- **Custom Noises:** IFTG provides a [noise template](noise_template.py) that allows you to easily create your own custom noise effects. This feature gives you even more control over the image augmentation process, enabling you to tailor the noises to your specific needs.

<table>
  <tr>
    <th>Background</th>
    <th>Blur</th>
    <th>Brightness</th>
    <th>Dilate</th>
  </tr>
  <tr>
    <td><img src="https://drive.google.com/uc?export=view&id=1x21Ae-alAtpF3yXrODnoy3gH3eA3Z6ih" alt="Background" width="100%"></td>
    <td><img src="https://drive.google.com/uc?export=view&id=1D2CWjze5DxnFwGBhOAyPlUtaHoDCHLS_" alt="Blur" width="100%"></td>
    <td><img src="https://drive.google.com/uc?export=view&id=1LnS61a0H2cTf8l5rZnVnUP-p1Fo87Kx5" alt="Brightness" width="100%"></td>
    <td><img src="https://drive.google.com/uc?export=view&id=1d5fQkxVOfWYrlK3A-_OR3QkLttyh6Kxb" alt="Dilate" width="100%"></td>
  </tr>
</table>

<table>
  <tr>
    <th>Elastic</th>
    <th>Erode</th>
    <th>Flip</th>
    <th>Gaussian</th>
  </tr>
  <tr>
    <td><img src="https://drive.google.com/uc?export=view&id=1JDQDsKQGKAu83tciNo_NvPS0b4NuwzF4" alt="Elastic" width="100%"></td>
    <td><img src="https://drive.google.com/uc?export=view&id=1jQ59Caw4Kd0dKM56mgtZoFNU1gH3lJdL" alt="Erode" width="100%"></td>
    <td><img src="https://drive.google.com/uc?export=view&id=11gwDnDNlr5XNLKmVgFOS_k-aSXDr4F8c" alt="Flip" width="100%"></td>
    <td><img src="https://drive.google.com/uc?export=view&id=1wEd0GmxKnAEGZ1tN9d3QHQl0EnlsieC_" alt="Gaussian" width="100%"></td>
  </tr>
</table>

<table>
  <tr>
    <th>Pixel Dropout</th>
    <th>Rotation</th>
    <th>Shadow</th>
  </tr>
  <tr>
    <td><img src="https://drive.google.com/uc?export=view&id=1-tK015rD9_qwkwagz6mq7_i9b-Ot3zAT" alt="Pixel Dropout" width="100%"></td>
    <td><img src="https://drive.google.com/uc?export=view&id=1P8x0rhe-y5PKbKwMwVEBLiSzI6kN7hSi" alt="Rotatoin" width="100%"></td>
    <td><img src="https://drive.google.com/uc?export=view&id=1I5vlwsYaG2eC4yGowuYMVOfWo1KbAFYM" alt="Shadow" width="100%"></td>
  </tr>
</table>

## Installation
To get started with IFTG, you'll need to install the package. You can do this using pip.
```bash
pip install iftg
```

## Quick Start
To get started with IFTG, follow these simple steps:
- **Import the Required Classes:** First, import the necessary classes from the IFTG package
    ```python
    from iftg.generators import ImagesGenerator
    from iftg.noises import RandomBlurNoise, RandomBrightnessNoise
    ```
- **generate Images:** Use the ImagesGenerator class to generate images with the desired text, font and apply noise
    ```python
    text = ['Hello, World!']
        
    results = ImagesGenerator(text=text,
                              font_path='path/to/the/font',
                              noises=[RandomBlurNoise(), RandomBrightnessNoise()],                                    
                             )
    ```
- **Save Images:** Finally, save the generated image to a file
    ```python
    results.generate_images_with_text()
    ```

## Usage
### Creators
- **ImageCreator:** The ImageCreator class is used to generate images with specified text and optional customization. It can be used to create images for testing or as inputs for other generator classes.

    Example Usage:
    ```python
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

### Generators
- **ImageGenerator:** ImagesGenerator class is designed to create images based on provided text and optional noise effects. It supports both generating images alone and with associated labels.

    Example Usage:
    ```python
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
    for i, (img, lbl) in enumerate(results):
        img.save(f'img_{i}.tif', **img.info)
    
    ```


- **BatchesImagesGenerator:** BatchesImagesGenerator class is designed to simplify the creation of multiple batches of images with minimal code. This class is particularly useful when you need to generate images in bulk, with different configurations for each batch.

    Example Usage:
    ```python
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


### Adders
- **DirectoryNoiseAdder:** DirectoryNoiseAdder class is designed to add noises to images in a specific directory.

    Example Usage:
    ```python
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


## Planned Features
- **Support for Multiprocessing:** Enhance performance by adding multiprocessing capabilities to speed up the image generation and noise application processes.

- **Addition of More Noise Effects:** Expand the library of noise effects to provide even more options for dataset augmentation.

- **Support for Multiline Text:** Enable the creation of images with multiline text, allowing for more complex and varied text-based datasets.
