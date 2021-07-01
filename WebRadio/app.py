from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os


app = Flask(__name__) 
app.secret_key = os.urandom(12)

 

Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

@app.route('/', methods=['GET','POST'])
def index():

    
    return render_template('index.html')

app.run(debug=True, port=5000, host='192.168.1.5') 
