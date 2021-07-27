import pygame


def render(surface: pygame.display.set_mode(), n: dict):
    for key, value in n:
        assert type(key) == tuple and len(key) == 2 and type(key[0]) == int and type(key[1]) == int, \
            "The coordinate must be in a tuple that looks like (x,y) where x,y is both int"
        surface.blit(value, key)

    return surface


def change_background():
    pass
