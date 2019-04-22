#-*- coding:utf-8 -*-

import sys
sys.path.insert(0, '/Users/limjisoo/PycharmProjects/Pro1')

from flask import Flask, render_template
from BackEnd import *
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def main():
    return render_template('main.html')

api.add_resource(getDir, '/getDir')    #add_resource(CLASS, URL) URL과 CLASS를 매칭해줌.

if __name__== '__main__':
    app.run('0.0.0.0', '80')
