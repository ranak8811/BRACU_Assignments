from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Window dimensions
W_Width, W_Height = 900, 900

# Rain properties
rain_drops = []
rain_speed = 2
rain_angle = 0  # Angle of rain, 0 is straight down

# Background color
bg_color = [1.0, 1.0, 1.0]  # Start as light (daylight)

# House dimensions
house_width, house_height = 300, 200
roof_height = 100


class RainDrop:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        glColor3f(0, 0, 1)  # Blue raindrop
        glBegin(GL_LINES)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + rain_angle, self.y - 10)  # Tilt by rain_angle
        glEnd()

    def update(self):
        self.x += rain_angle  # Adjust for rain angle
        self.y -= rain_speed
        if self.y < -W_Height // 2:  # Reset when out of view
            self.y = W_Height // 2
            self.x = random.randint(-W_Width // 2, W_Width // 2)


def create_rain(n):
    """Create a list of raindrops at random positions."""
    for _ in range(n):
        x = random.randint(-W_Width // 2, W_Width // 2)
        y = random.randint(-W_Height // 2, W_Height // 2)
        rain_drops.append(RainDrop(x, y))


def draw_rain():
    """Draw and update the rain."""
    for drop in rain_drops:
        drop.draw()
        drop.update()


def draw_house():
    """Draw the house with walls, roof, door, and a window."""
    # Roof
    glColor3f(0.7, 0.1, 0.1)  # Red roof
    glBegin(GL_TRIANGLES)
    glVertex2f(-house_width // 2, 0)
    glVertex2f(house_width // 2, 0)
    glVertex2f(0, roof_height)
    glEnd()

    # Walls
    glColor3f(0.8, 0.5, 0.2)  # Brown walls
    glBegin(GL_QUADS)
    glVertex2f(-house_width // 2, -house_height)
    glVertex2f(house_width // 2, -house_height)
    glVertex2f(house_width // 2, 0)
    glVertex2f(-house_width // 2, 0)
    glEnd()

    # Door
    glColor3f(0.4, 0.2, 0.0)  # Dark brown door
    glBegin(GL_QUADS)
    glVertex2f(-40, -house_height)
    glVertex2f(40, -house_height)
    glVertex2f(40, -house_height // 2)
    glVertex2f(-40, -house_height // 2)
    glEnd()

    # Window
    glColor3f(0.9, 0.9, 0.9)  # White window
    glBegin(GL_QUADS)
    glVertex2f(50, -50)
    glVertex2f(100, -50)
    glVertex2f(100, 0)
    glVertex2f(50, 0)
    glEnd()
    glColor3f(0, 0, 0)  # Black lines for window grid
    glBegin(GL_LINES)
    glVertex2f(75, -50)
    glVertex2f(75, 0)
    glVertex2f(50, -25)
    glVertex2f(100, -25)
    glEnd()


def change_bg_color(dark_to_light):
    """Simulate day-night transition by changing the background color."""
    global bg_color
    step = 0.5 if dark_to_light else -0.5
    for i in range(3):
        bg_color[i] = max(0, min(1, bg_color[i] + step))  # Clamp between 0 and 1


def keyboardListener(key, x, y):
    """Handle keyboard inputs for day-night transition."""
    global bg_color
    if key == b'1':  # Simulate night to day
        change_bg_color(True)
    elif key == b'2':  # Simulate day to night
        change_bg_color(False)
    glutPostRedisplay()


def specialKeyListener(key, x, y):
    """Handle special key inputs for adjusting rain angle."""
    global rain_angle
    if key == GLUT_KEY_LEFT:  # Bend rain to the left
        rain_angle -= 0.5
    elif key == GLUT_KEY_RIGHT:  # Bend rain to the right
        rain_angle += 0.5
    glutPostRedisplay()


def display():
    """Main display function."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(bg_color[0], bg_color[1], bg_color[2], 1)  # Set background color
    glLoadIdentity()

    # Draw the house and rain
    draw_house()
    draw_rain()

    glutSwapBuffers()


def animate():
    """Continuously update the display."""
    glutPostRedisplay()


def init():
    """Initialize OpenGL settings."""
    glClearColor(0, 0, 0, 1)  # Black background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-W_Width // 2, W_Width // 2, -W_Height // 2, W_Height // 2)  # Orthographic projection
    glMatrixMode(GL_MODELVIEW)


# OpenGL setup
glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(100, 100)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow(b"Rainfall Simulation with House")
init()

# Create raindrops
create_rain(100)

# Register callbacks
glutDisplayFunc(display)
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)

# Start the main loop
glutMainLoop()
