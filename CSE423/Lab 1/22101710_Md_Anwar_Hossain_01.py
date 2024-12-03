# Task -> 1

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width, W_Height = 900, 900


rain_drops = []
rain_speed = 1
rain_angle = 0


bg_color = [1.0, 1.0, 1.0]


rain_color = [0.0, 0.0, 1.0]  # Blue
house_color = [0.0, 0.0, 0.0]  # Black


class RainDrop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.active = True

    def draw(self):
        if not self.active:
            return
        glLineWidth(1)
        glColor3f(*rain_color)
        glBegin(GL_LINES)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + rain_angle, self.y - 20)  
        glEnd()

    def update(self):
        self.x += rain_angle
        self.y -= rain_speed
        
        if self.y <= 50:
            self.y = 250
            self.x = random.randint(-250, 250)

        if abs(self.x) > 250:
            self.x = random.randint(-250, 250)
            self.y = 200


def create_rain(n):
    for _ in range(n//3):
        x = random.randint(-250, 250)
        y = random.randint(50, 250)  # Between 50px and 250px
        rain_drops.append(RainDrop(x, y))


def draw_house():
    glColor3f(*house_color)
    glLineWidth(10)

    glBegin(GL_LINE_LOOP)
    glVertex2d(0, 150)     
    glVertex2d(-200, 50) 
    glVertex2d(200, 50)    
    glEnd()


    glBegin(GL_LINE_LOOP)
    glVertex2d(-190, -250)
    glVertex2d(190, -250)
    glVertex2d(190, 50)
    glVertex2d(-190, 50)
    glEnd()

    glLineWidth(2)

    glBegin(GL_LINE_LOOP)
    glVertex2d(-70, -250)
    glVertex2d(-70, -100)
    glVertex2d(70, -100)
    glVertex2d(70, -250)
    glEnd()

    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(40, -175)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex2d(90, -50) 
    glVertex2d(90, 20) 
    glVertex2d(160, 20) 
    glVertex2d(160, -50)
    glEnd()

    glBegin(GL_LINES)
    glVertex2d(125, -50)
    glVertex2d(125, 20)
    glVertex2d(90, -15)
    glVertex2d(160, -15)
    glEnd()


def draw_rain():
    for drop in rain_drops:
        drop.draw()
        drop.update()

# changing the background color here
def change_bg_color(dark_to_light):
    global bg_color, rain_color, house_color
    step = 0.5 if dark_to_light else -0.5
    for i in range(3):
        bg_color[i] = max(0.0, min(1.0, bg_color[i] + step))

    if dark_to_light:
        rain_color[:] = [0.0, 0.0, 1.0] 
        house_color[:] = [0.0, 0.0, 0.0]
    else:
        rain_color[:] = [0.8, 0.8, 1.0]
        house_color[:] = [1.0, 1.0, 1.0]

def keyboard_listener(key, x, y):
    if key == b'1':  # (Night to Day)
        change_bg_color(True)
    elif key == b'2':  # (Day to Night)
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

glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow(b"House in Rain")
init()

create_rain(200)

glutDisplayFunc(display)
glutIdleFunc(animate)
glutKeyboardFunc(keyboard_listener)
glutSpecialFunc(special_key_listener)

glutMainLoop()




# Task -> 2 

# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import random
# import threading
# import time

# W_WIDTH, W_HEIGHT = 500, 500

# speed = 2

# points = []
# blinking = False
# paused = False

# def random_color():
#     return [random.random() for _ in range(3)]

# def random_direction():
#     return random.choice([-1, 1]), random.choice([-1, 1])

# def add_point(x, y):
#     dx, dy = random_direction()
#     color = random_color()
#     points.append([x, y, dx, dy, color, 1])

# def update_points():
#     global points, paused
#     if paused:
#         return
#     for point in points:
#         point[0] += point[2] * speed
#         point[1] += point[3] * speed

#         # Bounce from walls happening here
#         if point[0] >= W_WIDTH // 2 or point[0] <= -W_WIDTH // 2:
#             point[2] *= -1
#         if point[1] >= W_HEIGHT // 2 or point[1] <= -W_HEIGHT // 2:
#             point[3] *= -1

# def draw_points():
#     global points
#     for point in points:
#         if point[5] == 1:
#             glColor3f(*point[4])
#             glPointSize(10)
#             glBegin(GL_POINTS)
#             glVertex2f(point[0], point[1])
#             glEnd()

# def toggle_blink():
#     global points, blinking
#     while blinking:
#         for point in points:
#             point[5] = 1 - point[5]
#         glutPostRedisplay()
#         time.sleep(0.3)

# def start_blinking():
#     global blinking
#     if not blinking:
#         blinking = True
#         threading.Thread(target=toggle_blink, daemon=True).start()
#         print("Blinking started.")
#     else:
#         blinking = False
#         print("Blinking stopped.")

# def mouse_listener(button, state, x, y):
#     global points
#     if state == GLUT_DOWN:
#         opengl_x = x - W_WIDTH // 2
#         opengl_y = -(y - W_HEIGHT // 2)

#         if button == GLUT_RIGHT_BUTTON:
#             add_point(opengl_x, opengl_y)
#             print(f"Point added at ({opengl_x}, {opengl_y}).")
#         elif button == GLUT_LEFT_BUTTON:
#             start_blinking()

# def keyboard_listener(key, x, y):
#     global speed, paused
#     if key == b' ':
#         paused = not paused
#         if paused:
#             print("Animation paused.")
#         else:
#             print("Animation resumed.")
#     elif key == GLUT_KEY_UP and not paused:
#         speed += 1
#         print(f"Speed increased to {speed}.")
#     elif key == GLUT_KEY_DOWN and not paused and speed > 1:
#         speed -= 1
#         print(f"Speed decreased to {speed}.")

# def display():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     draw_points()
#     glutSwapBuffers()

# def animate():
#     update_points()
#     glutPostRedisplay()

# def init():
#     glClearColor(0, 0, 0, 1)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     gluOrtho2D(-W_WIDTH // 2, W_WIDTH // 2, -W_HEIGHT // 2, W_HEIGHT // 2)
#     glMatrixMode(GL_MODELVIEW)

# glutInit()
# glutInitWindowSize(W_WIDTH, W_HEIGHT)
# glutInitWindowPosition(0, 0)
# glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
# glutCreateWindow(b"Amazing Box")
# init()

# glutDisplayFunc(display)
# glutIdleFunc(animate)
# glutMouseFunc(mouse_listener)
# glutSpecialFunc(keyboard_listener)
# glutKeyboardFunc(keyboard_listener)

# glutMainLoop()
