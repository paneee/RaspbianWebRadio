from flask import Flask, redirect, url_for, render_template, request
from flask_bootstrap import Bootstrap
import os
from model import WebRadios
from mpc import Mpc

app = Flask(__name__)
app.secret_key = os.urandom(12)

mpc = Mpc()
 

Bootstrap(app)
# app.config['BOOTSTRAP_SERVE_LOCAL'] = True


@app.route('/', methods=['GET', 'POST'])
def hello():

    if request.method == "GET":
        return render_template('index.html', radios=WebRadios, actualVolume=20, actualPlay="Radio Nowy Swiat")

    if request.method == "POST":
        if request.form['button'] == 'Play':
            mpc.play('http://radio.weszlo.fm/s7d70a7895/listen')
        if request.form['button'] == 'Stop':
            mpc.stop()
        # if request.form['button'] == 'VolumeUp':
            # print(mpc.GetVolume())

    return render_template('index.html', radios=WebRadios, actualVolume=20, actualPlay="Radio Nowy Swiat")


app.run(debug=True, port=5000, host='192.168.1.3')
