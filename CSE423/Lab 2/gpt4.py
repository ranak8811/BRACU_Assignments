from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math
import time

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
circle_speed = 5
unique_circle_flag = False

# Scoring and game state
score = 0
missed_circles = 0
misfires = 0
max_misses = 3
game_over = False
paused = False
start_time = time.time()

# Midpoint Algorithm Functions

def MidPointLine(zone, x1, y1, x2, y2):
    dx = (x2 - x1)
    dy = (y2 - y1)
    x = x1
    y = y1

    dInitial = 2 * dy - dx

    Del_E = 2 * dy
    Del_NE = 2 * (dy - dx)

    while x <= x2:
        a, b = ConvertToOriginal(zone, x, y)
        draw_points(a, b)

        if dInitial <= 0:
            x = x + 1
            dInitial = dInitial + Del_E
        else:
            x = x + 1
            y = y + 1
            dInitial = dInitial + Del_NE

def FindZone(x1, y1, x2, y2):
    dx = (x2 - x1)
    dy = (y2 - y1)

    if abs(dx) > abs(dy):
        if dx > 0 and dy > 0:
            return 0
        elif dx < 0 and dy > 0:
            return 3
        elif dx < 0 and dy < 0:
            return 4
        else:
            return 7
    else:
        if dx > 0 and dy > 0:
            return 1
        elif dx < 0 and dy > 0:
            return 2
        elif dx < 0 and dy < 0:
            return 5
        else:
            return 6

def ConvertToZoneZero(zone, x, y):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y

def ConvertToOriginal(zone, x, y):
    if zone == 0:
        return x, y
    if zone == 1:
        return y, x
    if zone == 2:
        return -y, -x
    if zone == 3:
        return -x, y
    if zone == 4:
        return -x, -y
    if zone == 5:
        return -y, -x
    if zone == 6:
        return y, -x
    if zone == 7:
        return x, -y

def DrawLine(x1, y1, x2, y2):
    zone = FindZone(x1, y1, x2, y2)
    x1, y1 = ConvertToZoneZero(zone, x1, y1)
    x2, y2 = ConvertToZoneZero(zone, x2, y2)
    MidPointLine(zone, x1, y1, x2, y2)

# Initialize OpenGL
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

def draw_points(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

# Function to draw the shooter

def draw_shooter():
    DrawLine(shooter_x - shooter_width // 2, shooter_y, shooter_x + shooter_width // 2, shooter_y)
    DrawLine(shooter_x + shooter_width // 2, shooter_y, shooter_x + shooter_width // 2, shooter_y + shooter_height)
    DrawLine(shooter_x + shooter_width // 2, shooter_y + shooter_height, shooter_x - shooter_width // 2, shooter_y + shooter_height)
    DrawLine(shooter_x - shooter_width // 2, shooter_y + shooter_height, shooter_x - shooter_width // 2, shooter_y)

# Function to draw projectiles
def draw_projectiles():
    for proj in projectiles:
        for angle in range(0, 360, 10):
            x = proj[0] + projectile_radius * math.cos(math.radians(angle))
            y = proj[1] + projectile_radius * math.sin(math.radians(angle))
            draw_points(x, y)

# Function to draw circles
def draw_circles():
    global unique_circle_flag
    for circ in circles:
        for angle in range(0, 360, 10):
            x = circ[0] + circle_radius * math.cos(math.radians(angle))
            y = circ[1] + circle_radius * math.sin(math.radians(angle))
            draw_points(x, y)

# Function to check collision
def check_collision():
    global score, unique_circle_flag
    for proj in projectiles[:]:
        for circ in circles[:]:
            distance = ((proj[0] - circ[0])**2 + (proj[1] - circ[1])**2)**0.5
            if distance < projectile_radius + circle_radius:
                projectiles.remove(proj)
                circles.remove(circ)
                score += 2 if unique_circle_flag else 1
                unique_circle_flag = False
                break

# Function to spawn a new circle
def spawn_circle():
    global unique_circle_flag
    x = random.randint(circle_radius, SCREEN_WIDTH - circle_radius)
    unique_circle_flag = random.randint(1, 10) == 1  # Rarely spawn a unique circle
    circles.append([x, SCREEN_HEIGHT - circle_radius])

# Function to handle keyboard input
def keyboard(key, x, y):
    global shooter_x
    if key == b'a' and shooter_x - shooter_width // 2 > 0:
        shooter_x -= shooter_speed
    elif key == b'd' and shooter_x + shooter_width // 2 < SCREEN_WIDTH:
        shooter_x += shooter_speed
    elif key == b' ':
        projectiles.append([shooter_x, shooter_y + shooter_height])

def update(value):
    global missed_circles, misfires, game_over

    if game_over:
        return

    # Move projectiles
    for proj in projectiles[:]:
        proj[1] += projectile_speed
        if proj[1] > SCREEN_HEIGHT:
            projectiles.remove(proj)
            misfires += 1

    # Move circles
    for circ in circles[:]:
        circ[1] -= circle_speed
        if circ[1] < 0:
            circles.remove(circ)
            missed_circles += 1

    # Check collisions
    check_collision()

    # Check game over conditions
    if missed_circles >= max_misses or misfires >= max_misses:
        game_over = True

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
    draw_text(10, SCREEN_HEIGHT - 50, f"Score: {score}", 0.2)
    draw_text(10, SCREEN_HEIGHT - 70, f"Missed: {missed_circles}/{max_misses}", 0.2)

    if game_over:
        draw_text(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, "GAME OVER", 0.3)

    glFlush()

def draw_text(x, y, text, scale=1.0):
    glPushMatrix()
    glTranslatef(x, y, 0)
    glScalef(scale, scale, scale)
    glColor3f(1.0, 1.0, 1.0)
    for char in text:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(char))
    glPopMatrix()

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
