# -*- coding: utf-8 -*-
"""
Created on Wed May  8 07:42:12 2019

@author: Invitado
"""
import numpy as np
from scipy.integrate import solve_ivp
global CA0, q, k2, k1, xf

CA0 = 1
q = 10
k2 = 1.234
k1 = 0.03
xf = 0.85

def Ec_D(x,V,R): #Ecuación de diseño del reactor
    
    CP = CA0*x
    CA = CA0*(1-x)
    rA = k1*CA+k2*CA*CP
    salida = q*(1+R)/rA
    
    return salida

def ROP(R): #Reciclo Óptimo
    
    x0 = (R/(R+1))*xf
    xi = np.array([0])
    fun = lambda x,V: Ec_D(x,V,R)
    salida = solve_ivp(fun,(x0,xf),xi)
    
    return salida.y[-1][-1]















