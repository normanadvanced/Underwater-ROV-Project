import os
os.system("sudo pigpiod")
from socket import *
from time import sleep
from codecs import decode
import pigpio
import picamera
import threading
import SharedFunctions

HOST = 'NARROVCommandModule.local'
PORT = 5001
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

pi = pigpio.pi()
ESCRIGHT = 5
ESCLEFT = 21
ESCBACKLIFT = 13 #unknown so far
ESCFRONTLIFT = 27 #also still known so far

baseSpeed = 1488	#the speed determined by r1 and l1
rightSpeed = 1488	#the speed that the right motor is moving at
leftSpeed = 1488	#the speed that the left motor is moving at
frontSpeed = 0
backSpeed = 0
pictureCount = 0	#GUI thing, can delete
started = False		#Checks if the motors should be able to move or not
rightHatPressed = False	#Checks if the right hat has been pressed
leftHatPressed = False	#Checks if the left hat has been pressed
upHatPressed = False	#Checks if the up hat has been pressed
downHatPressed = False	#Checks if the down hat has been pressed
leftJoystickLeft = False	#Checks if the left joystick has been moved to the left
leftJoystickRight = False	#Checks if the left joystick has been moved to the right
turbo = 1		#Checks if the turns need to be moved turbo
global trianglePress
trianglePress = 0

while True:
    try:
        server = socket(AF_INET, SOCK_STREAM)
        server.connect(ADDRESS)
        break
    except:
        pass

def _triangle():		#please look at Chris/Pranav. Not nessecery for movement
    SharedFunctions.screenshot()
def _square():
    '''toggle the GUI'''
    print("square commands here")

def _x():
    '''toggle 2'''
    print("x commands here")

def _circle():
    '''starts the translational motors'''
    global rightSpeed
    global leftSpeed
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
    
def _r1():
    '''increases the speed'''
    global baseSpeed
    if started == True:
        if baseSpeed < 1990:
            baseSpeed += 10
        else:
            baseSpeed = 1998   
        print("base: ", baseSpeed)
        #also add GUI message
    
def _r2(magnitude):
    '''makes the robot asend'''
    print("magnitude: ", magnitude)
    print("raising at ", (1488 + 255 * magnitude), " speed")
    pi.set_servo_pulsewidth(ESCBACKLIFT, 1488 + 255 * magnitude)
    pi.set_servo_pulsewidth(ESCFRONTLIFT, 1488 + 255 * magnitude)
    
def _l1():
    '''decreses translational speed'''
    global baseSpeed
    if started == True:
        if baseSpeed > 708:
            baseSpeed -= 10
        else:
            baseSpeed = 708
        print("base: ", baseSpeed)
        #also add GUI message
    
def _l2(magnitude):
    '''makes the robot desend'''
    print("magnitude: ", magnitude)
    print("Lowering at ", (1488 + 390 * magnitude), " speed")
    pi.set_servo_pulsewidth(ESCBACKLIFT, 1488 + 390 * magnitude)
    pi.set_servo_pulsewidth(ESCFRONTLIFT, 1488 + 390 * magnitude)

def _leftHat():
    '''makes the robot do a pivot turn to the left'''
    global leftSpeed
    global rightSpeed
    print("pivotLeft")
    leftSpeed = 1388
    rightSpeed = 1588

def _noHorizontalHatOrJoystick():
	'''Makes the robot drive straight again'''
	global leftSpeed
	global rightSpeed
	global baseSpeed
	#print("No horizontal")
	leftSpeed = baseSpeed
	rightSpeed = baseSpeed

def _rightHat():
    '''makes the robot do a pivot turn to the right'''
    global rightSpeed
    global leftSpeed
    print("pivotRight")
    leftSpeed = 1588
    rightSpeed = 1388

def _upHat():
	'''makes the robot pitch up'''
	pi.set_servo_pulsewidth(ESCBACKLIFT, 1438)
	pi.set_servo_pulsewidth(ESCFRONTLIFT, 1538)

def _downHat():
	'''makes the robot pitch down'''
	pi.set_servo_pulsewidth(ESCBACKLIFT, 1538)
	pi.set_servo_pulsewidth(ESCFRONTLIFT, 1438)

def _noVerticalHat():
	'''makes the robot stop pitching'''
	pi.set_servo_pulsewidth(ESCBACKLIFT, 1488)
	pi.set_servo_pulsewidth(ESCFRONTLIFT, 1488)

def _leftJoystickRight():
	'''makes the robot move to the right'''
	global rightSpeed
	global baseSpeed
	global leftSpeed
	print("the left joystick was moved to the right")
	if baseSpeed > 1488:
		rightSpeed = baseSpeed - 200 * turbo
	if baseSpeed < 1488:
		leftSpeed = baseSpeed + 200 * turbo

def _leftJoystickLeft():
	'''makes the robot move to the left'''
	global baseSpeed
	global leftSpeed
	global rightSpeed
	print("the left joystick was moved to the left")
	if baseSpeed > 1488:
		leftSpeed = baseSpeed - 200 * turbo
                print("LEFTSPEED" + str(leftSpeed)
	if baseSpeed < 1488:
		rightSpeed = baseSpeed + 200 * turbo

def _rightJoystick():
	'''we have not decided on what to do with this yet'''
	pass

def _center():
    '''makes the robot shoot up at full speed'''
    print("OFF")

def _calibrate(time):
    '''calibrates the robot's distance'''
    print("the calibrate function has been called")
    #listen for the sound
    #get the time when it hears the sound
    #compare the recieved time to the time sent and set that to a variable


def get_honk_time():
    heard = open('sent.txt', 'a')
    heard.seek(0)
    heard.truncate()
    print("starting horn thread");
    while True:
        server_data = decode(server.recv(BUFSIZE), "ascii")
        if str(server_data)[0:4] == "Honk":
            honk_time = server_data[11:]
            heard.write(str(honk_time))
            heard.flush()
            #print(honk_time)
        if os.path.getsize('sent.txt') > 1000000:  # clear file after it reaches 1 MB
            f.seek(0)
            f.truncate()

#setVariables = threading.Thread(target=SharedFunctions.setVariables, args=(leftSpeed, rightSpeed))
#horn_honked_thread = threading.Thread(target=get_honk_time())
#horn_honked_thread.daemon = True
print("honk")
#horn_honked_thread.start()
print("honk 2")


cont_data = open('controller_data.txt', 'a')
cont_data.seek(0)   # clears file
cont_data.truncate()
while True:
    button = decode(server.recv(BUFSIZE), "ascii")
    print(button)

    cont_data.write(str([frontSpeed, backSpeed, leftSpeed, rightSpeed]) + '\n')
    cont_data.flush()
    if os.path.getsize('controller_data.txt') > 1000000: # clears if the file is over 1 MB
        cont_data.seek(0)
        cont_data.truncate()

    try:
        analogButton = float(button)
        analogButton = round(analogButton, 4)
        print("got here %s" % analogButton)
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
            # _leftJoystickLeft()
            leftJoystickLeft = True
        elif button == "right":
            # _leftJoystickRight()
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
        else:
            pi.set_servo_pulsewidth(ESCRIGHT, 1488)
            pi.set_servo_pulsewidth(ESCLEFT, 1488)
