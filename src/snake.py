import pygame
import constants

class Snake:
    def __init__(self, screen, tiles):
        self.screen = screen
        self.tiles = tiles
                
    def spawn(self, position):
        
        x_pos = position[0]
        y_pos = position[1]
        offset = (constants.TILE_SIZE - constants.SNAKE_SIZE) // 2
        
        pygame.draw.rect(self.screen, constants.SNAKE_COLOR, [x_pos + offset, y_pos + offset, 13, 13])
        
        
    def eat(self, position):
        self.spawn(self, position, )