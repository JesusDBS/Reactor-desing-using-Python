# -*- coding: utf-8 -*-
"""
Created on Thu May  2 07:57:56 2019

@author: Invitado
"""
import math

def fun(F,T):
    
    V = 10 #dm^3
    Vo = 1000 #dm^3/min
    
    FA = F[0]
    FB = F[1]
    Ca0 = 0.3 #mol/dm^3
    Ca = FA/Vo
    Cb = FB/Vo
    k1 = 3.3*math.exp((9900/1.987)*((1/300)-(1/T)))
    k2 = 4.52*math.exp((27000/1.987)*((1/500)-(1/T)))
    FA0 = Ca0*Vo 

    ra = -k1*Ca
    rb = k1*Ca-(k2*Cb)
    
    sal1 = FA0 - FA + (ra*V)
    sal2 = -FB + (rb*V)
    
    return(sal1,sal2)