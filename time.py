from ftplib import FTP  
import socket
import telnetlib
import os,zipfile
from os.path import join
from datetime import date
from time import time
import time

time.localtime(time.time())
nowtime=time.strftime('%Y-%m-%d',time.localtime(time.time()))
print nowtime


