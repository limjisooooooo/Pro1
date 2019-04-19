from flask import Flask, render_template, Response
#from flask_restful import Api, Resource
#from pymysql import *
#import json

app = Flask(__name__)
#api = Api(app)

"""
conn = connect(host = '13.125.241.32', port = 8000, user = 'trefrasd', password = '000831', db = 'pro1_db', charset = 'utf8')

curs = conn.cursor()

BackEnd 에서 API 서버 만들 때나 필요할듯... FrontEnd에서는 걍 Flask 쓰는게 맘 편하겄오
class Index(Resource):
    def get(self, id):
        l = list()
        sql = " SELECT EMPID, EMPNAME FROM empmst WHERE EMPID = %s "
        curs.execute(sql, (id))
        for val in curs.fetchall():
            l.append(val)
        return Response(json.dumps(l, ensure_ascii=False).encode('utf8'), content_type='application/json; charset=utf-8')

api.add_resource(Index, '/get/<id>')    #add_resource(CLASS, URL) URL과 CLASS를 매칭해줌.
"""
@app.route('/')
def main():
    return render_template('main.html')

if __name__=='__main__':
    app.run('0.0.0.0', '80')