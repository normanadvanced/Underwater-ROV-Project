import os
os.system("printf 'raspberry\n' | sudo -S pigpiod")
from socket import *
from time import sleep
from codecs import decode
import pigpio
import threading
#import SharedFunctions

#os.system("printf 'raspberry \n' | sudo -S python3 HornClient.py &")

HOST = 'NARROVCommandModule.local'
PORT = 5007
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

pi = pigpio.pi()
ESCRIGHT = 5
ESCLEFT = 21
ESCBACK = 13 #unknown so far
ESCFRONT = 27 #also still known so far

horizontalSpeed = 1488    #the speed determined by r1 and l1
verticalSpeed = 1488
rightSpeed = 1488    #the speed that the right motor is moving at
leftSpeed = 1488    #the speed that the left motor is moving at
frontSpeed = 1488
backSpeed = 1488


started = False        #Checks if the motors should be able to move or not

rightHatPressed = False    #Checks if the right hat has been pressed
leftHatPressed = False    #Checks if the left hat has been pressed
upHatPressed = False    #Checks if the up hat has been pressed
downHatPressed = False    #Checks if the down hat has been pressed
leftJoystickLeft = False    #Checks if the left joystick has been moved to the left
leftJoystickRight = False    #Checks if the left joystick has been moved to the right
turbo = 1        #Checks if the turns need to be moved turbo

trianglePress = 0

while True:
    try:
        server = socket(AF_INET, SOCK_STREAM)
        server.connect(ADDRESS)
        break
    except:
        pass





def _triangle():        #please look at Chris/Pranav. Not nessecery for movement
    trianglePress = 1
def _triangleReleased():
    trianglePress = 0
    
def _circle():
    '''starts the translational motors'''
    global started
    if not started:
        #speed = 1488
        started = True
        #pi.set_servo_pulsewidth(ESCRIGHT, speed)
        #pi.set_servo_pulsewidth(ESCLEFT, speed)
        print("Started")
    elif started:
        started = False
        #speed = 1488
        print("Stopped")
        
        
    
def _r1(): #Increases horizontal speed
    global horizontalSpeed
    if started == True:
        if horizontalSpeed < 1990:
            horizontalSpeed += 10
        else:
            horizontalSpeed = 1998   
        print("base: ", horizontalSpeed)

def _l1(): 
    '''Decreases horizontal speed'''
    global horizontalSpeed
    if started == True:
        if horizontalSpeed > 708:
            horizontalSpeed -= 10
        else:
            horizontalSpeed = 708
        print("base: ", horizontalSpeed)
    
def _r2(magnitude): 
    '''Goes up'''
    global verticalSpeed
    if started == True:
        verticalSpeed = 1488 + 255 * magnitude
        frontSpeed = verticalSpeed
        backSpeed = verticalSpeed
    
def _l2(magnitude): 
    '''Goes down'''
    if started == True:
        verticalSpeed = 1488 - 255 * magnitude
        frontSpeed = verticalSpeed
        backSpeed = verticalSpeed

def _leftHat():
    '''makes the robot do a pivot turn to the left'''
    global leftSpeed
    global rightSpeed
 
    leftSpeed = 1388
    rightSpeed = 1588

def _rightHat():
    '''makes the robot do a pivot turn to the right'''
    global rightSpeed
    global leftSpeed
    leftSpeed = 1588
    rightSpeed = 1388

def _noHorizontalHatOrJoystick():
    '''Makes the robot drive straight again'''
    global leftSpeed
    global rightSpeed
    global horizontalSpeed
    
    leftSpeed = horizontalSpeed
    rightSpeed = horizontalSpeed

def _upHat():
    '''makes the robot pitch up'''
    global backSpeed
    global frontSpeed
    backSpeed = 1438
    frontSpeed = 1538

def _downHat():
    '''makes the robot pitch down'''
    global backSpeed
    global frontSpeed
    backSpeed = 1538
    frontSpeed = 1438

def _noVerticalHat():
    '''makes the robot stop pitching'''
    global backSpeed
    global frontSpeed
    global verticalSpeed
    
    backSpeed = verticalSpeed
    frontSpeed = verticalSpeed

def _leftJoystickRight():
    '''makes the robot move to the right'''
    global rightSpeed
    global horizontalSpeed
    global leftSpeed
    print("the left joystick was moved to the right")
    if horizontalSpeed > 1488:
        rightSpeed = horizontalSpeed - 200 * turbo
    if horizontalSpeed < 1488:
        leftSpeed = horizontalSpeed + 200 * turbo

def _leftJoystickLeft():
    '''makes the robot move to the left'''
    global horizontalSpeed
    global leftSpeed
    global rightSpeed
    print("the left joystick was moved to the left")
    if horizontalSpeed > 1488:
        leftSpeed = horizontalSpeed - 200 * turbo
    print("LEFTSPEED" + str(leftSpeed))
    if horizontalSpeed < 1488:
        rightSpeed = horizontalSpeed + 200 * turbo

def _center():
    '''makes the robot shoot up at full speed'''
    print("OFF")




def _calibrate(time):
    '''calibrates the robot's distance'''
    print("the calibrate function has been called")
    #listen for the sound
    #get the time when it hears the sound
    #compare the recieved time to the time sent and set that to a variable



cont_data = open('controller_data.txt', 'a')
cont_data.seek(0)   # clears file
cont_data.truncate()

while True:
    button = decode(server.recv(BUFSIZE), "ascii")
    print(button)

    cont_data.write(str([frontSpeed, backSpeed, leftSpeed, rightSpeed, trianglePress]) + '\n')
    cont_data.flush()
    if os.path.getsize('controller_data.txt') > 1000000: # clears if the file is over 1 MB
        cont_data.seek(0)
        cont_data.truncate()

    try:
        analogButton = float(button)
        analogButton = round(analogButton, 4)
        if analogButton < 2.5 and analogButton > -2.5:
            if analogButton < 0:
                _l2(analogButton)
            else:
                _r2(analogButton)

    except ValueError:
        if button == "circle":
            _circle()

        elif button == "x":
            _x()
            # started = False
            # print("got this far")

        elif button == "square":
            _square()

        elif button == "triangle":
            _triangle()
            
        elif button == "triangleReleased":
            _triangleReleased()

        elif button == "center":
            _center()
            server.close()
            break

        elif button == "r1":
            _r1()

        elif button == "l1":
            _l1()

        elif button == "upHatPressed":
            upHatPressed = True
            downHatPressed = False
        elif button == "downHatPressed":
            downHatPressed = True
            upHatPressed = False
        elif button == "no vertical hat pressed":
            upHatPressed = False
            downHatPressed = False

        elif button == "left":
            leftJoystickLeft = True
        elif button == "right":
            leftJoystickRight = True
        elif button == "not left or right":
            leftJoystickRight = False
            leftJoystickLeft = False
        elif button == "leftJoystickPressed":
            turbo = 2
        elif button == "leftJoystickReleased":
            turbo = 1
            
        elif button == "rightHatPressed":
            rightHatPressed = True
            leftHatPressed = False
        elif button == "leftHatPressed":
            leftHatPressed = True
            rightHatPressed = False
        elif button == "no horizontal hat pressed":
            rightHatPressed = False
            leftHatPressed = False

        if upHatPressed:
            _upHat()
        elif downHatPressed:
            _downHat()
        else:
            _noVerticalHat()

        if rightHatPressed:
            _rightHat()
        elif leftHatPressed:
            _leftHat()
        elif leftJoystickRight:
            _leftJoystickRight()
        elif leftJoystickLeft:
            _leftJoystickLeft()
        else:
            _noHorizontalHatOrJoystick()

        if started:
            pi.set_servo_pulsewidth(ESCRIGHT, rightSpeed)
            pi.set_servo_pulsewidth(ESCLEFT, leftSpeed)
            pi.set_servo_pulsewidth(ESCFRONT, frontSpeed)
            pi.set_servo_pulsewidth(ESCBACK, backSpeed)
        else:
            pi.set_servo_pulsewidth(ESCRIGHT, 1488)
            pi.set_servo_pulsewidth(ESCLEFT, 1488)
            pi.set_servo_pulsewidth(ESCFRONT,1488)
            pi.set_servo_pulsewidth(ESCBACK, 1488)
