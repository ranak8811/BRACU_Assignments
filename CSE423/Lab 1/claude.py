from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Window dimensions
W_Width, W_Height = 900, 900

# Rain properties
rain_drops = []
rain_speed = 1
rain_angle = 0

# Background color
bg_color = [1.0, 1.0, 1.0]

class RainDrop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.active = True

    def draw(self):
        if not self.active:
            return
        glLineWidth(1)
        glColor3f(0, 0, 1)
        glBegin(GL_LINES)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + rain_angle, self.y - 40)  # 20px height rain drops
        glEnd()

    def update(self):
        self.x += rain_angle
        self.y -= rain_speed
        
        # Reset if raindrop goes below 10px height
        if self.y <= 50:  # Minimum height is 10px
            self.y = 250  # Start from 200px height
            self.x = random.randint(-250, 250)  # Wider range for rain
        
        # Reset if it goes too far to sides
        if abs(self.x) > 250:
            self.x = random.randint(-250, 250)
            self.y = 200

def create_rain(n):
    for _ in range(n):
        x = random.randint(-250, 250)
        y = random.randint(50, 250)  # Between 10px and 200px
        rain_drops.append(RainDrop(x, y))

def draw_house():
    # Draw thick walls
    glLineWidth(10)
    glColor3f(0, 0, 0)

    # Roof (bigger)
    glBegin(GL_LINE_LOOP)
    glVertex2d(0, 150)      # Top point (higher)
    glVertex2d(-200, 50)    # Left point (wider)
    glVertex2d(200, 50)     # Right point (wider)
    glEnd()

    # Walls (bigger)
    glBegin(GL_LINE_LOOP)
    glVertex2d(-190, -250)  # Bottom left
    glVertex2d(190, -250)   # Bottom right
    glVertex2d(190, 50)     # Top right
    glVertex2d(-190, 50)    # Top left
    glEnd()

    # Switch to thin lines for door and window
    glLineWidth(2)

    # Door (bigger)
    glBegin(GL_LINE_LOOP)
    glVertex2d(-70, -250)   # Bottom left
    glVertex2d(-70, -100)   # Top left
    glVertex2d(70, -100)    # Top right
    glVertex2d(70, -250)    # Bottom right
    glEnd()

    # Door knob
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(40, -175)
    glEnd()

    # Window (bigger)
    glBegin(GL_LINE_LOOP)
    glVertex2d(90, -50)     # Bottom left
    glVertex2d(90, 20)      # Top left
    glVertex2d(160, 20)     # Top right
    glVertex2d(160, -50)    # Bottom right
    glEnd()

    # Window cross
    glBegin(GL_LINES)
    glVertex2d(125, -50)    # Vertical line
    glVertex2d(125, 20)
    glVertex2d(90, -15)     # Horizontal line
    glVertex2d(160, -15)
    glEnd()

def draw_rain():
    for drop in rain_drops:
        drop.draw()
        drop.update()

def change_bg_color(dark_to_light):
    global bg_color
    step = 0.05 if dark_to_light else -0.05
    for i in range(3):
        bg_color[i] = max(0, min(1, bg_color[i] + step))

def keyboard_listener(key, x, y):
    if key == b'1':
        change_bg_color(True)
    elif key == b'2':
        change_bg_color(False)
    glutPostRedisplay()

def special_key_listener(key, x, y):
    global rain_angle
    if key == GLUT_KEY_LEFT:
        rain_angle -= 0.5
    elif key == GLUT_KEY_RIGHT:
        rain_angle += 0.5
    glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(bg_color[0], bg_color[1], bg_color[2], 1)
    glLoadIdentity()
    
    draw_house()
    draw_rain()
    
    glutSwapBuffers()

def animate():
    glutPostRedisplay()

def init():
    glClearColor(1, 1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-W_Width // 2, W_Width // 2, -W_Height // 2, W_Height // 2)
    glMatrixMode(GL_MODELVIEW)

# Initialize GLUT
glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow(b"House in Rain")
init()

# Create raindrops
create_rain(200)

# Register callbacks
glutDisplayFunc(display)
glutIdleFunc(animate)
glutKeyboardFunc(keyboard_listener)
glutSpecialFunc(special_key_listener)

# Start the main loop
glutMainLoop()