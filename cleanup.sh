pkill -9 python &
pkill -9 ds4drv &
sshpass -p "raspberry" ssh -X -o "StrictHostKeyChecking=no" pi@raspberrypi.local "sudo pkill -9 python"
