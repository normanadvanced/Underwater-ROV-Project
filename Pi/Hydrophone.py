import pyaudio
import time
import numpy as np
CHANNELS = 1
RATE = 44100

def threshold():    # will decrease as depth increases
    threshold_val = 400
    try:
        file = open('data.txt', 'r')
        depth = float((file.readlines()[-1])[1:-2].split(',')[4])
        file.close()

        if abs(depth) > 10:
            threshold_val -= 3.2 * abs(depth)
    except:
        pass

    return threshold_val



hydrophone = pyaudio.PyAudio()
hydrophone_data = np.fromstring("")

def main():
    global fulldata, hydrophone_data
    stream = hydrophone.open(format=pyaudio.paFloat32,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    stream_callback=stream_callback)

    stream.start_stream()
    while stream.is_active():
        time.sleep(.01)
        sum = 0
        for bit in hydrophone_data:
            sum += abs(bit)
        print(sum)
        if sum > threshold():
             print("Ping")
             time.sleep(2)
             #write down ping time
             f = open('received.txt','a')
             f.write(str(time.time()) + "\n")
             f.flush()
             f.close()

    stream.close()

    p.terminate()

def stream_callback(in_data, frame_count, time_info, flag):
    global hydrophone_data
    hydrophone_data = np.fromstring(in_data, dtype=np.float32)
    return (hydrophone_data, pyaudio.paContinue)

if __name__ == '__main__':
    main()