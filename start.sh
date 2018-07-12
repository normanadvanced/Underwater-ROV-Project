#!/bin/bash
bash cleanup.sh && echo "$(<../password.txt)" | sudo -S ds4drv &
sleep .4m
echo "$(<../password.txt)" | sudo -S python3 Computer/baseServer.py || bash cleanup.sh && exit
sshpass -p "raspberry" ssh -X -o "StrictHostKeyChecking=no" pi@raspberrypi.local "export DISPLAY=:0 && echo raspberry | sudo -S xhost + && export DISPLAY=:0 && cd /home/pi/Desktop/Underwater-ROV-Project/Pi/ && echo raspberry | sudo -S python3 GUI.py" &
vncviewer raspberrypi.local &
