import pygame
import include.controller
import include.rooms
import include.renderer
# import utils.pic_compressor

WIDTH = 1000
HEIGHT = int(WIDTH * 2 / 3)
SCALE = 0.7


class example_class:

    def __init__(self):
        self.move_right = pygame.image.load("./assets/character_file_compressed/move_right.png").convert_alpha()
        self.move_left = pygame.image.load("./assets/character_file_compressed/move_left.png").convert_alpha()
        self.stand_right = pygame.image.load("./assets/character_file_compressed/stand_right.png").convert_alpha()
        self.stand_left = pygame.image.load("./assets/character_file_compressed/stand_left.png").convert_alpha()
        self.x = 0
        self.y = 0
        self.speedx = 5
        self.speedy = 5


def main():
    pygame.init()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Some 2D Shooting Game")
    background = pygame.image.load("./assets/backgrounds/background_1.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    running = True

    c = example_class()
    controller = include.controller.input_handling()
    while running:

        left, right, up, attack, leave = controller.check_event()
        if leave:
            running = False
        if left:
            c.x -= c.speedx
        if right:
            c.x += c.speedx
        if up:
            c.y -= c.speedy

        surface.blit(background, (0, 0))
        surface = include.renderer.render(surface=surface, n={(c.x, c.y): c.stand_right})
        pygame.display.flip()


if __name__ == '__main__':
    main()
