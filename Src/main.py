import pygame
import sys

from const import *

class Main:

    def __init__(self):
        # Initializing the pygame model
        pygame.init() 

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess")

    def mainloop(self):
        # Setting up the pygame file
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()

main = Main()
main.mainloop()