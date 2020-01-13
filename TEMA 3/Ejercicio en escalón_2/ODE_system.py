# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:44:02 2019

@author: Invitado
"""
#Definir el sistema de ecuaciones diferenciales
import numpy as np #Crear y manipular arrays

def fun(Y,t1,TM,f_inter):
    
    NA = Y[0]
    NB = Y[1]
    NC = Y[2]
    NT = NA+NB+NC
    
    caudal = 10 #m3/min
    k1 = 0.873 #min^-1
    k2 = 4.55 #min^-1
    R = 8.314 #Pa/K/mol
    To = 373 #K 
    Po = 1*101325 #Pa
    
    V = TM*caudal
    
    Co = Po/(R*To)
    CA = Co*(NA/NT)
    CB = Co*(NB/NT)
    
    R1 = k1*CA
    R2 = k2*CB
    
    rA = -R1
    rB = R1 - R2
    rC = R2
    
    salida_1 = rA*V*f_inter(t1)
    salida_2 = rB*V*f_inter(t1)
    salida_3 = rC*V*f_inter(t1)
    salida = np.array([salida_1,salida_2,salida_3])
    return salida