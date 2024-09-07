# **<a href='#gaussiannoise-module' style="text-decoration: underline;">`GaussianNoise`</a> & <a href='#randomgaussiannoise-module' style="text-decoration: underline;">`RandomGaussianNoise`</a> Modules**

!!! Note 
    - **Inheritance Structure:**
        - <a href='../noise/#noise-module' style="text-decoration: underline;">Noise</a> (Abstract Base Class) 
        - <a href='#gaussiannoise-module' style="text-decoration: underline;">GaussianNoise</a> (Concrete Implementation) 
        - <a href='#randomgaussiannoise-module' style="text-decoration: underline;">RandomGaussianNoise</a> (Extends GaussianNoise with randomness)

## **GaussianNoise Module**
The <a href='#gaussiannoise-module' style="text-decoration: underline;">`GaussianNoise`</a> class applies Gaussian noise to an image by adding random noise sampled from a normal distribution.

### **Attributes**
- **mean : `float`**

    The mean of the Gaussian distribution used to generate noise. This determines the average intensity of the noise.

- **sigma : `float`**

    The standard deviation of the Gaussian distribution. A larger sigma value results in higher noise variation.

### Methods
#### **`add_noise()`**
```py
add_noise(self, image: Image) -> Image:
```
Public method that applies `Gaussian` noise to the input image by adding random noise based on the specified mean and sigma.

- **Parameters:**

    - **image : `Image`**

        The input image to which Gaussian noise will be added.

- **Returns:**

    - `Image`:

        The image with Gaussian noise applied.

#### **`_gaussian_noise()`**
```py
_gaussian_noise(self, image: Image) -> Image:
```
Internal method that generates `Gaussian` noise based on the specified mean and sigma and adds it to the image.

- **Parameters:**

    - **image : `Image`**

        The image to which the Gaussian noise will be applied.

- **Returns:**

    - `Image`:

        The noisy image with Gaussian noise applied.

### Usage Example
```py
from PIL import Image
from iftg.noises import GaussianNoise

# Open an image
image = Image.open('path/to/image.tif')

# Create a GaussianNoise object with mean 0 and sigma 50
gaussian_noise = GaussianNoise(mean=0, sigma=50)

# Apply Gaussian noise to the image
noisy_image = gaussian_noise.add_noise(image)

# Save the noisy image
noisy_image.save('path/to/noisy_image.tif')
```

<br>

## **RandomGaussianNoise Module**
The <a href='#randomgaussiannoise-module' style="text-decoration: underline;">`RandomGaussianNoise`</a> class extends the functionality of <a href='#gaussiannoise-module' style="text-decoration: underline;">`GaussianNoise`</a> by allowing random selection of the mean and sigma values from specified ranges, resulting in varied noise application for each image.

### **Attributes**
- **mean_range : `tuple[float, float]`**

    The range for random selection of the mean of the Gaussian noise distribution. The mean controls the average intensity of the noise.

- **sigma_range : `tuple[float, float]`**

    The range for random selection of the standard deviation `sigma` of the Gaussian noise distribution. A larger sigma range will lead to noisier images.

### **Methods**
#### **`add_noise()`**
!!! Note 
    Each call to `add_noise()` results in a different noise pattern by selecting a random mean and sigma from the provided ranges, making it useful for introducing variability in image augmentation.

```py
add_noise(self, image: Image) -> Image:
```
Public method that applies random `Gaussian` noise to the input image by selecting random values for the mean and sigma within the specified ranges.

- **Parameters:**

    - **image : `Image`**

        The input image to which random Gaussian noise will be added.

- **Returns:**

    - `Image`:

        The image with random Gaussian noise applied.

### **Usage Example**

```py
from PIL import Image
from iftg.noises import RandomGaussianNoise

# Open an image
image = Image.open('path/to/image.tif')

# Create a RandomGaussianNoise object with mean range (0, 1) and sigma range (30, 60)
random_gaussian_noise = RandomGaussianNoise(mean_range=(0, 1), sigma_range=(30, 60))

# Apply random Gaussian noise to the image
random_noisy_image = random_gaussian_noise.add_noise(image)

# Save the randomly noisy image
random_noisy_image.save('path/to/random_noisy_image.tif')

```
