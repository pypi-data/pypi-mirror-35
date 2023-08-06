#!/usr/bin/python
import os.path
from configparser import SafeConfigParser

class config():
    def __init__(self, file='main.ini', section='postgresql'):
        """ Constructor
        :type file: str
        :param file: Config file to load

        :type section: str
        :param: section: Section of the ini config to read
        """
        filename = os.path.join(os.path.dirname(__file__), '..', 'config', file)
        if (os.path.isfile(filename)):
            self.filename = filename
            self.section = section
        else:
            raise Exception("Conf file doesn't exist")
        
    def read(self):
        """ read
        Read the ini file and return the requested content.
        """
        parser = SafeConfigParser()
        parser.read(self.filename)
        conf = {}

        if parser.has_section(self.section):
            params = parser.items(self.section)
            for param in params:
                conf[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the config file {1}'.format(self.section, self.filename))
        
        return conf

    def write(self, fields):
        """ write
        :type config: dict
        :param config: Dict of config data
        Write back to an ini config file.
        """
        config = SafeConfigParser()
        if (self.section == 'postgresql'):
            config.read(self.filename)

            if not (config.has_section('postgresql')):
                config.add_section('postgresql')

            config.set('postgresql', 'host', fields['host'])
            config.set('postgresql', 'database', fields['database'])
            config.set('postgresql', 'user', fields['user'])
            config.set('postgresql', 'password', fields['password'])

            with open(self.filename, 'w') as configfile:
                config.write(configfile)