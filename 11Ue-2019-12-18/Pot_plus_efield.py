# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt 
import os

   


    
class datamatrix():
    def __init__(self):
        self.valuematrix = None
        self.isstatic = None
        self.numberofplots = 0
    def Readmatrix(self,path):
        if not os.path.exists(path):
            return False
        with open(path, 'r') as f:
            tmpmatrix = [[str(num) for num in line.split()] for line in f]
        #for a in len(tmpmatrix)
        #tmpmatrix[0] = list(filter(None, tmpmatrix[0]))
     
        self.valuematrix =  np.zeros((len(tmpmatrix),len(tmpmatrix[0])))
        self.isstatic =  [ [ None for i in range(len(tmpmatrix))] for h in range(len(tmpmatrix[0]))]
        for x in range(len(tmpmatrix)):
            for y in range(len(tmpmatrix[x])):
                #print("{}  {}  {}".format(x,y,tmpmatrix[x][y]))
                
                if  tmpmatrix[x][y][0]=="*":
                    self.valuematrix[x][y]=tmpmatrix[x][y][1:]
                    self.isstatic[x][y] = True
                else:
                    self.valuematrix[x][y]=tmpmatrix[x][y]
                    self.isstatic[x][y] = False
                    
        return True
    
    def calculate_pot(self, Iterations):
        for i in range(Iterations):
            for x in range(1,len(self.valuematrix-1)):
                for y in range(1,len(self.valuematrix[x])-1):
                    if not self.isstatic[x][y]:
                        self.valuematrix[x][y]=(self.valuematrix[x-1][y]+self.valuematrix[x+1][y]+self.valuematrix[x][y-1]+self.valuematrix[x][y+1])/4
            
    def showmatrix(self,show):
        dummy= plt.figure(self.numberofplots)        
        plt.imshow(self.valuematrix, cmap ="jet")
        plt.colorbar()
        if show == True:
            
            plt.show()
        self.numberofplots +=1

        
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
        
if __name__== "__main__":
    a = datamatrix()
    path=r"C:\Users\Raphael\Desktop\UNI\Daten_2.5\Git_Daten\11Ue-2019-12-18\laplace_daten\dach_ko60x60.dat"
    if not a.Readmatrix(path):
        print("{} not found".format(path))
    a.showmatrix(False)
    a.calculate_pot(100)
    a.showmatrix(False)
    a.calculate_pot(100)
    a.showmatrix(True)
    
