import pygame
import math
import random

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Perlin Simulation")

WHITE = (255, 255, 255)
BLUE = (205, 255, 255)
COL = (150, 255, 255)

# Set colors
WHITE = (255, 255, 255)
BLUE = (205, 255, 255)
COL = (150, 255, 255)

# Generate Island
class IslandGenerator:
    noise_scale = 0.007
    pygame.init()

    # Perlin Noise
    def draw(win):
        win.fill(WHITE)
        noise_scale = 0.007
        def setup():
            size(800, 800)
            background(255, 255, 255)
            for x in range(1000):
                for y in range(1000):
                    n = noise(x * noise_scale, y * noise_scale)
                    if (n > 0.5):
                        stroke(204, 192, 155)
                    if (n > 0.54):
                        stroke(96, 117, 94)
                    if (n > 0.70):
                        stroke(255, 255, 255)
                    if (n < 0.5):
                        stroke(143, 196, 204)
                    if (n > 0.75):
                        stroke(150, 150, 150)
                    if (n > 0.4):
                        point(x, y)
        setup()
        pygame.display.update()

        # Pygame Window
        def main():
            run = True
            clock = pygame.time.Clock()
            WIN.fill(x, y)
            while run:
                clock.tick(60)
                draw(WIN)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
            pygame.quit()
        main()