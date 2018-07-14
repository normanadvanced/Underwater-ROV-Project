#! /bin/bash
echo "$(<../password.txt )" | sudo -S pkill -9 python &
echo "$(<../password.txt )" | sudo -S pkill -9 ds4drv &
sshpass -p "raspberry" ssh -X -o "StrictHostKeyChecking=no" pi@raspberrypi.local "echo raspberry | sudo -S pkill -9 python; echo raspberry | sudo -S pkill -9 pigpiod; echo raspberry | sudo -S killall pigpiod"
exit 0
