from PIL import ImageFont


def get_text_dimensions(text: str, font: ImageFont, is_multiline: bool) -> tuple[float, float, float, float]:

    lines = text.splitlines() 
    left, right, max_width, max_height = 0, 0, 0, 0
    _, top, _, _ = font.getbbox(lines[0])

    for line in lines:
        line_left, _, line_right, line_bottom = font.getbbox(line)
        
        max_width = max(max_width, line_right - line_left)
        max_height += line_bottom if is_multiline else line_bottom - top

        right = max_width

    return left, top, right, max_height


def get_image_dimensions(right: int, 
                         top: int,
                         bottom: int, 
                         margins: tuple[int, int, int, int]
                        ) -> tuple[int, int]:
    
    left_margin, top_margin, right_margin, bottom_margin = margins

    image_width = right + left_margin + right_margin
    image_height = bottom - top + top_margin + bottom_margin

    return image_width, image_height
    