# -*- coding: utf-8 -*-
"""
Created on Sun May 26 08:39:19 2019

@author: Invitado
"""

import math

def fun(V,x):
    
    #Parámetros
    To = 330 #K
    k1 = 31.1
    kc1 = 3.03
    E = 65.7*1000 #J/mol
    DHr = -6900 #J/molA
    FAo = 0.9*163*1000  #mol/h
    Fi = 0.1*163*1000 #mol/h
    CpA = 141 #J/mol
    Cpi = 161 #J/mol
    CAo = 9.3*1000 #mol/m^3
    R = 8.31
    
    #Balance de energía
    Qs = FAo*CpA+Fi*Cpi
    T = To + (-FAo*DHr*x)/Qs
    
    #Cinética
    k = k1*math.exp((E/R)*(1/360 - 1/T))
    kc = kc1*math.exp((DHr/R)*(1/333 - 1/T))
    CA = CAo*(1-x)
    CB = CAo*x
    rA = -k*CA+(k/kc)*CB
    
    salida = -FAo/rA
    
    return salida
