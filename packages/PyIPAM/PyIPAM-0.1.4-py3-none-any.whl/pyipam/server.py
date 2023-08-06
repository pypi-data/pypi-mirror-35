#!/usr/bin/env python
from flask import Flask
from waitress import serve
from pyipam.classes.db import db
from pyipam.classes.background import BackgroundTasks

app = Flask('pyipam',  static_url_path='')
from pyipam.controllers import main, subnets

def run():
    print('INFO: Initialising PyIPAM')
    # Startup the background tasks processes
    try:
        database = db()
    except:
        pass
    else:
        subnets = database.select('SELECT * FROM subnets ORDER BY subnet DESC')
        tasks = BackgroundTasks()
        tasks.start_all_threads(subnets)
    
    # Startup the main UI process
    serve(app, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    run()