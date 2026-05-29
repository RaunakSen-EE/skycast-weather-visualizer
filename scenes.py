import pygame
import sys
import random
import math

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SkyCast")

clock = pygame.time.Clock()

BLUE = (135, 206, 235)
YELLOW = (255, 223, 0)
GREEN = (34, 139, 34)

GRAY = (120, 120, 120)
DARK_BLUE = (70, 70, 120)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("Arial", 40)

# GRAPH LOADER FUNCTION

def draw_graph():

    try:

        graph = pygame.image.load("temp_graph.png")

        # resized graph nicely
        graph = pygame.transform.scale(graph, (320, 220))

        # displayed graph
        screen.blit(graph, (20, 340))

    except:
        pass


# SUNNY SCENE

sun_angle = 0

def draw_sunny_scene():

    global sun_angle

    running = True

    while running:

        screen.fill(BLUE)

        # Animated sun pulse
        radius = 60 + int(5 * math.sin(sun_angle))

        pygame.draw.circle(screen, YELLOW, (650, 100), radius)

        sun_angle += 0.05

        # Ground
        pygame.draw.rect(screen, GREEN, (0, 500, 800, 100))

        # Title
        text = font.render("Sunny Weather ☀️", True, BLACK)
        screen.blit(text, (20, 20))

        # analytics panel
        
        analytics = pygame.font.SysFont("Arial", 24)

        panel = analytics.render(
            "Analytics Dashboard 📊",
            True,
            BLACK
        )

        screen.blit(panel, (20, 300))

        # graph of display
        
        draw_graph()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()


# RAINY SCENE

def draw_rainy_scene():

    rain_drops = []

    for i in range(250):

        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)

        speed = random.randint(6, 12)

        rain_drops.append([x, y, speed])

    cloud_x = 0

    running = True

    while running:

        screen.fill(DARK_BLUE)

        # Moving clouds
        pygame.draw.circle(screen, GRAY, (200 + cloud_x, 100), 50)
        pygame.draw.circle(screen, GRAY, (260 + cloud_x, 100), 60)
        pygame.draw.circle(screen, GRAY, (320 + cloud_x, 100), 50)

        cloud_x += 1

        if cloud_x > WIDTH:
            cloud_x = -400

        # Rain animation
        for drop in rain_drops:

            pygame.draw.line(
                screen,
                WHITE,
                (drop[0], drop[1]),
                (drop[0], drop[1] + 12),
                2
            )

            drop[1] += drop[2]

            if drop[1] > HEIGHT:

                drop[0] = random.randint(0, WIDTH)
                drop[1] = 0

        # Ground
        pygame.draw.rect(screen, GREEN, (0, 500, 800, 100))

        # Title
        text = font.render("Rainy Weather 🌧️", True, WHITE)
        screen.blit(text, (20, 20))

        # analytics panel
        
        analytics = pygame.font.SysFont("Arial", 24)

        panel = analytics.render(
            "Analytics Dashboard 📊",
            True,
            WHITE
        )

        screen.blit(panel, (20, 300))

        # graph of display
        
        draw_graph()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()


# CLOUDY SCENE


def draw_cloudy_scene():

    cloud_x = 0

    running = True

    while running:

        screen.fill((180, 180, 180))

        # Moving clouds
        for i in range(3):

            pygame.draw.circle(
                screen,
                WHITE,
                (150 + cloud_x + (i * 220), 120),
                50
            )

            pygame.draw.circle(
                screen,
                WHITE,
                (200 + cloud_x + (i * 220), 100),
                60
            )

        cloud_x += 1

        if cloud_x > WIDTH:
            cloud_x = -300

        # Ground
        pygame.draw.rect(screen, GREEN, (0, 500, 800, 100))

        # Title
        text = font.render("Cloudy Weather ☁️", True, BLACK)
        screen.blit(text, (20, 20))

        # analytics panel
        
        analytics = pygame.font.SysFont("Arial", 24)

        panel = analytics.render(
            "Analytics Dashboard 📊",
            True,
            BLACK
        )

        screen.blit(panel, (20, 300))

        # graph of display
        
        draw_graph()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()


# THUNDERSTORM SCENE


def draw_thunder_scene():

    flash_timer = 0

    running = True

    while running:

        flash_timer += 1

        # Flash effect
        if flash_timer % 40 < 5:
            screen.fill(WHITE)
        else:
            screen.fill((30, 30, 50))

        # Lightning
        pygame.draw.line(screen, YELLOW, (400, 100), (350, 250), 6)
        pygame.draw.line(screen, YELLOW, (350, 250), (430, 420), 6)

        # Clouds
        pygame.draw.circle(screen, GRAY, (250, 100), 60)
        pygame.draw.circle(screen, GRAY, (320, 100), 70)
        pygame.draw.circle(screen, GRAY, (390, 100), 60)

        # Ground
        pygame.draw.rect(screen, GREEN, (0, 500, 800, 100))

        # Title
        text = font.render("Thunderstorm 🌩️", True, WHITE)
        screen.blit(text, (20, 20))

        # analytics panel
        

        analytics = pygame.font.SysFont("Arial", 24)

        panel = analytics.render(
            "Analytics Dashboard 📊",
            True,
            WHITE
        )

        screen.blit(panel, (20, 300))

        # graph of display
        
        draw_graph()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()