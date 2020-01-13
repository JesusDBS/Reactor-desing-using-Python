# -*- coding: utf-8 -*-
"""
Created on Sun May 26 10:40:12 2019

@author: Invitado
"""

import math
import numpy as np

def fun(y,v):
    
    FEB= y[0] #Flujo de etilbenceno
    FE= y[1] #Flujo de estireno
    FH= y[2] #Flujo de hidrógeno
    FB= y[3] #Flujo de benceno
    FET= y[4] #Flujo de etileno
    FT= y[5] #Flujo de tolueno
    Fm= y[6] #Flujo de metano
    FV= y[7] #Flujo de vapor
    T= y[8] #Temperatura
    
    #Parametros
    P = 2.4 #atm
    b1 = -17.34
    b2 = -1.302E4
    b3 = 5.051
    b4 = -2.314E-10
    b5 = 1.302E-6
    b6 = -4.931E-3
    fi = 0.4
    ro = 2137 #Kg/m3 de particulas
    DHr1 = 118000 #KJ/Kmol de etilbenceno
    DHr2 = 105200  #KJ/Kmol de etilbenceno
    DHr3 = -53900  #KJ/Kmol de etilbenceno
    Cpm = 68 #KJ/Kmol*K
    CpET = 90 #KJ/Kmol*K
    CpB = 201 #KJ/Kmol*K
    CpT = 249 #KJ/Kmol*K
    CpE = 273 #KJ/Kmol*K
    CpEB = 299 #KJ/Kmol*K
    CpH = 30 #KJ/Kmol*K
    CpVap = 40 #KJ/Kmol*K
    
    #Ecuaciones explícitas
    Kpl = math.exp(b1 + (b2/T) + (b3*math.log(T)) + ((b4*T + b5)*T + b6)*T)  #atm
    F_Total = FEB+FE+FH+FB+FET+FT+Fm+FV
    PEB = (FEB/F_Total)*P #Presión parcial de etilbenceno (atm)
    PE = (FE/F_Total)*P #Presión parcial de estireno (atm)
    PH = (FH/F_Total)*P #Presión parcial de hidrógeno (atm)
    r1E = ro*(1-fi)*math.exp(-0.08539-(10925/T))*(PEB - ((PE*PH)/Kpl)) #Velocidad de reacción del 
                                                                       #estireno en la reacción 1 (Kmol/m3*s)
    r2B = ro*(1-fi)*math.exp(13.2392-(25000/T))*PEB #Velocidad de reacción del benceno en la reacción 2 (Kmol/m3*s)
    r3T = ro*(1-fi)*math.exp(0.2961-(11000/T))*(PEB*PH) #Velocidad de reacción del Tolueno en la reacción 3 (Kmol/m3*s)
    r1EB = -r1E
    r2EB = -r2B
    r3EB = -r3T
        
    rEB = r1EB + r2EB +r3EB
    rE = -r1EB
    rH = -r1EB + r3EB
    rB = -r2EB
    rET = -r2EB
    rT = -r3EB
    rm = -r3EB
    
    
    Qr = r1EB*DHr1 + r2EB*DHr2 + r3EB*DHr3 #Calor de reacción
    Qs = FEB*CpEB + FE*CpE + FH*CpH + FB*CpB + FET*CpET + FT*CpT + Fm*Cpm + FV*CpVap #Calor senible
    
    #Ecuaciones diferenciales
    salida_1 = rEB #Etilbenceno
    salida_2 = rE #Estireno
    salida_3 = rH #Hidrógeno
    salida_4 = rB #Benceno
    salida_5 = rET #Etileno
    salida_6 = rT #Tolueno
    salida_7 = rm #metano
    salida_8 = 0 #vapor
    salida_9 = Qr/Qs #Balance de energía
    salida = np.array([salida_1,salida_2,salida_3,salida_4,salida_5,
                       salida_6,salida_7,salida_8,salida_9])
    
    return salida
    
    
    
    
    
    
    