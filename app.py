import os
import flask
import helpers
from flask import Flask, json, render_template, request
from flask_restful import Resource, Api
from flask.helpers import make_response
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from model import WebRadioEncoder, WebRadiosList
from mpc import Mpc


# Configuration region
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}) 

app.secret_key = os.urandom(12)

Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True


# MPC declaration region
_mpc = Mpc()


# Actual radios status region
_radios = WebRadiosList

def getRadios():
    return _radios

def getActualPlaying():
    for item in _radios:
        if item.isPlaying == True:
            ret = item
            return item
    return ""


# API region
api = Api(app)

class getAllStation(Resource):
    def get(self):
        resp = flask.Response(WebRadioEncoder().encode(_radios))
        return resp

class getVolume(Resource):
    def get(self):
        resp = flask.Response(_mpc.getVolume())
        return resp

class setVolume(Resource):
    def post(self):
        request_data = request.get_json()
        volume = request_data['volume']
        _mpc.volumeChange(volume)
        resp = make_response(json.dumps({'volume':_mpc.getVolume()}), 200) 
        return resp

class playRadio(Resource):
    def post(self):
        request_data = request.get_json()
        name = request_data['name']
        url = request_data['url']
        radio = helpers.webRadioFromName(name)
        _radios = _mpc.play(radio)            
        resp = make_response(json.dumps({'name':name, 'url': url}), 200) 
        return resp

class stopRadio(Resource):
    def post(self):
        _radios = _mpc.stop()
        resp = flask.Response()
        return resp

class getPlayingStation(Resource):
    def get(self):
        radio = _mpc.getActualPlayingStation()
        if radio != "":
            resp = make_response(json.dumps({'name':radio.name, 'url': radio.url}), 200)
            return resp
        else:
            return ""

api.add_resource(getAllStation, '/api/getAllStation/')
api.add_resource(getVolume, '/api/getVolume/')
api.add_resource(setVolume,'/api/setVolume/')
api.add_resource(playRadio,'/api/playRadio/')
api.add_resource(stopRadio,'/api/stopRadio/')


# Web page region
@app.route('/', methods=['GET', 'POST'])
def hello():

    if request.method == "GET":
        select = request.form.get('selectRadio')
        
        return render_template('index.html', radios = getRadios(), actualPlay = getActualPlaying(), volume=_mpc.getVolume())

    if request.method == "POST":
        select = request.form.get('selectRadio')
        if request.form['button'] == 'Play':
            radio = helpers.webRadioFromName(select)
            _radios = _mpc.play(radio)
        if request.form['button'] == 'Stop':
            _radios = _mpc.stop()
        if request.form['button'] == 'VolumeUp':
            _mpc.volumeChange('+1')
        if request.form['button'] == 'VolumeUpUp':
            _mpc.volumeChange('+10')
        if request.form['button'] == 'VolumeDown':
            _mpc.volumeChange('-1')
        if request.form['button'] == 'VolumeDownDown':
            _mpc.volumeChange('-10')
        return render_template('index.html', radios = getRadios(), actualPlay = getActualPlaying(), volume = _mpc.getVolume(), selectedItem=select)

# Start aplication regon 
app.run(debug=True,port=5000, host='0.0.0.0')



