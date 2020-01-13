# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:13:02 2019

@author: Invitado
"""

#Importando sistema de ecuaciones diferenciales 
import ODE_system as f

#Importando librerías para resolución del problema
import numpy as np #Creación y manejo de arrays
import matplotlib.pyplot as plt #Generación de gráficos
from scipy.interpolate import InterpolatedUnivariateSpline #Ajuste de datos
from scipy.integrate import odeint #Resolutor de sistema de ecuaciones
                                   #diferenciales

#Data del problema
#Tiempo (min)
t = np.array([0.0001, 0.1580, 0.4158, 0.6735, 0.7312, 0.8589, 0.9466, 1.1134,
              1.2802, 1.4168, 1.5533, 1.7197, 1.8861, 2.0329, 2.1796, 2.3168,
              2.4540, 2.6509, 2.8478, 2.9949, 3.1419, 3.2897, 3.4374, 3.6045,
              3.7717, 3.9293, 4.0868, 4.2740, 4.4611, 4.5893, 4.7175, 4.8852,
              5.0528, 5.2203, 5.3877, 5.5159, 5.6440, 5.8114, 5.9788, 6.1464,
              6.3141, 6.4916, 6.6691, 6.8171, 6.9650, 7.1326, 7.3002, 7.4579,
              7.6156, 7.7832, 7.9507, 8.1084, 8.2662, 8.4239, 8.5816]) 

#concentración del trazador
c = np.array([0.0127, 0.0190, 0.0250, 0.0379, 0.0407, 0.5537, 0.7691, 0.9878,
              1.3268, 1.4126, 1.4926, 1.5126, 1.6427, 1.6961, 1.7729, 1.8164,
              1.8599, 1.9167, 1.9963, 2.1326, 2.1574, 2.1823, 2.2506, 2.3188,
              2.3561, 2.3934, 2.4245, 2.4313, 2.4373, 2.4434, 2.4495, 2.4556,
              2.4562, 2.4811, 2.4874, 2.4937, 2.5310, 2.5319, 2.5320, 2.5322,
              2.5385, 2.5441, 2.5448, 2.5562, 2.5574, 2.5683, 2.5699, 2.5700,
              2.5701, 2.5380, 2.5501, 2.5622, 2.5689, 2.5751, 2.5800])                  

#Parte A: Calcular el tiempo medio de residencia 

F = (c-c[0])/(c[c.size-1]-c[0]) #Curva F(t)
E = np.diff(F)/np.diff(t) #Curva E(t)
t1 = t[1:t.size] #reduciendo las dimensiones la data t para poder  
                #graficar y ajustar
vector = t1*E

TM = np.trapz(vector,t1) #Tiempo medio de residencia
print("Parte A: ")
print("El tiempo medio de residencia es : %.2f" %TM, "minutos")


#Parte B: Graficar la curva E(t)

plt.figure(1)
plt.plot(t1,E,'r*')
plt.xlabel('tiempo (min)')
plt.ylabel('E(t)')
plt.title('Curva E(t)')
plt.show()

#Parte C: Determinar el perfil de distribución de productos

#Haciendo ajuste polinómico (picewise polinomial function) para el modelo
#segregacional
f_interp = InterpolatedUnivariateSpline(t1,E, k=3)
y_inter = f_interp(t1)

#Grafica el ajuste
plt.figure(2)
plt.plot(t1,E,'x',mew=3)
plt.plot(t1,y_inter)
plt.title("Ajuste")

#Datos
caudal = 10 #m3/min
R = 8.314 #Pa/K/mol
To = 373 #K 
Po = 1*101325 #Pa

V = TM*caudal

Co = Po/(R*To)


#Resolución del ODE system
Con_in =np.array([Co*V, 0, 0]) #Condiciones iniciales
p = np.linspace(t1[0],t1[t1.size-1],t1.size) #Intervalo de integración
fn = lambda Y,t1,TM,f_interp:f.fun(Y,t1,TM,f_interp) #Llamada al ODE system
sol = odeint(fn,Con_in,p,args=(TM,f_interp)) #resuelve el sistema

#Flujos mol/min
FA = sol[0:sol.size-1,0] #Flujos de A molA/min
FB = sol[0:sol.size-1,1] #Flujos de B molB/min
FC = sol[0:sol.size-1,2] #Flujos de C molC/min

#Concentraciones
FT = FA+FB+FC
CA = Co*(FA/FT)
CB = Co*(FB/FT)
CC = Co*(FC/FT)

#Grafica el perfil de flujos a lo largo del reactor
plt.figure(3)
plt.plot(p,FA,label='A')
plt.plot(p,FB,label ='B')
plt.plot(p,FC,label='C')
plt.xlabel('Tiempo(min)')
plt.ylabel('concentración(mol/L)')
plt.title('Distribución de productos')
plt.legend()
plt.show()

#Grafica el perfil de concentración a lo largo del reactor
plt.figure(4)
plt.plot(p,CA,label='A')
plt.plot(p,CB,label ='B')
plt.plot(p,CC,label='C')
plt.xlabel('Tiempo(min)')
plt.ylabel('concentración(mol/L)')
plt.title('Distribución de productos')
plt.legend()
plt.show()


#Parte D: Determine les concentraciones medias

vector_A = CA*E
vector_B = CB*E
vector_C = CC*E
CA_M = np.trapz(vector_A,t1)
CB_M = np.trapz(vector_B,t1)
CC_M = np.trapz(vector_C,t1)
print("Parte D: ")
print("La concentración media de A es : %.2f " %CA_M,"mol/l")
print("La concentración media de B es : %.2f " %CB_M,"mol/l")
print("La concentración media de C es : %.2f " %CC_M,"mol/l")



       