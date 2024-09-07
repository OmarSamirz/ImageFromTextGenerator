# **<a href='#shadownoise-module' style="text-decoration: underline;">`ShadowNoise`</a> Module**

!!! Note 
    - **Inheritance Structure:** 
        - <a href='../noise/#noise-module' style="text-decoration: underline;">`Noise`</a> (Abstract Base Class) 
        - <a href='#shadownoise-module' style="text-decoration: underline;">`ShadowNoise`</a> (Concrete Implementation) 

The <a href='#shadownoise-module' style="text-decoration: underline;">`ShadowNoise`</a> class adds shadow noise to an image by generating a polygonal mask based on random points. The shadow intensity is adjustable, simulating shadow effects on the image.

## **Attributes**
- **num_points : `int`**

    The number of points used to create the polygon for the shadow mask. Must be at `least 2` points to form a polygon.

- **shadow_intensity : `float`**

    The intensity of the shadow applied to the image, ranging from `0` (no shadow) to `1` (maximum shadow).

## **Methods**
### **`add_noise()`**
```py
add_noise(self, image: Image) -> Image:
```
Public method that applies `shadow` noise to the image.

- **Parameters:**

    - **image : `Image`**

        The input image to which the shadow noise will be applied.

- **Returns:**

    - `Image`:

        The image with the shadow noise applied.

### **`_shadow_noise()`**
```py
_shadow_noise(self, image: Image) -> Image:
```
Internal method that generates a `shadow` mask using a polygon of random points and applies the shadow to the image.

- **Parameters:**

    - **image : `Image`**

        The image to which shadow noise will be applied.

- **Returns:**

    - `Image`:

        The image with the shadow applied using the generated mask.

## **Usage Example**
```py
from PIL import Image
from iftg.noises import ShadowNoise

# Open an image
image = Image.open('path/to/image.tif')

# Create a ShadowNoise object with 6 points for the polygon and 0.4 shadow intensity
shadow_noise = ShadowNoise(num_points=6, shadow_intensity=0.4)

# Apply shadow noise to the image
shadowed_image = shadow_noise.add_noise(image)

# Save the shadowed image
shadowed_image.save('path/to/shadowed_image.tif')
```
