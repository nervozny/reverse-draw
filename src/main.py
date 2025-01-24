import pygame
from pygame.locals import QUIT

# Initialize pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Reversed Painting App")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)  # Marker color

# Set up variables
running = True
is_drawing = False  # Track if the user is holding down the mouse button
brush_size = 5

# Fill the background with white
screen.fill(WHITE)

# Variable to track the last position of the inverted mouse
last_pos = None

# Function to calculate the inverted position
def get_inverted_position(x, y):
    inverted_x = screen_width - x
    inverted_y = screen_height - y
    return inverted_x, inverted_y

# Create a separate surface to store the drawing
drawing_surface = screen.copy()

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            is_drawing = True  # Start drawing
            mouse_x, mouse_y = pygame.mouse.get_pos()
            last_pos = get_inverted_position(mouse_x, mouse_y)  # Capture the initial inverted position
        elif event.type == pygame.MOUSEBUTTONUP:
            is_drawing = False  # Stop drawing
            last_pos = None  # Reset the last position

    # Get the current mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    inverted_pos = get_inverted_position(mouse_x, mouse_y)

    # Draw if the user is holding down the mouse
    if is_drawing:
        if last_pos:  # Draw a line from the last inverted position to the current inverted position
            pygame.draw.line(drawing_surface, BLACK, last_pos, inverted_pos, brush_size)
        last_pos = inverted_pos  # Update the last inverted position

    # Redraw the drawing surface and the marker
    screen.blit(drawing_surface, (0, 0))  # Display the drawn lines
    pygame.draw.circle(screen, RED, inverted_pos, 5)  # Draw the marker

    # Update the display
    pygame.display.flip()

pygame.quit()
