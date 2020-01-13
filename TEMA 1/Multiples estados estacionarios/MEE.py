# -*- coding: utf-8 -*-
"""
Created on Thu May  2 07:54:32 2019

@author: Invitado
"""
#Ejemplo visto en clases
#Parte A perfiles de concentración

import numpy
import fun as nl
import scipy.optimize
import matplotlib.pyplot as plt
 

Vo = 1000
Cao = 0.3

T = numpy.linspace(273,723,100)

semilla = numpy.array([0.9,0.1])
flujo = numpy.zeros((2,100),dtype=numpy.float64)

for i in range(len(T)):
     
    f = lambda F : nl.fun(F,T[i])
    flujo[:,i]= scipy.optimize.broyden1(f,semilla)
    
FA = flujo[0,:]
FB = flujo[1,:]

CA = FA/Vo
CB = FB/Vo
CC = Cao-CA-CB

plt.plot(T,CA,label='Concentración de A')
plt.plot(T,CB,label='Concentración de B')
plt.plot(T,CC,label='Concentración de C')
plt.xlabel('Temperaturas (K)')
plt.ylabel('Concentraciones (mol/dm^3)')
plt.title('Perfil de concentraciones')
plt.legend()
plt.show()


#Balance de energía

Dha = -55000
Dhb = -71500
UA = 40000
Ta = (57+273)
To = 283
Fao = Cao*Vo
Cp = 200
V = 10

k1 = 3.3*numpy.exp((9900/1.987)*((1/300)-(1/T)))
k2 = 4.52*numpy.exp((27000/1.987)*((1/500)-(1/T)))

ra1 = -k1*CA;
rb2 = -k2*CB;

Qg = ((ra1*Dha)+ (rb2*Dhb))*V;
Qr = UA*(T-Ta)+ (Fao*Cp*(T-To));

plt.plot(T,Qg,label='Calor generado')
plt.plot(T,Qr,label='Calor retirado')
plt.title('Balance de energía')
plt.xlabel('Temperaturas (K)')
plt.ylabel('Calor (J/mol)')
plt.legend()
plt.show()
























