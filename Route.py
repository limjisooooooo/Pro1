import sys
sys.path.insert(0, '/Users/limjisoo/PycharmProjects/Pro1')
#sys.path.insert(0, '/home/ubuntu/Pro1')
#sys.path.append('/home/ubuntu/Pro1/venv/lib/python3.7/site-packages')

from flask import Flask, render_template
from BackEnd import *
from flask_restful import Api
from datetime import datetime

app = Flask(__name__)
api = Api(app)

@app.route('/')
def main():
    now = datetime.now()
    return render_template('main.html', now = now.strftime('%Y%m%d%H%M%S'))

api.add_resource(getFile, '/getFile')
api.add_resource(getMenu, '/getMenu')    #add_resource(CLASS, URL) URL과 CLASS를 매칭해줌.
api.add_resource(getItem, '/getItem')

if __name__== '__main__':
    app.run('0.0.0.0', '80')
