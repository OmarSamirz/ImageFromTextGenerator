import time
import io
from PIL import ImageFont, Image
from iftg.models.creators.image_creator import ImageCreator
from iftg.models.generators.images_generator import ImagesGenerator
from iftg.models.image_font_manager import ImageFontManager
from iftg.noises.dilate_noise import DilateNoise
from iftg.noises.gaussian_noise import GaussianNoise
from iftg.noises.erode_noise import ErodeNoise
from iftg.noises.shadow_noise import ShadowNoise
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, cpu_count


def save_image(args):
    i, img = args
    img.save(f'output_images/img_{i}.png')

def main():
    
    texts = ["我是奥马尔\n我是奥马尔\nDejaVuSans"]
    texts = ["""I am Omar\nI live in cairo\nI love playing tenis and playing football\nI love playing tenis and playing football\nI love playing tenis and playing football\nI love playing tenis and playing football"""]*10000
    texts = ['أنا عمر سمير', 'قُلْ يَا أَيُّهَا الْكَافِرُونَ\nقُلْ يَا أَيُّهَا الْكَافِرُونَ', 'ثُمَّ لَتَرَوُنَّهَا عَيْنَ الْيَقِينِ']
    texts = ['Hello, I am Omar']
    texts = ['नमस्ते, मैं उमर हूं']
    texts = ['Hello, World!']

    text = 'Hi I am Omar Samir Ibrahim'

    print("Using multiprocessing")
    start = time.time()

    results = ImagesGenerator(texts=texts, font_size=50, noises=[], font_path='iftg/fonts/AnekDevanagari-VariableFont_wdth,wght.ttf')

    with Pool(cpu_count()) as pool:
        # Map the save_image function to the results
        pool.map(save_image, [(i, img) for i, (img, lbl) in enumerate(results)])

    # for i, (img, lbl) in enumerate(results):
    #     print(i)
    #     img.save(f'output_images/img_{i}.png')
    end = time.time()
    print(f"Time: {end-start} sec")

    
    print("\nUsing normal for loop\n")
    start = time.time()
    results = ImagesGenerator(texts=texts, font_size=50, noises=[], font_path='iftg/fonts/AnekDevanagari-VariableFont_wdth,wght.ttf')

    for i, (img, _) in enumerate(results):
        img.save(f'output_images/img_{i}.png')
    end = time.time()
    print(f"Time: {end-start} sec")
    
    



if __name__ == '__main__':
    main()
    # text = """I am Omar\nI live in cairo"""
    # print(text.splitlines())
    
    
    
