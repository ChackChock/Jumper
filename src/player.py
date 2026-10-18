import pygame

from src.sprite import Sprite


class Player(Sprite):
    def __init__(self, center, image, speed):
        super().__init__(center, image)

        self.orig_image = image.copy()
        self.speed = speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.image = self.orig_image.copy()
            self.rect.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.image = pygame.transform.flip(self.orig_image, True, False)
            self.rect.x += self.speed

