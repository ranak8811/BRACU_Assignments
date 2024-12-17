from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math
import time
import sys

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Shooter settings
shooter_width = 20
shooter_height = 40
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

# Control buttons
back_button_pressed = False
play_pause_button_pressed = True  # Initially in play mode
exit_button_pressed = False

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
            x += 1
            dInitial += Del_E
        else:
            x += 1
            y += 1
            dInitial += Del_NE

def FindZone(x1, y1, x2, y2):
    dx = (x2 - x1)
    dy = (y2 - y1)

    if abs(dx) > abs(dy):
        if dx > 0 and dy > 0: return 0
        elif dx < 0 and dy > 0: return 3
        elif dx < 0 and dy < 0: return 4
        else: return 7
    else:
        if dx > 0 and dy > 0: return 1
        elif dx < 0 and dy > 0: return 2
        elif dx < 0 and dy < 0: return 5
        else: return 6

def ConvertToZoneZero(zone, x, y):
    transformations = {
        0: (x, y), 1: (y, x), 2: (-y, x), 3: (-x, y),
        4: (-x, -y), 5: (-y, -x), 6: (y, -x), 7: (x, -y)
    }
    return transformations[zone]

def ConvertToOriginal(zone, x, y):
    return ConvertToZoneZero(zone, x, y)

def DrawLine(x1, y1, x2, y2):
    zone = FindZone(x1, y1, x2, y2)
    x1, y1 = ConvertToZoneZero(zone, x1, y1)
    x2, y2 = ConvertToZoneZero(zone, x2, y2)
    MidPointLine(zone, x1, y1, x2, y2)

# Buttons
def play_button():
    glColor3f(1.0, 0.5, 0.0)  # Amber color
    DrawLine(200, 580, 220, 570)
    DrawLine(200, 560, 220, 570)
    DrawLine(200, 560, 200, 580)

def back_button():
    glColor3f(0.0, 1.0, 0.0)  # Green color
    DrawLine(10, 570, 30, 570)
    DrawLine(10, 570, 20, 580)
    DrawLine(10, 570, 10, 560)

def cross_button():
    glColor3f(1.0, 0.0, 0.0)  # Red color
    DrawLine(390, 580, 370, 560)
    DrawLine(370, 580, 390, 560)

# Draw the shooter as a rocket
def draw_shooter():
    glColor3f(0.5, 0.5, 0.5)  # Gray color
    # Rocket base
    DrawLine(shooter_x - shooter_width // 2, shooter_y, shooter_x + shooter_width // 2, shooter_y)
    DrawLine(shooter_x + shooter_width // 2, shooter_y, shooter_x, shooter_y + shooter_height)
    DrawLine(shooter_x, shooter_y + shooter_height, shooter_x - shooter_width // 2, shooter_y)

def draw_projectiles():
    glColor3f(1.0, 1.0, 0.0)
    for proj in projectiles:
        for angle in range(0, 360, 10):
            x = proj[0] + projectile_radius * math.cos(math.radians(angle))
            y = proj[1] + projectile_radius * math.sin(math.radians(angle))
            draw_points(x, y)

def draw_circles():
    glColor3f(0.0, 0.5, 1.0)
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
                score += 1

def mouse_listener(button, state, x, y):
    global back_button_pressed, play_pause_button_pressed, exit_button_pressed, score, missed_circles, circles, projectiles, paused

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if 10 <= x <= 30 and 20 <= y <= 40:
            print("Starting Over")
            back_button_pressed = True
            score = 0
            missed_circles = 0
            circles = []
            projectiles = []
        elif 200 <= x <= 220 and 20 <= y <= 40:
            paused = not paused
            print("Paused" if paused else "Playing")
        elif 370 <= x <= 390 and 20 <= y <= 40:
            print(f"Goodbye. Final Score: {score}")
            sys.exit()

def keyboard(key, x, y):
    global shooter_x
    if not paused:
        if key == b'a' and shooter_x > shooter_width:
            shooter_x -= shooter_speed
        elif key == b'd' and shooter_x < SCREEN_WIDTH - shooter_width:
            shooter_x += shooter_speed
        elif key == b' ':
            projectiles.append([shooter_x, shooter_y + shooter_height])

def update(value):
    global game_over, missed_circles
    if not paused and not game_over:
        for proj in projectiles[:]:
            proj[1] += projectile_speed
            if proj[1] > SCREEN_HEIGHT:
                projectiles.remove(proj)

        for circ in circles[:]:
            circ[1] -= circle_speed
            if circ[1] < 0:
                circles.remove(circ)
                missed_circles += 1

        check_collision()

        if random.randint(1, 50) == 1:
            circles.append([random.randint(20, SCREEN_WIDTH - 20), SCREEN_HEIGHT - 20])

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def draw_text(x, y, text):
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(char))

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_shooter()
    draw_projectiles()
    draw_circles()
    play_button()
    back_button()
    cross_button()
    draw_text(10, SCREEN_HEIGHT - 30, f"Score: {score}")
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
glutCreateWindow(b"Rocket Shooter with Buttons")
init()
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouse_listener)
glutTimerFunc(0, update, 0)
glutMainLoop()
