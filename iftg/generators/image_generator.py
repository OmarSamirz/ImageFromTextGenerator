from iftg.generators.generator import Generator, Image

class ImageGenerator(Generator):

    def next(self):
        if self._count == self.texts_len:
            raise StopIteration
        
        self._count += 1
        return self._generate_image(self.texts[self._count-1]), self.texts[self._count-1]
    
    def _create_image(self, text: str) -> Image:
        return super()._create_image(text)
        
    def _apply_noise(self, text: str, image: Image) -> Image:
        return super()._apply_noise(text, image)

    def _generate_image(self, text: str) -> Image:
        image = self._create_image(text)
        image = self._apply_noise(text, image)
            
        return image


