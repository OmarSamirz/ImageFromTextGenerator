# **Tutorial: To be continued**

## **Adders**


### **<a href='../../reference/adders/image_noise_adder' style="text-decoration: underline;">`ImageNoiseAdder`</a> Module**
<a href='../../reference/adders/image_noise_adder' style="text-decoration: underline;">`ImageNoiseAdder`</a> is a class used to apply various noise effects to an image and save the resulting noisy image to a specified directory. It extends the <a href='../../reference/adders/noise_adder', style="text-decoration: underline;">`NoiseAdder`</a> class, leveraging its functionality.

#### **How to use `ImageNoiseAdder`**
```py
from iftg.adders import ImageNoiseAdder
from iftg.noises import BlurNoise, BrightnessNoise

noise_adder = ImageNoiseAdder(img_path='path/to/image.tif',
                              output_path='',
                              noises=[BlurNoise(), BrightnessNoise()],
                              identifier: str = 'noisy',
                             )

noise_adder.transform_image()
```

### **<a href='../../reference/adders/directory_noise_adder' style="text-decoration: underline;">`DirectoryNoiseAdder`</a> Module**
The <a href='../../reference/adders/directory_noise_adder' style="text-decoration: underline;">`DirectoryNoiseAdder`</a> class is an extension of the abstract base class <a href='../../reference/adders/noise_adder', style="text-decoration: underline;">`NoiseAdder`</a>. It provides functionality for applying noise to multiple images located in a directory and saving the resulting noisy images to a specified output path. This class is ideal for batch image processing tasks where noise needs to be added to a collection of images.

#### **How to use `DirectoryNoiseAdder`**
```py

```

<br>
<br>

## **Creators**

### **<a href='../../reference/creators/image_creator' style="text-decoration: underline;">`ImageCreator`</a> Module**
The <a href='../../reference/creators/image_creator' style="text-decoration: underline;">`ImageCreator`</a> class extends the <a href="../../reference/creators/creator" style="text-decoration: underline;">`Creator`</a>
base class to provide functionality for generating images with customizable text, noise, and visual effects. This class is particularly useful for creating synthetic data by augmenting text-based images with noise or other transformations.

#### **How to use `ImageCreator`**
```py

```

<br>
<br>


## **Generators**

### **<a href='../../reference/generators/images_generator' style="text-decoration: underline;">`ImagesGenerator`</a> Module**

The <a href='../../reference/generators/images_generator' style="text-decoration: underline;">`ImagesGenerator`</a> class extends the <a href='../../reference/generators/generator' style="text-decoration: underline;">`Generator`</a> class to create a sequence of images with varying text and noise effects. It handles the generation of images based on the provided configuration and includes functionality to save both images and their corresponding text labels.

#### **How to use `ImagesGenerator`**
```py

```


### **<a href='../../reference/generators/batches_images_generator' style="text-decoration: underline;">`BatchesImagesGenerator`</a> Module**

<a href='../../reference/generators/batches_images_generator' style="text-decoration: underline;">`BatchesImagesGenerator`</a> is a class designed to generate images in batches, where each batch can have its own unique settings such as font, noise, background color, and margins. It inherits from the <a href='../../reference/generators/generator/' style="text-decoration: underline;">`Generator`</a> class and provides functionality to create and iterate over different batches of images.


#### **How to use `BatchesImagesGenerator`**
```py

```

