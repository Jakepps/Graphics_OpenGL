#tree
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import decimal

global xrot  
global yrot        
global ambient      
global greencolor  
global treecolor   
global ballcolor
global lightpos   

#def float_range(start, stop, step):
#  while start < stop:
#    yield float(start)
#    start += decimal.Decimal(step)

def init():
    global xrot    
    global yrot        
    global ambient    
    global greencolor   
    global treecolor   
    global ballcolor
    global lightpos     

    xrot = 0.0                          
    yrot = 0.0                          
    ambient = (1.0, 1.0, 1.0, 1)       
    greencolor = (0.2, 0.8, 0.0, 0.8)   
    treecolor = (0.9, 0.6, 0.3, 0.8)  
    ballcolor=(0.9,0.0,0.0,1)
    lightpos = (1.0, 1.0, 1.0)        

    glClearColor(0.5, 0.5, 0.5, 1.0)                
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)               
    glRotatef(-90, 1.0, 0.0, 0.0)                   
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient) 
    glEnable(GL_LIGHTING)                         
    glEnable(GL_LIGHT0)                           
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)   



def specialkeys(key, x, y):
    global xrot
    global yrot
    if key == GLUT_KEY_UP: 
        xrot -= 2.0
    if key == GLUT_KEY_DOWN: 
        xrot += 2.0 
    if key == GLUT_KEY_LEFT:
        yrot -= 2.0 
    if key == GLUT_KEY_RIGHT: 
        yrot += 2.0
    glutPostRedisplay()

def draw():
    global xrot
    global yrot
    global lightpos
    global greencolor
    global treecolor

    glClear(GL_COLOR_BUFFER_BIT)                               
    glPushMatrix()                                             
    glRotatef(xrot, 1.0, 0.0, 0.0)                             
    glRotatef(yrot, 0.0, 1.0, 0.0)                              
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)                

    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, treecolor)
    glTranslatef(0.0, 0.0, -0.7)                              
    glutSolidCylinder(0.1, 0.2, 20, 20)

    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, greencolor)
    glTranslatef(0.0, 0.0, 0.2) 
    glutSolidCone(0.5, 0.5, 20, 20)            
    glTranslatef(0.0, 0.0, 0.3)
    glutSolidCone(0.4, 0.4, 20, 20) 
    glTranslatef(0.0, 0.0, 0.3)     
    glutSolidCone(0.3, 0.3, 20, 20) 

    glMaterialfv(GL_FRONT_AND_BACK,GL_DIFFUSE,ballcolor)
    glTranslatef(0.0,0.0,0.3)
    glutSolidSphere(0.06,20,20)
    
    glPopMatrix()
    glutSwapBuffers()                                          

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

glutInitWindowSize(500, 500)
glutInitWindowPosition(50, 50)

glutInit(sys.argv)
glutCreateWindow(b"Tree")

glutDisplayFunc(draw)
glutSpecialFunc(specialkeys)

init()
glutMainLoop()