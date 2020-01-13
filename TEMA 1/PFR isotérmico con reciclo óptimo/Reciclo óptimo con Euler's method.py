# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:17:33 2019

@author: Invitado
"""
import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fmin
global CA0, q, k2, k1, xf,n

CA0 = 1
q = 10
k2 = 1.234
k1 = 0.03
xf = 0.85
n = 100

def Ec_D(V,x,R): #Ecuación de diseño del reactor
    
    CP = CA0*x
    CA = CA0*(1-x)
    rA = k1*CA+k2*CA*CP
    salida = q*(1+R)/rA
    
    return salida

def ROP(R): #Reciclo Óptimo
    
    x0 = (R/(R+1))*xf

#setup time discretization
    x = np.linspace(x0,xf,n)
    dx = x[1] - x[0]

#allocate storage space and initial conditions
    sol = np.zeros(n)
    sol[0] = 0 #initial x

    for i in range(1,n):
        sol[i] = sol[i-1] + dx*Ec_D(sol[i-1],x[i-1],R)
    return sol[n-1]

semilla = 1
R_O = fmin(ROP,semilla,disp=False)

x0 = (R_O/(R_O+1))*xf
x = np.linspace(x0,xf,n)
dx = x[1] - x[0]
sol = np.zeros(n)
sol[0] = 0 #initial x
for i in range(1,n):
    sol[i] = sol[i-1] + dx*Ec_D(sol[i-1],x[i-1],R_O)
    
print("El volumen óptimo del reactor es: %2.f Litros" %sol[n-1])