from PIL import Image, ImageDraw
import numpy as np
import random

def add_simple_random_shadow(image_path, output_path, num_points=10, shadow_intensity=0.5):
    # Open the image and get its properties
    with Image.open(image_path) as img:
        original_format = img.format
        
        width, height = img.size
        
        # Create a mask for the shadow
        mask = Image.new('L', (width, height), 0)
        
        # Generate random points for the polygon
        points = [(random.randint(0, width-1), random.randint(0, height-1)) for _ in range(num_points)]
        
        # Draw the polygon on the mask
        ImageDraw.Draw(mask).polygon(points, fill=255)
        
        # Convert images to numpy arrays
        img_array = np.array(img)
        mask_array = np.array(mask)
        
        # Apply the shadow
        shadow = img_array * (1 - (mask_array[:,:,np.newaxis] / 255.0) * shadow_intensity)
        
        # Ensure the array is in the correct data type
        shadow = np.clip(shadow, 0, 255).astype(img_array.dtype)
        
        # Create the final image
        result = Image.fromarray(shadow, 'RGB')
        
        # Ensure the output image has the same format as the input
        result.format = original_format
        
        # Save the result, preserving format and metadata
        result.save(output_path, format=original_format)

# Example usage
add_simple_random_shadow("img.png", "output_with_shadow.png")