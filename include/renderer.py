import pygame


def render(surface, n: dict):
    for key, value in n.items():
        assert type(key) , \
            "The coordinate must be a tuple that looks like (x,y) where x,y is both int"
        surface.blit(value, key)

    return surface


def change_background():
    pass
