# -*- coding: utf-8 -*-
"""
Created on Sun May 12 21:39:41 2019

@author: Invitado
"""
#Importando sistema de ecuaciones diferenciales 
import fun as f

#Importando librerías para resolución del problema
import numpy as np #Creación y manejo de arrays
import matplotlib.pyplot as plt #Generación de gráficos
from scipy.interpolate import InterpolatedUnivariateSpline #Ajuste de datos
from scipy.integrate import odeint #Resolutor de sistema de ecuaciones
                                   #diferenciales

#Data del problema
#Tiempo
t = np.array([3.057e-5, 0.1224, 0.2446, 0.3669, 0.4962, 0.6020,
              0.7311, 0.8448, 0.9512,1.1038, 1.2178, 1.3323, 1.4619, 
              1.5840, 1.7291, 1.8285, 1.9585, 2.0883,2.1876, 2.3173, 2.4473, 
              2.5849, 2.6996, 2.8295, 2.9518, 3.0817, 3.2040, 3.3262]) 

#concentración del trazador
c = np.array([0.0014, 0.0049, 0.0098, 0.0147, 0.1156, 0.2981, 0.4422, 0.5863,
              0.6872, 0.7209, 0.8266, 0.8459, 0.8988, 0.9277, 0.9518, 0.9471,
              0.9424, 0.9617, 0.9666, 0.9955, 0.9908, 0.9861, 0.9814, 0.9815,
              0.9864, 0.9961, 0.9962, 1.0000]) 

F = (c-c[0])/(c[c.size-1]-c[0]) #Curva F(t)

#Grafica F(t)
plt.figure(1)
plt.plot(t,F,"r.")
plt.xlabel("Tiempo (min)")
plt.ylabel("F(t)")


E = np.diff(F)/np.diff(t) #Curva E(t)

t1 = t[1:t.size] #reduciendo las dimensiones la data t para poder  
                 #graficar y ajustar
#Grafica E(t)
plt.figure(2)
plt.plot(t1,E,"b*")
plt.xlabel("Tiempo (min)")
plt.ylabel("E(t)")

#Calculando el tiempo medio de residencia
vector = t1*E

TM = np.trapz(vector,t1) #Tiempo medio de residencia
print("El tiempo medio de residencia es : %.2f" %TM, "minutos")

#Haciendo ajuste polinómico (picewise polinomial function) para el modelo
#segregacional
f_interp = InterpolatedUnivariateSpline(t1,E,k=3)
y_inter = f_interp(t1)

#Grafica el ajuste
plt.figure(3)
plt.plot(t1,E,'x',mew=3)
plt.plot(t1,y_inter)
plt.title("Ajuste")

#Datos del problema
R = 0.082 #atm*l/K*mol
T = 400 + 273 #K
P = 2 #atm
caudal = 25*1000 #l/min
V = TM*caudal #l
CTo = P/(R*T) #mol/l

#Resolución del ODE system
Co =np.array([(CTo*V), 0, 0, 0]) #Condiciones iniciales
p = np.linspace(t1[0],t1[t1.size-1],100) #Intervalo de integración
fn = lambda Y,t1,TM,f_interp:f.fun(Y,t1,TM,f_interp) #Llamada al ODE system
sol = odeint(fn,Co,p,args=(TM,f_interp)) #resuelve el sistema

#Flujos mol/min
A = sol[0:sol.size-1,0] #Flujos de A molA/min
B = sol[0:sol.size-1,1] #Flujos de B molB/min
C = sol[0:sol.size-1,2] #Flujos de C molC/min
D = sol[0:sol.size-1,3] #Flujos de D molD/min

#Grafica el perfil de los flujos a lo largo del reactor
plt.figure(4)
plt.plot(p,A,label='A')
plt.plot(p,B,label ='B')
plt.plot(p,C,label='C')
plt.plot(p,D,label='D')
plt.xlabel('Tiempo(min)')
plt.ylabel('Fujo(mol/min)')
plt.title('Perfil de flujos')
plt.legend()

#Calcula las concentraciones (mol/l)
concentraciones = sol/V
A = concentraciones[0:sol.size-1,0] #Concentración de A (molA/l)
B = concentraciones[0:sol.size-1,1] #Concentración de B (molB/l)
C = concentraciones[0:sol.size-1,2] #Concentración de C (molC/l)
D = concentraciones[0:sol.size-1,3] #Concentración de D (molD/l)

#Grafica el perfil de concentraciones a lo largo del reactor
plt.figure(5)
plt.plot(p,A,label='A')
plt.plot(p,B,label ='B')
plt.plot(p,C,label='C')
plt.plot(p,D,label='D')
plt.xlabel('Tiempo(min)')
plt.ylabel('concentración(mol/L)')
plt.title('Perfil de concentraciones')
plt.legend()























