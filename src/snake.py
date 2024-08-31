import pygame
import constants

class Snake:
    def __init__(self, screen, tiles):
        self.screen = screen
        self.tiles = tiles
        
    def spawn(self):
        
        x_pos = constants.SNAKE_STARTING_POS_X
        y_pos = constants.SNAKE_STARTING_POS_Y
        offset = (constants.TILE_SIZE - constants.SNAKE_SIZE) // 2
        
        pygame.draw.rect(self.screen, constants.SNAKE_COLOR, [x_pos + offset, y_pos + offset, 13, 13])
        
        
    def move(self, direction):
        if direction == 0: pygame.draw.rect(self.screen, constants.SNAKE_COLOR, [240 + 3.5, 220 + 3.5, 13, 13])