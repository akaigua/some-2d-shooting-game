from typing import *
import random
import pygame
import os
import numpy as np
import include.Character

PIC_WIDTH = 576
PIC_HEIGHT = 384

# 18 x 12

class Room:
    terrain_location = {
        1: {(0, 3): True, (0, 4): True, (0, 5): True, (0, 11): True, (1, 3): True}
    }

    def __init__(self, room_ID: int):
        self.room_id = room_ID
        self.room_structure = Room.terrain_location[1]
    
    def direction(self, rect1, rect2):
        if rect1.midtop[1] > rect2.midtop[1]:
            # print('up')
            return 'up'
        if rect1.midleft[0] > rect2.midleft[0]:
            # print('left')
            return 'left'
        if rect1.midright[0] < rect2.midright[0]:
            # print('right')
            return 'right'
        if rect1.midbottom[1] < rect2.midbottom[1]:
            # print('bottom')
            return 'bottom'
    
    def collide(self, nList,c:include.Character.Player):
        self.rect_list = []
        for i in range(len(nList)):
            self.rect_list.append(pygame.Rect(nList[i][0] * 32, nList[i][1] * 32, nList[i][2] * 32, nList[i][3] * 32))
    
        print(self.rect_list)
        print(c.rect)

        for i in range(len(self.rect_list)):
            print("fored")
            print(c.rect.colliderect(self.rect_list[i]))
            if c.rect.colliderect(self.rect_list[i]) == True:
                Room.direction(self, c.rect, self.rect_list[i])             
                print("ifed")  
            else:
                print("elsed")
                return False, False, False, False


class Map:

    def __init__(self):
        #map_list = []
        
        self.rect_list = []

    def map_1(self):
        nList = [[0, 3, 3, 1], [0, 4, 1, 2], [6, 4, 3, 1],
                 [8, 5, 1, 6], [17, 9, 1, 1],
                 [16, 11, 2, 1], [0, 11, 18, 1], [3, 7, 3, 1],
                 [12, 7, 4, 1], [11, 1, 1, 3],
                 [12, 3, 3, 1]]
        
        return nList

        '''''
        self.rect_list = []
        for i in range(len(nList)):
            self.rect_list.append(pygame.Rect(nList[i][0] * 32, nList[i][1] * 32, nList[i][2] * 32, nList[i][3] * 32))

        for i in self.rect_list:
            if c.rect.colliderect(self.rect_list[i]) != -1:
                Room.direction(c.rect, self.rect_list[i])
        ''''' 

    def map_2(self):
        nList = [[0,0,2,1],[0,1,1,1],[0,5,2,1],[0,6,1,1],[4,3,7,1],[3,8,1,3],[4,8,2,1],[5,6,1,2],[8,7,5,1],[10,8,1,1],
                 [13,0,1,4],[14,3,2,1],[15,6,3,1],[17,7,1,4],[14,9,2,1],[0,11,18,1]]
        
        return nList 
        '''''
        self.rect_list = []
        for i in range(len(nlist)):
            self.rect_list.append(
                pygame.Rect(nlist[i][0] * 32, nlist[i][1] * 32, nlist[i][2] * 32, nlist[i][3] * 32))
        '''''
        
    def map_3(self):
        nList = [[0,0,1,3],[1,2,3,1],[0,5,1,2],[3,8,1,3],[4,8,3,1],[6,5,2,1],[7,3,1,2],[8,3,5,1],[12,2,1,1],[9,7,5,1],
                 [15,5,3,1],[17,2,1,4],[16,10,2,1],[17,9,1,1],[0,11,18,1]]
        return nList
        '''''
        self.rect_list = []
        for i in range(len(nlist)):
            self.rect_list.append(
                pygame.Rect(nlist[i][0] * 32, nlist[i][1] * 32, nlist[i][2] * 32, nlist[i][3] * 32))
        '''''