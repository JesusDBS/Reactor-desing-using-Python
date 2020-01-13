# -*- coding: utf-8 -*-
"""
Created on Wed May  8 07:38:35 2019

@author: Invitado
"""

import funciones as f
from scipy.optimize import fmin

#Resuelve el sistema
semilla = 1
fun = lambda R: f.ROP(R)
R_O = fmin(fun,semilla,disp=False)[-1]
vol = fun(R_O)
print("El volumen óptimo del reactor es: %2.f Litros" %vol)