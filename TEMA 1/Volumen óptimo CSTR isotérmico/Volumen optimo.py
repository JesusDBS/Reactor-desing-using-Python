# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:17:29 2019

@author: Invitado
"""
#Importar liberías para resolución del problema
import numpy as np #Crear y manipular arrays
import funciones as f #Importar funciones 
from scipy.optimize import fmin #Busca el mínimo de la función

#Buscando el mínimo de la función
fun = lambda x: f.VT(x) #Llamada a la función del volumen total
semilla = np.array([0.2,0.4,0.6]) #Semillas de converisón
conv = fmin(fun,semilla) #encuentra valores de conversión que optimizan (minimizan)
                         # el volumen total

V_1 = f.vol(conv[0],0)*1000 #Volumen óptimo para el primer reactor
V_2 = f.vol(conv[1],conv[0])*1000 #Volumen óptimo para el segundo reactor
V_3 = f.vol(conv[2],conv[1])*1000 #volumen óptimo para el tercer reactor
V_4 = f.vol(0.8,conv[2])*1000 #volumen óptimo para el cuarto reactor
V_T = f.VT(conv)*1000 #volumen óptimo total

#Imprime los resultados
print('El volumen del primer reactor es: %.2f' %V_1,'Litros')
print('El volumen del segundo reactor es: %.2f' %V_2,'Litros')
print('El volumen del tercer reactor es: %.2f' %V_3,'Litros')
print('El volumen del cuarto reactor es: %.2f' %V_4,'Litros')
print('El volumen total del sistema es: %.2f' %V_T,'Litros')

