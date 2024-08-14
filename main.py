from PIL import ImageFont, Image
from multiprocessing import Pool, cpu_count
from concurrent.futures import ThreadPoolExecutor

import time

from iftg.creators import ImageCreator
from iftg.generators import ImagesGenerator
from iftg.noises import DilateNoise, RandomDilateNoise
from iftg.noises import GaussianNoise, RandomGaussianNoise, BlurNoise
from iftg.noises import ErodeNoise, RandomRotationNoise
from iftg.noises import ShadowNoise, NoiseAdder

def save_image(args):
    i, img = args
    img.save(f'output_images/img_{i}.png')

def main():
    
    texts = ["我是奥马尔"]
    texts = ['नमस्ते, मैं उमर हूं']
    texts = ['Hello, I am Omar', 'Omar', 'Samir', 'Ibrahim']
    texts = ['Hello World!']
    texts = ['أنا عمر سمير', 'قُلْ يَا أَيُّهَا الْكَافِرُونَ', 'ثُمَّ لَتَرَوُنَّهَا عَيْنَ الْيَقِينِ']

    text = 'Hi I am Omar Samir Ibrahim'
    print("Using multiprocessing")
    start = time.time()

    # results = ImagesGenerator(texts=texts, font_size=0, noises=[], font_path='iftg/fonts/AnekDevanagari-VariableFont_wdth,wght.ttf')

    

    # with Pool(cpu_count()) as pool:
    #     # Map the save_image function to the results
    #     pool.map(save_image, [(i, img) for i, (img, lbl) in enumerate(results)])

    # for i, (img, lbl) in enumerate(results):
    #     print(i)
    #     img.save(f'output_images/img_{i}.png')
    end = time.time()
    print(f"Time: {end-start} sec")
    noise_adder = NoiseAdder()
    m = noise_adder.add_noise()
    print(m)
    
    print("\nUsing normal for loop\n")
    start = time.time()
    results = ImagesGenerator(texts=texts, font_size=50, noises=[], font_path='iftg/fonts/Arial.ttf', 
                              img_output_path='./iftg/img_text_test', txt_output_path='./iftg/img_text_test',
                             )
    
    # results = ImagesGenerator(texts=texts, font_size=50, noises=[], font_path='iftg/fonts/Arial.ttf')

    if results.generate_images():
        print('True')
    # for i, (img, _) in enumerate(results):
    #     # img.save(f'output_images/img_{i}.png')
    #     img.show()
    #     # continue
        
    end = time.time()
    print(f"Time: {end-start} sec")
    


if __name__ == '__main__':
    main()
    # text = """I am Omar\nI live in cairo"""
    # print(text.splitlines())
    
    
    
