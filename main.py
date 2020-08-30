import pygame
import neat
import time
import os
import random

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800


def loadimage(fileName):
    return pygame.transform.scale2x(pygame.image.load(os.path.join("assets", fileName)))


BIRD_IMGS = [
    loadImage("bird1.png"),
    loadImage("bird2.png"),
    loadImage("bird3.png")]

PIPE_IMG = loadImage("pipe.png")

BASE_IMG = loadImage("base.png")

BG_IMG = loadImage("bg.png")
