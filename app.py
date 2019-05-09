# -*- coding: utf-8 -*-

import flask
from flask import Flask, redirect, url_for, render_template, request, session
import json
import sys
import os


app = Flask(__name__)

@app.route("/")
def index():
    return flask.render_template('index.html')

@app.route("/about")
def about():
    return flask.render_template('about.html')

@app.route('/causes')
def causes():
    return flask.render_template('causes.html')

@app.route('/event')
def event():
    return flask.render_template('/event.html')

@app.route('/contact')
def contact():
    return flask.render_template('contact.html')

@app.route('/auction')
def auction():
    return flask.render_template('auction.html')

if __name__ == '__main__':
    # start app
    app.run(host='0.0.0.0', port=8000)
