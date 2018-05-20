import pygame
import pywavefront
import pyglet
from pyglet.gl import *
import ctypes

rotation = 0
meshes = pywavefront.Wavefront("ROV_assembly_oriented_05.obj")
meshes.draw()

temperature = 0
depth = 0
roll = yaw = pitch = 0

window = pyglet.window.Window(600, 500)

lightfv = ctypes.c_float * 4


@window.event
def on_resize(width, height):
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(600., float(width) / height, 10., 1000.)
  glMatrixMode(GL_MODELVIEW)
  return True


@window.event
def on_draw():

  window.clear()
  glLoadIdentity()

  glLightfv(GL_LIGHT0, GL_POSITION, lightfv(-1.0, 1.0, 1.0, 0.0))
  glEnable(GL_LIGHT0)

  glTranslated(0, 150, -500)
  glRotatef(float(yaw), 0, 1, 0)
  glRotatef(float(pitch), 1, 0, 0)
  glRotatef(float(roll), 0, 0, 1)
  glEnable(GL_LIGHTING)
  #print("redrawn")
  #print(roll, pitch, yaw)
  #print("Depth: %.2f" % depth, "Temperature: %.2f" % temperature)

  meshes.draw()


def update(dt):
  global rotation
  global roll, pitch, yaw, temperature, depth
  rotation += 10 * dt
  if rotation > 720:
    rotation = 0

  f = open('data.txt', 'r')
  data = (f.readlines()[-1])[1:-2].split(',')
  #print(data[0])
  pitch = float(data[0])
  roll = float(data[1])
  yaw = float(data[2])
  temperature = data[3]
  depth = [data[4]]
  f.close()


pyglet.clock.schedule(update)

pyglet.app.run()


