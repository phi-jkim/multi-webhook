import json
# import json2html
import os 

from app import app
from flask import render_template, request, Flask, abort, jsonify

APP_ROOT = os.path.dirname(os.path.abspath(__file__))  
APP_STATIC = os.path.join(APP_ROOT, 'static')

@app.route('/')   
def index(): 
    return render_template('index.html') 

@app.route('/webhook', methods=['GET', 'POST']) 
def webhook(): 
    if request.method == 'POST': 
        # enter the server & function to be alerted (webhook portion)   
        return 'success', 200 
    elif request.method == 'GET': 
        with open(os.path.join(APP_STATIC, 'data.json'), 'r') as f: 
            data = json.load(f)
        return render_template('data.html', jsonfile = data) 
    else: 
        abort(400) 