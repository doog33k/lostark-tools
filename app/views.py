from app import app
from flask import Flask, redirect, url_for, request, render_template, json,jsonify, send_from_directory
import os
import json

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/data/<name>')
def showjson(name):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", name )
    data = json.load(open(json_url))
    print("Type:", type(data))
    print (data)
    #print(flatten(data))
    return jsonify(data)    

@app.route('/')
def template():
    return render_template('index.html')    