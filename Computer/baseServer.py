from socket import *
from codecs import *
import os
import pygame
import time
import sys
import threading

#we can clear the que with pygame.event.clear()
#pygame.event.wait() stops the program until an event becomes available

#os.system("echo '$(<~/password.txt)' | sudo -S python3 hornServer.py &")

#stuff needed for the server
HOST = str(os.popen("echo $(getent hosts NARROVCommandModule.local |cut -f1 -d ' ')").readline())
#HOST = '169.254.208.126'
print("Host is " + HOST)
PORT = 5006
ADDRESS = (HOST, PORT)
server = socket(AF_INET, SOCK_DGRAM)
#server.bind(ADDRESS)
print("Go!")
#keeps trying to connect to the joystick until it succeeds


pygame.init()
pygame.joystick.init()
while True:
    try:
        j = pygame.joystick.Joystick(0)
        j.init()
        joysticks = pygame.joystick.get_count()
        print(joysticks)
        #if joysticks < 1:
        #          raise ValueError
        #else:
        #    print("break")
        break
    except:
        sys.exit(1)
pygame.display.init()
screen = pygame.display.set_mode((1,1))


#print("Waiting for connection controller . . .")
#client, address = server.accept()
#print("ControllerCLi connected from: ", address)


#pygame.event.setBlocked

#all of the analog buttons on the controller
LJOYY_AXIS = 1
LJOYX_AXIS = 0
RJOYY_AXIS = 4
RJOYX_AXIS = 3
R2_AXIS = 5
L2_AXIS = 2
R2_BUTTON = 7
L2_BUTTON = 6

lJOY_MOVED = False
rJOY_MOVED = False
l2Pressed = False
r2Pressed = False
l2Released = True
r2Released = True

centerSent = False
timeCenterPressed = 0
upHatPressed = False
downHatPressed = False
rightHatPressed = False
leftHatPressed = False
lValue = 0
rValue = 0
lastRValue=0
lastLValue=0
done = False

try:

    while not done:
        server.sendto((bytes(" ", "ascii")),ADDRESS)
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                # print(event.dict, event.joy, event.button, "pressed")
                if event.button == 1:
                    server.sendto((bytes("circle", "ascii")),ADDRESS)
                elif event.button == 2:
                    server.sendto((bytes("triangle", "ascii")),ADDRESS)
                #elif event.button == 3:
                    #pass # we don't use square
                    #client.send(bytes("square", "ascii"))
                elif event.button == 0:
                    pass # we don't use x
                    server.sendto((bytes("x", "ascii")),ADDRESS)
                elif event.button == 4:
                    server.sendto(bytes("l1", "ascii"),ADDRESS)
                elif event.button == 5:
                    server.sendto((bytes("r1", "ascii")),ADDRESS)
                elif event.button == 10:
                    if not centerSent:
                        timeCenterPressed = time.time()
                        print(time.time())
                    else:
                        centerSent = False
                        server.sendto((bytes("center", "ascii")),ADDRESS)
                        os.system("cd ~/Underwater-ROV-Project/ && bash ~/Underwater-ROV-Project/cleanup.sh")
          #      elif event.button == 7:
          #          r2Pressed = True
          #      elif event.button == 6:
          #          l2Pressed = True
                elif event.button == 11:
                    server.sendto((bytes("leftJoystickPressed", "ascii")),ADDRESS)
                elif event.button == 12:
                    server.sendto((bytes("rightJoystickPressed", "ascii")),ADDRESS)
            elif event.type == pygame.JOYAXISMOTION:
                if event.axis == LJOYX_AXIS:
                    # print(event.value)
                    if event.value > .6:
                        if lJOY_MOVED == False:
                            server.sendto(bytes("right", "ascii"), ADDRESS)
                            lJOY_MOVED = True
                    elif event.value < -.6 :
                        if lJOY_MOVED == False:
                            server.sendto(bytes("left", "ascii"), ADDRESS)
                            lJOY_MOVED = True
                    else:
                        if lJOY_MOVED == True:
                            server.sendto(bytes("not left or right", "ascii"), ADDRESS)
                            lJOY_MOVED = False
                        if lJOY_MOVED == False:
                            pass
                if event.axis == RJOYY_AXIS:
                    # print(event.value)
                    if event.value < -.6:
                        if rJOY_MOVED == False:
                            server.sendto(bytes("up", "ascii"), ADDRESS)
                            rJOY_MOVED = True
                    elif event.value > .6 :
                        if rJOY_MOVED == False:
                            server.sendto(bytes("down", "ascii"), ADDRESS)
                            rJOY_MOVED = True
                    else:
                        if rJOY_MOVED == True:
                            server.sendto(bytes("not down or up", "ascii"), ADDRESS)
                            rJOY_MOVED = False
                        if rJOY_MOVED == False:
                            pass


            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 10:
                    timeCenterPressed = 0
                elif event.button == 11:
                    server.sendto(bytes("leftJoystickReleased", "ascii"), ADDRESS)
                    print(" ", end=" ")
                elif event.button == 12:
                    server.sendto(bytes("rightJoystickReleased", "ascii"), ADDRESS)
                elif event.button == 2:                    #JUST ADDED THIS FOR MY PROGRAM. YOU MAY BE ABLE TO DELETE
                    server.sendto(bytes("triangleReleased", "ascii"), ADDRESS)
         #       elif event.button == L2_BUTTON:
         #           l2Released = True
         #           l2Pressed = False
         #       elif event.button == R2_BUTTON:
         #           r2Released = True
         #           r2Pressed = False
            elif event.type == pygame.JOYHATMOTION:
                print((event.joy, event.hat, event.value))
                if event.value[0] == 1:
                    server.sendto(bytes("rightHatPressed", "ascii"), ADDRESS)
                    print(" ", end=" ")
                elif event.value[0] == -1:
                    server.sendto(bytes("leftHatPressed", "ascii"), ADDRESS)
                    print(" ", end=" ")
                    # elif event.value[0] == 0:
                    #client.send(bytes("no horizontal hat pressed", "ascii"))
                    #print("", end="")

                elif event.value[1] == 1:
                    server.sendto(bytes("upHatPressed", "ascii"), ADDRESS)
                   # client.send(bytes("no horizontal hat pressed", "ascii"))
                    print(" ", end=" ")
                elif event.value[1] == -1:
                    server.sendto(bytes("downHatPressed", "ascii"), ADDRESS)
                   # client.send(bytes("no horizontal hat pressed", "ascii"))
                    print(" ", end=" ")
                else:
                    #client.send(bytes("no vertical hat pressed", "ascii"))
                    server.sendto(bytes("no hat pressed", "ascii"), ADDRESS)
                    print("no hat")
        if timeCenterPressed + 5 < time.time() and timeCenterPressed != 0 and not centerSent:
            print(time.time() - timeCenterPressed)
            timeCenterPressed = 0
            server.sendto(bytes("center", "ascii"), ADDRESS)
            done = True
            centerSent = True

        #if r2Pressed == True:
        #    lastRValue = rValue
        #    rValue = j.get_axis(R2_AXIS)
        #    if rValue > -1 and rValue <= 1 or lastRValue == -1:
        #        print(rValue)  # someone should really figure out why this is needed
        #        print("", end="")
        #        client.send(bytes(str(round(((lValue + 1)*-1),4))+"\n", "ascii"))
        #        timer = time.time()
        #        while timer + .01 > time.time():
        #            pass
        #    if lastRValue == -1 or lastRValue == -10 and rValue == -1:
        #        rValue = -10

        #if l2Pressed == True:
        #    lastLValue = lValue
        #    lValue = j.get_axis(L2_AXIS)
        #    if lValue > -1 and lValue <= 1 or lastLValue == -1:
        #        print(lValue)
        #        print("", end="")
        #        client.send(bytes(str(round(((lValue + 1)*-1),4))+"\n", "ascii"))
        #        timer = time.time()
        #        while timer + .01 > time.time():
        #            pass
        #    if lastLValue == -1 or lastLValue == -10 and lValue == -1:
        #        lValue = -10
        #if r2Released == True:
        #    client.send(bytes("0","ascii"))
        #    r2Released = False
        #if l2Released == True:
        #    client.send(bytes("0","ascii"))
        #    l2Released = False
except:
    server.shutdown(SHUT_RWDR)
    server.close()
    print("Controller Server Closed")
    os.system("cd ~/Underwater-ROV-Project/ && bash ~/Underwater-ROV-Project/cleanup.sh")
