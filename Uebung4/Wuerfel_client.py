# -*- coding: utf-8 -*-


"""ssl_client.py host port message cert
"""

import sys,socket,time
import numpy as np
from tabulate import tabulate
import  os
import scipy.stats


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
        self.binstd = None
        self.binmean = None
        self.binoccurence = []
        self.bindeviationfrommean=[]
        self.neighbourcorrelation=None
        self.entropy = None
    def CalcBinomialStatistics(self):
        self.mean = np.mean(self.wuerfeldata)
        self.std = np.std(self.wuerfeldata)
        for x in range(1,7):
            self.binoccurence.append(np.sum(self.wuerfeldata == x))
            self.bindeviationfrommean.append((self.binoccurence[x-1]-binmean)/binstd)
       
    def CalcNeighbourcorrelation(self):
        self.neighbourcorrelation = np.zeros((6,6))
        for i in range(1,self.wuerfeldata.size):
            self.neighbourcorrelation[self.wuerfeldata[i-1]-1,self.wuerfeldata[i]-1]+=1
    def CalcEntropy(self):
        
        self.entropy = scipy.stats.entropy(self.binoccurence)
            
        
def printdata(filename, wuerfeldata):
    with open(filename, 'w') as f:
        for w in wuerfeldata:
            f.writelines("name= {}\n".format(w.name))
            for i,zahl in enumerate(w.binoccurence):
                f.writelines("number = {} | occurence={} | deviation in std={}\n".format(i+1,zahl,w.bindeviationfrommean[i]))
            f.writelines("Entropy= {}\n".format(w.entropy))
            
            f.writelines("Neighbourcorrelation\n")
            headers= [1,2,3,4,5,6]
            f.writelines(tabulate(w.neighbourcorrelation,headers,showindex=range(1,7)))
            f.writelines("\n\n---------------------------------------------\n")
            

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
binmean=NUMBEROFTHROWS/6
binstd=np.sqrt(binmean*(1-1/6))
outputfile= os.path.dirname(sys.argv[0])+ r"/output.txt"

 
# Oeffnen des Sockets
# Auch der client muss einen socket oeffnen
if __name__== "__main__":
    Wuerfelarray=[]
    
    for i,zahl in enumerate(KENNZAHLEN):
        try:
           s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error:
           s = None
        ConnectToServer(s)
        Wuerfelarray.append(Wuerfel(zahl))
        message = "throw {} {}".format(NUMBEROFTHROWS,zahl).encode("utf-8")
        Wuerfelarray[i].wuerfeldata = np.asarray(list(SendPlusRecive(s,message)))[:-1]-48
        s.close()
    
    
    for w in Wuerfelarray:
        w.CalcBinomialStatistics()
        w.CalcNeighbourcorrelation()
        w.CalcEntropy()
           
    printdata(outputfile,Wuerfelarray)
    

    





