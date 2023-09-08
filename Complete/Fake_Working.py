import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
FONT_SIZE = 20
FONT_COLOR = (0, 255, 0)  # Green color

# Create the Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Real-Time Typing Code for 5 Minutes")

# Create a font
font = pygame.font.Font(None, FONT_SIZE)

# Simulated code snippet
code_snippet = """
for i in range(100):
    print("This is a long and difficult code snippet.")
"""

# Calculate the number of times to repeat the code to fill 5 minutes
start_time = time.time()
total_duration = 5 * 60  # 5 minutes in seconds
code_repeats = int(total_duration / len(code_snippet)) + 1

# Text position
x, y = 20, 20

# Clock to control frame rate
clock = pygame.time.Clock()

running = True
current_repeat = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a black background
    screen.fill((0, 0, 0))

    # Render the code snippet being typed
    current_code = code_snippet * (current_repeat + 1)
    text_surface = font.render(current_code, True, FONT_COLOR)
    screen.blit(text_surface, (x, y))

    pygame.display.flip()

    # Control the typing speed
    pygame.time.delay(100)  # Adjust the value to control the typing speed

    current_time = time.time()
    elapsed_time = current_time - start_time

    # Check if 5 minutes have elapsed
    if elapsed_time >= total_duration:
        break

    # Increment the repeat count
    current_repeat += 1

# Quit Pygame
pygame.quit()
sys.exit()
