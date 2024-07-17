import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Racing Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Car settings
car_width = 50
car_height = 100
car_speed = 5

# Load car image
car_img = pygame.image.load('car1.png')
car_img = pygame.transform.scale(car_img, (car_width, car_height))

# Obstacle settings
obstacle_width = 50
obstacle_height = 100
obstacle_speed = 7

# Function to draw car
def draw_car(x, y):
    screen.blit(car_img, (x, y))

# Function to draw obstacles
def draw_obstacle(x, y):
    pygame.draw.rect(screen, red, [x, y, obstacle_width, obstacle_height])

# Main game loop
def game_loop():
    x = (screen_width * 0.45)
    y = (screen_height * 0.8)
    x_change = 0

    obstacle_startx = random.randrange(0, screen_width - obstacle_width)
    obstacle_starty = -600
    obstacle_speed = 7

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -car_speed
                elif event.key == pygame.K_RIGHT:
                    x_change = car_speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        screen.fill(white)

        draw_obstacle(obstacle_startx, obstacle_starty)
        obstacle_starty += obstacle_speed
        draw_car(x, y)

        if x > screen_width - car_width or x < 0:
            game_exit = True

        if obstacle_starty > screen_height:
            obstacle_starty = 0 - obstacle_height
            obstacle_startx = random.randrange(0, screen_width - obstacle_width)

        pygame.display.update()

    pygame.quit()
    quit()

game_loop()
