#!/usr/bin/python
import ipaddress
import subprocess
import threading
import time
import socket
import os
from ..classes.db import db

class BackgroundTasks(object):

    def __init__(self, interval=120):
        """ Constructor
        :type interval: int
        :param interval: Check the interval in seconds

        :type subnets: list
        :param: subnets: Holds the list of subnets to scan
        """
        self.interval = interval
        self.db = db()

    def start_thread(self, subnet):
        """ start_thread
        :type subnet: map
        :param subnet: Subnet to start a thread against.

        Start subnet thread
        """
        if (subnet == None):
            print('ERROR: No subnet supplied')
        else:
            thread = threading.Thread(target=self.run, args=(subnet,))
            thread.daemon = True
            thread.start()

    def start_all_threads(self, subnets):
        """ start_all_threads
        :type subnets: map
        :param subnets: Subnets to start threads against.

        Start all subnet threads
        """
        # Create system threads for each subnet
        if (subnets == None):
            print('ERROR: No subnets supplied')
        else:
            threads = []
            for subnet in subnets:
                thread = threading.Thread(target=self.run, args=(subnet,))
                threads.append(thread)
                thread.daemon = True
                thread.start()

    def ping_subnet(self, subnet):
        """ ping_subnets
        Scan all IP addresses within the subnets
        """
        net_address = subnet
        ip_network = ipaddress.ip_network(net_address[1])
        print("INFO: Scanning " + net_address[1])

        all_addresses = list(ip_network.hosts())

        if (os.name == 'nt'): # If running Windows
            # Sub process config to hide console window
            info = subprocess.STARTUPINFO()
            info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            info.wShowWindow = subprocess.SW_HIDE

        # Ping each IP in the network address range
        for i in range(len(all_addresses)):
            if (os.name == 'nt'):
                output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(all_addresses[i])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
            else:
                output = subprocess.Popen(['ping', '-c', '1', '-W', '1', str(all_addresses[i])], stdout=subprocess.PIPE).communicate()[0]

            try:
                if "Destination host unreachable" in output.decode('utf-8'):
                    self.db.query("UPDATE ip_subnet_addresses_" + str(subnet[0]) + " SET status = 'Offline' WHERE ip = '" + str(all_addresses[i]) + "'")
                elif "Request timed out" in output.decode('utf-8'):
                    self.db.query("UPDATE ip_subnet_addresses_" + str(subnet[0]) + " SET status = 'Offline' WHERE ip = '" + str(all_addresses[i]) + "'")
                elif "1 packets transmitted, 0 received" in output.decode('utf-8'): # For Linux pings
                    self.db.query("UPDATE ip_subnet_addresses_" + str(subnet[0]) + " SET status = 'Offline' WHERE ip = '" + str(all_addresses[i]) + "'")
                elif "1 packets transmitted, 0 packets received" in output.decode('utf-8'): # For Alpine Linux
                    self.db.query("UPDATE ip_subnet_addresses_" + str(subnet[0]) + " SET status = 'Offline' WHERE ip = '" + str(all_addresses[i]) + "'")
                else:
                    hostname = self.reverse_lookup(str(all_addresses[i]))
                    if (hostname == False):
                        hostname = "Unassigned"
                    
                    if (hostname):
                        self.db.query("UPDATE ip_subnet_addresses_" + str(subnet[0]) + " SET host = '" + hostname + "', status = 'Online' WHERE ip = '" + str(all_addresses[i]) + "'")
            except RuntimeError:
                break

    def reverse_lookup(self, ip):
        """ reverse_lookup
        :type ip: str
        :param ip: IP address to reverse lookup
        Reverse lookup an IP address
        """
        try:
            data = socket.gethostbyaddr(ip)
            hostname = data[0]
            hostname = hostname.strip("'")
            return hostname
        except Exception:
            return False # Don't raise an exception just return false

    def run(self, subnet):
        """ Run
        :type subnet: str
        :param subnet: Subnet to run thread against
        Run daemon until application terminates
        """
        print("INFO: Worker thread started")
        try:
            while True:
                self.ping_subnet(subnet)
                print('INFO: Completed scan of ' + str(subnet[1]))
                time.sleep(self.interval)
        except Exception as err:
            print("ERROR: Worker thread for '" + str(subnet[1]) + "' terminating due to the following issue '" + str(err) + "'")