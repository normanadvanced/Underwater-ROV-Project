	#!/bin/bash
echo "$(<../password.txt)" | sudo -S ds4drv &
python3 Computer/baseServer.py & 
sshpass -p "raspberry" ssh -X -o "StrictHostKeyChecking=no" pi@raspberrypi.local "export DISPLAY=:0; echo raspberry | sudo -S bash /home/pi/Desktop/Underwater-ROV-Project/piStart.sh" &
vncviewer raspberrypi.local &
