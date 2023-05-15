import os
from turtle import delay

from scripts.characters.Ball import Ball, BallType
from scripts.utils.Vector import Vector
from scripts.utils.Window import Window
from scripts.utils.Dimension import Dimension

import pygame


def run():
    pygame.init()
    windows = Window(pygame, "Galaxy Bricker", Dimension(780, 600))

    ball1 = Ball(Vector(0, 0), Dimension(15, 15))
    ball1.select_ball(BallType.basic_white)
    ball1.set_speed(0.1, 0.1)

    ball2 = Ball(Vector(0, 100), Dimension(10, 10))
    ball2.select_ball(BallType.basic_white)
    ball2.set_speed(0.1, 0.0)

    ball3 = Ball(Vector(0, 300), Dimension(20, 20))
    ball3.select_ball(BallType.basic_white)
    ball3.set_speed(0.1, 0.0)

    windows.add_element(ball1, ball2, ball3)

    game_is_active = True
    while game_is_active:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_is_active = False

        windows.update()

    pygame.quit()
