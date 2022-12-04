from flask import Flask, render_template, request
import pymysql



app = Flask(__name__)



@app.route('/')
def index():
    db = pymysql.connect(host='localhost', user='root', password='1234', db='mydb')
    cur = db.cursor()
    
    cur.execute("SELECT * from dht ORDER BY id DESC LIMIT 10")
    rows = cur.fetchall()
    
    db.close()
    
    return render_template('flask_dht2.html', rows=rows)

@app.route('/view',methods=['post'])
def view():
    tempData = request.form['tempData']
    humiData = request.form['humiData']
    with open("data/InputData.txt","a", encoding='utf-8') as f:
            f.write("%s,%s" % (tempData, humiData))
            
    return render_template('flask_dht2.html', tempData=tempData, humiData=humiData)



if __name__=='__main__':
    app.run(debug=True, port=7080, host='192.168.35.135')
    
