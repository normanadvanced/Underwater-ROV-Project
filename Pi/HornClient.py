import os
from socket import *
from time import sleep
from codecs import decode


HOST = os.popen("getent hosts NARROVCommandModule.local |cut -f1 -d ' '").readline()
PORT = 5003
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

while True:
    try:
        server = socket(AF_INET, SOCK_STREAM)
        server.connect(ADDRESS)
        break
    except:
        pass
print("horn connected")
#os.system("printf 'raspberry \n' | sudo -S python3 ControllerClient2.py &")

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
            heard.write(str(honk_time)[:15]+'\n')
            heard.flush()
            #print(honk_time)
        if os.path.getsize('sent.txt') > 1000000:  # clear file after it reaches 1 MB
            f.seek(0)
            f.truncate()

#horn_honked_thread = threading.Thread(target=get_honk_time())
#horn_honked_thread.daemon = True
print("honk")
#horn_honked_thread.start()
print("honk 2")

while True:
    get_honk_time()

