

from iftg.noises.noise import Noise
from iftg.generators import ImagesGenerator
from iftg.generators.generator import Generator
from iftg.image_font_manager import ImageFontManager


class BatchesImagesGenerator(Generator):
    """
    A generator class for creating batches of images, where each batch can have different text, noise, and style settings.
    Inherits from `Generator` and provides functionality to generate images in batches.

    Attributes:
        texts (list[list[str]]): 
            A list of lists of texts, where each inner list contains texts for one batch of images.
        noises (list[list[Noise]]): 
            A list of lists of noise objects, where each inner list contains noises to be applied to one batch of images.
        font_paths (list[str]): 
            A list of font file paths, where each font corresponds to a batch of images.
        font_sizes (list[float]): 
            A list of font sizes, where each size corresponds to a batch of images.
        font_colors (list[str]): 
            A list of font colors, where each color corresponds to a batch of images.
        background_colors (list[str]): 
            A list of background colors, where each color corresponds to a batch of images.
        margins (list[tuple[int, int, int, int]]): 
            A list of margin tuples (left, top, right, bottom) for text placement, where each margin corresponds to a batch of images.
        dpi (list[tuple[float, float]]): 
            A list of DPI (dots per inch) settings, where each DPI value corresponds to a batch of images.
        img_names (list[str]): 
            A list of base names for the output image files, where each name corresponds to a batch of images.
        img_formats (list[str]): 
            A list of file formats for the output images, where each format corresponds to a batch of images.
        img_output_paths (list[str]): 
            A list of directories where the generated images will be saved, where each directory corresponds to a batch of images.
        txt_names (list[str]): 
            A list of base names for the output text files containing image labels, where each name corresponds to a batch of images.
        txt_formats (list[str]): 
            A list of file formats for the output text files, where each format corresponds to a batch of images.
        txt_output_paths (list[str]): 
            A list of directories where the generated text files will be saved, where each directory corresponds to a batch of images.
        background_image_paths (list[str]):
            A list of file paths to the background image, if any.
    """

    
    def __init__(self, 
                 texts: list[list[str]],
                 font_paths: list[str],
                 noises: list[list[Noise]] = [],
                 font_sizes: list[float] = [40.0],
                 font_colors: list[str] = ['black'],
                 background_colors: list[str] = ['white'],
                 margins: list[tuple[int, int, int, int]] = [(5, 5, 5, 5)],
                 dpi: list[tuple[float, float]] = [(300, 300)],
                 img_names: list[str] = ['img'],
                 img_formats: list[str] = ['.tif'],
                 img_output_paths: list[str] = [''],
                 txt_names: list[str] = ['text'],
                 txt_formats: list[str] = ['.txt'],
                 txt_output_paths: list[str] = [''],
                 background_image_paths: list[str] = ['']
                ):
        

        def extend_list(lst, default_value):
            return lst + [default_value] * (max_len - len(lst))
        
        # Check if all input lists have the same length
        list_lengths = [len(texts), len(noises), len(font_paths), len(font_sizes),
                        len(font_colors), len(background_colors), len(margins),
                        len(dpi), len(img_names), len(img_formats),
                        len(img_output_paths), len(txt_names), len(txt_formats),
                        len(txt_output_paths), len(background_image_paths)]
        
        if len(set(list_lengths)) != 1:
            max_len = max(list_lengths)

            texts = extend_list(texts, [])
            noises = extend_list(noises, [])
            font_paths = extend_list(font_paths, font_paths[-1])
            font_sizes = extend_list(font_sizes, font_sizes[-1])
            font_colors = extend_list(font_colors, font_colors[-1])
            background_colors = extend_list(background_colors, background_colors[-1])
            margins = extend_list(margins, margins[-1])
            dpi = extend_list(dpi, dpi[-1])
            img_names = extend_list(img_names, img_names[-1])
            img_formats = extend_list(img_formats, img_formats[-1])
            img_output_paths = extend_list(img_output_paths, img_output_paths[-1])
            txt_names = extend_list(txt_names, txt_names[-1])
            txt_formats = extend_list(txt_formats, txt_formats[-1])
            txt_output_paths = extend_list(txt_output_paths, txt_output_paths[-1])
            background_image_paths = extend_list(background_image_paths, background_image_paths[-1])

        super().__init__(texts, 
                         font_paths,
                         noises, 
                         font_sizes,
                         font_colors,
                         background_colors,
                         margins,
                         dpi,
                         img_names,
                         img_formats,
                         img_output_paths,
                         txt_names,
                         txt_formats,
                         txt_output_paths,
                         background_image_paths
                        )            
    

    def _generate_next(self):
        """
        Generates the next batch of images using the specified settings for that batch.

        Returns:
            ImagesGenerator: 
                A generator object that generates images for the current batch.

        Raises:
            StopIteration:
            When all batches have been generated and the font cache for the last batch is cleared.
        """
        if self._count >= self._texts_len:
            ImageFontManager.remove_font(self.font_path[self._count-1], self.font_size[self._count-1])
            raise StopIteration
        
        generator =  ImagesGenerator(self.texts[self._count], 
                                     self.font_path[self._count],
                                     self.noises[self._count],
                                     self.font_size[self._count],
                                     self.font_color[self._count],
                                     self.background_color[self._count],
                                     self.margins[self._count],
                                     self.dpi[self._count],
                                     self.img_name[self._count] + f'_{self._count}',
                                     self.img_format[self._count],
                                     self.img_output_path[self._count],
                                     self.txt_name[self._count] + f'_{self._count}',
                                     self.txt_format[self._count],
                                     self.txt_output_path[self._count],
                                     auto_remove_font=False,
                                    )
        
        self._count += 1
        return generator

    
    def generate_batches(self, is_with_label: bool = True) -> None:
        """
        Generates and saves images for each batch.

        Parameters:
            is_with_label (bool): 
                If True, generates images with corresponding text labels and saves them. 
                If False, generates images without saving labels.
        """
        for generator in self:
            if is_with_label == True:
                generator.generate_images_with_text()
            else:
                generator.generate_images()