import include.Character
import include.rooms
import numpy as np

G = 10

WIDTH = 1000
HEIGHT = int(WIDTH * 2 / 3)


class physics:

    def __init__(self, p: include.Character.Player):
        self.p = p
        #self.m = m
        #, m: include.Character.Player
        self.in_air_time = 0

    def __in_air(self, lat, m: include.rooms.Room):
        h = self.p.status_avatar.get_height()
        w = self.p.status_avatar.get_width()
        # print((int((self.p.x + w)/WIDTH*18-1), (int((self.p.y + h)/HEIGHT*12))))
        if m.room_structure.get((int((self.p.x + w) / WIDTH * 18 - 1), (int((self.p.y + h) / HEIGHT * 12))), None):
            self.in_air_time = 0
        else:
            self.in_air_time += lat

    def side_by_side(self, m: include.rooms.Room) -> list:
        left_side_collide, right_side_collide = [False] * 2

        left_side = self.p.x
        right_side = self.p.x + self.p.w

        head = int((self.p.y / HEIGHT) * 12)
        left_side_block = int(left_side / WIDTH * 18)
        right_side_block = int(right_side / WIDTH * 18)

        # print(left_side_block, head, right_side_block)
        # print((right_side_block, head + 1))
        # print(m.room_structure.get((left_side_block, head), None) , m.room_structure.get(
        #         (left_side_block, head - 1),None) , m.room_structure.get((left_side_block, head - 2),None))
        # print(m.room_structure.get((right_side_block, head), None) , m.room_structure.get(
        #         (right_side_block, head - 1),None) , m.room_structure.get((right_side_block, head - 2),None))

        if m.room_structure.get((left_side_block, head), None) or m.room_structure.get(
                (left_side_block, head + 1), None):
            left_side_collide = True
        if m.room_structure.get((right_side_block, head), None) or m.room_structure.get(
                (right_side_block, head + 1), None):
            right_side_collide = True

        return [left_side_collide,right_side_collide]

    def head_by_head(self, m:include.rooms.Room):
        head = int((self.p.y / HEIGHT) * 12)
        left_side = self.p.x
        left_side_block = int(left_side / WIDTH * 18)

        head_collide = False

        if m.room_structure.get((left_side_block,head),None):
            head_collide = True

        return head_collide



    def physic_handling(self, latency: float, m: include.rooms.Room):
        self.__in_air(latency, m)
        return self.p.y + 0.25 * G * (self.in_air_time ** 2)
