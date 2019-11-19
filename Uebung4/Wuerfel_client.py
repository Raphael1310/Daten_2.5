# -*- coding: utf-8 -*-


"""ssl_client.py host port message cert
"""

import sys,string,socket,time
# 
# if len(sys.argv) != 4:
#    print  "Usage: %s host port message" % sys.argv[0]
#    sys.exit(0)
# # Schreibt Nachricht zu einem socket und wartet auf Antwort
# =============================================================================
host = "server4.physprak.tuwien.ac.at"
port = 56701
message = "help".encode("utf-8")

# Oeffnen des Sockets
# Auch der client muss einen socket oeffnen
try:
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error:
   s = None
try:
   s.connect((host,port)) # Verbinde
except socket.error:
   s.close()
   s = None
if s is None:
   print('Can not open socket ')
   sys.exit(1)

# senden der daten
s.send(message+b"\r\n")
# lesen der Antwort
time.sleep(1)
data = s.recv(1000000)
s.close()
#print 'Received', `data`
#print data
print('Received:\n', data)
