from flask_restful import Api, Resource, reqparse
from flask import Flask, Response
import json
import os

from pymysql import *
import json

app = Flask(__name__)
api = Api(app)

#conn = connect(host = '127.0.0.1', port = 8000, user = 'trefrasd', password = '000831', db = 'pro1_db', charset = 'utf8')

#curs = conn.cursor()

class getDir(Resource):
    def post(self):
        """
        l = list()
        sql = " SELECT EMPID, EMPNAME FROM empmst WHERE EMPID = %s "
        curs.execute(sql, (id))
        for val in curs.fetchall():
            l.append(val)
        return Response(json.dumps(l, ensure_ascii=False).encode('utf8'), content_type='application/json; charset=utf-8')
        """
        parser = reqparse.RequestParser()
        parser.add_argument('dir', type=str)
        args = parser.parse_args()
        dir = args['dir']
        l = os.listdir(dir)
        l.sort(reverse=True)
        return Response(json.dumps(l, ensure_ascii=False).encode('utf8'), content_type='application/json; charset=utf-8')

if __name__=='__main__':
    app.run('0.0.0.0', '80')
