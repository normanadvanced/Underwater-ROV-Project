
echo "$(<../password.txt )" | sudo -S pkill -9 python &
echo "$(<../password.txt )" | sudo -S pkill -9 ds4drv &
sshpass -p "raspberry" ssh -X -o "StrictHostKeyChecking=no" pi@raspberrypi.local "sudo pkill -9 python;sudo pkill -9 pigpiod"
