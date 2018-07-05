#!/bin/bash
sudo ds4drv &
python3 Computer/baseServer.py &
ssh pi@raspberrypi.local "bash Desktop/Underwater-ROV-Project/piStart.sh" &
vncviewer raspberrypi.local
