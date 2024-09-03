from PIL import ImageFont, Image
from multiprocessing import Pool, cpu_count
from concurrent.futures import ThreadPoolExecutor

import time

from iftg.adder import DirectoryNoiseAdder
from iftg.creators import ImageCreator
from iftg.generators import ImagesGenerator, BatchesImagesGenerator
from iftg.noises import (
    BlurNoise, BrightnessNoise, DilateNoise, ElasticNoise, ErodeNoise,
    FlipNoise, GaussianNoise, PixelDropoutNoise, RotationNoise, ShadowNoise
)


def main1():
    
    texts = ["我是奥马尔"]
    texts = ['नमस्ते, मैं उमर हूं']
    text = 'Hi I am Omar Samir Ibrahim'
    texts = ['こんにちは、オマールです']
    texts = ['أنا عمر سمير', 'قُلْ يَا أَيُّهَا الْكَافِرُونَ', 'ثُمَّ لَتَرَوُنَّهَا عَيْنَ الْيَقِينِ']
    texts = ['Hello, I am Omar', 'Omar', 'Samir', 'Ibrahim', 'Desoky', 'Ahmed', 'Oraby', 'Oraby']
    texts = ['Hello World!']*100
    start = time.time()

    

    # with Pool(cpu_count()) as pool:
    #     # Map the save_image function to the results
    #     pool.map(save_image, [(i, img) for i, (img, lbl) in enumerate(results)])

    # for i, (img, lbl) in enumerate(results):
    #     print(i)
    #     img.save(f'output_images/img_{i}.png')
    end = time.time()
    # print(f"Time: {end-start} sec")
    
    # print("\nUsing normal for loop\n")
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
    noise_adder = DirectoryNoiseAdder(dir_path='img_text_test', 
                                      output_path='img_text_test_2',
                                      noises=[BrightnessNoise(), ErodeNoise()]
                                     )
    noise_adder.transform_images()
    end = time.time()
    print(f'Taken time: {end-start} ms')


def main3():
    texts_lst = [['Hello, World!']]*10
    results = BatchesImagesGenerator(texts_lst, 
                                     img_output_paths=['noisy_images'], 
                                     img_formats=['.tif'],
                                     noises=[[BlurNoise()], [BrightnessNoise()], [DilateNoise()], 
                                             [ElasticNoise()], [ErodeNoise()], [FlipNoise()],
                                             [GaussianNoise()], [PixelDropoutNoise()], [RotationNoise(20)], [ShadowNoise()]])
    results.generate_batches(False)
    img = ImageCreator.create_image('Hello, World!', background_img=Image.open('water.png'))
    img.save('noisy_images/img_with_background.png')


if __name__ == '__main__':
    main3()
    # img = Image.open('img_text_test/img_0.tif')
    # print(img.info['dpi'])
    # text = """I am Omar\nI live in cairo"""
    # print(text.splitlines())

    
    
