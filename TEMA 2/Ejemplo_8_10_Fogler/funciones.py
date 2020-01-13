# -*- coding: utf-8 -*-
"""
Created on Sun May 26 09:36:35 2019

@author: Invitado
"""

import math
import numpy as np

def fun(y,v):
    
    FA = y[0]
    FB = y[1]
    FC = y[2]
    T = y[3]
    CAo = 0.1 #mol/dm3
    CpA = 90 #J/mol
    CpB = 90
    CpC = 180
    DHr1 = -20000
    DHr2 = -60000
    UA = 4000 #J/dm3*s*C
    Ta = 100 + 273
    To = 150 + 273
    FT = FA +FB +FC
    CA = CAo*(FA/FT)*(To/T)
    k1 = 10*math.exp(4000*(1/300 - 1/T))
    k2 = 0.09*math.exp(9000*(1/300 - 1/T))
    r1A = -k1*CA
    r2A = -k2*CA**2
    rA = r1A + r2A
    rB = -r1A
    rC = -r2A/2
    Qr = -r1A*DHr1 - r2A*DHr2
    Qs = FA*CpA + FB*CpB + FC*CpC
    
    salida_1 = rA
    salida_2 = rB
    salida_3 = rC
    salida_4 = (UA*(Ta - T) - Qr)/Qs
    
    salida = np.array([salida_1,salida_2,salida_3,salida_4])
    
    return salida

