
from flask import Flask, render_template, Response
from flask_restful import Api
from BackEnd import *

app = Flask(__name__)
api = Api(app)

@app.route('/')
def main():
    return render_template('main.html')

api.add_resource(getDir, '/getDir')    #add_resource(CLASS, URL) URL과 CLASS를 매칭해줌.

if __name__== '__main__':
    app.run('0.0.0.0', '80')
