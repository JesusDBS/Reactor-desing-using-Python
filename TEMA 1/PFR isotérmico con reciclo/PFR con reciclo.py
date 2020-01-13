# -*- coding: utf-8 -*-
"""
Created on Sat May  4 07:03:16 2019

@author: Invitado
"""

#A ---> Productos

#Qué volumen de reactor se requiere para lograr una conversión
#del 0.9?

#Importar liberías
import numpy #crear y manipular arrays
import dvdx as f #función que contiene la ecuación diferencial
from scipy.integrate import odeint #Resolutor de ODE


#Datos del problema
R = 1 #Relación de reciclo
xf = 0.9 #Conversión final del reactor
x0 = (R/(R+1))*xf #Conversión inicial
n = 100
P = numpy.linspace(x0,xf,n) #Intervalo de integración
xi = 0 #condición inicial

fun = lambda V,x,R=1 : f.dvdx(V,x,R) #Llamada de ecuación diferencial

sol = odeint(fun,xi,P)[-1] #Solución de la ecuación diferencial
print("El volumen del reactor es: %.2f" %sol,"Litros") #Imprime el resultado

#Cuál sería el volumen requerido para un PFR convencional?

n = 100
P = numpy.linspace(0,xf,n)
xi = 0

fun = lambda V,x,R=0 : f.dvdx(V,x,R)

sol = odeint(fun,xi,P)[-1]
print("El volumen del reactor convencional es: %.2f" %sol,"Litros")





