#!/usr/bin/env python2

import socket
import io
import sys
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XML, fromstring
from bs4 import BeautifulSoup
from htmlcreator import HTMLDocument

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '0.0.0.0'
server_port = 10300

server = (server_address, server_port)
sock.bind(server)
print("Listening on " + server_address + ":" + str(server_port))

document = HTMLDocument()
document.set_title('Ubicacion Terminales')

while True:

        payload, client_address = sock.recvfrom(1024)

#        print('Conexion desde la IP :' + str(client_address))
        print("\n")
        payload= BeautifulSoup(payload,'xml')
        
#        print (payload)
        
        nombres = payload.find_all('name')
        extensiones = payload.find_all('address')
    
        document = HTMLDocument()
        document.set_title('Ubicacion Terminales'+ ' '  +nombres[0].get_text() )
        output_filepath = '/var/www/html/'+ nombres[0].get_text()+ '.html'
        
        print ("En la Base" + ' ' + nombres[0].get_text() + ' ' + "se encuentran los siguientes terminales")        	


        for i in range (0, len(nombres)-1):
         print(nombres[i+1].get_text() + ' ' + extensiones[i].get_text() )
         document.add_text(nombres[i+1].get_text() + ' ' + extensiones[i].get_text() )
         
         document.write(output_filepath)

#         print(f'{output_filepath} has been saved successfully!')