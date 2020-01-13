# -*- coding: utf-8 -*-
"""
Created on Sun May 26 10:39:12 2019

@author: Invitado
"""

import numpy as np
import funciones as f
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Parte A
R = 14.5
Co = np.array([0.00344,0,0,0,0,0,0,0.00344*R,800])
v = np.linspace (0,10,100)
fun = lambda y,v: f.fun(y,v)
sol = odeint(fun,Co,v)
F_Estireno = sol[-1,1]
F_Benceno  = sol[-1,3]
F_Tolueno  = sol[-1,5]
S = F_Estireno/(F_Benceno+F_Tolueno)
    
print("Resultados de la parte a: ")
print("- El flujo de estireno es %.7f Kmol/s" %F_Estireno)
print("- El flujo de benceno es %.4E Kmol/s" %F_Benceno)
print("- El flujo de tolueno es %.4E Kmol/s" %F_Tolueno)
print("- La selectividad respoecto al benceno y tolueno es %.2f" %S)

#Parte B
Co = np.array([0.00344,0,0,0,0,0,0,0.00344*R,930])
v = np.linspace (0,10,100)
fun = lambda y,v: f.fun(y,v)
sol = odeint(fun,Co,v)
F_Estireno = sol[-1,1]
F_Benceno  = sol[-1,3]
F_Tolueno  = sol[-1,5]
S = F_Estireno/(F_Benceno+F_Tolueno)
    
print("Resultados de la parte b: ")
print("- El flujo de estireno es %.7f Kmol/s" %F_Estireno)
print("- El flujo de benceno es %.4E Kmol/s" %F_Benceno)
print("- El flujo de tolueno es %.4E Kmol/s" %F_Tolueno)
print("- La selectividad respoecto al benceno y tolueno es %.2f" %S)

#Parte C
Co = np.array([0.00344,0,0,0,0,0,0,0.00344*R,1100])
v = np.linspace (0,10,100)
fun = lambda y,v: f.fun(y,v)
sol = odeint(fun,Co,v)
F_Estireno = sol[-1,1]
F_Benceno  = sol[-1,3]
F_Tolueno  = sol[-1,5]
S = F_Estireno/(F_Benceno+F_Tolueno)
    
print("Resultados de la parte c: ")
print("- El flujo de estireno es %.7f Kmol/s" %F_Estireno)
print("- El flujo de benceno es %.4E Kmol/s" %F_Benceno)
print("- El flujo de tolueno es %.4E Kmol/s" %F_Tolueno)
print("- La selectividad respoecto al benceno y tolueno es %.2f" %S)

#Parte D
Intervalo_T = np.linspace(800,1200,100)
F_Estireno = np.zeros(len(Intervalo_T))

for ii in range(Intervalo_T.size):
    R = 58
    Co = np.array([0.00344,0,0,0,0,0,0,0.00344*R,Intervalo_T[ii]])
    v = np.linspace (0,10,100)
    fun = lambda y,v: f.fun(y,v)
    sol = odeint(fun,Co,v)
    F_Estireno[ii] = sol[-1,1]
    

plt.figure(1)
plt.plot(Intervalo_T,F_Estireno,"r")
plt.title("Fujo de estireno Vs Temperatura")
plt.xlabel("Temperatura(K)")
plt.ylabel("Flujo de estireno(Kmol/s)")

F_E_maximo = np.amax(F_Estireno)
T_ideal = Intervalo_T[np.where(F_E_maximo==F_Estireno)]
print("Resultados de la parte d: ")
print("la temperatura ideal de entrada es %2.f K" %T_ideal)

#Parte E
Intervalo_R = np.linspace(10,70,100)

for ii in range(Intervalo_R.size):
    To = 900
    Co = np.array([0.00344,0,0,0,0,0,0,0.00344*Intervalo_R[ii],To])
    v = np.linspace(0,10,100)
    fun = lambda y,v: f.fun(y,v)
    sol = odeint(fun,Co,v)
    F_Estireno[ii]= sol[-1,1]
    
plt.figure(2)
plt.plot(Intervalo_R,F_Estireno,"b")
plt.title("Flujo de estireno vs Relación de vapor")
plt.xlabel("Relación de vapor/Flujo de estilbenceno")
plt.ylabel("Flujo de estireno (Kmol/s)")

Est_maxi = np.amax(F_Estireno)
R_Ideal = Intervalo_R[np.where(Est_maxi==F_Estireno)]
print("Resultados de la parte e: ")
print("La relación de vapor/etilbenceno idea el %.2f" %R_Ideal)














