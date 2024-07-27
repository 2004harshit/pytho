import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Set up initial conditions
x, y = width // 4, height // 4
speed_x, speed_y = 5, 5
radius = 100

# Main animation loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the position
    x += speed_x
    y += speed_y

    # Bounce off the edges
    if x - radius < 0 or x + radius > width:
        speed_x = -speed_x
    if y - radius < 0 or y + radius > height:
        speed_y = -speed_y

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the circle
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(1000)
