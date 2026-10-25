from random import randint

import pygame

from src.config import SPAWN_STEP, WIN_SIZE, WIN_WIDTH
from src.player import Player
from src.sprite import Sprite


def main():
    window = pygame.Window("Jumper", WIN_SIZE)
    surface = window.get_surface()
    clock = pygame.Clock()

    background_image = pygame.image.load("assets/background.png")
    background_image = pygame.transform.scale(background_image, WIN_SIZE)

    platform_image = pygame.image.load("assets/platform.png")
    platforms = [Sprite([200, 550], platform_image)]
    for y in range(550 - SPAWN_STEP, 0, -SPAWN_STEP):
        platforms.append(Sprite([randint(0, WIN_WIDTH), y], platform_image))

    player_image = pygame.image.load("assets/player.png")
    player = Player([200, 450], player_image, 6)
    window.set_icon(player_image)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                running = False

        player.update(platforms)

        surface.blit(background_image)
        for platform in platforms:
            platform.render(surface)
        player.render(surface)

        window.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
