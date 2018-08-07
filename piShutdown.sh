sshpass -p "raspberry" ssh -o "StrictHostKeyChecking=no" pi@raspberrypi.local "echo raspberry | sudo -S shutdown now"
