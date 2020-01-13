# -*- coding: utf-8 -*-
"""
Created on Sun May 26 17:50:31 2019

@author: Invitado
"""

import numpy as np
import matplotlib.pyplot as plt
import funciones as f
from scipy.integrate import odeint

Co = np.array([55,0,0,350,60])
t = np.linspace(0,180,100)
fun = lambda y,t: f.fun(y,t)
sol = odeint(fun,Co,t)

#Gráficos
plt.figure(1)
plt.plot(t,sol[0:sol.size-1,0],"y",label="CA")
plt.plot(t,sol[0:sol.size-1,1],"b",label="CB")
plt.plot(t,sol[0:sol.size-1,2],"g",label="CC")
plt.xlabel("Tiempo (min)")
plt.ylabel("Conecentraciones (mol/L)")
plt.title("Perfil de Concentraciones")
plt.legend()
plt.show()

plt.figure(2)
plt.plot(t,sol[0:sol.size-1,3],"r")
plt.title("Perfil de temperaturas")
plt.xlabel("Tiempo (min)")
plt.ylabel("Temperatura (K)")

Cmax = np.amax(sol[0:sol.size-1,2])
x = np.where(Cmax==sol[0:sol.size-1,2])
t = t[x]
print("El tiempo necesario para alcanzar la máxima concentración de C es %2.f minutos" %t)