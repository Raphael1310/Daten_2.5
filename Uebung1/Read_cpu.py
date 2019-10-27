# -*- coding: utf-8 -*-
import time
import random

class Cpustats:
    def __init__(self, name):
        self.name = name
        self.oldstat = float(0)
        self.newstat = float(0)

def UpdateCpustats(cpustatlist, cpuread):
    for x,stats in enumerate(cpustatlist):
        stats.oldstat = stats.newstat
        stats.newstat = float(cpuread[x+1])

def Readcpu():
    cpufilepfad = r"/proc/stat"
    cpufile=open(cpufilepfad,"r")
    cpuread = cpufile.readlines(1)[0].split()
    cpufile.close()
    return cpuread

Cpustatlist= []
names = ["user","nice","system", "idle", "iowait", "irq", "softirq"]
for name in names:
    Cpustatlist.append(Cpustats(name))


cpuread=Readcpu()

UpdateCpustats(Cpustatlist, cpuread)

failsafe = 0 
while True: 
    cpuread = Readcpu()
    UpdateCpustats(Cpustatlist,cpuread)
    
    for cpustat in Cpustatlist:
        aenderung = 0
        if cpustat.oldstat != 0:
            aenderung = (cpustat.oldstat - cpustat.newstat)/cpustat.oldstat
        print(cpustat.name + " = " + str(aenderung)  + "%")
    
    
    failsafe +=1
    if failsafe == 20 :
        break
    print("---------------------------------------------------")
    time.sleep(5)




