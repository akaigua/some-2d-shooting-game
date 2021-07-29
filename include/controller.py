import pygame


class input_handling:
    def __init__(self):
        self.left, self.right, self.up, self.attack, self.leave = [False] * 5
        self.stop_move_left = False
        self.stop_move_right = False

    def check_event(self):
        # we don't need these two lines
        # self.attack = False
        # self.stop_move_right,self.stop_move_right = [False] * 2

        for event in pygame.event.get():
            self.stop_move_right, self.stop_move_left = [False] * 2
            if event.type == pygame.QUIT:
                self.leave = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.leave = True
                if event.key == pygame.K_a:
                    self.left = True
                if event.key == pygame.K_d:
                    self.right = True
                if event.key == pygame.K_w:
                    self.up = True
                if event.key == pygame.K_j:
                    self.attack = True
            if event.type == pygame.KEYUP:
                # You don't need this
                # if event.key == pygame.K_ESCAPE:
                #     self.leave = False
                if event.key == pygame.K_a:
                    self.left = False
                    self.stop_move_left = True
                if event.key == pygame.K_d:
                    self.right = False
                    self.stop_move_right = True
                if event.key == pygame.K_w:
                    self.up = False
                    # self.stop_move = True

        return [self.left, self.right, self.up, self.attack, self.leave, self.stop_move_left, self.stop_move_right]
