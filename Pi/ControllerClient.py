import os
os.system("printf 'raspberry\n' | sudo -S pigpiod")
from socket import *
from time import sleep
from codecs import decode
import pigpio
import threading
#import SharedFunctions

#os.system("printf 'raspberry \n' | sudo -S python3 HornClient.py &")

HOST = os.popen("echo $(getent hosts NARROVCommandModule.local |cut -f1 -d ' ')").readline()
print(HOST)
#HOST='169.254.208.126'
PORT = 5006
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

pi = pigpio.pi()
ESCRIGHT = 13
ESCLEFT = 21
ESCBACK = 27
ESCFRONT = 5

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
rightJoystickUp = False    #Checks if the left joystick has been moved to the left
rightJoystickDown = False    #Checks if the left joystick has been moved to the right
turbo = 1        #Checks if the turns need to be moved turbo
turboVert = 1   #vertical turbo

trianglePress = 0

while True:
    try:
        server = socket(AF_INET, SOCK_STREAM)
        server.bind(ADDRESS)
        break
    except:
        pass





def _triangle():        #please look at Chris/Pranav. Not nessecery for movement
    global trianglePress
    trianglePress = 1
    print("Triangle " + str(trianglePress))
    
def _triangleReleased():
    global trianglePress
    trianglePress = 0
    
def _circle():
    '''starts the translational motors'''
    global started
    if not started:
        #speed = 1488
        started = True
        print("Started")
    elif started:
        started = False
        print("Stopped")
        
        
    
def _r1(): #Increases horizontal speed
    global horizontalSpeed,leftSpeed,rightSpeed
    if started == True:
        if horizontalSpeed < 1990:
            horizontalSpeed += 10
        else:
            horizontalSpeed = 1998   
        print("base: ", horizontalSpeed)
        leftSpeed = horizontalSpeed
        rightSpeed = horizontalSpeed

def _l1(): 
    '''Decreases horizontal speed'''
    global horizontalSpeed, leftSpeed, rightSpeed
    if started == True:
        if horizontalSpeed > 708:
            horizontalSpeed -= 10
        else:
            horizontalSpeed = 708
        print("base: ", horizontalSpeed)
        leftSpeed = horizontalSpeed
        rightSpeed = horizontalSpeed
        print(leftSpeed)
        print(rightSpeed)
    
def _r2(magnitude): 
    '''Goes up'''
    global verticalSpeed, frontSpeed, backSpeed
    if started == True:
        verticalSpeed = 1488 + 255 * magnitude
        frontSpeed = verticalSpeed
        backSpeed = verticalSpeed
    
def _l2(magnitude): 
    '''Goes down'''
    global verticalSpeed, frontSpeed, backSpeed
    if started == True:
        verticalSpeed = 1488 + 390 * magnitude
        frontSpeed = verticalSpeed
        backSpeed = verticalSpeed

def _leftHat():
    '''makes the robot do a pivot turn to the left'''
    global leftSpeed
    global rightSpeed
    if started == True:
        leftSpeed = 1388
        rightSpeed = 1588

def _rightHat():
    '''makes the robot do a pivot turn to the right'''
    global rightSpeed
    global leftSpeed
    if started == True:
        leftSpeed = 1588
        rightSpeed = 1388

def _noHorizontalHatOrJoystick():
    '''Makes the robot drive straight again'''
    global leftSpeed
    global rightSpeed
    global horizontalSpeed
    
    leftSpeed = horizontalSpeed
    rightSpeed = horizontalSpeed
def _noVerticalHatOrJoystick():
    '''Makes the robot drive straight again'''
    global frontSpeed
    global backSpeed
    global verticalSpeed
    
    frontSpeed = verticalSpeed
    backSpeed = verticalSpeed

def _upHat():
    '''makes the robot pitch up'''
    global backSpeed
    global frontSpeed
    if started == True:
        backSpeed = 1438
        frontSpeed = 1538

def _downHat():
    '''makes the robot pitch down'''
    global backSpeed
    global frontSpeed
    if started == True:
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
    if horizontalSpeed >= 1488:
        rightSpeed = horizontalSpeed - 200 * turbo
    if horizontalSpeed < 1488:
        leftSpeed = horizontalSpeed + 200 * turbo

def _leftJoystickLeft():
    '''makes the robot move to the left'''
    global horizontalSpeed
    global leftSpeed
    global rightSpeed
    print("the left joystick was moved to the left")
    if horizontalSpeed >= 1488:
        leftSpeed = horizontalSpeed - 200 * turbo
    print("LEFTSPEED" + str(leftSpeed))
    if horizontalSpeed < 1488:
        rightSpeed = horizontalSpeed + 200 * turbo
        
def _rightJoystickDown():
    '''makes the robot move down'''
    global frontSpeed, backSpeed, verticalSpeed
    print("the  joystick was moved down")
    frontSpeed = 1469 - 50 * turboVert
    backSpeed = 1100 - 200 * turboVert

def _rightJoystickUp():
    '''makes the robot move up'''
    global frontSpeed, backSpeed, verticalSpeed
    print("the  joystick was moved up")
    frontSpeed = 1509 + 200 * turboVert
    backSpeed = 1509 + 200 * turboVert

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
    button, ADDRESS = decode(server.recvfrom(BUFSIZE), "ascii")
    print(button)

    
    try:
        analogButton = float(button)
        analogButton = round(analogButton, 4)
        if analogButton < 2.5 and analogButton > -2.5:
            if analogButton < 0:
                #_l2(analogButton)
                pass
            else:
                #_r2(analogButton)
                pass
           

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
            rightHatPressed = False
            leftHatPressed = False
        elif button == "downHatPressed":
            downHatPressed = True
            upHatPressed = False
            rightHatPressed = False
            leftHatPressed = False
        elif button == "no hat pressed":
            upHatPressed = False
            downHatPressed = False
            rightHatPressed = False
            leftHatPressed = False

        elif button == "left":
            leftJoystickLeft = True
        elif button == "right":
            leftJoystickRight = True
        elif button == "not left or right":
            leftJoystickRight = False
            leftJoystickLeft = False
        elif button == "up":
            rightJoystickUp = True
        elif button == "down":
            rightJoystickDown = True
        elif button == "not down or up":
            rightJoystickUp = False
            rightJoystickDown = False
        elif button == "leftJoystickPressed":
            turbo = 2
        elif button == "leftJoystickReleased":
            turbo = 1
        elif button == "rightJoystickPressed":
            turboVert = 2
        elif button == "rightJoystickReleased":
            turboVert = 1
            
        elif button == "rightHatPressed":
            rightHatPressed = True
            leftHatPressed = False
            upHatPressed = False
            downHatPressed = False
        elif button == "leftHatPressed":
            leftHatPressed = True
            rightHatPressed = False
            upHatPressed = False
            downHatPressed = False
        if upHatPressed:
            _upHat()
        elif downHatPressed:
            _downHat()
        else:
            _noVerticalHat()

        if rightHatPressed:
            _rightHat()
            print("_rightHat()")
        elif leftHatPressed:
            _leftHat()
            print("_leftHat()")
        elif leftJoystickRight:
            print("_leftJoystickRight()")
            _leftJoystickRight()
        elif leftJoystickLeft:
            _leftJoystickLeft()
            print("(_leftJoystickLeft()")
        elif rightJoystickUp:
            print("_rightJoystickUp()")
            _rightJoystickUp()
        elif rightJoystickDown:
            _rightJoystickDown()           
        else:
            _noHorizontalHatOrJoystick()
            _noVerticalHatOrJoystick()

    if started:
        pi.set_servo_pulsewidth(ESCRIGHT, rightSpeed)
        pi.set_servo_pulsewidth(ESCLEFT, leftSpeed)
        pi.set_servo_pulsewidth(ESCFRONT, frontSpeed)
        pi.set_servo_pulsewidth(ESCBACK, backSpeed)
        cont_data.write(str([frontSpeed, backSpeed, leftSpeed, rightSpeed, trianglePress]) + '\n')
        cont_data.flush()
        
    else:
        pi.set_servo_pulsewidth(ESCRIGHT, 1488)
        pi.set_servo_pulsewidth(ESCLEFT, 1488)
        pi.set_servo_pulsewidth(ESCFRONT,1488)
        pi.set_servo_pulsewidth(ESCBACK, 1488)
        cont_data.write(str([1488, 1488, 1488, 1488, trianglePress]) + '\n')
        cont_data.flush()
    
    
    if os.path.getsize('controller_data.txt') > 1000000: # clears if the file is over 1 MB
        cont_data.seek(0)
        cont_data.truncate()
