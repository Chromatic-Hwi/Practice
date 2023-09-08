import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
FONT_SIZE = 20
FONT_COLOR = (0, 255, 0)  # Green color

# Create the Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix Rain")

# Create a font
font = pygame.font.Font(None, FONT_SIZE)

# Characters to display
characters = [chr(i) for i in range(33, 127)]  # ASCII characters from '!' to '~'

# Create a list of raindrops
raindrops = []

for _ in range(100):  # Adjust the number of raindrops
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    speed = random.randint(5, 20)
    raindrops.append([x, y, speed])

# Clock to control frame rate
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a black background
    screen.fill((0, 0, 0))

    for drop in raindrops:
        x, y, speed = drop
        text = random.choice(characters)
        text_surface = font.render(text, True, FONT_COLOR)
        screen.blit(text_surface, (x, y))

        # Move the raindrop down
        drop[1] += speed

        # Reset the raindrop when it goes off the screen
        if drop[1] > HEIGHT:
            drop[1] = 0
            drop[0] = random.randint(0, WIDTH)

    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)  # Adjust the value to control the speed of the rain

# Quit Pygame
pygame.quit()
sys.exit()
