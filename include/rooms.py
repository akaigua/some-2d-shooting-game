from typing import *
import random
import pygame
import os


class Room:
    connections = {}


class FightRoom(Room):
    pass


class PuzzleRoom(Room):
    pass


class BossRoom(Room):
    pass


class MiniBoss(BossRoom):
    pass


class Map:
    direction = ["e", "s", "w", "n"]


    def __init__(self, r=10):
        self.room_numbers = r
        self.available_rooms = {PuzzleRoom: random.randint(1, int(self.room_numbers / 3)),
                                MiniBoss: random.randint(1, int(self.room_numbers / 3)), FightRoom: 0, BossRoom: 1}
        self.available_rooms[FightRoom] = 10 - self.available_rooms[BossRoom] - self.available_rooms[PuzzleRoom] - \
                                          self.available_rooms[MiniBoss]
        self.steps = 0

    def enter_room(self):
        self.steps += 1
        for keys, values in self.available_rooms:
            if values == 0:
                del self.available_rooms[keys]

        current_room = self.available_rooms[
            list(self.available_rooms.keys())[random.randint(0, len(list(iter(self.available_rooms))) - 1)]]
        self.available_rooms[current_room] -= 1

        return current_room

    def new_room(self):
        return Room
