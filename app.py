from flask import Flask, redirect, url_for, render_template, request
from flask_bootstrap import Bootstrap
from model import WebRadios
from mpc import Mpc
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)

mpc = Mpc()


Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True


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
            mpc.volumeUp()
        if request.form['button'] == 'VolumeUpUp':
            mpc.volumeUpUp()
        if request.form['button'] == 'VolumeDown':
            mpc.volumeDown()
        if request.form['button'] == 'VolumeDownDown':
            mpc.volumeDownDown()

        return render_template('index.html', radios=WebRadios, volume=mpc.getVolume(), actualPlay=select, selectedItem=select)


app.run(debug=True, port=5000, host='192.168.1.3')