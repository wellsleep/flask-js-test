# -*- coding:utf-8 -*-


import os
from flask import Flask
from flask import jsonify
from flask import render_template, request
import random

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/calculate')
def add_numbers():
    a = random.randint(10, 2000)
    # a = request.args.get('a', 0, type=int)  # 第二个参数作为默认值
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b, in_a=a)  # 对应$("#input-a").text(data.in_a), $("#result").text(data.result);的变量名


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
