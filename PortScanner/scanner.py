#!/usr/bin/python3

import socket #library to use
from ports import ports_and_services
import validate

def getOpenPorts(target, portRange):
    openPorts = []
    validity = validate.validate(target)
    if validity!="Valid URL" and validity!="Valid IP":
        return validity
    #Obtener el host con socket
    host = socket.gethostbyname(target)
    #hacer un loop sobre el rango de puertos
    for port in range (portRange[0], portRange[1]+1):
    	sock = socket.socket(socket,AF_INET,socket.SOCK_STREAM)
    	sock.settimeout(0.5)
    #abrir el socket determinado
    	if not (sock.connet_ex[(host,port)]):
        	open_ports.append(port)
    	sock.close()
    #verificar si se conecta
    #si se conecta agregarlo al array
    return openPorts
