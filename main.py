import pygame
import include.controller
import include.rooms
import include.renderer

width = 1000
length = 668


def main():
    pygame.init()
    surface = pygame.display.set_mode((width, length))
    pygame.display.set_caption("Some 2D Shooting Game")
    background = pygame.image.load("./assets/platformer_0.png")
    background = pygame.transform.scale(background, (width, length))
    running = True

    while running:
        left, right, up, down, attack, leave = include.controller.check_event()
        if leave:
            running = False
        surface.blit(background, (0, 0))
        # surface = include.renderer.render(surface,)
        pygame.display.flip()


if __name__ == '__main__':
    main()
