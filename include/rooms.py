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
        1: np.array([[0 / 18, 3 / 12], [0 / 18, 4 / 12], [0 / 18, 5 / 12], [0 / 18, 11 / 12], [1 / 18, 3 / 12]])
    }


class Map:

    def __init__(self):
        map_list = []
