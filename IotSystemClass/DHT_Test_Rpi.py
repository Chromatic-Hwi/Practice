import serial
import time

ser = serrial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.flush()

try:
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip()
            print(data)

except KeyboardInterrupt:
    print("End")
