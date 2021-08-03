import pygame
import os
import numpy as np
import include.Character
PIC_WIDTH = 576
PIC_HEIGHT = 384


# 18 x 12
'''''
class Room:
    terrain_location = {
        1: {(0, 3): True, (0, 4): True, (0, 5): True, (0, 11): True, (1, 3): True}
    }

    def __init__(self, room_ID: int):
        self.room_id = room_ID
        self.room_structure = Room.terrain_location[1]
    
    def direction(self, rect1, rect2, collision_list):
        if rect1.top > rect2.top:
            # print('up')
            collision_list[0] = True
        if rect1.left > rect2.left:
            # print('left')
            collision_list[1] = True
        if rect1.right < rect2.right:
            # print('right')
            collision_list[2] = True
        if rect1.bottom < rect2.bottom:
            collision_list[3 ] = True

    def collide(self, nList,c:include.Character.Player):
        self.rect_list = []
        collision_list = [False, False, False, False]
        for i in range(len(nList)):
            self.rect_list.append(pygame.Rect(nList[i][0] * 32, nList[i][1] * 32, nList[i][2] * 32, nList[i][3] * 32))
    

        for i in range(len(self.rect_list)):
            if pygame.Rect.colliderect(c.rect, self.rect_list[i]) == True:
                Room.direction(self, c.rect, self.rect_list[i],collision_list) 
        print(c.rect)
        print(self.rect_list)          
        return collision_list

class Block(pygame.sprite.Sprite()):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        rect_group = pygame.sprite.Group()
        rect_group = pygame.sprite.Group()

class Map:

    def __init__(self):
        # map_list = []

        self.rect_list = []

    def map_1(self):
        nList = [[0, 3, 3, 1], [0, 4, 1, 2], [6, 4, 3, 1],
                 [8, 5, 1, 6], [17, 9, 1, 1],
                 [16, 11, 2, 1], [0, 11, 18, 1], [3, 7, 3, 1],
                 [12, 7, 4, 1], [11, 1, 1, 3],
                 [12, 3, 3, 1]]

        return nList

    def map_2(self):
        nList = [[0, 0, 2, 1], [0, 1, 1, 1], [0, 5, 2, 1], [0, 6, 1, 1], [4, 3, 7, 1], [3, 8, 1, 3], [4, 8, 2, 1],
                 [5, 6, 1, 2], [8, 7, 5, 1], [10, 8, 1, 1],
                 [13, 0, 1, 4], [14, 3, 2, 1], [15, 6, 3, 1], [17, 7, 1, 4], [14, 9, 2, 1], [0, 11, 18, 1]]

        return nList
        
=======
        self.rect_list = []
        for i in range(len(nList)):
            self.rect_list.append(
                pygame.Rect(nList[i][0] * 576, nList[i][1] * 384, nList[i][2] * 576, nList[i][3] * 384))

    def map_2(self):
        nlist = [[0, 0, 2, 1], [0, 1, 1, 1], [0, 5, 2, 1], [0, 6, 1, 1], [4, 3, 7, 1], [3, 8, 1, 3], [4, 8, 2, 1],
                 [5, 6, 1, 2], [8, 7, 5, 1], [10, 8, 1, 1],
                 [13, 0, 1, 4], [14, 3, 2, 1], [15, 6, 3, 1], [17, 7, 1, 4], [14, 9, 2, 1], [0, 11, 18, 1]]
>>>>>>> Stashed changes
        self.rect_list = []
        for i in range(len(nlist)):
            self.rect_list.append(
                pygame.Rect(nlist[i][0] * 32, nlist[i][1] * 32, nlist[i][2] * 32, nlist[i][3] * 32))
        

    def map_3(self):
        nList = [[0, 0, 1, 3], [1, 2, 3, 1], [0, 5, 1, 2], [3, 8, 1, 3], [4, 8, 3, 1], [6, 5, 2, 1], [7, 3, 1, 2],
                 [8, 3, 5, 1], [12, 2, 1, 1], [9, 7, 5, 1],
                 [15, 5, 3, 1], [17, 2, 1, 4], [16, 10, 2, 1], [17, 9, 1, 1], [0, 11, 18, 1]]
        return nList

        
=======
        nlist = [[0, 0, 1, 3], [1, 2, 3, 1], [0, 5, 1, 2], [3, 8, 1, 3], [4, 8, 3, 1], [6, 5, 2, 1], [7, 3, 1, 2],
                 [8, 3, 5, 1], [12, 2, 1, 1], [9, 7, 5, 1],
                 [15, 5, 3, 1], [17, 2, 1, 4], [16, 10, 2, 1], [17, 9, 1, 1], [0, 11, 18, 1]]
>>>>>>> Stashed changes
        self.rect_list = []
        for i in range(len(nlist)):
            self.rect_list.append(
                pygame.Rect(nlist[i][0] * 32, nlist[i][1] * 32, nlist[i][2] * 32, nlist[i][3] * 32))
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        


    def map_4(self):
        nList = [[0, 3, 3, 1], [0, 7, 5, 1], [4, 5, 1, 2], [5, 5, 1, 1], [7, 2, 3, 1], [11, 4, 4, 1], [8, 7, 1, 4],
                 [9, 7, 2, 1], [16, 0, 2, 1], [17, 1, 1, 2], [16, 8, 2, 1], [17, 7, 1, 1], [0, 11, 18, 1]]
        return nList
        
                self.rect_list = []
                for i in range(len(nlist)):
                    self.rect_list.append(
                        pygame.Rect(nlist[i][0] * 32, nlist[i][1] * 32, nlist[i][2] * 32, nlist[i][3] * 32))
        

    def map_end_1(self):
        nList = [[0, 3, 4, 1], [0, 7, 2, 1], [15, 3, 3, 1], [16, 7, 2, 1], [0, 11, 18, 1], [4, 9, 1, 2], [5, 7, 1, 3],
                 [6, 5, 1, 3], [7, 3, 1, 3], [8, 2, 1, 2], [10, 2, 1, 2], [11, 3, 1, 3], [12, 5, 1, 3], [13, 7, 1, 3],
                 [18, 9, 1, 2], [9, 2, 1, 1]]
        return nList


    def map_end_2(self):
        nList = [[0, 3, 4, 1], [0, 7, 2, 1], [15, 3, 3, 1], [16, 7, 2, 1], [0, 11, 18, 1], [4, 9, 1, 2], [5, 7, 1, 3],
                 [6, 5, 1, 3], [7, 3, 1, 3], [8, 2, 1, 2], [10, 2, 1, 2], [11, 3, 1, 3], [12, 5, 1, 3], [13, 7, 1, 3],
                 [18, 9, 1, 2]]
        return nList
'''''

class Room:
    terrain_location = {
        1: {(0, 3): True, (0, 4): True, (0, 5): True, (0, 11): True, (1, 3): True, (2, 3): True, (3, 7): True, (4, 7): True,
            (5, 7): True, (6, 4): True, (7, 4): True, (8, 4): True, (8, 5): True, (8, 6): True, (8, 7): True, (8, 8): True,
            (8, 9): True, (8, 10): True, (11, 1): True, (11, 2): True, (11, 3): True, (12, 3): True, (13, 3): True, (14, 3): True,
            (12, 7): True, (13, 7): True, (14, 7): True, (15, 7): True, (16, 10): True, (17, 10): True, (17, 9): True, (1, 11): True,
            (2, 11): True, (3, 11): True, (4, 11): True, (5, 11): True, (6, 11): True, (7, 11): True, (8, 11): True, (9, 11):True,
            (10, 11): True, (11, 11): True, (12, 11): True, (13, 11): True, (14, 11): True, (15, 11): True, (16, 11): True, (17, 11): True
            },


        2: {(0, 0): True, (0, 1): True, (1, 0): True, (0, 5): True, (0, 6): True, (1, 5): True, (4, 3): True, (5, 3): True, (6, 3): True,
            (7, 3): True, (8, 3): True, (9, 3): True, (10, 3): True, (3, 8): True, (3, 9): True, (3, 10): True, (4, 8): True, (5, 8): True,
            (5, 7): True, (5, 6): True, (8, 7): True, (9, 7): True, (10, 7): True, (11, 7): True, (12, 7): True, (10, 8): True,
            (13, 0): True, (13, 1): True, (13, 2): True, (13, 3): True, (14, 3): True, (15, 3): True, (14, 9): True, (15, 9): True,
            (15, 6): True, (16, 6): True, (17, 6): True, (17, 7): True, (17, 8): True, (17, 9): True, (17, 10): True, (0, 11): True,
            (1, 11): True, (2, 11): True, (3, 11): True, (4, 11): True, (5, 11): True, (6, 11): True, (7, 11): True, (8, 11): True,
            (9, 11): True, (10, 11): True, (11, 11): True, (12, 11): True, (13, 11): True, (14, 11): True, (15, 11): True, (16, 11): True, (17, 11): True
            },

        3: {(0, 11): True, (1, 11): True, (2, 11): True, (3, 11): True, (4, 11): True, (5, 11): True, (6, 11): True, (7, 11): True, (8, 11): True,
            (9, 11): True, (10, 11): True, (11, 11): True, (12, 11): True, (13, 11): True, (14, 11): True, (15, 11): True, (16, 11): True, (17, 11): True,
            (0, 0): True, (0, 1): True, (0, 2): True, (1, 2): True, (2, 2): True, (3, 2): True, (0, 5): True, (0, 6): True, (3, 8): True,
            (4, 8): True, (5, 8): True, (6, 8): True, (3, 9): True, (3, 10): True, (6, 5): True, (7, 5): True, (7, 4): True, (7, 3): True, (8, 3): True,
            (9, 3): True, (10, 3): True, (11, 3): True, (12, 3): True, (12, 2): True, (9, 7): True, (10, 7): True, (11, 7): True, (12, 7): True, (13, 7): True,
            (15, 5): True, (16, 5): True, (17, 5): True, (17, 4): True, (17, 3): True, (17, 2): True, (17, 9): True, (17, 10): True, (16, 10): True
            },

        4: {(0, 11): True, (1, 11): True, (2, 11): True, (3, 11): True, (4, 11): True, (5, 11): True, (6, 11): True, (7, 11): True, (8, 11): True,
            (9, 11): True, (10, 11): True, (11, 11): True, (12, 11): True, (13, 11): True, (14, 11): True, (15, 11): True, (16, 11): True, (17, 11): True,
            (0, 3): True, (1, 3): True, (2, 3): True, (0, 7): True, (1, 7): True, (2, 7): True, (3, 7): True, (4, 7): True, 
            (4, 6): True, (4, 5): True, (5 ,5): True, (7,2): True, (8, 2): True, (9, 2): True, (8, 7): True, (9, 7): True, (10, 7): True, 
            (8, 8): True, (8, 9): True, (8, 10): True, (16, 0): True, (17, 0): True, (17, 1): True, (17, 2): True, (17, 3): True,
            (16,8): True, (17, 8): True, (17, 7): True},

        5: {(0, 3): True, (1, 3): True, (2, 3): True, (3, 3): True, (0,7): True, (1,7): True, (15, 3): True, (16, 3): True, (17, 3): True,
            (4, 10): True, (4, 9): True, (5, 9): True, (5, 8): True, (5, 7): True, (6, 7): True, (6, 6): True, (6, 5): True, (7, 5): True,
            (7, 4): True, (7, 3): True, (8, 3): True, (8, 2): True, (9, 2): True, (10, 2): True, (10, 3): True, (11, 3): True, (11, 4): True,
            (11, 5): True, (12, 5): True, (12, 6): True, (12, 7): True, (13, 7): True, (13, 8): True, (13, 9): True, (14, 9): True, (14, 10): True,
            (0, 11): True, (1, 11): True, (2, 11): True, (3, 11): True, (4, 11): True, (5, 11): True, (6, 11): True,
            (7, 11): True, (8, 11): True, (9, 11): True, (10, 11): True, (11, 11): True, (12, 11): True, (13, 11): True, (14, 11): True,
            (15, 11): True, (16, 11): True, (17, 11): True
            },

        6: {(0, 3): True, (1, 3): True, (2, 3): True, (3, 3): True, (0,7): True, (1,7): True, (15, 3): True, (16, 3): True, (17, 3): True,
            (4, 10): True, (4, 9): True, (5, 9): True, (5, 8): True, (5, 7): True, (6, 7): True, (6, 6): True, (6, 5): True, (7, 5): True,
            (7, 4): True, (7, 3): True, (8, 3): True, (8, 2): True,(10, 2): True, (10, 3): True, (11, 3): True, (11, 4): True,
            (11, 5): True, (12, 5): True, (12, 6): True, (12, 7): True, (13, 7): True, (13, 8): True, (13, 9): True, (14, 9): True, (14, 10): True,
            (0, 11): True, (1, 11): True, (2, 11): True, (3, 11): True, (4, 11): True, (5, 11): True, (6, 11): True,
            (7, 11): True, (8, 11): True, (9, 11): True, (10, 11): True, (11, 11): True, (12, 11): True, (13, 11): True, (14, 11): True,
            (15, 11): True, (16, 11): True, (17, 11): True,
        }}

    def __init__(self, room_ID: int):
        self.room_id = room_ID
        self.room_structure = Room.terrain_location[1]
        self.Mxy_list = [()]


class Map:

    def __init__(self):
        map_list = []