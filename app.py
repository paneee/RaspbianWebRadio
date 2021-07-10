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


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}) 

app.secret_key = os.urandom(12)

mpc = Mpc()

Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

api = Api(app)

class getAllStation(Resource):
    def get(self):
        resp = flask.Response(WebRadioEncoder().encode(WebRadiosList))
        return resp

class getVolume(Resource):
    def get(self):
        resp = flask.Response(mpc.getVolume())
        return resp

class setVolume(Resource):
    def post(self):
        request_data = request.get_json()
        volume = request_data['volume']
        mpc.volumeChange(volume)
        resp = make_response(json.dumps({'volume':mpc.getVolume()}), 200) 
        return resp

class playRadio(Resource):
    def post(self):
        request_data = request.get_json()
        name = request_data['name']
        url = request_data['url']
        radio = helpers.webRadioFromName(name)
        if radio is not None:
            mpc.play(radio)

        resp = make_response(json.dumps({'name':name, 'url': url}), 200) 
        return resp

class stopRadio(Resource):
    def post(self):
        mpc.stop()
        resp = flask.Response()
        return resp

class getActualStation(Resource):
    def get(self):
        resp = flask.Response(mpc.getPlayedStation()) 
        return resp

api.add_resource(getAllStation, '/api/getAllStation/')
api.add_resource(getVolume, '/api/getVolume/')
api.add_resource(setVolume,'/api/setVolume/')
api.add_resource(playRadio,'/api/playRadio/')
api.add_resource(stopRadio,'/api/stopRadio/')
api.add_resource(getActualStation,'/api/getActualStation/')

@app.route('/', methods=['GET', 'POST'])
def hello():
    
    if request.method == "GET":
        select = request.form.get('selectRadio')
        return render_template('index.html', radios=WebRadiosList, volume=mpc.getVolume(), actualPlay=mpc.getActualPlayedStation())

    if request.method == "POST":
        select = request.form.get('selectRadio')
        if request.form['button'] == 'Play':
            radio = helpers.webRadioFromName(select)
            mpc.play(radio)
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
        aaaa = mpc.getActualPlayedStation()
        return render_template('index.html', radios=WebRadiosList, volume=mpc.getVolume(), actualPlay=mpc.getActualPlayedStation(), selectedItem=select)

app.run(debug=True,port=5000, host='0.0.0.0')



