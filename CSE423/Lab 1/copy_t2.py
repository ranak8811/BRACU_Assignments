from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time


def iterate(): #display
    glViewport(0, 0, 1000,1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000,0.0, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()



def drawbox():
    glBegin(GL_QUADS)  # outer
    glColor3f(0,0,0)
    glVertex2d(50, 50)
    glColor3f(0,0,0)
    glVertex2d(450, 50)
    glColor3f(0,0,0)
    glVertex2d(450, 450)
    glColor3f(0,0,0)
    glVertex2d(50, 450)
    glColor3f(0,0,0)
    glEnd()

def draw_points(x, y,rgb):
    glPointSize(4) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glColor3f(rgb[0], rgb[1], rgb[2])
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()


points= []

def prandomizer(x,y):
    movement= random.choice([(-1, 1), (-1, -1), (1, 1), (1, -1)])
    return {'x':x,"y":y,'dx':movement[0],'dy':movement[1],'color':crandomizer()}


def crandomizer():
    rgb= [random.random(), random.random(), random.random()]
    return rgb

speed= 0.3
def pmovement():
    global speed, points
    for i in points:
        if freeze==False:

            if i['x'] <= 50 or i['x'] >= 450:
                i['dx'] = -i['dx']                # spawns multiple first if  this ones down
            if i['y'] <= 50 or i['y'] >= 450:
                i['dy'] = -i['dy']

            i['x'] += i['dx']*speed   #First check then print  (for visibility)
            i['y'] += i['dy']*speed   #it makes spawn one at a time






freeze= False
blink = False
def mouseListener(button, state, x, y):	#/#/x, y is the x-y of the screen (2D)
    global freeze, blink, speed, create_new,points
    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):    # 		// 2 times?? in ONE click? -- solution is checking DOWN or UP
            if blink==True:
                blink= False
                print("Blinking ON")
            elif blink == False:
                blink = True
                print("Blinking OFF")

    if button==GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            if 49<x<451 and 49<y<451:
                x,y = x, 450- y
                point= prandomizer(x,y)
                points.append(point)
                print("New random point at:",x,y)
            else:
                print("Click inside the Blackbox")

    if button == GLUT_MIDDLE_BUTTON:
        if state == GLUT_DOWN:
            speed = 0.3
            points=[]
            print("Speed was reset")
            print("Blackbox Cleared")

    glutPostRedisplay()


def specialKeyListener(key, x, y):
    global freeze, speed
    if  freeze==False:
        if key == GLUT_KEY_UP:
            speed *= 2
            print("Speed increased", "Speed:", speed)
        if key == GLUT_KEY_DOWN:
            speed /= 2
            print("Speed Decreased", "Speed:", speed)

    glutPostRedisplay()


def keyBoardListener(key, x, y):
    global freeze
    if key == b' ':
        freeze = not freeze
        if freeze==True:
            print("Freezeee!!")
        else:
            print("Unfreezee!!")
    glutPostRedisplay()



blinking = False
blinktime=time.time()
bintervalsec=1
def blinkonoff():
    global points, blinking
    for i in points:
        if blink==True and blinking==False:
            ncolor=[0,0,0]
        else:
            ncolor= i['color']
        draw_points(i["x"],i["y"],ncolor)

    glutSwapBuffers()


def animate():
    global blinktime, blinking, bintervalsec
    livetime= time.time()
    pmovement()

    if blink == True and freeze== False:
        if livetime-blinktime > bintervalsec:
            blinking = not blinking
            blinktime = livetime

    glutPostRedisplay()


def showScreen():
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    #=====================
    drawbox()
    blinkonoff()
    #======================
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b" A1 T2 ") #window name
glutDisplayFunc(showScreen)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutKeyboardFunc(keyBoardListener)
glutIdleFunc(animate)
glutMainLoop()