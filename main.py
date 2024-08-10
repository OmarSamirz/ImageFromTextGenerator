import time
from PIL.Image import Resampling
from iftg.generators.image_generator import ImageGenerator
from iftg.noises.gaussian_noise import GaussianNoise
# from iftg.noises.blur_noise import BlurNoise

def main():
    texts = ['Hi', """I am Omar""", "Hello, World!"]
    # texts = ['Hi I am Omar Samir Ibrahim']

    # result = ImageGenerator(texts=texts, texts_len=len(texts), font_size=50, rotation_angle=50, random_rotation=True,
                            # noises=[GaussianNoise(0, 40)])
    
    result = ImageGenerator(texts=texts, texts_len=len(texts), font_size=50, random_rotation=True)
    
    start = time.time()

    for i, (img, lbl) in enumerate(result):
        print(lbl)
        # img = img.rotate(5, resample=Resampling.BICUBIC, expand=True, fillcolor=result.background_color)
        img.show()
    end = time.time()

    print(end-start)

if __name__ == '__main__':
    main()