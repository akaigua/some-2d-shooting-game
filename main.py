import pygame
import include.controller
import include.rooms
import include.renderer
import include.Character
import include.physics
import random
import time

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
    # background = pygame.image.load("./assets/backgrounds/background_1.jpg")
    # background = pygame.image.load("./assets/debug_resource/debug_m1.png")
    # background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    running = True

    c = include.Character.Player(max_hp=random.randint(15, 20), mx=5, strength=random.randint(5, 7))
    p = include.physics.physics(c)
    # r = include.rooms.Room(1)
    r1,r2,r3,r4,r5 = [include.rooms.Room(i) for i in range(1,6)]
    rs = {1:r1,2:r2,3:r3,4:r4,5:r5}
    bg = include.renderer.BackgroundChanger()
    controller = include.controller.input_handling()
    start, end = 0, 0.1
    bg_id = 1
    while running:
        r = rs[bg_id]
        background = bg.background(bg_id)
        # if c.x == 0 and bg_id > 1:
        #     bg_id -= 1
        #     c.y = HEIGHT - c.h - 53
        if c.x == WIDTH and bg_id < 5:
            bg_id += 1
            c.y = HEIGHT - c.h - 53
            c.x = 0

        last_latency = end - start
        start = time.time()
        left, right, up, attack, leave, stop_move_left, stop_move_right = controller.check_event()
        # print(left, right, up, attack, leave, stop_move_left, stop_move_right)
        left_col,right_col = p.side_by_side(r)
        head = p.head_by_head(r)
        if leave:
            running = False
        if left and not left_col:
            c.x -= c.speedx
            c.status_avatar = c.move_left
        if right and not right_col:
            c.x += c.speedx
            c.status_avatar = c.move_right
        if stop_move_right:
            c.status_avatar = c.stand_left
        if stop_move_left:
            c.status_avatar = c.stand_right
        if up and not head:
            c.y -= c.speedy
        c.y = p.physic_handling(last_latency,r)
        if attack:
            print(f"[INFO] Player has attacked")

        surface.blit(background, (0, 0))
        surface = include.renderer.render(surface=surface, n={(c.x, c.y): c.status_avatar})
        pygame.display.flip()
        end = time.time()
        # FPS display
        # print(f"[INFO] FPS: {1/last_latency}")


if __name__ == '__main__':
    main()
