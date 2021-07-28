import pygame
import include.controller
import include.rooms
import include.renderer

width = 1000
height = int(width * 2 / 3)


class example_class:

    def __init__(self):
        self.move_right = pygame.image.load("./assets/character_file_compressed/move_right.png").convert_alpha()
        self.move_left = pygame.image.load("./assets/character_file_compressed/move_left.png").convert_alpha()
        self.stand_right = pygame.image.load("./assets/character_file_compressed/stand_right.png").convert_alpha()
        self.stand_left = pygame.image.load("./assets/character_file_compressed/stand_left.png").convert_alpha()
        self.x = 0
        self.y = 0


def main():
    pygame.init()
    surface = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Some 2D Shooting Game")
    background = pygame.image.load("./assets/resource_example.png")
    background = pygame.transform.scale(background, (width, height))
    running = True

    c = example_class()

    while running:

        left, right, up, down, attack, leave = include.controller.check_event()
        if leave:
            running = False
        if left:
            c.x -= 10
        if right:
            c.x += 10
        if up:
            c.y -= 10
        if down:
            c.y += 10

        surface.blit(background, (0, 0))
        surface = include.renderer.render(surface=surface, n={(c.x,c.y):c.stand_right})
        # surface.blit(ch,(ch_x,ch_y))
        pygame.display.flip()


if __name__ == '__main__':
    main()
