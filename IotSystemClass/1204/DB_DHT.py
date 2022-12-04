from flask import Flask, render_template, request
import time
import serial
import pymysql

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
        time.sleep(1)

except KeyboardInterrupt:
    db.close()
