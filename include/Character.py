import pygame
# import rooms
import time
# import renderer
import random


# from PIL import Image
# size = Image.open().size


class Player(pygame.sprite.Sprite):
    """the characteristic of character
        speed in x,speed in y,the acceleration of speed in x,the acceleration of speed in y,health point,its strength"""

    def __init__(self, speedx, speedy, hp, strength, x, y):
        self.image = pygame.image.load("some-2d-shooting-game/image/螳螂右 end.png").convert_alpha()  # the image of player
        self.rect = self.image.get_rect()
        self.w, self.h = pygame.image.load("some-2d-shooting-game/image/螳螂右 end.png").get_rect().size
        self.speedx = speedx
        self.speedy = speedy
        self.hp = hp
        self.M = Monster()
        self.strength = strength
        self.SCREEN_W = 1024
        self.SCREEN_H = 768
        self.x = x
        self.y = y

    def move(self, left, right, up):
        if left:
            self.x -= self.speedx
        elif right:
            self.x += self.speedx
        elif up:
            self.y = self.speedy
        else:
            self.x = 0
            self.y = -self.speedy

        if self.x + self.w > self.SCREEN_W:
            self.x = self.SCREEN_W

        if self.x - self.w < 0:
            self.x = 0

        if self.y + self.h > self.SCREEN_H:
            self.y = self.SCREEN_H

        if self.y - self.h < 0:
            self.y = 0

    def attack(self, attack):
        if attack:
            if abs(self.x - self.M.x) < 25:
                self.M.hp -= self.strength
                time.sleep(round(random.uniform(0.5, 0.8), 3))

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


class Monster(pygame.sprite.Sprite):
    def __init__(pic, self, x, y, speedx, speedy, hp, strength):
        # The monster would attack the player if their distance is too close or the player has alraedy attack him.
        '''''
        Monsters would go towards the player when they are in the same layer. 
        They also go back and forthin their platform.
        ## If the player is shooting at them more than three times, they would go towards the player together.
        The player won't be allowed to go through the door without shooting all of the monsters.
        '''''
        self.image = pygame.image.load(pic).convert_alpha()  # the image of player
        self.rect = self.image.get_rect()
        self.w, self.h = pygame.image.load().get_rect().size
        self.x, self.y = x, y
        self.P = Player()
        # self.P.x, self.P.y
        self.speedx = speedx
        self.speedy = speedy
        self.hp = hp
        self.strength = strength

    def move(self):
        if self.hp <= 50 or abs(self.y - self.P.y) < 40:
            # 怪物被激怒的时候的反应
            if self.x - self.P.x < 0:
                self.speedx += 0.5
            elif self.x - self.P.x > 0:
                self.speedx -= 0.5
            else:
                self.speedx == 0
        else:
            # 怪物日常巡游（划水）
            self.speedx = 2
            r, l = Monster.collide(self)
            if r == False or l == False:
                self.speedx *= -1

    def collide(self):
        r, l = True, True
        if self.x + self.w > self.SCREEN_W:
            self.x = self.SCREEN_W
            return False
        if self.x - self.w < 0:
            self.x = 0
            return False

        if self.y + self.h > self.SCREEN_H:
            self.y = self.SCREEN_H
        if self.y - self.h < 0:
            self.y = 0

        return r, l

    def damage(self):
        if abs(self.x - self.P.x) < 25:
            self.P.hp -= self.strength
            time.sleep(round(random.uniform(0.7, 1), 3))

    '''''
    def dead(self):
        if self.hp <= 0:
            return 'dead'
        else:
            return 'live'
    '''''

    def draw(self, surface):
        # renderer((self.x, self.y), )
        surface.blit(self.image, (self.x, self.y))


def check_event():
    left, right, up, attack, leave = [False] * 6

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            leave = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                leave = True
            if event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_d:
                right = True
            if event.key == pygame.K_SPACE:
                up = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                leave = False
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_d:
                right = False
            if event.key == pygame.K_SPACE:
                up = False

    return [left, right, up, attack, leave]

    # ------------------


SCREEN_W = 1024
SCREEN_H = 768


def main():
    pygame.init()
    surface = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Some 2D Shooting Game")

    while True:
        left, right, jump, attack, leave = check_event()


if __name__ == '__main__':
    main()
