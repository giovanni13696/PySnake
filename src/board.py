import pygame
import constants

class Board:
    def __init__(self, screen):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.tiles = []
    
    def draw_board(self): 
        
        border_padding = constants.BORDER_PADDING
        tile_spacing = constants.TILE_SPACING
        tile_size = constants.TILE_SIZE
        
        tile_count = 0
        self.tiles.clear()
        
        for x_pos in range(border_padding, self.width - border_padding, tile_size):
            row = []
            for y_pos in range(border_padding, self.height - border_padding, tile_size):
                tile_count += 1
                if tile_count % 2 == 0: color = constants.ODD_TILE_COLOR
                else: color = constants.EVEN_TILE_COLOR
                
                row.append(pygame.draw.rect(self.screen, color, [x_pos, y_pos, tile_size, tile_size]))
            self.tiles.append(row)
        return self.tiles