import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shoot The Circles!")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Shooter settings
shooter_width = 50
shooter_height = 20
shooter_x = SCREEN_WIDTH // 2 - shooter_width // 2
shooter_y = SCREEN_HEIGHT - 50
shooter_speed = 5

# Projectile settings
projectiles = []  # List of active projectiles
projectile_radius = 5
projectile_speed = -7

# Circle settings
circles = []  # List of falling circles
circle_radius = 20
circle_speed = 3

# Scoring and game state
score = 0
missed_circles = 0
max_misses = 3
game_over = False

# Fonts
font = pygame.font.Font(None, 36)

def draw_text(text, x, y, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw_shooter():
    pygame.draw.rect(screen, BLUE, (shooter_x, shooter_y, shooter_width, shooter_height))

def draw_projectiles():
    for proj in projectiles:
        pygame.draw.circle(screen, YELLOW, (proj[0], proj[1]), projectile_radius)

def draw_circles():
    for circ in circles:
        pygame.draw.circle(screen, RED, (circ[0], circ[1]), circle_radius)

def check_collision():
    global score
    for proj in projectiles[:]:
        for circ in circles[:]:
            distance = ((proj[0] - circ[0])**2 + (proj[1] - circ[1])**2)**0.5
            if distance < projectile_radius + circle_radius:
                projectiles.remove(proj)
                circles.remove(circ)
                score += 1
                break

def game_loop():
    global shooter_x, missed_circles, game_over

    # Main game loop
    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and shooter_x > 0:
            shooter_x -= shooter_speed
        if keys[pygame.K_d] and shooter_x < SCREEN_WIDTH - shooter_width:
            shooter_x += shooter_speed
        if keys[pygame.K_SPACE]:
            if len(projectiles) < 5:  # Limit the number of active projectiles
                projectiles.append([shooter_x + shooter_width // 2, shooter_y])

        # Update projectiles
        for proj in projectiles[:]:
            proj[1] += projectile_speed
            if proj[1] < 0:
                projectiles.remove(proj)

        # Spawn circles
        if random.randint(1, 50) == 1:  # Adjust spawn rate
            x = random.randint(circle_radius, SCREEN_WIDTH - circle_radius)
            circles.append([x, 0])

        # Update circles
        for circ in circles[:]:
            circ[1] += circle_speed
            if circ[1] > SCREEN_HEIGHT:
                circles.remove(circ)
                missed_circles += 1

        # Check collisions
        check_collision()

        # Draw everything
        draw_shooter()
        draw_projectiles()
        draw_circles()

        # Display score and misses
        draw_text(f"Score: {score}", 10, 10, WHITE)
        draw_text(f"Missed: {missed_circles}/{max_misses}", 10, 40, WHITE)

        # Check for game over
        if missed_circles >= max_misses:
            game_over = True
            running = False

        # Update display
        pygame.display.flip()

        # Control frame rate
        clock.tick(60)

    # Game over screen
    screen.fill(BLACK)
    draw_text("GAME OVER", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, RED)
    draw_text(f"Final Score: {score}", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, WHITE)
    pygame.display.flip()
    pygame.time.wait(3000)

# Run the game
game_loop()
