import pygame
import time
import random
import include.rooms.Room


# from PIL import Image
# size = Image.open().size


class Player(pygame.sprite.Sprite):
    """the characteristic of character
        speed in x,speed in y,the acceleration of speed in x,the acceleration of speed in y,health point,its strength"""

    def __init__(self, mx, Mhp, max_hp, strength):  # Mx is the x value of the Monster
        self.stand_right = pygame.image.load(
            "./assets/character_file_compressed/stand_right.png").convert_alpha()  # image of the player
        self.stand_left = pygame.image.load(
            "./assets/character_file_compressed/stand_left.png").convert_alpha()  
        self.move_left = pygame.image.load(
            "./assets/character_file_compressed/move_left.png").convert_alpha()
        self.move_right = pygame.image.load(
            "./assets/character_file_compressed/move_right.png").convert_alpha()
        self.status_avatar = self.stand_right
        # rect.center need to be updated
        self.w, self.h = pygame.image.load("./assets/character_file_compressed/stand_right.png").get_rect().size
        self.SCREEN_W = 1000
        self.SCREEN_H = int(self.SCREEN_W * 2 / 3)
        self.x = 0
        self.y = self.SCREEN_H - self.h - 53
        self.rect = self.stand_right.get_rect()
        pygame.Rect.move_ip(self.rect, self.x, self.y)
        print(self.rect)
        self.speedx = 5
        self.speedy = 5
        self.hp = max_hp
        self.Mhp = Mhp
        self.distance = self.x - mx
        self.strength = strength

    def move(self, left, right, up):
        #while self.collision()
        if self.x + self.w - 40 > self.SCREEN_W:
            right = False

        if self.x + 24 < 0:
            left = False

        if self.y < 0:
            up = False

        # for testing
        if self.y > self.SCREEN_H:
            self.y = 100
        #for testing

        if left:
            self.x -= self.speedx
        if right:
            self.x += self.speedx
        if up:
            self.y -= self.speedy
        
            # self.y = -self.speedy
                
    def display_direction(self,left, right, up, stop_move_left, stop_move_right):
        if left:
            self.status_avatar = self.move_left
            return True
            # towards the right
        if right:
            self.status_avatar = self.move_right
            return False
            # towards the left
        if stop_move_right:
            self.status_avatar = self.stand_left
        if stop_move_left:
            self.status_avatar = self.stand_right

    def attack(self, attack):
        if attack:
            if abs(self.distance) < 25:
                self.Mhp -= self.strength
                #time.sleep(round(random.uniform(0.5, 0.8), 3))

    def update(self, Mx, Mhp):
        self.distance = self.x - Mx
        Mhp = Mhp

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))



class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, Px, Php, speedx, hp, strength):
        # The monster would attack the player if their distance is too close or the player has alraedy attack him.
        
        # Monsters would go towards the player when they are in the same layer. 
        #They also go back and forthin their platform.
        ## If the player is shooting at them more than three times, they would go towards the player together.
        #The player won't be allowed to go through the door without shooting all of the monsters.
        
        self.stand_right = pygame.image.load(
            "./assets/character_file_compressed/Monster1_stand_right.png").convert_alpha()  # the image of player
        self.stand_left = pygame.image.load(
            "./assets/character_file_compressed/Monster1_stand_left.png").convert_alpha()  # the image of player
        self.move_left = pygame.image.load(
            "./assets/character_file_compressed/Monster1_move_left.png").convert_alpha()
        self.move_right = pygame.image.load(
            "./assets/character_file_compressed/Monster1_move_right.png").convert_alpha()
        self.status_avatar = self.stand_right  # the image of Monster

        self.rect = self.image.get_rect()
        self.w, self.h = self.stand_left.get_rect().size
        self.x, self.y = x, y
        self.distance = self.x - Px
        self.Php = Php
        self.speedx = speedx
        self.speedy = 0
        self.hp = hp
        self.strength = strength

    def move(self):
        if self.hp <= 50 or abs(self.distance) < 40:
            # when the monster is angery
            if self.distance >= 0:
                self.speedx += 0.5
            elif self.distance < 0:
                self.speedx -= 0.5
            else:
                self.speedx == 0
            # walk back and forth when he's peace

    def display_direction(self):
        # lack of photo now
        if self.speedX >= 0:
            if self.speed == 0:
                self.status_avatar = self.stand_right
            else:
                self.status_avatar = self.move_right
            return True
            # towards the right
        elif self.speedX < 0:
            if self.speed == 0:
                self.status_avatar = self.stand_left
            else:
                self.status_avatar = self.move_left
            return False 
            # towards the left

    def update(self, Px, Php):
        self.distance = self.x - Px
        self.Php = Php

    def collide(self, m: include.rooms.Room):
        WIDTH = 1000
        HEIGHT = int(WIDTH * 2 / 3)
        h = self.status_avatar.get_height()
        w = self.status_avatar.get_width()

        if self.x + self.w - 40 > self.SCREEN_W:
            self.speedx *= -1

        if self.x + 24 < 0:
            self.speedx *= -1

        if m.room_structure.get((int((self.c.x + w) / WIDTH * 18 - 1), (int((self.c.y + h) / HEIGHT * 12))), None) == False:
            self.speedx *= -1

        #if self.y < 0:
            #self.
        
    def damage(self):
        if abs(self.distance) < 25:
            self.Php -= self.strength
            # time.sleep(round(random.uniform(0.7, 1), 3))
        

    def draw(self, surface):
        # renderer((self.x, self.y), )
        surface.blit(self.image, (self.x, self.y))




