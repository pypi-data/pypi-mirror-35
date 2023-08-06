#!/usr/bin/python
from ..classes.db import db
from ..classes.config import config

class MainModel(object):
    def __init__(self):
        self.db = db()
    
    def setup_app(self, fields):
        """ setup_app
        :type fields: dict
        :param fields: Dict of config data
        Initial setup for PyIPAM
        """
        try:
            print("INFO: App setup in progress")
            self.config = config()
            self.config.write(fields)
            self.db = None
            self.db = db()
            self.db.create_tables()
        except (Exception) as Error:
            print("ERROR: Config write error.", str(Error))