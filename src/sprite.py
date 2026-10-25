import pygame


class Sprite:
    def __init__(self, center: list[float], image: pygame.Surface):
        self.image = image
        self.rect = image.get_frect(center=center)

    def render(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)
