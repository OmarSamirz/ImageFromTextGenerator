import os

from iftg.noises.noise import Noise
from iftg.image_font_manager import ImageFontManager
from iftg.creators.image_creator import ImageCreator
from iftg.generators.generator import Generator, Image


class ImagesGenerator(Generator):
    """
    A generator class for creating a sequence of images with varying text, noise, blur, rotation, and other effects.
    Inherits from `Generator` and provides functionality to iterate over the generated images.

    Attributes:
        texts (list[str]): A list of texts to be used for image creation.
        noises (list[Noise]): A list of noise objects to be applied to the images.
        font_path (str): The file path to the font used in the images.
        font_size (float): The size of the font used in the images.
        font_color (str): The color of the text in the images.
        background_color (str): The background color of the images.
        margins (tuple[int, int, int, int]): Margins for text placement on the images.
        clear_fonts (bool): Whether to clear the font cache after generating images.
    """
    
    
    def __init__(self, 
                 texts: list[str],
                 noises: list[Noise] = [],
                 font_path: str = "iftg/fonts/Arial.ttf",
                 font_size: float = 40.0,
                 font_color: str = 'black',
                 background_color: str = 'white',
                 margins: tuple[int, int, int, int] = (5, 5, 5, 5),
                 img_name: str = 'img',
                 img_format: str = '.tif',
                 img_output_path: str = '',
                 txt_name: str = 'text',
                 txt_format: str = '.txt',
                 txt_output_path: str = '',
                 clear_fonts: bool = False,
                ):
        super().__init__(texts, 
                         noises, 
                         font_path,
                         font_size,
                         font_color,
                         background_color,
                         margins,
                         img_name,
                         img_format,
                         img_output_path,
                         txt_name,
                         txt_format,
                         txt_output_path,
                         clear_fonts
                        )


    def __iter__(self):
        return self


    def __next__(self):
        return self._generate_next_image()

    
    def _generate_next_image(self) -> tuple[Image.Image, str]:
        """
        Generates the next image in the sequence.

        Returns:
            tuple: A tuple containing the generated image and the text used for the image.
        
        Raises:
            StopIteration: When all images have been generated and the font cache is cleared.
        """
        if self._count >= self._texts_len:
            ImageFontManager.remove_font(self.font_path, self.font_size)
            raise StopIteration

        self._count += 1
        return (ImageCreator.create_image(
            self.texts[self._count-1],
            self.noises,
            self.font_path,
            self.font_size,
            self.font_color,
            self.background_color,
            self.margins,
            self.clear_fonts
        ), self.texts[self._count-1])


    def _cehck_inputs(self) -> None:
        if self.img_output_path == '':
            answer = ''
            
            while answer != 'y' and answer != 'n':
                answer = input('Do you want to save the images in current directory? (Y or N): ').lower()
            
            if answer == 'y':
                self.img_output_path = input('Enter directory path: ')
            
            else:
                print('Your images are going to be saved in current directory')
        
        if self.txt_output_path == '':
            answer = ''
            
            while answer != 'y' and answer != 'n':
                answer = input('Do you want to save the text files in current directory? (Y or N): ').lower()
            
            if answer == 'y':
                self.img_output_path = input('Enter directory path: ')
            
            else:
                print('Your text files are going to be saved in current directory')


    def save_images_and_labels(self, img: Image, lbl: str, i: int) -> None:

        img_path = os.path.join(self.img_output_path, self.img_name + f'_{i}' + self.img_format)
        text_path = os.path.join(self.txt_output_path, self.txt_name + f'_{i}' + self.txt_format)

        img.save(img_path)
        
        with open(text_path, 'w') as text_file:
                text_file.write(lbl)


    def generate_images(self) -> bool:
        self._cehck_inputs()

        for i, (img, lbl) in enumerate(self):
            img_path = os.path.join(self.img_output_path, self.img_name + f'_{i}' + self.img_format)
            text_path = os.path.join(self.txt_output_path, self.txt_name + f'_{i}' + self.txt_format)
            
            img.save(img_path)
            with open(text_path, 'w') as text_file:
                text_file.write(lbl)

    
    def generate_images_with_text(self) -> bool:
        return super().generate_images_with_text()
        