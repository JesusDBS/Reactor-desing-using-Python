# -*- coding: utf-8 -*-
"""
Created on Sun May 12 21:52:14 2019

@author: Invitado
"""

import numpy as np #creación y manejo de arrays

#Define el sistema de ecuaciones diferenciales
def fun(Y,t1,TM,f_interp):
    na=Y[0] #Flujo de A
    nb=Y[1] #Flujo de B
    nc=Y[2] #Flujo de C
    nd=Y[3] #Flujo de D
    tm = TM #Tiempo medio de residencia
    k1 = 16 #Constante cinética específica de primer orden min^-1
    k2 = 1 #Constante cinética específica de primer orden min^-1
    k3 = 0.5 #Constante cinética específica de primer orden min^-1
    R = 0.082 #atm*l/K*mol
    T = 400 + 273 #K
    P = 2; #atm
    caudal = 25*1000 #l/min
    V = tm*caudal #l
    CTo = P/(R*T) #mol/l
    nt = na + nb + nc + nd
    Ca = CTo*(na/nt)
    Cb = CTo*(nb/nt)
    R1 = k1*Ca
    R2 = k2*Cb
    R3 = k3*Cb
    ra = -R1
    rb = R1 - R2 - R3
    rc = R2
    rd = R3
    dadt=ra*V*f_interp(t1)
    dbdt=rb*V*f_interp(t1)
    dcdt=rc*V*f_interp(t1)
    dddt=rd*V*f_interp(t1)
    salida = np.array([dadt,dbdt,dcdt,dddt])
    return salida
