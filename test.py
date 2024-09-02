import numpy as np
from PIL import Image

def add_noise_effect(image_path, noise_intensity=0.2):
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to a numpy array
    img_array = np.array(img)
    
    # Create a noise array with the same shape as the image
    noise = np.random.normal(0, noise_intensity, img_array.shape)
    
    # Add the noise to the image array
    noisy_img_array = img_array + noise * 255
    
    # Clip the values to be between 0 and 255
    noisy_img_array = np.clip(noisy_img_array, 0, 255).astype(np.uint8)
    
    # Create a new image from the noisy array
    noisy_img = Image.fromarray(noisy_img_array)
    
    return noisy_img

# Example usage:
noisy_image = add_noise_effect('img.png', noise_intensity=0.2)
noisy_image.save('noisy_checkerboard.png')