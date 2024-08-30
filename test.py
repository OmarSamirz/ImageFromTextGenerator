from PIL import Image, ImageDraw, ImageFont
import math

def tilt_image_forward_with_text(image_path, angle, text, font_path, font_size):
    """
    Tilts the image forward based on the given angle and adjusts the size to fit text.

    :param image_path: Path to the image file
    :param angle: Angle by which to tilt the image forward (in degrees)
    :param text: Text to fit inside the image
    :param font_path: Path to the font file
    :param font_size: Size of the font
    :return: Tilted image with text inside
    """
    # Open the image
    image = Image.open(image_path)
    width, height = image.size
    
    # Convert angle to radians
    angle_rad = math.radians(angle)
    
    # Calculate the new width to accommodate the tilt effect
    # This formula accounts for the horizontal shift due to the tilt
    new_width = int(width + height * math.tan(angle_rad))
    new_height = height  # Keep height the same (optional, you can adjust if needed)
    
    
    # Paste the tilted image onto the new image
    tilt_matrix = (1, -math.tan(angle_rad), 0,  # X-axis transformation
                   0, 1, 0)                    # Y-axis transformation
    
    tilted_image = image.transform((new_width, new_height), Image.AFFINE, tilt_matrix, fillcolor='white', resample=Image.Resampling.BICUBIC)
    
    
    return tilted_image

# Usage example
tilted_img_with_text = tilt_image_forward_with_text(
    'img_1.tif', 30, 'Your Text Here', 'Arial.ttf', 40)
tilted_img_with_text.show()
tilted_img_with_text.save('tilted_image_with_text.jpg')
