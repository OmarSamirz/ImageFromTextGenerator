import numpy as np
from PIL import Image

def add_skew_noise(image_path, output_path, skew_factor=0.5, noise_factor=0.1):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size
    
    # Convert image to numpy array
    img_array = np.array(img)

    # Create meshgrid
    x, y = np.meshgrid(np.arange(width), np.arange(height))

    # Calculate skew
    skew = skew_factor * (y / height - 0.5)
    
    # Apply skew transformation
    x_skewed = x + skew * width
    
    # Ensure x_skewed is within image boundaries
    x_skewed = np.clip(x_skewed, 0, width - 1)

    # Interpolate values
    x0 = np.floor(x_skewed).astype(int)
    x1 = np.ceil(x_skewed).astype(int)
    y0 = y.astype(int)

    # Calculate interpolation weights
    wx = x_skewed - x0
    wx = wx[:,:,np.newaxis]

    # Perform interpolation for each color channel
    skewed_array = (1 - wx) * img_array[y0, x0] + wx * img_array[y0, x1]

    # Add random noise
    noise = np.random.normal(0, noise_factor, skewed_array.shape)
    noisy_image = np.clip(skewed_array + noise * 255, 0, 255).astype(np.uint8)

    # Create and save the final image
    final_image = Image.fromarray(noisy_image)
    final_image.save(output_path)

    return final_image

add_skew_noise('img.png', 'img_1.png', noise_factor=0)