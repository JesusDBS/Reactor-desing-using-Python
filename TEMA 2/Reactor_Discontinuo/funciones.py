# -*- coding: utf-8 -*-
"""
Created on Sun May 26 17:52:11 2019

@author: Invitado
"""

import math
import numpy as np

def fun(y,t):
    
    CA = y[0]
    CB = y[1]
    CC = y[2]
    T = y[3]
    V = y[4]
    
    #Parámetros
    ro = 950 #g/L
    vo = 5 #L/min
    CBo = 30 #mol/L
    Ta = 320 #K
    TB = 520 #K
    Cp = 0.6 #Cal/g*K
    DHr = -5000 #Cal/molA
    UA = 10000 #Cal/min*K
    
    k = 4E6*math.exp(-7900/T)
    rA = -k*CA*CB
    rB = rA
    rC = -rA
    
    salida_1 = rA - CA*vo/V
    salida_2 = rB + (CBo - CB)*(vo/V)
    salida_3 = rC - CC*vo/V
    salida_4 = (-UA*(T-Ta) + ro*Cp*vo*(TB-T) + rA*DHr*V)/(ro*Cp*V)
    salida_5 = vo
    
    salida = np.array([salida_1,salida_2,salida_3,salida_4,
                       salida_5])
    return salida
    
    
    
    
    
    
    
    