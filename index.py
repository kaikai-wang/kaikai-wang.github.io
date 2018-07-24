#!usr/bin/python3
# _*_ coding: utf-8 _*_

from flask import Flask, url_for, redirect
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return 'index.py'


@app.route('/login/')
def login():
    return 'login page'

if __name__ == '__main__':
    app.run(port=80, debug=True)