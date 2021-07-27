import pygame
import include.controller
import include.rooms
import include.renderer

width = 1024
length = 768


def main():
    pygame.init()
    surface = pygame.display.set_mode((width, length))
    pygame.display.set_caption("Some 2D Shooting Game")

    while True:
        left, right, up, down, attack, leave = include.controller.check_event()


if __name__ == '__main__':
    main()
