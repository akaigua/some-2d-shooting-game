import pygame
import include.controller
import include.rooms
import include.renderer
import include.Character
import random

# import utils.pic_compressor

WIDTH = 1000
HEIGHT = int(WIDTH * 2 / 3)
SCALE = 0.7


#
# class example_class:
#
#     def __init__(self):
#         self.move_right = pygame.image.load("./assets/character_file_compressed/move_right.png").convert_alpha()
#         self.move_left = pygame.image.load("./assets/character_file_compressed/move_left.png").convert_alpha()
#         self.stand_right = pygame.image.load("./assets/character_file_compressed/stand_right.png").convert_alpha()
#         self.stand_left = pygame.image.load("./assets/character_file_compressed/stand_left.png").convert_alpha()
#         self.x = 0
#         self.y = 0
#         self.speedx = 5
#         self.speedy = 5


def main():
    pygame.init()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Some 2D Shooting Game")
    background = pygame.image.load("./assets/backgrounds/background_1.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    running = True

    c = include.Character.Player(max_hp=random.randint(15, 20), mx=5, strength=random.randint(5, 7))
    controller = include.controller.input_handling()
    while running:

        left, right, up, attack, leave, stop_move_left, stop_move_right = controller.check_event()
        print(left, right, up, attack, leave, stop_move_left, stop_move_right)
        if leave:
            running = False
        if left:
            c.x -= c.speedx
            c.status_avatar = c.move_left
        if right:
            c.x += c.speedx
            c.status_avatar = c.move_right
        if stop_move_right:
            c.status_avatar = c.stand_left
        if stop_move_left:
            c.status_avatar = c.stand_right
        if up:
            c.y -= c.speedy

        if attack:
            print(f"[INFO] Player has attacked")

        surface.blit(background, (0, 0))
        surface = include.renderer.render(surface=surface, n={(c.x, c.y): c.status_avatar})
        pygame.display.flip()


if __name__ == '__main__':
    main()
