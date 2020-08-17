# -*- coding: utf-8 -*-

import paramiko
import tarfile
import os
import sys
import datetime
import socket
#from datetime import datetime


class Timer(object):
    """A simple timer class"""
    
    def __init__(self):
        pass
    def start(self):
        """Starts the timer"""
        self.start = datetime.datetime.now()
    def stop(self):
        """Stops the timer.  Returns the time elapsed"""
        self.stop = datetime.datetime.now()
        print str(self.stop - self.start)
    def elapsed(self):
        """Time elapsed since start was called"""
        print str(datetime.datetime.now() - self.start)[:-3]
    def now(self):
	print str(datetime.datetime.now())[:-3]

watch=Timer()
watch.start()
os.system("./docker-volumes.sh database save database-volumes.tgz")
#os.system("docker save -o database.tgz database")
sys.stdout.write("Checkpoint Archived ")
watch.elapsed()

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.0.110",username="toshiba",password="123456")
#Raises BadHostKeyException,AuthenticationException,SSHException,socket error
sftp=ssh.open_sftp()
sftp.put('/snapshot/database-volumes.tgz','/snapshot/database-volumes.tgz')
#sftp.put('/snapshot/database.tgz','/snapshot/database.tgz')
ssh.close()
watch.elapsed()

port = 8282
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.5.140.186',port))
sys.stdout.write("Handover Completed ")
watch.elapsed()
s.close()


