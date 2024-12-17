from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math
import time

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Shooter settings
shooter_width = 50
shooter_height = 20
shooter_x = SCREEN_WIDTH // 2
shooter_y = 50
shooter_speed = 30

# Projectile settings
projectiles = []
projectile_radius = 5
projectile_speed = 10

# Circle settings
circles = []
circle_radius = 20
circle_speed = 0.5
unique_circle_flag = False

# Game state
score = 0
missed_circles = 0
misfires = 0
max_misses = 3
game_over = False
paused = False

# Button Flags
back_buttonCon = False
play_buttonCon = True
cross_buttonCon = False

# Midpoint Algorithm Functions
def MidPointLine(zone, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    x, y = x1, y1
    dInitial = 2 * dy - dx
    Del_E = 2 * dy
    Del_NE = 2 * (dy - dx)

    while x <= x2:
        a, b = ConvertToOriginal(zone, x, y)
        draw_points(a, b)
        if dInitial <= 0:
            x += 1
            dInitial += Del_E
        else:
            x += 1
            y += 1
            dInitial += Del_NE

def FindZone(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    if abs(dx) > abs(dy):
        return 0 if dx > 0 and dy > 0 else 4 if dx < 0 and dy < 0 else 3 if dx < 0 else 7
    return 1 if dx > 0 and dy > 0 else 5 if dx < 0 and dy < 0 else 6 if dx > 0 else 2

def ConvertToZoneZero(zone, x, y):
    transforms = [
        (x, y), (y, x), (-y, x), (-x, y), (-x, -y), (-y, -x), (y, -x), (x, -y)
    ]
    return transforms[zone]

def ConvertToOriginal(zone, x, y):
    return ConvertToZoneZero(zone, x, y)

def DrawLine(x1, y1, x2, y2):
    zone = FindZone(x1, y1, x2, y2)
    x1, y1 = ConvertToZoneZero(zone, x1, y1)
    x2, y2 = ConvertToZoneZero(zone, x2, y2)
    MidPointLine(zone, x1, y1, x2, y2)

# Buttons
def play_button(): DrawLine(200, 580, 220, 570), DrawLine(200, 560, 220, 570), DrawLine(200, 560, 200, 580)
def back_button(): DrawLine(10, 570, 30, 570), DrawLine(10, 570, 20, 580), DrawLine(10, 570, 10, 560)
def cross_button(): DrawLine(390, 580, 370, 560), DrawLine(370, 580, 390, 560)

# Utility Functions
def draw_points(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def draw_text(x, y, text, size):
    glColor3f(1, 1, 1)
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

def draw_shooter():
    DrawLine(shooter_x - shooter_width // 2, shooter_y, shooter_x + shooter_width // 2, shooter_y)
    DrawLine(shooter_x + shooter_width // 2, shooter_y, shooter_x + shooter_width // 2, shooter_y + shooter_height)
    DrawLine(shooter_x + shooter_width // 2, shooter_y + shooter_height, shooter_x - shooter_width // 2, shooter_y + shooter_height)
    DrawLine(shooter_x - shooter_width // 2, shooter_y + shooter_height, shooter_x - shooter_width // 2, shooter_y)

def draw_projectiles():
    for proj in projectiles:
        for angle in range(0, 360, 10):
            x = proj[0] + projectile_radius * math.cos(math.radians(angle))
            y = proj[1] + projectile_radius * math.sin(math.radians(angle))
            draw_points(x, y)

def draw_circles():
    for circ in circles:
        for angle in range(0, 360, 10):
            x = circ[0] + circle_radius * math.cos(math.radians(angle))
            y = circ[1] + circle_radius * math.sin(math.radians(angle))
            draw_points(x, y)

def check_collision():
    global score
    for proj in projectiles[:]:
        for circ in circles[:]:
            if ((proj[0] - circ[0])**2 + (proj[1] - circ[1])**2)**0.5 < projectile_radius + circle_radius:
                projectiles.remove(proj)
                circles.remove(circ)
                score += 2 if unique_circle_flag else 1

def spawn_circle():
    x = random.randint(circle_radius, SCREEN_WIDTH - circle_radius)
    circles.append([x, SCREEN_HEIGHT - circle_radius])

# Input and Update Logic
def keyboard(key, x, y):
    global shooter_x
    if key == b'a' and shooter_x - shooter_width // 2 > 0: shooter_x -= shooter_speed
    if key == b'd' and shooter_x + shooter_width // 2 < SCREEN_WIDTH: shooter_x += shooter_speed
    if key == b' ': projectiles.append([shooter_x, shooter_y + shooter_height])

def update(value):
    global missed_circles, game_over
    for proj in projectiles[:]:
        proj[1] += projectile_speed
        if proj[1] > SCREEN_HEIGHT: projectiles.remove(proj)
    for circ in circles[:]:
        circ[1] -= circle_speed
        # if circ[1] < 0: circles.remove(circ), missed_circles += 1
        if circ[1] < 0: 
            circles.remove(circ)
            missed_circles += 1

    check_collision()
    if random.randint(1, 50) == 1: spawn_circle()
    if missed_circles >= max_misses: game_over = True
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    if not game_over:
        draw_shooter(), draw_projectiles(), draw_circles()
        play_button(), back_button(), cross_button()
        draw_text(10, SCREEN_HEIGHT - 65, f"Score: {score}", 0.2)
    else:
        draw_text(SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT//2, "GAME OVER", 0.3)
    glFlush()

# Initialization and Main Loop
def init():
    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
glutCreateWindow("Shooter Game")
init()
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutTimerFunc(0, update, 0)
glutMainLoop()
