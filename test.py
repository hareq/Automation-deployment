from ftplib import FTP  
import socket
import telnetlib
import os,zipfile
from os.path import join
from datetime import date
from time import time
import time
Host = '192.168.71.71'
ftpip='192.168.71.71'

f = zipfile.ZipFile('buildfiles.zip','w',zipfile.ZIP_DEFLATED)
startdir = "E:\\buildfiles"
for dirpath, dirnames, filenames in os.walk(startdir):
    for filename in filenames:
        f.write(os.path.join(dirpath,filename))
f.close()


time.localtime(time.time())
nowtime=time.strftime('%Y-%m-%d',time.localtime(time.time()))





username = 'root'
password = 'root'
finish = '# '

tn = telnetlib.Telnet(Host)

tn.read_until('login: ')
tn.write(username + '\n')

tn.read_until('Password: ')
tn.write(password + '\n')

tn.read_until(finish)
tn.write('bash'+'\n')


tn.read_until(finish)
tn.write('ps -ef | grep java'+'\n')



prep=tn.read_until(finish)
print prep

tn.write('ps -ef | grep pc'+'\n')


pcprep=tn.read_until(finish)
print pcprep


f = open('grep.dcb','w')
f.write(prep)
f.write(pcprep)
f.close()

f=open('grep.dcb','r')
str=f.read()
m=len(str)
for n in range(0,m):
    f.seek(n)
    t=f.read(4)
    if t=="root":
      t=f.read(7)
      print t
      tn.write('kill -9 '+t+'\n')
f.close()

f=open('grep.dcb','r')
str=f.read()
m=len(str)
for n in range(0,m):
    f.seek(n)
    t=f.read(4)
    if t=="omcr":
      t=f.read(7)
      print t
      tn.write('kill -9 '+t+'\n')
      time.sleep(5)
f.close()


      
tn.read_until(finish)
tn.close()



    
username = 'omcr'
password = 'omcr'
finish = '$ '

tn = telnetlib.Telnet(Host)

tn.read_until('login: ')
tn.write(username + '\n')

tn.read_until('Password: ')
tn.write(password + '\n')

tn.read_until(finish)
tn.write('bash'+'\n')



tn.read_until(finish)
tn.write('mkdir '+nowtime+'\n')

tn.read_until(finish)
tn.close()




timeout = 30
port = 21
ftpusername='omcr'
ftppassword='omcr'
ftp = FTP()
ftp.connect(ftpip,port,timeout)
ftp.login(ftpusername,ftppassword)
ftp.cwd(nowtime)

ftp.storbinary('STOR '+'buildfiles.zip', open('buildfiles.zip', 'rb'))

ftp.quit()




tn = telnetlib.Telnet(Host)

tn.read_until('login: ')
tn.write(username + '\n')

tn.read_until('Password: ')
tn.write(password + '\n')

tn.read_until(finish)
tn.write('bash'+'\n')


tn.read_until(finish)
tn.write('cd '+nowtime+'\n')


tn.read_until(finish)
tn.write('unzip buildfiles.zip'+'\n')



tn.read_until(finish)
tn.write('cd buildfiles'+'\n')


tn.read_until(finish)
tn.write('chmod 777 *'+'\n')

tn.read_until(finish)
tn.write('sh run.sh'+'\n')

tn.read_until(finish)
tn.close()
time.sleep(600)

username = 'root'
password = 'root'
finish = '# '
tn = telnetlib.Telnet(Host)

tn.read_until('login: ')
tn.write(username + '\n')

tn.read_until('Password: ')
tn.write(password + '\n')

tn.read_until(finish)
tn.write('bash'+'\n')

tn.read_until(finish)
tn.write('cd opt/omcr/'+nowtime+'/buildfiles'+'\n')

tn.read_until(finish)
tn.write('chmod 777 *'+'\n')

tn.read_until(finish)
tn.write('sh runnea.sh'+'\n')

tn.read_until(finish)
tn.close()


