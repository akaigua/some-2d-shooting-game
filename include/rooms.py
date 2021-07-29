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
