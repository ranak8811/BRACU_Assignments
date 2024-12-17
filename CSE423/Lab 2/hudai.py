import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin, pi

# Window size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Spaceship settings
shooter_width = 50
shooter_height = 20
shooter_x = SCREEN_WIDTH // 2
shooter_y = 50
shooter_speed = 300  # Space ship speed (we'll use delta time for accurate movement)

# Circle (enemy) settings
circle_radius = 20
circle_x = SCREEN_WIDTH // 2
circle_y = SCREEN_HEIGHT - 100
circle_speed = 100  # Circle speed

# Time tracking
last_time = time.time()
delta_time = 0.016  # Set a default delta_time to avoid the initial errors

# Draw the spaceship (rocket)
def draw_shooter():
    # Rocket body (rectangle)
    body_top_y = shooter_y + 20  # The top of the body starts after the triangle
    glBegin(GL_QUADS)
    glVertex2f(shooter_x - shooter_width // 2, body_top_y)
    glVertex2f(shooter_x + shooter_width // 2, body_top_y)
    glVertex2f(shooter_x + shooter_width // 2, body_top_y + shooter_height)
    glVertex2f(shooter_x - shooter_width // 2, body_top_y + shooter_height)
    glEnd()

    # Rocket nose (triangle)
    glBegin(GL_TRIANGLES)
    glVertex2f(shooter_x - shooter_width // 2, shooter_y)  # Left side of the triangle
    glVertex2f(shooter_x + shooter_width // 2, shooter_y)  # Right side of the triangle
    glVertex2f(shooter_x, shooter_y + 20)  # Apex of the triangle
    glEnd()

# Draw the circle (enemy)
def draw_circle(x, y, radius):
    segments = 50
    glBegin(GL_POLYGON)
    for i in range(segments):
        angle = 2 * pi * i / segments
        dx = radius * cos(angle)
        dy = radius * sin(angle)
        glVertex2f(x + dx, y + dy)
    glEnd()

# Handle keyboard input for movement
def handle_keys(key, x, y):
    global shooter_x
    if key == b'a':  # Left
        shooter_x -= shooter_speed * delta_time
    elif key == b'd':  # Right
        shooter_x += shooter_speed * delta_time

# Game loop
def game_loop():
    global last_time, delta_time, circle_y, circle_speed

    # Calculate delta time
    current_time = time.time()
    delta_time = current_time - last_time
    last_time = current_time

    # Clear screen
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw spaceship
    draw_shooter()

    # Move and draw circle (enemy)
    circle_y -= circle_speed * delta_time
    if circle_y < 0:
        circle_y = SCREEN_HEIGHT - 100  # Reset position
    draw_circle(circle_x, circle_y, circle_radius)

    # Check for collision (simple collision detection)
    if (shooter_x + shooter_width // 2 > circle_x - circle_radius and
        shooter_x - shooter_width // 2 < circle_x + circle_radius and
        shooter_y + shooter_height > circle_y - circle_radius and
        shooter_y < circle_y + circle_radius):
        print("Game Over!")
        glutLeaveMainLoop()  # Stop the game loop

    glutSwapBuffers()

# Initialize the OpenGL window
def init():
    glClearColor(0, 0, 0, 1)  # Black background
    glOrtho(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT, -1, 1)  # Set coordinate system
    glutKeyboardFunc(handle_keys)  # Keyboard input
    glutIdleFunc(game_loop)  # Game loop

    # Set display function to render
    glutDisplayFunc(game_loop)

# Start the game
glutInit()
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
glutCreateWindow(b"Spaceship Game")
init()

# Start the GLUT main loop
glutMainLoop()  # This will start the event processing loop
