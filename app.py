from flask import Flask, redirect, url_for, render_template, request
from flask_bootstrap import Bootstrap
from model import WebRadios
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

class GetAllStation(Resource):
    def get(self):
        return WebRadios

class GetVolume(Resource):
    def get(self):
        return mpc.getVolume()

class SetVolume(Resource):
    def post(self, value):
        mpc.volumeChange(value)
        return mpc.getVolume(), 201

class Play(Resource):
    def post(self, station):
        mpc.play(WebRadios[station])
        return {station,WebRadios[station]}, 201

class Stop(Resource):
    def post(self):
        mpc.stop()
        return "OK", 201

        
api.add_resource(GetAllStation, '/api/getAllStation')
api.add_resource(GetVolume, '/api/getVolume')
api.add_resource(SetVolume,'/api/setVolume/<value>')
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



app.run(debug=True,port=5000, host='0.0.0.0')



