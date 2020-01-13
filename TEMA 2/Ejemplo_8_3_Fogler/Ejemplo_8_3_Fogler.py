# -*- coding: utf-8 -*-
"""
Created on Sun May 26 08:50:12 2019

@author: Invitado
"""

from scipy.integrate import odeint
import numpy as np
import funciones as f
import matplotlib.pyplot as plt

#Resolver ecuación diferencial
fun = lambda V,x:f.fun(V,x)
Co = 0
P = np.linspace(0,0.7,100)
v = odeint(fun,Co,P)
x = P


#Datos
To = 330 #K
k1 = 31.1
kc1 = 3.03
E = 65.7*1000 #J/mol
DHr = -6900 #J/molA
FAo = 0.9*163*1000 #mol/h
Fi = 0.1*163*1000 #mol/h
CpA = 141 #J/mol
Cpi = 161 #J/mol
CAo = 9.3 #mol/m^3
R = 8.31 
Qs = FAo*CpA+Fi*Cpi
T= To +(-FAo*DHr*x)/Qs
kc = kc1*np.exp((DHr/R)*(1/333 - 1/T))
k = k1*np.exp((E/R)*(1/360 - 1/T))
xe = kc/(1+kc)
CA = CAo*(1-x)
CB = CAo*x
rA = k*CA-(k/kc)*CB;
FAo_2 = 0.9*163 #Kmol/h
GL = FAo_2/rA

#Gráficos
plt.figure(1)
plt.plot(x,GL,'g')
plt.title("Gráfica de Levenspiel")
plt.xlabel("Conversión (x)")
plt.ylabel("FAo/-rA (m^3)")
plt.show()

plt.figure(2)
plt.plot(v,x)
plt.title("Perfil de Conversión")
plt.xlabel("v (m^3)")
plt.ylabel("Conversión (x)")
plt.show()

plt.figure(3)
plt.plot(v,T,"r")
plt.title("Perfil de Temperaturas")
plt.xlabel("Volumen (m^3)")
plt.ylabel("Temperatura (K)")
plt.show()

plt.figure(4)
plt.plot(v,rA,"y")
plt.title("Perfil de velocidades de reacción")
plt.xlabel("V (m^3)")
plt.ylabel("-rA (Kmol/m^3*h)")
plt.show()





















