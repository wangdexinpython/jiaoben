#!/usr/bin/env python
# -*- coding: UTF-8 -*-'
from flask import Flask
from conn_redis import RedisClient

app = Flask(__name__)
conn = RedisClient()

@app.route('/add/<num>')
def tianjia(num):
    print num

@app.route('/get')
def hello():
    val=conn.get_val('fei')
    print val
    return '你已经在数据库中添加一个一条 \n'

@app.route('/jian')
def jian():
    conn.get('oooooooooo', 25)
    return '你删了数据库'


if __name__ == '__main__':
    app.run(debug=True)