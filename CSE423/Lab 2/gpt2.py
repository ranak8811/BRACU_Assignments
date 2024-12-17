from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math  # Importing math module for cos and sin

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Shooter settings
shooter_width = 50
shooter_height = 20
shooter_x = SCREEN_WIDTH // 2
shooter_y = 50
shooter_speed = 10

# Projectile settings
projectiles = []  # List of active projectiles
projectile_radius = 5
projectile_speed = 10

# Circle settings
circles = []  # List of falling circles
circle_radius = 20
circle_speed = 2

# Scoring and game state
score = 0
missed_circles = 0
max_misses = 3
game_over = False

# Initialize OpenGL
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

def draw_text(x, y, text):
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(char))

def draw_shooter():
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(shooter_x - shooter_width // 2, shooter_y)
    glVertex2f(shooter_x + shooter_width // 2, shooter_y)
    glVertex2f(shooter_x + shooter_width // 2, shooter_y + shooter_height)
    glVertex2f(shooter_x - shooter_width // 2, shooter_y + shooter_height)
    glEnd()

def draw_projectiles():
    glColor3f(1.0, 1.0, 0.0)
    for proj in projectiles:
        glBegin(GL_POLYGON)
        for angle in range(0, 360, 10):
            x = proj[0] + projectile_radius * math.cos(angle * math.pi / 180)
            y = proj[1] + projectile_radius * math.sin(angle * math.pi / 180)
            glVertex2f(x, y)
        glEnd()

def draw_circles():
    glColor3f(1.0, 0.0, 0.0)
    for circ in circles:
        glBegin(GL_POLYGON)
        for angle in range(0, 360, 10):
            x = circ[0] + circle_radius * math.cos(angle * math.pi / 180)
            y = circ[1] + circle_radius * math.sin(angle * math.pi / 180)
            glVertex2f(x, y)
        glEnd()

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

def spawn_circle():
    x = random.randint(circle_radius, SCREEN_WIDTH - circle_radius)
    circles.append([x, SCREEN_HEIGHT - circle_radius])

def update(value):
    global shooter_x, missed_circles, game_over

    if game_over:
        return

    # Move projectiles
    for proj in projectiles[:]:
        proj[1] += projectile_speed
        if proj[1] > SCREEN_HEIGHT:
            projectiles.remove(proj)

    # Move circles
    for circ in circles[:]:
        circ[1] -= circle_speed
        if circ[1] < 0:
            circles.remove(circ)
            missed_circles += 1

    # Check collisions
    check_collision()

    # Check for game over
    if missed_circles >= max_misses:
        game_over = True
        return

    # Spawn new circles
    if random.randint(1, 50) == 1:
        spawn_circle()

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw elements
    draw_shooter()
    draw_projectiles()
    draw_circles()

    # Display score and misses
    draw_text(10, SCREEN_HEIGHT - 20, f"Score: {score}")
    draw_text(10, SCREEN_HEIGHT - 40, f"Missed: {missed_circles}/{max_misses}")

    glFlush()

def keyboard(key, x, y):
    global shooter_x
    if key == b'a' and shooter_x - shooter_width // 2 > 0:
        shooter_x -= shooter_speed
    elif key == b'd' and shooter_x + shooter_width // 2 < SCREEN_WIDTH:
        shooter_x += shooter_speed
    elif key == b' ':
        projectiles.append([shooter_x, shooter_y + shooter_height])

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
    glutCreateWindow(b"Shoot The Circles!")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(16, update, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
