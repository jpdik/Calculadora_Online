# coding: utf-8

import json
import os
import sys
import requests
import socket
import threading
import calc

from flask import Flask, Response, render_template, request

sys.path.insert(0, os.getcwd()[:os.getcwd().rfind('/')])

app = Flask(__name__)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api():
  if request.method == 'GET':
    return render_template('index.html') 
  else:
    return json.dumps({'404': 'Not Found'})

@app.route('/calcular', methods=['POST'])
def calcular():
  content = request.get_json(silent=True)

  calcu = calc.Calc("10.3.1.36", 8888)

  calcu.inserir_valores(json.dumps(content))

  calcu.calcular()
  return json.dumps(calcu.resultado())

if __name__ == "__main__":
  app.run(debug=True)
