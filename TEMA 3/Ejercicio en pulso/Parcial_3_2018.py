# -*- coding: utf-8 -*-
"""
Created on Sun May 19 17:35:42 2019

@author: Invitado
"""

#Importando librerías para resolución del problema
import ODE_system as f
import numpy as np #Creación y manejo de arrays
import matplotlib.pyplot as plt #Generación de gráficos
from scipy.interpolate import InterpolatedUnivariateSpline #Ajuste de datos
from scipy.integrate import odeint #Resolutor de sistema de ecuaciones
                                   #diferenciales

#Data del problema
#Tiempo (min)
t = np.array([0, 10, 20, 30, 45, 65, 85, 100, 118, 135, 150, 160, 175, 180, 195,
              202, 208, 216, 225, 235, 250, 259, 268, 278, 288, 300, 313, 323,
              337, 348, 356, 370, 391, 415, 430])

#Concentración del trazador
c = np.array([0.1520, 0.1510, 0.1520, 0.1510, 0.1510, 0.1510, 0.1520, 0.1510,
              0.1510, 0.1500, 0.2250, 2.2267, 3.4856, 4.8000, 7.6300, 13.7600, 
              14.0123,9.0800, 7.8753, 4.8900, 4.0221, 2.6600, 1.6600, 1.0300,
              0.7500, 0.5100, 0.4100, 0.3300, 0.2900, 0.2500, 0.2200, 0.2000,
              0.1900, 0.1800, 0.1530])

E = c/np.trapz(c,t) #Curva E(t)
plt.figure(1)
plt.plot(t,E,'r.',mew=3)


#Determinar curva F(t)
F=np.zeros(len(c))
for i in range (t.size):
    F[i] = np.trapz(E[1:i],t[1:i])

plt.figure(2)
plt.plot(t,F,"b*")

TM = np.trapz(t*E,t)
print("El tiempo medio de residencia es : %.2f" %TM, "minutos")

#Haciendo ajuste polinómico (picewise polinomial function) para el modelo
#segregacional
f_interp = InterpolatedUnivariateSpline(t,E,k=3)
y_inter = f_interp(t)

#Grafica el ajuste
plt.figure(3)
plt.plot(t,E,'x',mew=3)
plt.plot(t,y_inter)
plt.title("Ajuste")

#Datos
caudal = 8.5 #m3/min
k1 = 4.23 #min^-1
k2 = 3.67 #min^-1
R = 8.314 #Pa m3/Kmol
To = (25 + 273) #K   
Po = 101325 #Pa 

V = TM*caudal

C_in = Po/(R*To)


#Resolución del ODE system
Co =np.array([(C_in*V), 0, 0]) #Condiciones iniciales
p = np.linspace(t[0],t[t.size-1],100) #Intervalo de integración
fn = lambda Y,t,TM,f_interp:f.fun(Y,t,TM,f_interp) #Llamada al ODE system
sol = odeint(fn,Co,p,args=(TM,f_interp)) #resuelve el sistema

#Flujos mol/min
A = sol[0:sol.size-1,0] #Flujos de A molA/min
B = sol[0:sol.size-1,1] #Flujos de B molB/min
C = sol[0:sol.size-1,2] #Flujos de C molC/min

#Grafica el perfil de los flujos a lo largo del reactor
plt.figure(4)
plt.plot(p,A,label='A')
plt.plot(p,B,label ='B')
plt.plot(p,C,label='C')
plt.xlabel('Tiempo(min)')
plt.ylabel('Fujo(mol/min)')
plt.title('Distribución de productos')
plt.legend()




