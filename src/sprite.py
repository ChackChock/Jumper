class Sprite:
    def __init__(self, center, image):
        self.image = image
        self.rect = image.get_frect(center=center)

    def render(self, surface):
        surface.blit(self.image, self.rect)
