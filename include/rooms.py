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