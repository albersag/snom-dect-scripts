#!/usr/bin/python2

import socket
import datetime
import time 
import sys 

from datetime import datetime

UDP_IP1 = "10.0.1.43"
UDP_IP2 = "10.0.1.44"
UDP_PORT = 10300

alarmnumber = 5
messageuui = 'Positivo COVID19'
message1= 'Prueba de Mensaje 1'
message2='Prueba de Mensaje 2'
flash= 0
rings= 0
confirmationtype=2
destination= 1030 

now = datetime.now()

dt_string = now.strftime("%Y-%m-%dT%H:%M:%S")

#print(dt_string)


message="""<?xml version="1.0" encoding="UTF-8"?> 
<request version="1.0" type="job">
<systemdata>
<name>Alarma</name>
<datetime>"""+ str(dt_string) + """</datetime>
<timestamp>5948cde4</timestamp>
<status>1</status>
<statusinfo>System running</statusinfo>
</systemdata>
<jobdata>
<alarmnumber>1</alarmnumber>
<referencenumber>100</referencenumber>
<priority>1</priority>
<flash>"""+ str(flash) +"""</flash>
<rings>"""+ str(rings) +"""</rings> 
<confirmationtype>"""+ str(confirmationtype) +"""</confirmationtype>
<messages>
<message1>"""+ str(message1) +"""</message1>
<message2>"""+ str(message2) +"""</message2>
<messageuui>"""+ str(messageuui) +"""</messageuui>
</messages>
<status>0</status>
<statusinfo/>
</jobdata>
<persondata>
<address>"""+ str(destination) +"""</address>
<status>0</status>
<statusinfo/>
</persondata>
<externalid>ffeeaa</externalid>
</request>"""

#print(message)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((UDP_IP1,UDP_PORT ))

s.send(message)

print('Mensaje enviado Antena1')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((UDP_IP2,UDP_PORT ))

s.send(message)

print('Mensaje enviado Antena2')

#time.sleep(0.5)
#resp = s.recv(1024)

#print resp

