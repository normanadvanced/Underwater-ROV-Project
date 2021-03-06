from socket import *
from codecs import *
import pygame
import time

import serial
import threading

horn = serial.Serial('/dev/ttyACM0', 115200, timeout=.1)  # COM4 for windows, /dev/ttyAMC0

#we can clear the que with pygame.event.clear()
#pygame.event.wait() stops the program until an event becomes available

#all of the analog buttons on the controller
LJOYY_AXIS = 1
LJOYX_AXIS = 0
RJOYY_AXIS = 5
RJOYX_AXIS = 2
R2_AXIS = 4
L2_AXIS = 3

l2Pressed = False
r2Pressed = False
centerSent = False
timeCenterPressed = 0
upHatPressed = False
downHatPressed = False
rightHatPressed = False
leftHatPressed = False
lValue = 0
rValue = 0

#stuff needed for the server
HOST = "169.254.208.126"
PORT = 5000
ADDRESS = (HOST, PORT)
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(1)

#keeps trying to connect to the joystick until it succeeds
while True:
    try:
        pygame.init()
        j = pygame.joystick.Joystick(0)
        j.init()
        pygame.display.init()
        screen = pygame.display.set_mode((1,1))
        break
    except:
        os.system("sudo killall 'sudo ds4drv'")
        os.system("sudo ds4drv")
        print("Please connect Joystick.")
        time.sleep(5)
#debug for server connection
print("Waiting for connection . . .")
client, address = server.accept()
print("connected from: ", address)

done = False

#pygame.event.setBlocked


def create_horn():
    while True:
        if str(horn.readline())[2:-5] == 'Honk':
            honk_time = "Honk time: " + str(time.time())
            client.send(bytes(honk_time, "ascii"))

horn_thread = threading.Thread(target=create_horn())
horn_thread.daemon = True
horn_thread.start()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            # print(event.dict, event.joy, event.button, "pressed")
            if event.button == 3:
                client.send(bytes("triangle", "ascii"))
            elif event.button == 0:
                client.send(bytes("square", "ascii"))
            elif event.button == 1:
                client.send(bytes("x", "ascii"))
            elif event.button == 4:
                client.send(bytes("l1", "ascii"))
            elif event.button == 5:
                client.send(bytes("r1", "ascii"))
            elif event.button == 13:
                if not centerSent:
                    timeCenterPressed = time.time()
                    print(time.time())
                else:
                    centerSent = False
                    client.send(bytes("center", "ascii"))
            elif event.button == 2:
                client.send(bytes("circle", "ascii"))
            elif event.button == 7:
                r2Pressed = True
            elif event.button == 6:
                l2Pressed = True
            elif event.button == 10:
                client.send(bytes("leftJoystickPressed", "ascii"))

        elif event.type == pygame.JOYAXISMOTION:
            if event.axis == 0:
                # print(event.value)
                if event.value > .6:
                    client.send(bytes("right", "ascii"))
                elif event.value < -.6:
                    client.send(bytes("left", "ascii"))
                else:
                    client.send(bytes("not left or right", "ascii"))

        elif event.type == pygame.JOYBUTTONUP:
            if event.button == 13:
                timeCenterPressed = 0
            elif event.button == 10:
                client.send(bytes("leftJoystickReleased", "ascii"))
                print("", end="")

        elif event.type == pygame.JOYHATMOTION:
            print((event.joy, event.hat, event.value))
            if event.value[0] == 1:
                client.send(bytes("rightHatPressed", "ascii"))
                print("", end="")
            elif event.value[0] == -1:
                client.send(bytes("leftHatPressed", "ascii"))
                print("", end="")
                # elif event.value[0] == 0:
            #	client.send(bytes("no horizontal hat pressed", "ascii"))
            #	print("", end="")

            elif event.value[1] == 1:
                client.send(bytes("upHatPressed", "ascii"))
                client.send(bytes("no horizontal hat pressed", "ascii"))
                print("", end="")
            elif event.value[1] == -1:
                client.send(bytes("downHatPressed", "ascii"))
                client.send(bytes("no horizontal hat pressed", "ascii"))
                print("", end="")
            else:
                client.send(bytes("no verticle hat pressed", "ascii"))
                client.send(bytes("no horizontal hat pressed", "ascii"))
                print("this actually did go off??!")

    if timeCenterPressed + 5 < time.time() and timeCenterPressed != 0 and not centerSent:
        print(time.time() - timeCenterPressed)
        timeCenterPressed = 0
        client.send(bytes("center", "ascii"))
        done = True
        centerSent = True

    if r2Pressed == True:
        lastRValue = rValue
        rValue = j.get_axis(R2_AXIS)
        if rValue > -1 and rValue <= 1 or lastRValue == -1:
            print(rValue)  # someone should really figure out why this is needed
            print("", end="")
            client.send(bytes(str(rValue + 1), "ascii"))
            timer = time.time()
            while timer + .01 > time.time():
                pass
        if lastRValue == -1 or lastRValue == -10 and rValue == -1:
            rValue = -10

    if l2Pressed == True:
        lastLValue = lValue
        lValue = j.get_axis(L2_AXIS)
        if lValue > -1 and lValue <= 1 or lastLValue == -1:
            print(lValue)
            print("", end="")
            client.send(bytes(str((lValue + 1) * -1), "ascii"))
            timer = time.time()
            while timer + .01 > time.time():
                pass
        if lastLValue == -1 or lastLValue == -10 and lValue == -1:
            lValue = -10
