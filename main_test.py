from PIL import ImageFont, Image
from multiprocessing import Pool, cpu_count
from concurrent.futures import ThreadPoolExecutor

import os
import time

from iftg.adders import ImageNoiseAdder, DirectoryNoiseAdder
from iftg.creators import ImageCreator
from iftg.generators import ImagesGenerator, BatchesImagesGenerator
from iftg.image_font_manager import ImageFontManager
from iftg.noises import (
    BlurNoise, BrightnessNoise, DilateNoise, ElasticNoise, ErodeNoise,
    FlipNoise, GaussianNoise, PixelDropoutNoise, RotationNoise, ShadowNoise
)


def main0():
    
    image = ImageCreator.create_image('Hello, world', './fonts/Arial.ttf')
    image.save('img.tif', **image.info)


def main1():
    
    texts = ["我是奥马尔"]
    texts = ['नमस्ते, मैं उमर हूं']
    text = 'Hi I am Omar Samir Ibrahim'
    texts = ['こんにちは、オマールです']
    texts = ['أنا عمر سمير', 'قُلْ يَا أَيُّهَا الْكَافِرُونَ', 'ثُمَّ لَتَرَوُنَّهَا عَيْنَ الْيَقِينِ']
    texts = ['Hello, I am Omar', 'Omar', 'Samir', 'Ibrahim', 'Desoky', 'Ahmed', 'Oraby', 'Oraby']
    texts = ['Hello World!']*100
    start = time.time()
    results = ImagesGenerator(texts=texts, font_size=50, noises=[
                                                                PixelDropoutNoise(dropout_prob=0.2, pixel_dimensions=(1, 10)),
                                                                ErodeNoise(),
                                                                 ], 
                              font_path='iftg/fonts/Arial.ttf', img_output_path='./output', 
                              txt_output_path='./output',
                             )
    
    results.generate_images()
    # if results.generate_batches():
        # print('True')
    # for i, (img, _) in enumerate(results):
    #     img.save(f'output_images/img_{i}.tif', **img.info)
    #     # img.show()
    #     # continue
        
    end = time.time()
    print(f"Time: {end-start} sec")
    

def main2():
    start = time.time()
    noise_adder = DirectoryNoiseAdder(dir_path='output', 
                                      output_path='output',
                                      noises=[BrightnessNoise(), ErodeNoise()]
                                     )
    noise_adder.transform_images()
    end = time.time()
    print(f'Taken time: {end-start} ms')


def main3():
    texts_lst = [["Text1", "Text2"], ["Text3", "Text4"]]
    inputs = {
        "texts": texts_lst,
        "font_paths": ["tests/Arial.ttf", "tests/Arial.ttf"],
        "noises": [[BlurNoise()], [BlurNoise()]],
        "font_sizes": [40.0, 45.0],
        "font_colors": ["black", "blue"],
        "background_colors": ["white", "gray"],
        "margins": [(5, 5, 5, 5), (10, 10, 10, 10)],
        "dpi": [(300, 300), (72, 72)],
        "img_names": ["batch1", "batch2"],
        "img_formats": [".png", ".jpeg"],
        "img_output_paths": ["output1", "output2"],
        "txt_names": ["label1", "label2"],
        "txt_formats": [".txt", ".md"],
        "txt_output_paths": ["output1", "output2"],
        "background_image_paths": ["", ""],
    }
    results = BatchesImagesGenerator(**inputs)
    results.generate_batches()


def main4():
    start = time.time()

    texts = ['Hello, World!']
    results = ImagesGenerator(texts=texts, font_path='fonts/Arial.ttf')
    results.generate_images_with_text()

    end = time.time()
    print(f'{end-start} ms')


def main5():
    img_noise_adder = ImageNoiseAdder(img_path='img.png', noises=[GaussianNoise()])
    img_noise_adder.transform_image()


if __name__ == '__main__':
    main3()