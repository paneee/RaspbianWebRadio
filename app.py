from typing import Any
from flask import Flask, json, redirect, url_for, render_template, request
import flask
from flask.helpers import make_response
from flask_bootstrap import Bootstrap
from model import WebRadioEncoder, WebRadios
from model import WebRadiosList
from mpc import Mpc
import os
from flask_restful import Resource, Api
from flask import jsonify 
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.secret_key = os.urandom(12)

mpc = Mpc()

Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

api = Api(app)

class getAllStation2(Resource):
    def get(self):
        resp = flask.Response(WebRadioEncoder().encode(WebRadiosList))
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        resp.headers['Access-Control-Allow-Origin'] = '	*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,PATCH,DELETE,HEAD,OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = 'Content-Type, Origin, Accept, Authorization, Content-Length, X-Requested-With'
        return resp

class getAllStation(Resource):
    def get(self):
        resp = flask.Response(WebRadioEncoder().encode(WebRadios))
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        resp.headers['Access-Control-Allow-Origin'] = '	*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,PATCH,DELETE,HEAD,OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = 'Content-Type, Origin, Accept, Authorization, Content-Length, X-Requested-With'
        return resp

class getVolume(Resource):
    def get(self):
        resp = flask.Response(mpc.getVolume())
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        resp.headers['Access-Control-Allow-Origin'] = '	*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,PATCH,DELETE,HEAD,OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = 'Content-Type, Origin, Accept, Authorization, Content-Length, X-Requested-With'
        return resp


class setVolume(Resource):
    def post(self):
        request_data = request.get_json()
        volume = request_data['volume']
        mpc.volumeChange(volume)
        resp = make_response(json.dumps({'volume':mpc.getVolume()}), 200) 
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,PATCH,DELETE,HEAD,OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = 'Content-Type, Origin, Accept, Authorization, Content-Length, X-Requested-With'
        return resp


class playRadio(Resource):
    def post(self):
        request_data = request.get_json()
        name = request_data['name']
        url = request_data['url']
        mpc.play(WebRadios[name])
        resp = make_response(json.dumps({'name':name, 'url': url}), 200) 
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        resp.headers['Access-Control-Allow-Origin'] = '	*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,PATCH,DELETE,HEAD,OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = 'Content-Type, Origin, Accept, Authorization, Content-Length, X-Requested-With'
        return resp


class stopRadio(Resource):
    def post(self):
        mpc.stop()
        resp = flask.Response()
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        resp.headers['Access-Control-Allow-Origin'] = '	*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,PATCH,DELETE,HEAD,OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = 'Content-Type, Origin, Accept, Authorization, Content-Length, X-Requested-With'
        return resp

        
api.add_resource(getAllStation, '/api/getAllStation/')
api.add_resource(getAllStation2, '/api/getAllStation2/')
api.add_resource(getVolume, '/api/getVolume/')
api.add_resource(setVolume,'/api/setVolume/')
api.add_resource(playRadio,'/api/playRadio/')
api.add_resource(stopRadio,'/api/stopRadio/')

@app.route('/', methods=['GET', 'POST'])
def hello():
    
    if request.method == "GET":
        select = request.form.get('selectRadio')
        return render_template('index.html', radios=WebRadios, volume=mpc.getVolume(), actualPlay=select)

    if request.method == "POST":
        select = request.form.get('selectRadio')
        if request.form['button'] == 'Play':
            link = WebRadios[select]
            mpc.play(link)
        if request.form['button'] == 'Stop':
            mpc.stop()
        if request.form['button'] == 'VolumeUp':
            mpc.volumeChange('+1')
        if request.form['button'] == 'VolumeUpUp':
            mpc.volumeChange('+10')
        if request.form['button'] == 'VolumeDown':
            mpc.volumeChange('-1')
        if request.form['button'] == 'VolumeDownDown':
            mpc.volumeChange('-10')

        return render_template('index.html', radios=WebRadios, volume=mpc.getVolume(), actualPlay=select, selectedItem=select)


app.run(debug=True,port=8080, host='0.0.0.0')



