import pygame
import cv2
from pygame.locals import *
import numpy as np


class Display(object):
    def __init__(self, W=1920 // 2, H=1080 // 2):

        pygame.init()
        self.screen = pygame.display.set_mode((W, H))
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)

        self.W, self.H = W, H

    def paint(self, img):
        """ Display a numpy image on the pygame window"""
        #print(type(img), img.shape, img)
        self.screen.fill([0, 0, 0])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = np.rot90(img)
        surf = pygame.surfarray.make_surface(img)  # .convert()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
        self.screen.blit(surf, (0, 0))
        pygame.display.update()
        # pygame.quit()
        # print(img.shape)
