#!/usr/bin/python2

import socket
import datetime
import time 
import sys 

from datetime import datetime


UDP_IP1 = "10.0.1.43"
UDP_IP2 = "10.0.1.44"

UDP_PORT = 10300

now = datetime.now()

dt_string = now.strftime("%Y-%m-%dT%H:%M:%S")
externalidvalue= sys.argv[1]
priorityvalue= sys.argv[2]
#print(dt_string)

message="""<?xml version="1.0" encoding="UTF-8"?> <request version="17.6.15.1526" type="job">
<externalid>0649396368</externalid>
<systemdata>
<name>Micromedia-SMS</name>
<datetime>"""+ str(dt_string) + """</datetime>
<timestamp>5948e6f0</timestamp>
<status>1</status>
<statusinfo>System running</statusinfo>
</systemdata>
<jobdata> 
<priority>"""+ str(priorityvalue) + """</priority>
<messages>
<message1></message1>
<message2></message2>
<messageuui>"""+ str(externalidvalue) + """</messageuui>
</messages>
<status>0</status>
<statusinfo></statusinfo>
</jobdata>
<senderdata> 
<address>1010</address>
<name>CENTRO DE CONTROL</name>
<location>Central</location>
</senderdata>
<persondata> 
<address>1030</address>
</persondata>
</request>"""

#print(message)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((UDP_IP1,UDP_PORT ))

s.send(message)

print('Mensaje enviado Antena1')

s.connect((UDP_IP2,UDP_PORT ))

s.send(message)

print('Mensaje enviado Antena2')


#time.sleep(0.5)
#resp = s.recv(1024)

#print resp

