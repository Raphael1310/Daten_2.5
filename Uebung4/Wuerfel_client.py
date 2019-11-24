# -*- coding: utf-8 -*-


"""ssl_client.py host port message cert
"""

import sys,string,socket,time
import numpy as np
# 
# if len(sys.argv) != 4:
#    print  "Usage: %s host port message" % sys.argv[0]
#    sys.exit(0)
# # Schreibt Nachricht zu einem socket und wartet auf Antwort
# =============================================================================
class Wuerfel():
    def __init__(self, name):
        self.name = name 
        self.wuerfeldata = []
        self.std = None
        self.mean = None
        self.occurence = []
        

def ConnectToServer(s):
    host = "server4.physprak.tuwien.ac.at"
    port = 56701
    try:
        s.connect((host,port)) # Verbinde
    except socket.error:
       s.close()
       s = None
    if s is None:
       print('Can not open socket ')
       sys.exit(1)
      
def SendPlusRecive(s,message):
    # senden der daten
    s.send(message+b"\r\n")
    # lesen der Antwort
    time.sleep(1)
    data = s.recv(4096)
    return data

KENNZAHLEN = [0, 1, 2, 3, 4, 5, 6, 71, 10, 11, 12, 13, 80, 20, 21, 22, 23, 100, 90, 70]
NUMBEROFTHROWS = 1000
message = "help".encode("utf-8")

# Oeffnen des Sockets
# Auch der client muss einen socket oeffnen

Wuerfelarray=[]


for i,zahl in enumerate(KENNZAHLEN):
    try:
       s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error:
       s = None
    ConnectToServer(s)
    Wuerfelarray.append(Wuerfel(zahl))
    message = "throw {} {}".format(NUMBEROFTHROWS,zahl).encode("utf-8")
    with Wuerfelarray[i-1] as w: 
        w.wuerfeldata = np.asarray(list(SendPlusRecive(s,message)))[:-1]-48
        w.mean = np.mean(w.wuerfeldata)
        w.std = np.std(w.wuerfeldata)
        for x in range(6):
            w.occurence.append(np.sum(w.wuerfeldata == x))
        print("name = {} || mean={} || std = {}".format(w.name,w.mean,w.std))
        print(w.occurence)
    s.close()
    

    





