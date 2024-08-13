import time
from PIL import ImageFont, Image
from iftg.creators import ImageCreator
from iftg.generators import ImagesGenerator
from iftg.utils import ImageFontManager
from iftg.noises import DilateNoise
from iftg.noises import GaussianNoise
from iftg.noises import ErodeNoise
from iftg.noises import ShadowNoise
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, cpu_count

def save_image(args):
    i, img = args
    img.save(f'output_images/img_{i}.png')

def main():
    
    texts = ["我是奥马尔\n我是奥马尔\nDejaVuSans"]
    texts = ['أنا عمر سمير', 'قُلْ يَا أَيُّهَا الْكَافِرُونَ\nقُلْ يَا أَيُّهَا الْكَافِرُونَ', 'ثُمَّ لَتَرَوُنَّهَا عَيْنَ الْيَقِينِ']
    texts = ['Hello, I am Omar']
    texts = ['नमस्ते, मैं उमर हूं']
    texts = ["""I am Omar\nI live in cairo\nI love playing tenis and playing football\nI love playing tenis and playing football\nI love playing tenis and playing football\nI love playing tenis and playing football"""]
    texts = ['Hello, World!']

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

    
    print("\nUsing normal for loop\n")
    start = time.time()
    results = ImagesGenerator(texts=texts, font_size=20, noises=[], font_path='iftg/fonts/AnekDevanagari-VariableFont_wdth,wght.ttf', )

    for i, (img, _) in enumerate(results):
        # img.save(f'output_images/img_{i}.png')
        img.show()
        continue
    end = time.time()
    print(f"Time: {end-start} sec")
    
    



if __name__ == '__main__':
    main()
    # text = """I am Omar\nI live in cairo"""
    # print(text.splitlines())
    
    
    
