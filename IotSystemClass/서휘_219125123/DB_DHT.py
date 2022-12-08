from flask import Flask, render_template, request
import time
import serial
import pymysql
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

app = Flask(__name__)

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.flush()

db = pymysql.connect(host='localhost',user='root',password='1234',db='mydb')
cur = db.cursor()

try:
    while True:
        ser.write("1".encode())
        print("a")
        if ser.in_waiting > 0:
            print("b")
            data = ser.readline().decode('utf-8').rstrip()
            data_s = data.split(',')
            
            if len(data_s) < 5:
                continue
            if data_s[0] == 'T':
                tem = data_s[1]
            if data_s[2] == 'H':
                hum = data_s[3]
                
            cur.execute("INSERT INTO dht(temp,humi) VALUES (%s,%s)", (tem,hum))
            db.commit()
            print("temp={}, hum={}".format(tem,hum))

            tem = int(tem)
            hum = int(hum)

            with open("./data/InputData.txt") as file:
                value = file.readlines()
                lastValue=value[-1]
                tempData=lastValue[0][:-2]
                tempData=lastValue[1][:-2]
            
            if (tem >= tempData and hum >= humiData):
                GPIO.output(5, True)
                GPIO.output(6, True)
            elif (tem >= tempData and hum < humiData):
                GPIO.output(5, True)
                GPIO.output(6, False)
            elif (tem < tempData and hum >= humiData):
                GPIO.output(5, False)
                GPIO.output(6, True)
            else:
                GPIO.output(5, False)
                GPIO.output(6, False)
        time.sleep(1)

except KeyboardInterrupt:
    db.close()
