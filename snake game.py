import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set up display
width = 640
height = 480
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (213, 50, 80)
blue = (50, 153, 213)

# Set up game clock
clock = pygame.time.Clock()

# Define snake block size and speed
snake_block = 30
snake_speed = 10

# Font for the score
font_style = pygame.font.SysFont("bahnschrift", 25)

# Score function
def your_score(score):
    value = font_style.render("Your Score: " + str(score), True, black)
    game_window.blit(value, [0, 0])

# Snake function
def our_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(game_window, green, [x[0], x[1], snake_block, snake_block])

# Message function
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [width / 6, height / 3])

# Main game function
def gameLoop():
    game_over = False
    game_close = False

    # Initial snake position
    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Initial food position
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_window.fill(blue)
            message("You Lost! Press E-exit or P-Play Again", yellow)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        game_window.fill(blue)
        pygame.draw.rect(game_window, white, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
gameLoop()
