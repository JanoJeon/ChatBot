# -- coding : utf-8 --

from flask import Flask, render_template
import main

question = []
app = Flask(__name__)

@app.route('/')
@app.route('/<result>')
def home(result=None):
    global question
    question.append(result)
    # print -> ['문자열 출력됨']

    question = ''.join(question)
    question = main.check(question)

    # template 디렉터리 안에 home.html 파일 반환
    output = render_template('home.html', question=question)
    question = []
    return output

if __name__ == '__main__':
    # 디버그모드는 서버 공개시 비활성화 하는것이 좋다.
    # 오류가 발생할 시 소스코드가 공개되기 때문
    app.debug = True
    #app.debug = False
    app.run(host='0.0.0.0', port=5000)
