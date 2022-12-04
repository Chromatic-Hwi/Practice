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
    
    return render_template('flask_dht.html', rows=rows)

if __name__=='__main__':
    app.run(debug=True, port=7080, host='192.168.35.135')
