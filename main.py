import pygame


def main():
    window = pygame.Window("Jumper", [400, 600])
    surface = window.get_surface()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                running = False

        window.flip()

if __name__ == "__main__":
    main()
