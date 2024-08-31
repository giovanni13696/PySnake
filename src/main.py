import pygame, random
import constants
from board import Board
from snake import Snake

pygame.init()

direction = None
running = True
eaten = True

move_delay = 10
move_counter = 0 

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("PySnake")
width = screen.get_width()
height = screen.get_height()

snake_x_pos = constants.SNAKE_STARTING_POS_X
snake_y_pos = constants.SNAKE_STARTING_POS_Y

clock = pygame.time.Clock()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(constants.BORDER_COLOR)
    
    board = Board(screen)
    tiles = board.draw_board()
    snake = Snake(screen, tiles)
    
    if eaten:
        apple_tile = board.get_random_tile()
        
        apple_center_x = apple_tile.x + constants.TILE_SIZE // 2
        apple_center_y = apple_tile.y + constants.TILE_SIZE // 2
        
        eaten = False
        
    pygame.draw.circle(screen, (0,0,0), (apple_center_x, apple_center_y), 5)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != 'DOWN':
        direction = 'UP'
    elif keys[pygame.K_DOWN] and direction != 'UP':
        direction = 'DOWN'
    elif keys[pygame.K_RIGHT] and direction != 'LEFT':
        direction = 'RIGHT'
    elif keys[pygame.K_LEFT] and direction != 'RIGHT':
        direction = 'LEFT'

    if move_counter >= move_delay:
        if direction == 'UP':
            snake_y_pos -= 20
        elif direction == 'DOWN':
            snake_y_pos += 20
        elif direction == 'RIGHT':
            snake_x_pos += 20
        elif direction == 'LEFT':
            snake_x_pos -= 20
        move_counter = 0
    else:
        move_counter += 1
        
    if snake_x_pos <= 460:
        snake.spawn((snake_x_pos, snake_y_pos))
    elif snake_x_pos > 460:
        print("Dead")
        
    if snake_x_pos == apple_tile.x and snake_y_pos == apple_tile.y:
        eaten = True
    
    pygame.display.flip()
    clock.tick(60)
    

pygame.quit()