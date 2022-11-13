from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global xrot        
global yrot        
global zrot
global ambient     
global wormcolor    
global legscolor
global earscolor
global lightpos     

def drawBody():
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)  
    glRotatef(yrot, 0.0, 1.0, 0.0)  
    
    glMaterialfv(GL_FRONT, GL_DIFFUSE, wormcolor)
    glTranslatef(0.0, 0.0, -0.5)
    quadratic = gluNewQuadric()
    gluSphere(quadratic, 0.35, 100, 100)
    
    glTranslatef(0.0, 0.0, 0.5)            
    gluSphere(quadratic, 0.35, 100, 100)

    glTranslatef(0.0, 0.0, 0.6)            
    gluSphere(quadratic, 0.35, 100, 100)

    glPopMatrix() 
    
def drawEyes():
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)  
    glRotatef(yrot, 0.0, 1.0, 0.0)  
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (1,1,1,1))
    quadratic = gluNewQuadric()
    glTranslatef(0.15, -0.125, -0.8)
    gluSphere(quadratic, 0.1, 100, 100)
    glPopMatrix() 
    
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)  
    glRotatef(yrot, 0.0, 1.0, 0.0)  
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (1,1,1,1))
    quadratic = gluNewQuadric()

    glTranslatef(-0.15, -0.125, -0.8)
    gluSphere(quadratic, 0.1, 100, 100)
    glPopMatrix() 
    
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)  
    glRotatef(yrot, 0.0, 1.0, 0.0)  
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0,0,0,1))
    quadratic = gluNewQuadric()
    glTranslatef(0.1, -0.125, -0.9)
    gluSphere(quadratic, 0.05, 100, 100)
    glPopMatrix() 
        
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)  
    glRotatef(yrot, 0.0, 1.0, 0.0)  
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0,0,0,1))
    quadratic = gluNewQuadric()
    glTranslatef(-0.1, -0.125, -0.9)
    gluSphere(quadratic, 0.05, 100, 100)
    
    glPopMatrix() 
 

def drawLegs():
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)  
    glRotatef(yrot, 0.0, 1.0, 0.0)  
    glRotatef(90, 1.0, 0.0, 0.0)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, legscolor)
    quadratic = gluNewQuadric()
    
    glTranslatef(0.25, -0.5, -0.6)
    gluCylinder(quadratic, 0.05, 0.05, 0.5, 100, 100) 
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)  
    glRotatef(yrot, 0.0, 1.0, 0.0)  
    glRotatef(90, 1.0, 0.0, 0.0)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, legscolor)
    quadratic = gluNewQuadric()
    
    glTranslatef(-0.25, -0.5, -0.6)
    gluCylinder(quadratic, 0.05, 0.05, 0.5, 100, 100) 
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)  
    glRotatef(yrot, 0.0, 1.0, 0.0)  
    glRotatef(90, 1.0, 0.0, 0.0)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, legscolor)
    quadratic = gluNewQuadric()
    
    glTranslatef(0.25, 0.5, -0.6)
    gluCylinder(quadratic, 0.05, 0.05, 0.5, 100, 100) 
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)  
    glRotatef(yrot, 0.0, 1.0, 0.0)  
    glRotatef(90, 1.0, 0.0, 0.0)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, legscolor)
    quadratic = gluNewQuadric()
    
    glTranslatef(-0.25, 0.5, -0.6)
    gluCylinder(quadratic, 0.05, 0.05, 0.5, 100, 100) 
    glPopMatrix() 
    #################
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)  
    glRotatef(yrot, 0.0, 1.0, 0.0)  
    glRotatef(90, 1.0, 0.0, 0.0)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, legscolor)
    quadratic = gluNewQuadric()
    
    glTranslatef(-0.25, 0.05, -0.6)
    gluCylinder(quadratic, 0.05, 0.05, 0.5, 100, 100) 
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)  
    glRotatef(yrot, 0.0, 1.0, 0.0)  
    glRotatef(90, 1.0, 0.0, 0.0)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, legscolor)
    quadratic = gluNewQuadric()
    
    glTranslatef(0.25, 0.05, -0.6)
    gluCylinder(quadratic, 0.05, 0.05, 0.5, 100, 100) 
    glPopMatrix()

def drawEars():
    glPushMatrix()
    glRotatef(xrot, 1.0, 0.0, 0.0)  
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glRotatef(zrot, 0.0, 0.0, 1.0)  
    glRotatef(30, 1.0, 0.0, 0.0)
    glRotatef(30, 0.0, 1.0, 0.0)
    glRotatef(30, 0.0, 0.0, 1.0)
    glTranslatef(0.05, -0.5, -0.1)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, earscolor)
    quadratic = gluNewQuadric()
    
    gluCylinder(quadratic, 0.025, 0.025, 0.3, 100, 100) 
    glPopMatrix()
    
    glPushMatrix()
    glRotatef(xrot, 1.0, 0.0, 0.0)  
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glRotatef(zrot, 0.0, 0.0, 1.0)  
    glRotatef(30, 1.0, 0.0, 0.0)
    glRotatef(-30, 0.0, 1.0, 0.0)
    glRotatef(30, 0.0, 0.0, 1.0)
    glTranslatef(-0.5, -0.25, -0.15)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, earscolor)
    quadratic = gluNewQuadric()
    
    gluCylinder(quadratic, 0.025, 0.025, 0.3, 100, 100) 
    glPopMatrix()
    

def init():
    global xrot         
    global yrot         
    global zrot
    global ambient   
    global legscolor  
    global wormcolor 
    global earscolor  
    global lightpos    

    xrot = 0.0                    
    yrot = 0.0                    
    zrot = 0.0
    ambient = (1.0, 1.0, 1.0, 1)      
    wormcolor = (0, 0.27058824, 0.14117647,0.8)   
    legscolor = (0.15686275,0.44705882,0.2)
    earscolor = (0.18431373,0.27058824,0.21960784)
    lightpos = (2, -2, 0)      

    glClearColor(0.5, 0.5, 0.5, 1.0)                
    gluOrtho2D(-1.5, 1.5, -1.5, 1.5)                
    glRotatef(-90, 1.0, 0.0, 0.0)                
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient) 
    glEnable(GL_LIGHTING)                       
    glEnable(GL_LIGHT0)                           
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)   
    glEnable(GL_DEPTH_TEST)


def specialkeys(key, x, y):
    global xrot
    global yrot
    if key == GLUT_KEY_UP:      
        xrot -= 4.0            
    if key == GLUT_KEY_DOWN:    
        xrot += 4.0             
    if key == GLUT_KEY_LEFT:   
        yrot -= 4.0            
    if key == GLUT_KEY_RIGHT:   
        yrot += 4.0            

    glutPostRedisplay()      


def draw():
    global xrot
    global yrot
    global zrot
    global lightpos
    global legscolor
    global wormcolor
    global earscolor

    #glClear(GL_COLOR_BUFFER_BIT) 
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)                

    drawBody()  
    drawEyes()
    drawLegs()
    drawEars()
    glutSwapBuffers()


glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutInitWindowPosition(50, 50)

glutInit(sys.argv)

glutCreateWindow(b"Worm")

glutDisplayFunc(draw)

glutSpecialFunc(specialkeys)

init()

glutMainLoop()