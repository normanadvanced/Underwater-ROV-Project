import picamera

leftSpeed = rightSpeed = frontSpeed = backSpeed = trianglePress = 0


def camera_start_preview():
    camera = picamera.PiCamera()
    camera.start_preview(fullscreen=False, window = (620, 2, 650, 450))
def screenshot():
    """
    camera = picamera.PiCamera()
    global amount
    amount = 0
    AmountFile = open('Photos/amount', 'r')
    x = AmountFile.readline().strip()
    try:
        amount = int(x)
    except ValueError:
        print("WHY??")
    AmountFile.close()
    camera.capture('Photos/' + 'snapshot' + str(amount) + '.jpg')
    amount += 1
    WriteAmount = open('Photos/amount', 'w')
    WriteAmount.write("%d" % amount)
    camera.close()"""
    pass
    
def setVariables(_leftSpeed, _rightSpeed):
    global leftSpeed, rightSpeed, frontSpeed, backSpeed
    leftSpeed = _leftSpeed
    rightSpeed = _rightSpeed
    

