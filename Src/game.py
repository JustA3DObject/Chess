import itertools
import pygame

from const import *

class Game:

    def __init__(self):
        pass

    # Show methods
    
    def show_bg(self, surface):
        for row, col in itertools.product(range(ROWS), range(COLS)):
+            color = (234, 235, 200) if (row+col)%2 == 0 else (119, 154, 88)
+            rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
 
+            pygame.draw.rect(surface, color, rect)
