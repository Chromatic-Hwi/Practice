from flask import Flask

app = Flask(__name__) #Flask 객체를 app에 할당

@app.route('/') #라우팅 경로 설정. 주소 접속시 아래 함수 실행

def hello():
    return "Hello World!"

@app.route('/page')

def page():
    return "New Page"

if __name__ == '__main__':
    app.run(debug=True, port=xxxx, host='0.0.0.0')
    #debug=True는 내용 수정을 실시간으로 반영한다는 설정, host에서 0.0.0.0은 모든 IP에 대한 접근 허용을 의미.

    
