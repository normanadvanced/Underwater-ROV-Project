import serial
#from serial import serial
from multiprocessing import Process,Queue,Pipe
from raw_data import pass_data

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
while True:
  try:

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
      print("redrawn")
      print(roll, pitch, yaw)
      print("Depth: %.2f" % depth, "Temperature: %.2f" % temperature)

      meshes.draw()


    def update(dt):
      global rotation
      rotation += 10 * dt
      if rotation > 720: rotation = 0

      global roll, pitch, yaw, temperature, depth

      parent_conn, child_conn = Pipe()
      p = Process(target=pass_data, args=(child_conn,))
      p.start()
      roll = parent_conn.recv()[0]
      pitch = parent_conn.recv()[1]
      yaw = parent_conn.recv()[2]
      temperature = parent_conn.recv()[3]
      depth = parent_conn.recv()[4]


    pyglet.clock.schedule(update)

    pyglet.app.run()



  except IndexError:
    print("")
  except TypeError:
    print("")
  except ValueError:
    print("")
