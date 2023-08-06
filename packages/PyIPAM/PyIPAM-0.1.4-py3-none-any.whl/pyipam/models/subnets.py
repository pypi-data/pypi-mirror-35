#!/usr/bin/python
import ipaddress
import socket
from ..classes.db import db
from ..classes.config import config
from ..classes.background import BackgroundTasks

class SubnetsModel(object):
    def __init__(self):
        self.db = db()

    def load_subnet(self, id):
        return(self.db.select("SELECT * FROM subnets WHERE id =" + id))

    def load_subnets(self):
        return(self.db.select('SELECT * FROM subnets ORDER BY subnet DESC'))
    
    def add_subnet(self, fields):
        # Check first that subnet doesn't exist
        if (len(self.db.select("SELECT * FROM subnets WHERE subnet ='" + fields['subnet'] + "'")) < 1):
            # Add new subnet
            self.db.query("INSERT INTO subnets(subnet, vlan, description) VALUES ('" + fields['subnet'] + "', '" + fields['vlan'] + "', '" + fields['description'] + "')")

            # Add new ip range table
            subnet = self.db.select("SELECT * FROM subnets WHERE subnet = '" + fields['subnet'] + "'")
            ip_network_query = [
                """
                CREATE TABLE IF NOT EXISTS ip_subnet_addresses_{0} (
                    id serial,
                    ip VARCHAR(15) NOT NULL,
                    status VARCHAR(7),
                    host VARCHAR(50),
                    note VARCHAR(150),
                    PRIMARY KEY(id)
                )
                """
            ]
            self.db.query(ip_network_query[0].format(subnet[0][0]))

            # import IP addresses into the new table:
            net4 = ipaddress.ip_network(fields['subnet'])

            for x in net4.hosts():
                self.db.query("INSERT INTO ip_subnet_addresses_" + str(subnet[0][0]) + "(ip, status, host) VALUES ('" + str(x) + "', 'Offline', 'Unassigned')")

            tasks = BackgroundTasks()
            tasks.start_thread(subnet[0])
            return True
        else:
            print("ERROR: Subnet already exists")
            return False
    
    def edit_subnet(self, id, fields):
        # Edit a subnet
        self.db.query("UPDATE subnets SET vlan='" + fields['vlan'] + "', description='" + fields['description'] + "' WHERE id=" + id)

    # Delete request subnet and ip_range table
    def delete_subnet(self, id):
        commands = [
            'DELETE FROM subnets WHERE id = ' + id,
            'DROP table ip_subnet_addresses_' + id
        ]
        for command in commands:
            try:
                self.db.query(command)
            except ():
                print("ERROR: failed to run query")

    def load_ip_address(self, subnet_id, ip_id):
        return(self.db.select('SELECT * FROM ip_subnet_addresses_' + subnet_id + ' WHERE ID = ' + ip_id))

    def load_ip_addresses(self, subnet_id):
        return(self.db.select('SELECT * FROM ip_subnet_addresses_' + subnet_id + ' ORDER BY id'))

    def load_last_id(self, subnet_id):
        return(self.db.select('SELECT id FROM ip_subnet_addresses_' + subnet_id + ' ORDER BY id DESC LIMIT 1'))
    
    def save_ip_address(self, subnet_id, ip_id, field, value):
        if (field == 'host'):
            self.db.query("UPDATE ip_subnet_addresses_" + subnet_id + " SET host='" + value + "' WHERE id=" + ip_id)
        elif (field == 'note'):
            self.db.query("UPDATE ip_subnet_addresses_" + subnet_id + " SET note='" + value + "' WHERE id=" + ip_id)

    def scan_ip(self, subnet_id, ip):
        """ 
        scan_ip
        :type subnet_id: str
        :param subnet_id: Subnet ID
        :type ip: str
        :param ip: IP address re-scan
        Scan a indrividual IP address
        """
        try:
            data = socket.gethostbyaddr(str(ip))
            hostname = data[0]
            hostname = hostname.strip("'")
            self.db.query("UPDATE ip_subnet_addresses_" + str(subnet_id) + " SET host = '" + hostname + "', status = 'Online' WHERE ip = '" + str(ip) + "'")
        except Exception:
            return False # Don't raise an exception just return false