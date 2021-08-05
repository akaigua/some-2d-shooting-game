import pygame
import include.controller
import include.rooms
import include.renderer
import include.Character
import include.physics
import random
import time
import math

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
    blue_screen = False

    c = include.Character.Player(max_hp=random.randint(15, 20), strength=random.randint(5, 7))
    p = include.physics.physics(c)
    # r = include.rooms.Room(1)
    r0, r1, r2, r3, r4, r5 = [include.rooms.Room(i) for i in range(6)]
    rs = {0: r0, 1: r1, 2: r2, 3: r3, 4: r4, 5: r5}
    bg = include.renderer.BackgroundChanger()
    controller = include.controller.input_handling()
    start, end = 0, 0.1
    bg_id = 0
    if 0 < bg_id <= 5:
        monster_list = [include.Character.Monster(i) for i in include.rooms.Room.Monster_Dic[bg_id].keys()]


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
        if blue_screen:
            background = pygame.image.load(f"./assets/backgrounds/blue_screen.png")
            background = pygame.transform.scale(background, (WIDTH, HEIGHT))
            time.sleep(5)
            running = False
        
        if bg_id == 0:
            buttons = pygame.mouse.get_pressed()
            x1, y1 = pygame.mouse.get_pos()
            if 176 <= x1 <= 385 and 153 <= y1 <= 187:#start
                if buttons[0]:
                    bg_id += 1
            elif 49 <= x1 <= 104 and 299 <= y1 <= 324: #quit
                if buttons[0]:
                    pygame.quit()
                    exit()
            elif 176 <= x1 <= 385 and 197 <= y1 <= 230: #continue
                if buttons[0]:
                    time.sleep(2)
                    blue_screen = True
            elif 176 <= x1 <= 385 and 240 <= y1 <= 275: #option
                if buttons[0]:
                    time.sleep(2)
                    blue_screen = True
                    

        # monster_list = [include.Character.Monster(i) for i in include.rooms.Room.Monster_Dic[bg_id].keys()]
        if 0 < bg_id <= 5:
            monster_render_list = {(mons.x/18*WIDTH, mons.y/12*HEIGHT): mons.status_avatar for mons in monster_list}

            last_latency = end - start
            start = time.time()
            left, right, up, attack, leave, stop_move_left, stop_move_right, timer, reset = controller.check_event()
            # print(left, right, up, attack, leave, stop_move_left, stop_move_right)
            left_col, right_col = p.side_by_side(r)
            head = p.head_by_head(r)
            for i in monster_list:
                i.move(last_latency)
            if leave:
                running = False
            '''
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
            '''
            c.y = p.physic_handling(last_latency, r)
            if attack:
                print(f"[INFO] Player has attacked")
            
            c.move(left, right, up, stop_move_left, stop_move_right, left_col, right_col, head)
            surface = include.renderer.render(surface=surface, n={(c.x, c.y): c.status_avatar})
            surface = include.renderer.render(surface=surface, n=monster_render_list)
            
        surface.blit(background, (0, 0))
        pygame.display.flip()
        end = time.time()
        # print(math.sqrt((i.x-c.x)**2 + (i.y-c.y)**2))
        if 0 < bg_id <= 5:
            collides = []
            for i in monster_list:
                collides.append(math.sqrt((i.x/18*WIDTH-c.x)**2 + (i.y/12*HEIGHT-c.y)**2))
            if min(collides) < 30:
                # dead 
                p.in_air_time += p.lat
                c.y + 0.25 * G * (p.in_air_time ** 2)
                bg_id += 1
                c.y = HEIGHT - c.h - 53
                c.x = 0


        # FPS display
        # print(f"[INFO] FPS: {1/last_latency}")

if __name__ == '__main__':
    main()
