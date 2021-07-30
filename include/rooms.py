from typing import *
import random
import pygame
import os
import numpy as np

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


class Map:

    def __init__(self):
        map_list = []
        self.rect_list = []

    def map_1(self):
        nList = [[0, 3 / 12, 3 / 18, 1 / 12], [0, 4 / 12, 1 / 18, 2 / 12], [6 / 18, 4 / 12, 3 / 18, 1 / 12],
                 [8 / 18, 5 / 12, 1 / 18, 6 / 12], [17 / 18, 9 / 12, 1 / 18, 1 / 12],
                 [16 / 18, 11 / 12, 2 / 18, 1 / 12], [0, 11 / 12, 18 / 18, 1 / 12], [3 / 18, 7 / 12, 3 / 18, 1 / 12],
                 [12 / 18, 7 / 12, 4 / 18, 1 / 12], [11 / 18, 1 / 12, 1 / 18, 3 / 12],
                 [12 / 18, 3 / 12, 3 / 18, 1 / 12]]
        self.rect_list = []
        for i in range(len(nList)):
            self.rect_list.append(pygame.Rect(nList[i][0] * 576, nList[i][1] * 384, nList[i][2] * 576, nList[i][3] * 384))

    def map_2(self):
        nlist = [[0,0,2,1],[0,1,1,1],[0,5,2,1],[0,6,1,1],[4,3,7,1],[3,8,1,3],[4,8,2,1],[5,6,1,2],[8,7,5,1],[10,8,1,1],
                 [13,0,1,4],[14,3,2,1],[15,6,3,1],[17,7,1,4],[14,9,2,1],[0,11,18,1]]
        self.rect_list = []
        for i in range(len(nlist)):
            self.rect_list.append(
                pygame.Rect(nlist[i][0] * 32, nlist[i][1] * 32, nlist[i][2] * 32, nlist[i][3] * 32))

    def map_3(self):
        nlist = [[0,0,1,3],[1,2,3,1],[0,5,1,2],[3,8,1,3],[4,8,3,1],[6,5,2,1],[7,3,1,2],[8,3,5,1],[12,2,1,1],[9,7,5,1],
                 [15,5,3,1],[17,2,1,4],[16,10,2,1],[17,9,1,1],[0,11,18,1]]
        self.rect_list = []
        for i in range(len(nlist)):
            self.rect_list.append(
                pygame.Rect(nlist[i][0] * 32, nlist[i][1] * 32, nlist[i][2] * 32, nlist[i][3] * 32))