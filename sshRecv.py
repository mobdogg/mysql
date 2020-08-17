import time 
import os
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler 
import sys
from datetime import datetime
import socket
  
listensocket = socket.socket()
port=8282
ip = socket.gethostname()
listensocket.bind(('',port))
listensocket.listen(5)
clientsocket, client_address = listensocket.accept()
os.system("python sshRecv2.py")
exit()

