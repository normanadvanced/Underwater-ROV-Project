#!/bin/bash
sudo ds4drv &
python3 Computer/baseServer.py &
sshpass -p "raspberry" ssh -o StrictHostKeyChecking=no pi@raspberrypi.local "cd Desktop/Underwater-ROV-Project/ && bash piStart.sh"
vncviewer raspberrypi.local
