# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import random
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/result")
def result():
    # 한글 써봄, 한글 주석 써도 에러 안나요 !
    name1 = request.args.get('name1')
    name2 = request.args.get('name2')
    match = random.randrange(50, 101)
    # 'names.csv' 파일을 만들어서 저장한다.
    with open('names.csv', 'a') as f:
        a = csv.writer(f)
        a.writerow([name1, name2])
    return render_template('result.html',name1=name1,name2=name2,match=match)

@app.route("/admin")
def admin():
    # names에 들어가 있는 모든 이름을 출력한다.
    f = open('names.csv', mode='r')
    rr = csv.reader(f)
    names = rr
    return render_template('admin.html', names=names)
    
app.run(host='0.0.0.0', port='8080', debug=True)