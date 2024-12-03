from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import threading
import time

# Window dimensions
W_WIDTH, W_HEIGHT = 600, 600

# Speed of movement
speed = 2

# Points and their properties
points = []
blinking = False
paused = False

# Point structure: [x, y, dx, dy, color, blink_state]
# dx, dy represent the direction of movement
# blink_state determines visibility (1: visible, 0: invisible)


def random_color():
    """Generate a random color."""
    return [random.random() for _ in range(3)]


def random_direction():
    """Generate a random diagonal direction."""
    return random.choice([-1, 1]), random.choice([-1, 1])


def add_point(x, y):
    """Add a new point with random properties."""
    dx, dy = random_direction()
    color = random_color()
    points.append([x, y, dx, dy, color, 1])


def update_points():
    """Update the position of points and handle bouncing."""
    global points, paused
    if paused:
        return
    for point in points:
        # Update position
        point[0] += point[2] * speed
        point[1] += point[3] * speed

        # Bounce from walls
        if point[0] >= W_WIDTH // 2 or point[0] <= -W_WIDTH // 2:
            point[2] *= -1  # Reverse x-direction
        if point[1] >= W_HEIGHT // 2 or point[1] <= -W_HEIGHT // 2:
            point[3] *= -1  # Reverse y-direction


def draw_points():
    """Draw all the points."""
    global points
    for point in points:
        if point[5] == 1:  # Only draw if blink state is visible
            glColor3f(*point[4])
            glPointSize(10)
            glBegin(GL_POINTS)
            glVertex2f(point[0], point[1])
            glEnd()


def toggle_blink():
    """Toggle the blink state of points."""
    global points, blinking
    while blinking:
        for point in points:
            point[5] = 1 - point[5]  # Toggle visibility
        glutPostRedisplay()
        time.sleep(0.3)


def start_blinking():
    """Start the blinking functionality in a separate thread."""
    global blinking
    if not blinking:
        blinking = True
        threading.Thread(target=toggle_blink, daemon=True).start()
        print("Blinking started.")
    else:
        blinking = False
        print("Blinking stopped.")


def mouse_listener(button, state, x, y):
    """Handle mouse clicks."""
    global points
    if state == GLUT_DOWN:
        # Convert screen coordinates to OpenGL coordinates
        opengl_x = x - W_WIDTH // 2
        opengl_y = -(y - W_HEIGHT // 2)

        if button == GLUT_RIGHT_BUTTON:
            add_point(opengl_x, opengl_y)
            print(f"Point added at ({opengl_x}, {opengl_y}).")
        elif button == GLUT_LEFT_BUTTON:
            start_blinking()


def keyboard_listener(key, x, y):
    """Handle keyboard inputs."""
    global speed, paused
    if key == b' ':
        paused = not paused
        if paused:
            print("Animation paused.")
        else:
            print("Animation resumed.")
    elif key == GLUT_KEY_UP and not paused:
        speed += 1
        print(f"Speed increased to {speed}.")
    elif key == GLUT_KEY_DOWN and not paused and speed > 1:
        speed -= 1
        print(f"Speed decreased to {speed}.")


def display():
    """Render the scene."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    draw_points()
    glutSwapBuffers()


def animate():
    """Animate the points."""
    update_points()
    glutPostRedisplay()


def init():
    """Initialize OpenGL settings."""
    glClearColor(0, 0, 0, 1)  # Black background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-W_WIDTH // 2, W_WIDTH // 2, -W_HEIGHT // 2, W_HEIGHT // 2)
    glMatrixMode(GL_MODELVIEW)


# Initialize GLUT
glutInit()
glutInitWindowSize(W_WIDTH, W_HEIGHT)
glutInitWindowPosition(100, 100)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutCreateWindow(b"Amazing Box")
init()

# Register callbacks
glutDisplayFunc(display)
glutIdleFunc(animate)
glutMouseFunc(mouse_listener)
glutSpecialFunc(keyboard_listener)
glutKeyboardFunc(keyboard_listener)

# Start the main loop
glutMainLoop()
