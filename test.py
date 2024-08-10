from PIL import Image, ImageDraw, ImageFont
import math

def create_image_with_rotated_text(text, font_path, font_size, rotation_angle):
    # Load the font
    font = ImageFont.truetype(font_path, font_size)
    
    # Get the size of the text
    left, top, right, bottom = font.getbbox(text)
    text_width = right - left
    text_height = bottom - top

    # Calculate the size of the rotated text
    angle_rad = math.radians(rotation_angle)
    rotated_width = int(abs(text_width * math.cos(angle_rad)) + abs(text_height * math.sin(angle_rad)))
    rotated_height = int(abs(text_width * math.sin(angle_rad)) + abs(text_height * math.cos(angle_rad)))
    
    # Create a new image with a size that accommodates the rotated text
    image_size = (rotated_width + 40, rotated_height + 40)  # Add padding
    image = Image.new('RGB', image_size, color='white')
    
    # Create a draw object
    draw = ImageDraw.Draw(image)
    image.transform(Image.Transform.AFFINE)
    
    
    # Calculate the position to center the text
    x = (image_size[0] - text_width) / 2
    y = (image_size[1] - text_height) / 2
    
    # Rotate the image
    rotated_image = image.rotate(rotation_angle, expand=1, center=(image_size[0]/2, image_size[1]/2))
    rotated_draw = ImageDraw.Draw(rotated_image)
    
    # Draw the rotated text
    rotated_draw.text((x, y), text, font=font, fill='black')
    
    # Save the image
    rotated_image.show()

# Example usage
create_image_with_rotated_text(
    text="Hello, Rotated World!",
    font_path="arial.ttf",  # Replace with the path to your desired font
    font_size=40,
    rotation_angle=30,
)