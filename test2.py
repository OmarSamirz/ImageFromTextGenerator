from PIL import Image, ImageDraw, ImageFont

def create_image_with_text(text, font_path, margins, font_size, bg_color, text_color):
    # Margins
    top_margin, left_margin, right_margin, bottom_margin = margins
    
    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Calculate text size
    left, top, right, bottom = font.getbbox(text) # ((left, top, right, bottom))
    print(f"left: {left}, top: {top}, right: {right}, bottom: {bottom}")

    # Calculate the image size with margins
    image_width = right + left_margin + right_margin
    image_height = bottom + top_margin + bottom_margin

    # Create the image
    image = Image.new('RGB', (image_width, image_height+top), color=bg_color)
    draw = ImageDraw.Draw(image)


    # Draw the text onto the image
    draw.text((0+left_margin, 0+top_margin), text, font=font, fill=text_color)

    return image

# Example usage
text = """Hello World! I am Omar H"""
font_path = "arial.ttf"  # Provide the path to a .ttf font file
margins = (0, 0, 0, 0)  # Margins as (top, left, right, bottom)
font_size = 50  # Font size
bg_color = "white"  # Background color
text_color = "#234234"  # Text color

image = create_image_with_text(text, font_path, margins, font_size, bg_color, text_color)
image.show()  # Display the image
