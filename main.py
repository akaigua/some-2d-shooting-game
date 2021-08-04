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
    pygame.display.set_caption("Mantis Knight")
    background = pygame.image.load("./assets/backgrounds/background_1.jpg")
    #background = pygame.image.load("./assets/debug_resource/debug_m1.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    running = True

    c = include.Character.Player(max_hp=random.randint(15, 20), mx=5, strength=random.randint(5, 7))
    p = include.physics.physics(c)
    r = include.rooms.Room(1)
    controller = include.controller.input_handling()
    start, end = 0, 0.1
    
    r1,r2,r3,r4,r5 = [include.rooms.Room(i) for i in range(1,6)]
    rs = {1:r1,2:r2,3:r3,4:r4,5:r5} 
    bg = include.renderer.BackgroundChanger()
    bg_id = 1

    mx, my = 1,5
    m = include.Character.Monster(mx, my, c.x, 4, random.randint(15, 20), strength=random.randint(3, 5))
    t = pygame.time.get_ticks()

    while running:

        last_latency = end - start
        start = time.time()
        left, right, up, attack, leave, stop_move_left, stop_move_right, timer, reset = controller.check_event()
        # print(left, right, up, attack, leave, stop_move_left, stop_move_right)
        left_col,right_col = p.side_by_side(r)
        head = p.head_by_head(r)

        r = rs[bg_id]
        background = bg.background(bg_id)
        # if c.x == 0 and bg_id > 1:
        #     bg_id -= 1
        #     c.y = HEIGHT - c.h - 53
        if c.x == WIDTH and bg_id < 5:
            bg_id += 1
            c.y = HEIGHT - c.h - 53
            c.x = 0
        
        #_ = r.collide(map.map_1(),c)
        #c_up, c_left, c_right, c_bottom = _
        #print(c_up, c_left, c_right, c_bottom)
        c.move(left, right, up, stop_move_left, stop_move_right, left_col, right_col, head)
        c.update(m.x,m.hp)
        m.update(c.x,c.hp)
        # c.display_direction(left, right, up, stop_move_left, stop_move_right)
        if c.hp <= 0:
            c.x, c.y = 0, c.SCREEN_H - c.h - 53
        if m.hp <= 0:
            print('You won')
            #如何实现让死亡的怪兽消失
        #print(round(t * 1000, 2))
        # print the time the player used

        c.y = p.physic_handling(last_latency,r)
        # c.rect.topleft = (c.x, c.y)
        #pygame.Rect.move_ip(c.rect, c.x, c.y)
        #print(c.rect)

        if attack:
            c.damage(attack, m.hp)
        if leave:
            running = False
        if reset:
            c.x, c.y = 0, c.SCREEN_H - c.h - 53


        # Update

        surface.blit(background, (0, 0))
        surface = include.renderer.render(surface=surface, n={(c.x, c.y): c.status_avatar})
        pygame.display.flip()
        end = time.time()
        # FPS display
        # print(f"[INFO] FPS: {1/last_latency}")


if __name__ == '__main__':
    main()