#!/bin/bash
bash cleanup.sh &
vncviewer raspberrypi.local &
sleep 4s
echo "$(<../password.txt)" | sudo -S python3 Computer/baseServer.py &
echo "$(<../password.txt)" | sudo -S python3 Computer/hornServer.py &
sleep 5s
sshpass -p "raspberry" ssh -X -o "StrictHostKeyChecking=no" pi@raspberrypi.local "cd ~/Desktop/Underwater-ROV-Project/Pi && echo raspberry | sudo -S python3 ControllerClient.py &" &
sshpass -p "raspberry" ssh -X -o "StrictHostKeyChecking=no" pi@raspberrypi.local "cd ~/Desktop/Underwater-ROV-Project/Pi && echo raspberry | sudo -S python3 HornClient.py &" &
sleep 5s
sshpass -p "raspberry" ssh -X -o "StrictHostKeyChecking=no" pi@raspberrypi.local "cd ~/Desktop/Underwater-ROV-Project/Pi && export DISPLAY=:0 && echo raspberry | sudo -S python3 GUI.py &" &
