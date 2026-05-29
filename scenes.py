import pygame
import sys
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SkyCast")

# Colors
BLUE = (135, 206, 235)
YELLOW = (255, 223, 0)
GREEN = (34, 139, 34)

GRAY = (120, 120, 120)
DARK_BLUE = (70, 70, 120)

WHITE = (255, 255, 255)

# ---------------- SUNNY ---------------- #

def draw_sunny_scene():

    running = True

    while running:

        screen.fill(BLUE)

        # Sun
        pygame.draw.circle(screen, YELLOW, (650, 100), 60)

        # Ground
        pygame.draw.rect(screen, GREEN, (0, 500, 800, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
    sys.exit()


# ---------------- RAINY ---------------- #

def draw_rainy_scene():

    rain_drops = []

    for i in range(200):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)

        rain_drops.append([x, y])

    running = True

    while running:

        screen.fill(DARK_BLUE)

        # Clouds
        pygame.draw.circle(screen, GRAY, (200, 100), 50)
        pygame.draw.circle(screen, GRAY, (260, 100), 60)
        pygame.draw.circle(screen, GRAY, (320, 100), 50)

        # Rain animation
        for drop in rain_drops:

            pygame.draw.line(
                screen,
                WHITE,
                (drop[0], drop[1]),
                (drop[0], drop[1] + 10),
                2
            )

            drop[1] += 8

            if drop[1] > HEIGHT:
                drop[1] = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
    sys.exit()