import pygame
from pygame.locals import QUIT

# Initialize pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Painting App")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up variables
running = True
is_drawing = False  # Track if the user is holding down the mouse button
brush_size = 5

# Fill the background with white
screen.fill(WHITE)

# Variable to track the last position of the mouse
last_pos = None

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            is_drawing = True  # Start drawing
            last_pos = pygame.mouse.get_pos()  # Capture the initial position
        elif event.type == pygame.MOUSEBUTTONUP:
            is_drawing = False  # Stop drawing
            last_pos = None  # Reset the last position

    # Draw if the user is holding down the mouse
    if is_drawing:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if last_pos:  # Draw a line from the last position to the current position
            pygame.draw.line(screen, BLACK, last_pos, (mouse_x, mouse_y), brush_size)
        last_pos = (mouse_x, mouse_y)  # Update the last position

    # Update the display
    pygame.display.flip()

pygame.quit()
