#!/usr/bin/python
import os.path
from flask import flash, redirect, render_template, send_from_directory, url_for, request, session, abort
from pyipam.server import app
from pyipam.models.main import MainModel
from pyipam.models.subnets import SubnetsModel

# Initalise models
model = MainModel()
subnetsModel = SubnetsModel()

# Publish the public resources, CSS etc.
@app.route('/res/<path:path>')
def send_res(path):
    return send_from_directory('static', path)

@app.route('/')
def home():
    filename = os.path.join(os.path.dirname(__file__), '..', 'config', 'main.ini')
    subnets = subnetsModel.load_subnets()
       
    # Redirect to setup page if conf doesn't exist
    if not(os.path.isfile(filename)):
        return redirect('/setup')
    else:
        return render_template(
            'main/home.html', 
            subnets=subnets
        )

@app.route('/setup', methods=['GET', 'POST'])
def setup():
    if request.method == 'GET':
        return render_template(
            'main/setup.html', **locals()
        )
    elif request.method == 'POST':
        fields={
            'host': request.form['host'],
            'database': request.form['database'],
            'user': request.form['user'],
            'password': request.form['password']
        }
        model.setup_app(fields)
        return redirect('/')

@app.route('/about')
def about():
    return render_template(
        'main/about.html', **locals()
    )