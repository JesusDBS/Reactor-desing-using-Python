# -*- coding: utf-8 -*-
"""
Created on Sun May 26 09:35:04 2019

@author: Invitado
"""

from scipy.integrate import odeint
import numpy as np
import funciones as f
import matplotlib.pyplot as plt

#Resolver ODE system
fun = lambda y,v:f.fun(y,v)
Co = np.array([100,0,0,(150+273)])
P = np.linspace(0,1,100)
sol = odeint(fun,Co,P)

#Gráficas
plt.figure(1)
plt.plot(P,sol[0:sol.size-1,0],"y",label="FA")
plt.plot(P,sol[0:sol.size-1,1],"b",label="FB")
plt.plot(P,sol[0:sol.size-1,2],"g",label="FC")
plt.title("Perfil de flujos")
plt.xlabel("Volumen (dm^3)")
plt.ylabel("Flujos (mol/s)")
plt.legend()
plt.show()

plt.figure(2)
plt.plot(P,sol[0:sol.size-1,3],"r")
plt.title("Perfil de Temperaturas")
plt.xlabel("Volumen (dm^3)")
plt.ylabel("Temperaturas (K)")
plt.show()

