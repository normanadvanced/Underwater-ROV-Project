#!/bin/bash
sudo ds4drv & 
python3 Computer/baseServer.py & 
sshpass -p "raspberry" ssh -X -o "StrictHostKeyChecking=no" pi@raspberrypi.local "export DISPLAY=:0; sudo bash /home/pi/Desktop/Underwater-ROV-Project/piStart.sh" &
vncviewer raspberrypi.local &
