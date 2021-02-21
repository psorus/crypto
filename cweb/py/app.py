from flask import Flask,url_for,redirect
app = Flask(__name__)

from loadaddress import *

@app.route('/')
def index():
    return "To visit a smart address (kovan network), add the address to this webaddress (this address/contract address)"


@app.route('/<add>')
def handlepage(add):
    #return loadaddress(add)
    return load(add)
   
@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))



