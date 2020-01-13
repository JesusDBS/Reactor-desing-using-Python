# -*- coding: utf-8 -*-
"""
Created on Fri May 24 18:45:27 2019

@author: Invitado
"""

#Reacción exotérmica reversible y de primer orden en ambos sentidos
#A<--->R

import scipy.optimize 
import funciones as f

#Datos
V = 1000 #volumen del reactor en litros
x = 0.8 #converisón a T optima
R = 1.987 #Constante de los gases en %cal/mol/l
CAo = 2 #Concentración inicial de A mol/l
ro_Cp = 2000 #cal/l*C
DH = -20000 #cal/mol

#Parte A: Determinar la temperatura que maximiza el flujo de R
fun = lambda T,x=0.8: -f.rA(T,x)
semilla = 200 
T_O = scipy.optimize.fmin(fun,semilla,disp=0)
FR = f.rA(T_O,x)*V

print("Parte A: ")
print("La temperatura que maximiza el flujo de R es: %2.f K" %T_O)
print("El flujo de R es: %2.f mol/h" %FR)

#Parte B: Determinar la temperatura de alimentación al reactor
BE = lambda T: ro_Cp*(T_O-T)+CAo*x*DH #Balance de energía
Te = scipy.optimize.broyden1(BE,semilla)
print("Parte B: ")
print("La temperatura de entrada al reactor es: %2.f K" %Te)

#Parte C: Determinar volumen óptimo del reactor
x = 0.9
fun = lambda T,x=0.9: f.volumen(T,x)
T_O = scipy.optimize.fmin(fun,300,disp=False)
V_O = f.volumen(T_O,x)
print("Parte C: ")
print("El volumen óptimo del reactor es: %2.f litros" %V_O)

#Parte D: Temperatura de entrada al reactor
Te = scipy.optimize.broyden1(BE,semilla)
print("Parte D: ")
print("La temperatura de entrada al reactor es: %2.f K" %Te)















