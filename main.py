import time
from PIL import ImageFont
from iftg.models.creators.image_creator import ImageCreator
from iftg.models.generators.images_generator import ImagesGenerator
from iftg.models.image_font_manager import ImageFontManager
from iftg.noises.dilate_noise import DilateNoise
from iftg.noises.gaussian_noise import GaussianNoise
from iftg.noises.erode_noise import ErodeNoise
from iftg.noises.shadow_noise import ShadowNoise

def main():
    texts = ['Hi', """I am Omar""", "Hello, World!"]
    text = 'Hi I am Omar Samir Ibrahim'

    
    
    
    
    start = time.time()
    
    result = ImageCreator.create_image(text=text, font_size=50, blur_radius=0,
                            noises=[ShadowNoise(),])
    
    # for img, lbl in result:
    #     print(lbl)
    #     img.show()
    result.show()

    end = time.time()


    print(end-start)
    print(ImageFontManager.fonts)

if __name__ == '__main__':
    main()
    
    
