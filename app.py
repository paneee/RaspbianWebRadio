from flask import Flask, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
import os
# from model import WebRadios

app = Flask(__name__) 
app.secret_key = os.urandom(12)



Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

# print (WebRadios.items)

@app.route('/', methods=['GET','POST'])
def hello():
    #return "Hello World"
    return render_template('index.html')

app.run(debug=True, port=5010, host='192.168.1.3')  


