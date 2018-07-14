from socket import *
from codecs import *
import os
import pygame
import time
import sys
import serial
import threading

horn = serial.Serial('/dev/ttyACM0', 115200, timeout=.1)  # COM4 for windows, /dev/ttyAMC0

#we can clear the que with pygame.event.clear()
#pygame.event.wait() stops the program until an event becomes available


#stuff needed for the server
HOST = os.popen("echo $(getent hosts NARROVCommandModule.local |cut -f1 -d ' ')").readline()
PORT = 5008
ADDRESS = (HOST, PORT)
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)


print("Waiting for connection horn . . .")
client, address = server.accept()
print("horn connected from: ", address)


#pygame.event.setBlocked


while True:
    if str(horn.readline())[2:-5] == 'Honk':
        honk_time = "Honk time: " + str(time.time())
        client.send(bytes(honk_time, "ascii"))



