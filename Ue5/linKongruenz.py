# -*- coding: utf-8 -*-
import  sys, math

def rand():
    global last_y
    
    last_y = ((a*last_y+c) % m)

    #print ("a:", a,"c:", c,"m:",m,"last_y:",last_y)
    return last_y

def uni(imax):
    global last_y
    global a
    global c
    
    last_y = (a*last_y+c) % (math.floor(imax)+1)
    result = math.floor(last_y)
   # print ("a:", a,"c:", c,"m:",m,"last_y:",last_y,"Zahl zwischen 0 und", imax,":",result)    
    return result

def uni01_alt():
    #in angabe is 1 dabei!!hier nicht!!! 
    global last_y
    global a
    global c
    global m
    
    last_y = ((a*last_y+c) % m)
    result = (last_y/m)
    #print ("a:", a,"c:", c,"m:",m,"last_y:",last_y,"Zahl zwischen 0 und 1:",result)    
    
    return result

def uni01():
    #in angabe is 1 dabei!!hier ist sie auch dabei!! 
    global last_y
    global a
    global c
    global m
    last_y = ((a*last_y+c) % m)
    value1 = last_y
    last_y = ((a*last_y+c) % m)
    value2 = last_y
    result = 0
    if (value1 >= value2):
        if (value1 == 0):
            result = 0
        else:
            result = value2/value1
    else:
        result = value1/value2
    #print ("a:", a,"c:", c,"m:",m,"Zahl zwischen 0 und 1:",result)    
    
    return result

def setup(_a, _c, _m, y0):
    global a
    global c
    global m
    global last_y
    
    if (a >= m):
        print ("a muss kleiner sein als m")
        return
    
    a = _a
    c = _c
    m = _m
    last_y = y0

def setup_RANDU():
    setup(65539,0,2147483648,1)# 2147483648 = 2**31 und  65539 = 2**16 + 3
    
def setup_C():
    setup(25214903917,11,2**48,0)

#wie ywertegrenzen automatisch finden für rand?
    #Funktion darf keinen 0-Durchgang haben!
def monteCarlo(xuntergrenze, xobergrenze,yuntergrenze, yobergrenze, werteanzahl,obernull, f,*f_arguments):
    setup_C()
    bereichlaenge = xobergrenze - xuntergrenze
    wertebereich = yobergrenze - yuntergrenze
    infunction_counter = 0
    for x in range(werteanzahl):
        xrandzahl = xuntergrenze + uni01()*bereichlaenge#x-Argument
        wert = f(xrandzahl,*f_arguments)#funktionswert an x
        yrandzahl = yuntergrenze + uni01()*wertebereich#y-Argument
        #print ("Zufallswert:",yrandzahl,"Wert:",wert)
        if(wert > yrandzahl and obernull):            
            infunction_counter = infunction_counter + 1
            #print(infunction_counter)
        else:
            if(wert < yrandzahl and (not obernull)):            
                infunction_counter = infunction_counter + 1
    
    #print (infunction_counter,"von" , werteanzahl,"im Wertebreich, Gesamtfläche Bereich:", bereichlaenge*wertebereich)
    return (infunction_counter/werteanzahl)*bereichlaenge*wertebereich

#aufgabe 2
def kugel_vol_MC(werteanzahl,dimensionsanzahl):
    setup_C()
    
    counter = 0
    for y in range(werteanzahl):
        r2 = 0
        for x in range(dimensionsanzahl):
            randzahl =  uni01()
            r2 = r2 + randzahl**2
            #print(r2,randzahl**2)
        if (r2 < 1):
            counter = counter +1
            #print(counter)
    return (counter/werteanzahl)*math.pow(2,dimensionsanzahl)

def kugelvol_formel(dimensionen):
    # v = (pi hoch (n/2)) / (gamma(1+n/2))
    # v = (pi hoch (n/2)) / (!(n/2)) !!!nur für gerade n!!!
    return ((math.pi)**(float(dimensionen)/2.0) / (math.gamma(1.0 + float(dimensionen)/2.0)))
    #return ((math.pi)**(float(dimensionen)/2.) / (math.factorial(float(dimensionen)/2.)))
a = 1
c = 1
m = 2
last_y = 1     
#print ("Argv-Len:" , len(sys.argv), " (benötigt sind 5)")
#if __name__ == '__main__':
#    if len (sys.argv) < 5:
#        print ("Error: ungültige Parameteranzahl: Anzugeben sind a,c,m und last_y als Integer!")
#        sys.exit()
#
#try:
#    a = int(sys.argv[1])
#    c = int(sys.argv[2])
#    m = int(sys.argv[3])
#    last_y = int(sys.argv[4])
#    if (m == 0):
#       print ("Modullo m=0 ist verboten. wird 41 gesetzt.") 
#       m = 41
#except:
#    print ("Error: a,c,m und last_y müssen Integer sein")
#    raise
    #return
    
       
#list1 =[]
#for x in range(10):
#    list1.append(rand())
#print ("Randliste:" , list1)


#randu
setup_RANDU()
f= open("Spektraltest_Randu.txt","w+")
row = 5000
column = 3
matrix = [ [ 0 for i in range(column)] for h in range(row)]
for x in range(row):
    for y in range(column):
        matrix[x][y]= uni01()
        f.write("%7.6f\t" % (matrix[x][y]))
    f.write("\r\n")
f.close()

#c
setup_C()
f= open("Spektraltest_c.txt","w+")
row = 5000
column = 3
matrix = [ [ 0 for i in range(column)] for h in range(row)]
for x in range(row):
    for y in range(column):
        matrix[x][y]= uni01()
        f.write("%7.6f\t" % (matrix[x][y]))
    f.write("\r\n")
f.close() 

#monte carlo a
cnt = 10
f= open("f_integral.txt","w+")
loopcount = 7
real_result = 1000./3.
for x in range(1,loopcount):
    
    result = monteCarlo(0, 10,0, 120, cnt,True, math.pow,(2))
    print ("Punkteanzahl:",cnt, "Integralwert:",result, "Abweichung:",abs(real_result-result))
    f.write("%d\t%6.5f\n" % (cnt, abs(real_result-result)))
    cnt = cnt * 10
f.close() 

#monte carlo b
#werte für echtes vol ungenau und mc volumen falsch!
dims = [2,4,6,8,10,12,14]#dimensionen
points = 100000#anzahl mc punkte
print("")
f= open("vol_integral.txt","w+")
for d in dims:
    real_result = kugelvol_formel(d)
    result = kugel_vol_MC(points,d)
    print ("Punkteanzahl:",points,"Dimensionen:",d, "Integralwert:",result,"echter Wert:",real_result, "Abweichung:",abs(real_result-result))
    if (result == 0):
        result = 0.001
    f.write("%d\t%6.5f\n" % (d,real_result/result ))
f.close() 