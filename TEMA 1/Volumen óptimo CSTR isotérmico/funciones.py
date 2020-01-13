# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:06:29 2019

@author: Invitado
"""

#2A <----> B + C #Reacción en fase líquida reversible
#Datos del problema
global CA0, k1, k2, v0 #definir variables
CA0 = 48 #mol/m^3
k1 = 0.75 #m^3/mol*h
k2 = 16 #m^3/mol*h
v0 = 3.5 #m^3/h

#Ley de velocidad
def rA(x):
    
    CA = CA0*(1-x)
    CB = 0.5*CA0*x
    CC = 0.5*CA0*x
    
    salida = -k1*CA**2+(k1/k2)*CB*CC
    return salida

#Ecuación de diseño
def vol(xf,x0):
        
    F0 = v0*CA0
        
    salida = F0*(xf-x0)/-rA(xf)
    return salida
    
#Volumen total del sistema de reactores
def VT(x):
    V1 = vol(x[0],0)
    V2 = vol(x[1],x[0])
    V3 = vol(x[2],x[1])
    V4 = vol(0.8,x[2])
        
    salida = V1+V2+V3+V4
    return salida