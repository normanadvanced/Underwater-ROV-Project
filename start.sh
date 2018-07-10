#!/bin/bash
sudo ds4drv &
python3 Computer/baseServer.py &
vncviewer raspberrypi.local
