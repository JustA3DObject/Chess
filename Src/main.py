import pygame
import sys

from const import *
from game import Game

class Main:

    def __init__(self):
        # Initializing the pygame model
        pygame.init() 

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess")
        self.game = Game()

    def mainloop(self):
        # Setting up the pygame file
        while True:
            self.game.show_bg(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()

main = Main()
main.mainloop()