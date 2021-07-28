import pygame


class input_handling:
    def __init__(self):
        self.left, self.right, self.up, self.attack, self.leave = [False] * 5

    def check_event(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.leave = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.leave = True
                if event.key == pygame.K_a:
                    self.left = True
                if event.key == pygame.K_d:
                    self.right = True
                if event.key == pygame.K_SPACE:
                    self.up = True
            if event.type == pygame.KEYUP:
                # You don't need this
                # if event.key == pygame.K_ESCAPE:
                #     self.leave = False
                if event.key == pygame.K_a:
                    self.left = False
                if event.key == pygame.K_d:
                    self.right = False
                if event.key == pygame.K_SPACE:
                    self.up = False
        
        return [self.left, self.right, self.up, self.attack, self.leave]
