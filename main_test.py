from PIL import ImageFont, Image
from multiprocessing import Pool, cpu_count
from concurrent.futures import ThreadPoolExecutor

import os
import time

from iftg.adders import ImageNoiseAdder, DirectoryNoiseAdder
from iftg.creators import ImageCreator
from iftg.generators import ImagesGenerator, BatchesImagesGenerator
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
    texts_lst = [['Hello, World!', 'I am'], ['Omar Samir', 'Ahmed']]
    print(texts_lst)
    results = BatchesImagesGenerator(texts_lst, 
                                     font_paths=['./fonts/Arial.ttf'],
                                     img_output_paths=['noisy_images'])
    results.generate_batches(False)


def main4():
    start = time.time()

    texts = ['Hello, World!']
    results = ImagesGenerator(texts=texts, font_path='fonts/Arial.ttf')
    results.generate_images_with_text()

    end = time.time()
    print(f'{end-start} ms')


def main5():
    img_noise_adder = ImageNoiseAdder(img_path='output/img_0.tif', noises=[GaussianNoise()])
    img_noise_adder.transform_image()


if __name__ == '__main__':
    main2()