# -*- coding: utf-8 -*-
"""
Created on Sun May  5 00:40:31 2019

@author: Invitado
"""
#Definición de la ecuación diferencial 
def dvdx(V,x,R):

    CA0 = 1.5 #Concentración inicial molA/l
    FA0 = 100 #Flujo inicial de molA/min
    k = 0.15 #constante cinética específica de primer orden min^-1
    CA = CA0*(1-x)
    rA = -k*CA   
    
    salida = (-FA0*(R+1)/rA)
    
    return salida
