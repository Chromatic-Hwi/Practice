from flask import Flask, render_template, request
import serial

app = Flask(__name__)

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.flush()

tem = '0'
hum = '0'

@app.route('/')
def index():
    return render_template('dht.html',tem=tem, hum=hum)

@app.route('/data_get_act',methods=['GET'])
def data_get_act():
    if request.method == 'GET':
        while True:
            ser.write("1".encode())
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8').rstrip()
                data_s = data.split(',')

                if len(data_s) <5:
                    continue
                
                else:
                    if data_s[0] == 'T':
                        tem = data_s[1]
                    if data_s[2] == 'H':
                        hum = data_s[3]
                    return render_template('dht.html',tem=tem,hum=hum)
            break

if __name__=='__main__':
    app.run(debug=True, port=80xx,host='0.0.0.0')
