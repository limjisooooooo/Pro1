#*--encoding
from flask_restful import Api, Resource, reqparse
from flask import Flask, Response
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *
import os
import base64
#from pymysql import *
import io
import json
import magic

app = Flask(__name__)
api = Api(app)

#conn = connect(host = '127.0.0.1', port = 8000, user = 'trefrasd', password = '000831', db = 'pro1_db', charset = 'utf8')

#curs = conn.cursor()
class getFile(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('path', type=str)
        args = parser.parse_args()
        path = args['path']
        try:
            f = open(path, 'rb')
            data = f.read()
            mime_type = magic.from_file(path, True)
            if mime_type.split('/')[0] == 'text':
                res = "<p>" + data.decode() + "</p>"
            elif mime_type.split('/')[0] == 'image':
                #res = base64.b64encode(data).decode()
                res = "<img src='" + path.replace('/Users/limjisoo/PycharmProjects/Pro1','') + "'/>"
            elif mime_type.split('/')[0] == 'video':
                #res = base64.b64encode(data).decode()
                #res = "<video controls autoplay> <source type='" + mime_type + "' src='data:" + mime_type + ";base64," + base64.b64encode(data).decode() + "'> </video>"
                res = "<video controls autoplay> <source type='" + mime_type + "' src='" + path.replace('/Users/limjisoo/PycharmProjects/Pro1','') + "'> </video>"
        except IsADirectoryError:
            res = path
            mime_type = 'Directory'

        return Response(json.dumps({'res': res, 'mime_type': mime_type}), content_type='application/json; charset=utf-8')
        #return Response(data.decode('utf-8'), content_type=mime_type)

class getItem(Resource):
    def post(self):
        #root = "/home/ubuntu/Pro1/"
        root = "/Users/limjisoo/PycharmProjects/Pro1/"
        parser = reqparse.RequestParser()
        parser.add_argument('path', type=str)
        args = parser.parse_args()
        path = args['path']
        path = path.replace('/Users/limjisoo/PycharmProjects/Pro1/', '')
        files = os.listdir(root+path)
        #tmp = os.listdir(root + dir.encode().decode('ascii','surrogateescape'))
        files.sort(reverse=True)
        l = list()
        for fname in files:
            # path = val.encode('ascii','surrogateescape').decode()
            if fname[0] == '.':
                continue
            try:
                mime_type = magic.from_file(root + path + fname, True)
                if mime_type.split('/')[0] == 'text':
                    img = Image.new('RGB', (200, 150), (242, 242, 242))
                    draw = ImageDraw.Draw(img)
                    fnt = ImageFont.truetype('/Library/Fonts/AppleGothic.ttf')
                    #fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf')
                    f = open(os.path.join(root+path, fname), 'r')
                    draw.text((10, 10), f.read(), font=fnt, fill=(10, 10, 10))
                    f.close()
                    b = io.BytesIO()
                    img.save(b, 'PNG')
                    imstr = b.getvalue()
                    imstr = base64.b64encode(imstr)
                    l.append({'fname': fname, 'img': imstr.decode(), 'path': os.path.join(root+path, fname)})

                elif mime_type.split('/')[0] == 'image':
                    f = open(os.path.join(root+path, fname), 'rb')
                    imstr = f.read()
                    f.close()
                    imstr = base64.b64encode(imstr)
                    l.append({'fname': fname, 'img': imstr.decode(), 'path': os.path.join(root+path, fname)})

                elif mime_type.split('/')[0] == 'video':
                    clip = VideoFileClip(os.path.join(root+path, fname))
                    img = Image.fromarray(clip.get_frame(t = 0),'RGB')
                    b = io.BytesIO()
                    img.save(b, 'PNG')
                    imstr = b.getvalue()
                    imstr = base64.b64encode(imstr)
                    l.append({'fname': fname, 'img': imstr.decode(), 'path': os.path.join(root+path, fname)})

                else:
                    img = Image.new('RGB', (200, 150), (242, 242, 242))
                    draw = ImageDraw.Draw(img)
                    b = io.BytesIO()
                    img.save(b, 'PNG')
                    imstr = b.getvalue()
                    imstr = base64.b64encode(imstr)
                    l.append({'fname': fname, 'img': imstr.decode(), 'path': os.path.join(root+path, fname)})
            except IsADirectoryError:
                img = Image.new('RGB', (200, 150), (242, 242, 242))
                draw = ImageDraw.Draw(img)
                b = io.BytesIO()
                img.save(b, 'PNG')
                imstr = b.getvalue()
                imstr = base64.b64encode(imstr)
                l.append({'fname': fname, 'img': imstr.decode(), 'path': os.path.join(root+path, fname)})

        return Response(json.dumps(l), content_type='application/json; charset=utf-8')

class getMenu(Resource):
    def post(self):
        """
        l = list()
        sql = " SELECT EMPID, EMPNAME FROM empmst WHERE EMPID = %s "
        curs.execute(sql, (id))
        for val in curs.fetchall():
            l.append(val)
        return Response(json.dumps(l, ensure_scii=False).encode('utf8'), content_type='application/json; charset=utf-8')
        """
        root = "/Users/limjisoo/PycharmProjects/Pro1/"
        parser = reqparse.RequestParser()
        parser.add_argument('path', type=str)
        args = parser.parse_args()
        path = args['path']
        files = os.listdir(root + path)
        files.sort(reverse=True)
        l = list()
        for fname in files:
            if fname[0] == '.':
                continue
            l.append(fname)

        return Response(json.dumps(l), content_type='application/json; charset=utf-8')

if __name__=='__main__':
    app.run('0.0.0.0', '80')
