import pygame
import math

pygame.init()

# Init pygame
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Perlin Simulation")

# Set colors
WHITE = (255, 255, 255)
BLUE = (205, 255, 255)
COL = (150, 255, 255)

def draw(win):
    def draw(win):
    win.fill(WHITE)
    pygame.display.update()
    noise_scale = 0.007
    def setup():
        background(255, 255, 255)
        for x in range(800):
            for y in range(800):
                stroke(0, 0, 0, 255.0 * noise(x * noise_scale, y * noise_scale))
                point(x, y)
    def draw():
        setup()
    draw()

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        draw(WIN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()
main()