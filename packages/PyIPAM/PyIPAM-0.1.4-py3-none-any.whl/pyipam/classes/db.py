#!/usr/bin/python
import psycopg2
from .config import config

class db():
    def __init__(self):
        """ Constructor
        Initiate database class.
        """
        self.conn = None
        try:
            # Read configuration for the db
            conf = config()
            self.params = conf.read()
        except:
            print('ERROR: Failed load the application config')
    
    def connect(self):
        try:           
            self.conn = psycopg2.connect(**self.params)
            self.cur = self.conn.cursor()
        except (Exception, psycopg2.DatabaseError):
            print('ERROR: Failed to connect to configured host')
            return False
        else:
            return True
    
    def create_tables(self):
        """ create_tables
        Create the default tables required by PyIPAM
        """
        commands = [
            """
            CREATE TABLE IF NOT EXISTS subnets (
            id serial,
            subnet VARCHAR(100) NOT NULL,
            vlan VARCHAR(10),
            description VARCHAR(255),
            PRIMARY KEY(id)
            );
            """
        ]
        if (self.conn == None):
            self.connect()
        try:
            for command in commands:
                self.query(command)
        except (Exception, psycopg2.DatabaseError) as error:
            print('ERROR: ' + str(error))

    def select(self, query):
        """ select
        :type query: str
        :param query: SELECT query to run against the DB

        Returns the properly formatted results from a SELECT query.
        """
        if (self.conn == None):
            self.connect()
        try:
            self.cur.execute(query)
            rows = self.cur.fetchall()

            # Construct array and return the results
            results = []
            for row in rows:
                results.append(row)
            
            return results
        except (Exception, psycopg2.DatabaseError) as error:
            print('ERROR: ' + str(error))

    def query(self, query):
        """ query
        :type query: str
        :param query: SQL query to run against the DB
        
        Runs requested SQL queries against the DB.
        """
        if (self.conn == None):
            self.connect()
        try:
            self.cur.execute(query)
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            self.conn.rollback()
            print('ERROR: ' + str(error))
            raise

    def close(self):
        """ close
        Close the connection to the db cleanly.
        """
        self.cur.close()
        self.conn.close()