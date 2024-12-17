from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

shooter_width = 50
shooter_height = 20
shooter_x = SCREEN_WIDTH // 2
shooter_y = 50
shooter_speed = 30

projectiles = []
projectile_radius = 5
projectile_speed = 10


circles = [] 
circle_radius = 20
circle_speed = 0.5
unique_circle_flag = False

score = 0
missed_circles = 0
misfires = 0
max_misses = 3
game_over = False
paused = False

back_buttonCon = False
play_buttonCon = True
cross_buttonCon = False

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

def play_button():
    glColor3f(1.0, 0.5, 0.0)
    DrawLine(200, 580, 220, 570)
    DrawLine(200, 560, 220, 570)
    DrawLine(200, 560, 200, 580)


def back_button():
    glColor3f(0.0, 1.0, 0.0)
    DrawLine(10, 570, 30, 570)
    DrawLine(10, 570, 20, 580)
    DrawLine(10, 570, 10, 560)

def cross_button():
    glColor3f(1.0, 0.0, 0.0)
    DrawLine(390, 580, 370, 560)
    DrawLine(370, 580, 390, 560)

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

def draw_points(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def draw_shooter():

    DrawLine(shooter_x - shooter_width // 2, shooter_y, shooter_x + shooter_width // 2, shooter_y)
    DrawLine(shooter_x + shooter_width // 2, shooter_y, shooter_x + shooter_width // 2, shooter_y + shooter_height)
    DrawLine(shooter_x + shooter_width // 2, shooter_y + shooter_height, shooter_x - shooter_width // 2, shooter_y + shooter_height)
    DrawLine(shooter_x - shooter_width // 2, shooter_y + shooter_height, shooter_x - shooter_width // 2, shooter_y)
    

    triangle_height = 20
    DrawLine(shooter_x - shooter_width // 2, shooter_y, shooter_x, shooter_y + triangle_height)
    DrawLine(shooter_x, shooter_y + triangle_height, shooter_x + shooter_width // 2, shooter_y)

def draw_projectiles():
    for proj in projectiles:
        for angle in range(0, 360, 10):
            x = proj[0] + projectile_radius * math.cos(math.radians(angle))
            y = proj[1] + projectile_radius * math.sin(math.radians(angle))
            draw_points(x, y)

def draw_circles():
    global unique_circle_flag
    for circ in circles:
        for angle in range(0, 360, 10):
            x = circ[0] + circle_radius * math.cos(math.radians(angle))
            y = circ[1] + circle_radius * math.sin(math.radians(angle))
            draw_points(x, y)

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

def spawn_circle():
    global unique_circle_flag
    x = random.randint(circle_radius, SCREEN_WIDTH - circle_radius)
    unique_circle_flag = random.randint(1, 10) == 1
    circles.append([x, SCREEN_HEIGHT - circle_radius])

def keyboard(key, x, y):
    global shooter_x
    if key == b'a' and shooter_x - shooter_width // 2 > 0 and play_buttonCon:
        shooter_x -= shooter_speed
    elif key == b'd' and shooter_x + shooter_width // 2 < SCREEN_WIDTH and play_buttonCon:
        shooter_x += shooter_speed
    elif key == b' ' and play_buttonCon:
        projectiles.append([shooter_x, shooter_y + shooter_height])

def update(value):
    global missed_circles, misfires, game_over, play_buttonCon

    if game_over:
        return

    if play_buttonCon:
        for proj in projectiles[:]:
            proj[1] += projectile_speed
            if proj[1] > SCREEN_HEIGHT:
                projectiles.remove(proj)
                misfires += 1

        for circ in circles[:]:
            circ[1] -= circle_speed
            if circ[1] < 0:
                circles.remove(circ)
                missed_circles += 1
        check_collision()

    if missed_circles >= max_misses or misfires >= max_misses:
        game_over = True

    if random.randint(1, 50) == 1 and play_buttonCon:
        spawn_circle()

    glutPostRedisplay()
    if not cross_buttonCon:
        glutTimerFunc(16, update, 0)
    

def reset():
    global projectiles, circles, score, missed_circles, misfires, max_misses

    if back_buttonCon:
        projectiles = []
        circles = []
        score = 0
        missed_circles = 0
        misfires = 0
        max_misses = 3
        # print('back_buttonCon', back_buttonCon)

def exitTheGame():
    print("Goodbye")
    print(f"Final Score: {score}")
    glutLeaveMainLoop()

def mouse_listener(button, state, x, y):
    global back_buttonCon, play_buttonCon, cross_buttonCon

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if 10 <= x <= 30 and (600-580) <= y <= (600-560):
            back_buttonCon = not back_buttonCon
            reset()
            back_buttonCon = not back_buttonCon
        elif 370 <= x <= 390 and (600-580) <= y <= (600-560):
            cross_buttonCon = True
            exitTheGame()
        elif 200 <= x <= 220 and (600-580) <= y <= (600-560):
            play_buttonCon = not play_buttonCon

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    draw_shooter()
    draw_projectiles()
    draw_circles()
    
    play_button()
    back_button()
    cross_button()

    draw_text(10, SCREEN_HEIGHT - 65, f"Score: {score}", 0.2)
    draw_text(10, SCREEN_HEIGHT - 90, f"Missed: {missed_circles}/{max_misses}", 0.2)

    if game_over:
        print(f"Final Score: {score}")
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


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
glutCreateWindow(b"Shoot The Circles!")
init()
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouse_listener)
glutTimerFunc(16, update, 0)
glutMainLoop()