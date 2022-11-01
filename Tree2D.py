from tokenize import Double
import pygame as pygame
import random as random

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class point:
    x: float
    y: float
    z: float
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
def cube(p1: point,p2: point, scale): #p1-левая верхняя передняя
    width = p2.x - p1.x
    height = p2.y - p1.y
    depth = p2.z - p1.z
    width *= scale
    height *= scale
    depth *= scale
    
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_QUADS)
    glVertex3f(p1.x * scale, p1.y * scale, p1.z * scale)
    glVertex3f(p1.x * scale + width, p1.y * scale, p1.z * scale)
    glVertex3f(p1.x * scale + width, p1.y * scale + height, p1.z * scale)
    glVertex3f(p1.x * scale, p1.y * scale + height, p1.z * scale)
    glEnd()
    
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_QUADS)
    glVertex3f(p1.x * scale, p1.y * scale, p1.z * scale)
    glVertex3f(p1.x * scale + width, p1.y * scale, p1.z * scale)
    glVertex3f(p1.x * scale + width, p1.y * scale, p1.z * scale + depth)
    glVertex3f(p1.x * scale, p1.y * scale, p1.z * scale + depth)
    glEnd()
    
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_QUADS)
    glVertex3f(p1.x * scale, p1.y * scale, p1.z * scale)
    glVertex3f(p1.x * scale, p1.y * scale + height, p1.z * scale)
    glVertex3f(p1.x * scale, p1.y * scale + height, p1.z * scale + depth)
    glVertex3f(p1.x * scale, p1.y * scale, p1.z * scale + depth)
    glEnd()
    
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_QUADS)
    glVertex3f(p1.x * scale + width, p1.y * scale + height, p1.z * scale + depth)
    glVertex3f(p1.x * scale, p1.y * scale + height, p1.z * scale + depth)
    glVertex3f(p1.x * scale, p1.y * scale, p1.z * scale + depth)
    glVertex3f(p1.x * scale + width, p1.y * scale, p1.z * scale + depth)
    glEnd()
    
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_QUADS)
    glVertex3f(p1.x * scale + width, p1.y * scale + height, p1.z * scale + depth)
    glVertex3f(p1.x * scale, p1.y * scale + height, p1.z * scale + depth)
    glVertex3f(p1.x * scale, p1.y * scale + height, p1.z * scale)
    glVertex3f(p1.x * scale + width, p1.y * scale + height, p1.z * scale)
    glEnd()
    
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_QUADS)
    glVertex3f(p1.x * scale + width, p1.y * scale + height, p1.z * scale + depth)
    glVertex3f(p1.x * scale + width, p1.y * scale, p1.z * scale + depth)
    glVertex3f(p1.x * scale + width, p1.y * scale, p1.z * scale)
    glVertex3f(p1.x * scale + width, p1.y * scale + height, p1.z * scale)

    glEnd()
        
def main():
    scale = 1.0 / 10.0

    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), scale * 2, 100)
    
    glTranslatef(scale * -2.5,scale * -2.5, -2)
    glEnable(GL_DEPTH_TEST)
    
    while True:        
        keys=pygame.key.get_pressed()
        
        glTranslatef(scale * 2.5,scale * 2.5, 0)
        if keys[K_LEFT]:
            glRotate(-0.2, 0, 0, 1)
        if keys[K_RIGHT]:
            glRotate(0.2, 0, 0, 1)
        if keys[K_UP]:
            glRotate(-0.2, 1, 0, 0)
        if keys[K_DOWN]:
            glRotate(0.2, 1, 0, 0)
        if keys[K_a]:
            glRotate(-0.2, 0, 1, 0)
        if keys[K_d]:
            glRotate(0.2, 0, 1, 0)
        glTranslatef(scale * -2.5,scale * -2.5, 0)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glRotate(0, 0, 0, 0)

        glColor3f(0.301960078,0.13333333,0.05490196)        
        cube(point(0,0,0),point(1,1,1),scale)
        cube(point(0,1,0),point(1,1.5,1),scale)   
        cube(point(0,1.5,0),point(1,2,1),scale)
        cube(point(0,2,0),point(1,2.5,1),scale)
        cube(point(0,2.5,0),point(1,3,1),scale)
        
        glColor3f(0.13333333,0.54509804,0.13333333) 
        cube(point(0,3,0),point(1,4,1),scale)
        cube(point(1,1,0),point(2,2,1),scale)
        cube(point(2,1,0),point(3,2,1),scale)
        cube(point(1,2,0),point(2,3,1),scale)
        
        cube(point(-1,1,0),point(2,2,1),scale)
        cube(point(-2,1,0),point(3,2,1),scale)
        cube(point(-1,2,0),point(2,3,1),scale)
        
        cube(point(0,1,-1),point(1,2,2),scale)
        cube(point(0,2,-1),point(1,3,2),scale)
        
        cube(point(1,1,-1),point(2,2,2),scale)
        cube(point(0,1,-1),point(-1,2,2),scale)

        cube(point(0,1,-2),point(1,2,3),scale)


        glColor3f(255,255,0) 
        cube(point(0.4, 4, 0.4),point(0.6, 5, 0.6),scale) 
        cube(point(0, 4.5, 0.4),point(1, 4.7, 0.6),scale) 

        glColor3f(1,0,0) 
        for i in range (5):
            for j in range (5):
                if (i+j >= 2 and j-i <= 2 and i-j <= 2 and i+j <= 6):
                    cube(point(i-1.7,0.5,j-1.7),point(i-1.3,1,j-1.3),scale)

        #cube(point(2,1,0),point(2,2,1),scale)
        
        pygame.display.flip()
        pygame.time.wait(1)
main()