#flag
import pygame as pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def rect(x0,y0,w,h):
    glTranslate(x0,y0,0)
    glBegin(GL_QUADS)
    glVertex2f(-w, h)
    glVertex2f(w, h)
    glVertex2f(w, -h)
    glVertex2f(-w, -h)
    glEnd()
    glTranslate(-x0,-y0,-0)

def rectDiagLeftWhite(x0,y0):
    glTranslate(x0,y0,0)
    glBegin(GL_POLYGON)
    glVertex2f(-1, 0.7)
    glVertex2f(-1, 1)
    glVertex2f(-0.7, 1)    
    glVertex2f(1, -0.7)
    glVertex2f(1, -1)
    glVertex2f(0.7, -1) 
    glEnd()
    glTranslate(-x0,-y0,-0)

def rectDiagRightWhite(x0,y0):
    glTranslate(x0,y0,0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.7, -1)
    glVertex2f(-1, -1)
    glVertex2f(-1, -0.7)    
    glVertex2f(0.7, 1)
    glVertex2f(1, 1)
    glVertex2f(1, 0.7)
    glEnd()
    glTranslate(-x0,-y0,-0)

def rectDiagRightRed1(x0,y0):
    glTranslate(x0,y0,0)
    glBegin(GL_POLYGON)
    glVertex2f(0.2, 0.2)
    glVertex2f(0.4, 0.2)
    glVertex2f(1, 0.8)
    glVertex2f(1, 1)  
    glEnd()
    glTranslate(-x0,-y0,-0)
  

def rectDiagRightRed2(x0,y0):
    glTranslate(x0,y0,0)
    glBegin(GL_POLYGON)
    glVertex2f(1, -1)
    glVertex2f(0.2, -0.2)
    glVertex2f(0.4, -0.2)
    glVertex2f(1, -0.8)  
    glEnd()
    glTranslate(-x0,-y0,-0)

def rectDiagLeftRed1(x0,y0):
    glTranslate(x0,y0,0)
    glBegin(GL_POLYGON)       
    glVertex2f(-0.4, 0.2)
    glVertex2f(-1, 0.8)
    glVertex2f(-1, 1)
    glVertex2f(-0.2, 0.2)   
    glEnd()
    glTranslate(-x0,-y0,-0)

def rectDiagLeftRed2(x0,y0):
    glTranslate(x0,y0,0)
    glBegin(GL_POLYGON) 
    glVertex2f(-0.4, -0.2)
    glVertex2f(-0.2, -0.2)
    glVertex2f(-1, -1)
    glVertex2f(-1, -0.8)  
    glEnd()
    glTranslate(-x0,-y0,-0)
    
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity(); 
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity() #загрузить единичную матрицу

        glColor3f(0.01568627, 0.1176471, 0.55294118)#синий
        rect(0,0,2,1)

        glColor3f(0.98039216, 0.94901961, 0.9294118)#белый
        rect(0,0,2,0.2)
        rect(0,0,0.2,1) 
        rectDiagLeftWhite(0,0)
        rectDiagRightWhite(0,0)

        glColor3f(0.99607843, 0.02745098, 0.02745098)#красный
        rect(0,0,2,0.1)  
        rect(0,0,0.1,1)
        rectDiagRightRed1(0,0)
        rectDiagRightRed2(0,0)
        rectDiagLeftRed1(0,0)
        rectDiagLeftRed2(0,0) 
        pygame.display.flip()
        pygame.time.wait(1)

main()