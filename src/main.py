import pygame
import constants
from board import Board
from snake import Snake

pygame.init()
running = True

screen = pygame.display.set_mode((500, 500))
width = screen.get_width()
height = screen.get_height()

clock = pygame.time.Clock()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(constants.BORDER_COLOR)
    
    board = Board(screen)
    tiles = board.draw_board()
    
    snake = Snake(screen, tiles)
    snake.spawn()
    
    pygame.display.flip()
    clock.tick(60)
    

pygame.quit()