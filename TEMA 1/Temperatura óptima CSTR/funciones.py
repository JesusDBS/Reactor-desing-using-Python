# -*- coding: utf-8 -*-
"""
Created on Fri May 24 18:49:53 2019

@author: Invitado
"""
import math

global CAo,R
R = 1.987 #Constante de los gases en %cal/mol/l
CAo = 2 #Concentración inicial de A mol/l

def rA(T,x):
      
    k1 = (5*(10**8))*math.exp(-12500/(R*T))
    k2 =( 3.422*(10**21))*math.exp(-32500/(R*T))

    rR = (k1*CAo*(1-x))-(CAo*x*k2)
    return rR

def volumen(T,x):
    
    FR = 100 #mol de R/min
    
    k1 = (5*(10**8))*math.exp(-12500/(R*T))
    k2 =( 3.422*(10**21))*math.exp(-32500/(R*T))
    
    rA = -(k1*CAo*(1-x))+(CAo*x*k2)
    rR = -rA
    v = FR/rR
    return v

        