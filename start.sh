#!/bin/bash
sudo ds4drv &
python3 Computer/baseServer.py &
vncviewer raspberrypi.local
sshpass -p "raspberry" ssh -X pi@raspberrypi.local "cd /home/pi/Desktop/Underwater-Rov-Project | sudo bash piStart.sh"
