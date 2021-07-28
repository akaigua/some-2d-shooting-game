import pygame


def check_event():
    left, right, up, down, attack, leave = [False] * 6

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
            if event.key == pygame.K_w:
                up = True
            if event.key == pygame.K_s:
                down = True

    return [left, right, up, down, attack, leave]