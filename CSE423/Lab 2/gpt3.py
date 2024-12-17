from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math
import time

# Screen dimensions
SCREEN_WIDTH = 300
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
unique_circle_flag = False

# Scoring and game state
score = 0
missed_circles = 0
misfires = 0
max_misses = 3
game_over = False
paused = False
start_time = time.time()

# Initialize OpenGL
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

# Function to draw text on screen
def draw_text(x, y, text, scale=1.0):
    glPushMatrix()
    glTranslatef(x, y, 0)
    glScalef(scale, scale, scale)
    glColor3f(1.0, 1.0, 1.0)
    for char in text:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(char))
    glPopMatrix()

# Function to draw the shooter
def draw_shooter():
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(shooter_x - shooter_width // 2, shooter_y)
    glVertex2f(shooter_x + shooter_width // 2, shooter_y)
    glVertex2f(shooter_x + shooter_width // 2, shooter_y + shooter_height)
    glVertex2f(shooter_x - shooter_width // 2, shooter_y + shooter_height)
    glEnd()

# Function to draw projectiles
def draw_projectiles():
    glColor3f(1.0, 1.0, 0.0)
    for proj in projectiles:
        glBegin(GL_POINTS)
        glVertex2f(proj[0], proj[1])
        glEnd()

# Function to draw circles
def draw_circles():
    global unique_circle_flag
    glColor3f(1.0, 0.0, 0.0)
    for circ in circles:
        if unique_circle_flag:
            glColor3f(1.0, 1.0, 0.0)
        glBegin(GL_POINTS)
        for angle in range(360):
            x = circ[0] + circle_radius * math.cos(math.radians(angle))
            y = circ[1] + circle_radius * math.sin(math.radians(angle))
            glVertex2f(x, y)
        glEnd()

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

# Function to draw buttons (Restart, Pause, Exit)
def draw_buttons():
    # Restart Button
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(10, SCREEN_HEIGHT - 30)
    glVertex2f(60, SCREEN_HEIGHT - 30)
    glVertex2f(60, SCREEN_HEIGHT - 10)
    glVertex2f(10, SCREEN_HEIGHT - 10)
    glEnd()
    draw_text(15, SCREEN_HEIGHT - 25, "Restart", 0.1)

    # Pause Button
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(70, SCREEN_HEIGHT - 30)
    glVertex2f(120, SCREEN_HEIGHT - 30)
    glVertex2f(120, SCREEN_HEIGHT - 10)
    glVertex2f(70, SCREEN_HEIGHT - 10)
    glEnd()
    draw_text(75, SCREEN_HEIGHT - 25, "Pause", 0.1)

    # Exit Button
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(130, SCREEN_HEIGHT - 30)
    glVertex2f(180, SCREEN_HEIGHT - 30)
    glVertex2f(180, SCREEN_HEIGHT - 10)
    glVertex2f(130, SCREEN_HEIGHT - 10)
    glEnd()
    draw_text(135, SCREEN_HEIGHT - 25, "Exit", 0.1)

# Function to handle mouse clicks
def mouse(button, state, x, y):
    global paused, game_over, score, missed_circles, misfires, circles, projectiles
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        # Restart Button
        if 10 <= x <= 60 and SCREEN_HEIGHT - 30 <= y <= SCREEN_HEIGHT - 10:
            game_over = False
            score = 0
            missed_circles = 0
            misfires = 0
            circles.clear()
            projectiles.clear()
        # Pause Button
        elif 70 <= x <= 120 and SCREEN_HEIGHT - 30 <= y <= SCREEN_HEIGHT - 10:
            paused = not paused
        # Exit Button
        elif 130 <= x <= 180 and SCREEN_HEIGHT - 30 <= y <= SCREEN_HEIGHT - 10:
            print(f"Goodbye! Final Score: {score}")
            glutLeaveMainLoop()

# Function to update the game state
def update(value):
    global missed_circles, misfires, game_over

    if game_over or paused:
        glutTimerFunc(16, update, 0)
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

# Function to display game elements
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw elements
    draw_shooter()
    draw_projectiles()
    draw_circles()
    draw_buttons()

    # Display score and misses
    draw_text(10, SCREEN_HEIGHT - 50, f"Score: {score}", 0.2)
    draw_text(10, SCREEN_HEIGHT - 70, f"Missed: {missed_circles}/{max_misses}", 0.2)
    draw_text(10, SCREEN_HEIGHT - 90, f"Misfires: {misfires}/{max_misses}", 0.2)

    if game_over:
        draw_text(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, "GAME OVER", 0.3)

    glFlush()

# Function to handle keyboard input
def keyboard(key, x, y):
    global shooter_x
    if key == b'a' and shooter_x - shooter_width // 2 > 0:
        shooter_x -= shooter_speed
    elif key == b'd' and shooter_x + shooter_width // 2 < SCREEN_WIDTH:
        shooter_x += shooter_speed
    elif key == b' ' and not paused and not game_over:
        # Add a new projectile from the center of the shooter
        projectiles.append([shooter_x, shooter_y + shooter_height])

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Shoot The Circles!")
    init()
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)
    glutTimerFunc(16, update, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()

