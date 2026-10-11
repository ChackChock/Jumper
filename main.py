import pygame

from src.sprite import Sprite


def main():
    window = pygame.Window("Jumper", [400, 600])
    surface = window.get_surface()

    platform_image = pygame.image.load("assets/platform.png")
    platform = Sprite([200, 550], platform_image)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                running = False

        platform.render(surface)

        window.flip()

if __name__ == "__main__":
    main()
