import serial

arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=.1)  # COM4 for windows, /dev/ttyAMC0
global roll, pitch, yaw, temperature, depth
temperature = 0
depth = 0
roll = yaw = pitch = 0.00


f = open('data.txt', 'a')
f.seek(0)
f.truncate()

while True:

    try:

        data_raw = str(arduino.readline())
        data_shaved = ""
        for i in range(len(data_raw) - 5):
            data_shaved += (data_raw[i + 2])
            #print(data_shaved)


        if data_shaved[0:1] == "T":  # for temperature
            temperature = float(data_shaved[13:-8])
        elif data_shaved[0:1] == "D":  # for depth
            depth = float(data_shaved[6:-4])
        elif len(data_shaved) > 9:  # for gyro
            imu = data_shaved.split(" ")
            yaw = float(imu[0])
            roll = float(imu[1])
            pitch = float(imu[2])

    except IndexError:
        print("")
    except TypeError:
        print("")
    except ValueError:
        print("")

    #print(str([pitch, roll, yaw, temperature, depth])+ '\n')
    f.write(str([pitch, roll, yaw, temperature, depth])+ '\n')
    f.flush()
