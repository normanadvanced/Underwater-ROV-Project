#!/bin/bash
echo "$(<../password.txt)" | sudo -S ds4drv &
python3 Computer/baseServer.py & 
sshpass -p "raspberry" ssh -X -o "StrictHostKeyChecking=no" pi@raspberrypi.local "echo raspberry | sudo -S xhost +;export DISPLAY=:0 && cd /home/pi/Desktop/Underwater-ROV-Project/Pi/ && echo raspberry | sudo -S python3 GUI.py" &
vncviewer raspberrypi.local &
