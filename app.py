from flask import Flask, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__) 
app.secret_key = os.urandom(12)

# WebRadios={"ChiliZet":"https://ch.cdn.eurozet.pl/chi-net.mp3",
# "357":"https://n06a-eu.rcs.revma.com/ye5kghkgcm0uv?rj-ttl=5&rj-tok=AAABduJfGVcAbh2i1fQT0iMZcA",
# "RNS":"https://stream.nowyswiat.online/aac",
# "Record Chillout":"http://air2.radiorecord.ru:805/chil_aac_64",
# "Radio Kampus":"http://193.0.98.66:8005/",
# "Weszlo":"http://radio.weszlo.fm/s7d70a7895/listen",
# "PR3 Trojka":"mms://stream.polskieradio.pl/program3"}

Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True


@app.route('/', methods=['GET','POST'])
def hello():
    # print(WebRadios)
    return render_template('index.html')

app.run(debug=True, port=5000, host='192.168.1.3')  













