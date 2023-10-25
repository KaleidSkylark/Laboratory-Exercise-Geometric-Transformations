import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
pygame.display.set_caption("04 Lab 1 - Janabajab")
glEnable(GL_DEPTH_TEST)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0, 0, -5)

def draw_cube():
    glBegin(GL_TRIANGLES)
    
    # Face 1
    glColor3f(148,0,211)
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)
    
    # Face 2
    glColor3f(0, 0, 255)
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, -1, 1)
    
    # Face 3
    glColor3f(150, 20, 0)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)
    
    # Face 4
    glColor3f(0, 180, 69)
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, -1)
    
    # Face 5
    glColor3f(0, 70, 96)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)
    
    # Face 6
    glColor3f(0, 140, 0)
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, -1, -1)

    glEnd()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                glTranslatef(-1, 0, 0)
            if event.key == pygame.K_w:
                glTranslatef(0, 0, 1)
            if event.key == pygame.K_d:
                glTranslatef(1, 0, 0)
            if event.key == pygame.K_s:
                glTranslatef(0, 0, -1)
            if event.key == pygame.K_q:
                glScalef(0.5, 0.5, 0.5)
            if event.key == pygame.K_e:
                glScalef(2, 2, 2)
    glRotatef(1, 1, 0.3, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_cube()
    pygame.display.flip()
    pygame.time.wait(15)
