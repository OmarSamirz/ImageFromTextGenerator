# **<a href='#noise-module' style="text-decoration: underline;">`Noise`</a> Module**
!!! Warning
    This module is considered internal.


<a href='#noise-module' style="text-decoration: underline;">`Noise`</a> is an abstract base class that defines a common interface for applying noise to images. Classes that inherit from <a href='#noise-module' style="text-decoration: underline;">`Noise`</a> must implement the <a href='#add_noise' style="text-decoration: underline;">`add_noise`</a> method, which applies a specific type of noise effect to an image.

## **Methods**

### **`add_noise()`**
```py
add_noise(self, image: Image) -> Image:
```
This method applies a specific type of noises to an image and returns the resulting image. Each subclass of <a href='#noise-module' style="text-decoration: underline;">`Noise`</a> must implement this method to define its own noise effects.

- **Parameters:**
    - **image : `Image`**
        
        An instance of PIL.Image representing the image to which noise will be applied.

- **Returns:**
    - `Image`: 
        
        A PIL.Image object representing the image after the noise has been applied.