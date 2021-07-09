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

app = Flask(__name__)
app.secret_key = os.urandom(12)

mpc = Mpc()

Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

api = Api(app)

class GetAllStation2(Resource):
    def get(self):
        resp = flask.Response(WebRadioEncoder().encode(WebRadiosList))
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        resp.headers['Access-Control-Allow-Origin'] = '	*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,PATCH,DELETE,HEAD,OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = 'Content-Type, Origin, Accept, Authorization, Content-Length, X-Requested-With'
        return resp

class GetAllStation(Resource):
    def get(self):
        resp = flask.Response(WebRadioEncoder().encode(WebRadios))
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        resp.headers['Access-Control-Allow-Origin'] = '	*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,PATCH,DELETE,HEAD,OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = 'Content-Type, Origin, Accept, Authorization, Content-Length, X-Requested-With'
        return resp

class GetVolume(Resource):
    def get(self):
        resp = flask.Response(mpc.getVolume())
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        resp.headers['Access-Control-Allow-Origin'] = '	*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,PATCH,DELETE,HEAD,OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = 'Content-Type, Origin, Accept, Authorization, Content-Length, X-Requested-With'
        return resp


class SetVolume(Resource):
    def post(self):
        request_data = request.get_json()
        volume = request_data['volume']
        mpc.volumeChange(volume)
        
        resp = make_response(json.dumps({'volume':mpc.getVolume()}), 200)
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        resp.headers['x-powered-by'] = 'Express'
        resp.headers['x-ratelimit-limit'] = '1000'
        resp.headers['x-ratelimit-remaining'] = '999'
        resp.headers['x-ratelimit-reset'] = '1625845561'
        resp.headers['vary'] = 'Origin, X-HTTP-Method-Override, Accept-Encoding'
        resp.headers['access-control-allow-credentials'] = 'true'
        resp.headers['cache-control'] = 'no-cache'
        resp.headers['pragma'] = 'no-cache'
        resp.headers['expires'] = '-1'
        resp.headers['access-control-expose-headers'] = 'Location'
        resp.headers['location'] = 'http://jsonplaceholder.typicode.com/albums/101'
        resp.headers['x-content-type-options'] = 'nosniff'
        resp.headers['etag'] = 'W/"27-GXZSzxO5YfccqfzIfdOgpe12rcI"'
        resp.headers['via'] = '1.1 vegur'
        resp.headers['cf-cache-status'] = 'DYNAMIC'
        #resp.headers['expect-ct'] = 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"'
        #resp.headers['report-to'] = '{"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v2?s=QYiW1cLPxdL44NAppEaiAMMjMcfsUTkMI2OwSbyXYMgGX3LH%2F3sVSVWUcE9HVVM9uX1VIBS3L4L4RC6s2Z44yMRDRgWERlm2gkAV%2FWH2lJaldrDmrVtVn2MV7ALRmc9yvz5WvCgHzkayWw%3D%3D"}],"group":"cf-nel","max_age":604800}'
        resp.headers['nel'] = '{"report_to":"cf-nel","max_age":604800}'
        resp.headers['server'] = 'cloudflare'
        resp.headers['cf-ray'] = '66c2add16aa0dfcf-FRA'
        resp.headers['alt-svc'] = 'h3-27=":443"; ma=86400, h3-28=":443"; ma=86400, h3-29=":443"; ma=86400, h3=":443"; ma=86400'

        return resp


class Play(Resource):
    def post(self, station):
        mpc.play(WebRadios[station])
        resp = flask.Response("OK")
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        resp.headers['Access-Control-Allow-Origin'] = '	*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,PATCH,DELETE,HEAD,OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = 'Content-Type, Origin, Accept, Authorization, Content-Length, X-Requested-With'
        return "OK"


class Stop(Resource):
    def post(self):
        mpc.stop()
        resp = flask.Response("OK")
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        resp.headers['Access-Control-Allow-Origin'] = '	*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,PATCH,DELETE,HEAD,OPTIONS'
        resp.headers['Access-Control-Allow-Headers'] = 'Content-Type, Origin, Accept, Authorization, Content-Length, X-Requested-With'
        return "OK"

        
api.add_resource(GetAllStation, '/api/getAllStation')
api.add_resource(GetAllStation2, '/api/getAllStation2')
api.add_resource(GetVolume, '/api/getVolume')
api.add_resource(SetVolume,'/api/setVolume/')
api.add_resource(Play,'/api/Play/<station>')
api.add_resource(Stop,'/api/Stop')

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



