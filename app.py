import os
import flask
from flask import Flask, json, render_template, request, redirect, url_for
from flask_restful import Resource, Api
from flask.helpers import make_response
from flask_bootstrap import Bootstrap
from flask_cors import CORS

from rpi.mpc import Mpc
from rpi.speaker import Speaker
from rpi.radio import WebRadioEncoder


# Configuration region
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}) 

app.secret_key = os.urandom(12)

Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True


# MPC declaration region
_mpc = Mpc()


# Speaker declaration region
_speaker = Speaker()


# API region
api = Api(app)

class getAllStation(Resource):
    def get(self):
        resp = flask.Response(WebRadioEncoder().encode(_mpc.webRadios.getAll()))
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
        radio = _mpc.webRadios.fromName(name)
        _mpc.play(radio)
        resp = make_response(json.dumps({'name':name, 'url': url}), 200) 
        return resp

class stopRadio(Resource):
    def post(self):
        _mpc.stop() 
        resp = flask.Response()
        return resp

class getPlayingStation(Resource):
    def get(self):
        radio = _mpc.webRadios.getPlaying()
        if radio != "":
            resp = make_response(json.dumps({'name':radio.name, 'url': radio.url}), 200)
            return resp
        else:
            return ""

class speakerOnOff(Resource):
    def post(self):
        _speaker.OnOff()
        return 'OK'

class speakerVolumeUP(Resource):
    def post(self):
        _speaker.VolumeUP()
        return 'OK'

class speakerVolumeDOWN(Resource):
    def post(self):
        _speaker.VolumeDOWN()
        return 'OK'

api.add_resource(getAllStation, '/api/getAllStation/')
api.add_resource(getVolume, '/api/getVolume/')
api.add_resource(setVolume,'/api/setVolume/')
api.add_resource(playRadio,'/api/playRadio/')
api.add_resource(stopRadio,'/api/stopRadio/')
api.add_resource(speakerOnOff,'/api/speakerOnOff/')
api.add_resource(speakerVolumeUP,'/api/speakerVolumeUP/')
api.add_resource(speakerVolumeDOWN,'/api/speakerVolumeDOWN/')


# Web page region
@app.route('/', methods=['GET', 'POST'])
def hello():

    if request.method == "GET":
        select = request.form.get('selectRadio')
        
        return render_template('index.html', radios = _mpc.webRadios.getAll(), actualPlay = _mpc.webRadios.getPlaying(), volume=_mpc.getVolume())

    if request.method == "POST":
        select = request.form.get('selectRadio')
        if request.form['button'] == 'Play':
            radio = _mpc.webRadios.fromName(select)
            _mpc.play(radio)
        if request.form['button'] == 'Stop':
            _mpc.stop()
        if request.form['button'] == 'VolumeUp':
            _mpc.volumeChange('+1')
        if request.form['button'] == 'VolumeUpUp':
            _mpc.volumeChange('+10')
        if request.form['button'] == 'VolumeDown':
            _mpc.volumeChange('-1')
        if request.form['button'] == 'VolumeDownDown':
            _mpc.volumeChange('-10')
        if request.form['button'] == 'SpeakerVolumeDown':
            _speaker.VolumeDOWN()
        if request.form['button'] == 'SpeakerVolumeUp':
            _speaker.VolumeUP()
        if request.form['button'] == 'SpeakerOnOff':
            _speaker.OnOff()

        return redirect(request.referrer)


# Start aplication region 
app.run(debug=True,port=5000, host='192.168.1.50')







