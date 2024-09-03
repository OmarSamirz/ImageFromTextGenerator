# ImageFromTextGenerator

IFTG (ImageFromTextGenerator) is a Python package designed to create datasets for Optical Character Recognition (OCR) models, by generating synthetic text images with various noise and augmentation techniques.

## Table of Contents
- [IFTG](#imagefromtextgenerator)
    1. [Why IFTG](#why-iftg)
    2. [Noises](#noises)
    3. [Installation](#installation)
    4. [Quick Start](#quick-start)
    5. [Usage](#usage)
         - To be added
    6. [License](#license)
        


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
| Background | Blur | Brightness | Dilate | Elastic |
|------------|------|------------|--------|---------|
| ![Background](./noisy_images/background_img.tif) | ![Blur](./noisy_images/blur_img.tif) | ![Brightness](./noisy_images/brightness_img.tif) | ![Dilate](./noisy_images/dilate_img.tif) | ![Elastic](./noisy_images/elastic_img.tif) |

| Erode | Flip | Gaussian | Pixel Dropout | Rotation | Shadow |
|-------|------|----------|---------------|----------|--------|
| ![Erode](./noisy_images/erode_img.tif) | ![Flip](./noisy_images/flip_img.tif) | ![Gaussian](./noisy_images/gaussian_img.tif) | ![Pixel Dropout](./noisy_images/pixeldropout_img.tif) | ![Rotation](./noisy_images/rotation_img.tif) | ![Shadow](./noisy_images/shadow_img.tif) |


## Installation
To get started with IFTG, you'll need to install the package. You can do this using pip.
```bash
pip install iftg
```

## Quick Start

## Usage

## License