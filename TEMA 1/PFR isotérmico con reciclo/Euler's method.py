# -*- coding: utf-8 -*-
"""
Created on Sun May  5 00:30:17 2019

@author: Invitado
"""

#setup time discretization
n = 1000 #numbr of steps
x = numpy.linspace(x0,xf,n)
dx = x[1] - x[0]

#allocate storage space and initial conditions
sol = numpy.zeros(n)
sol[0] = 0 #initial x

for i in range(1,n):
    sol[i] = sol[i-1] + dx*dvdx(sol[i-1],x[i-1])
    
print("El volumen del reactor es",sol[n-1],"Litros")




#setup time discretization
    n = 100 #numbr of steps
    x = np.linspace(x0,xf,n)
    dx = x[1] - x[0]

#allocate storage space and initial conditions
    sol = np.zeros(n)
    sol[0] = 0 #initial x

    for i in range(1,n):
        sol[i] = sol[i-1] + dx*Ec_D(sol[i-1],x[i-1],R)
    return sol[n-1]

semilla = 1
R_O = fmin(ROP,semilla)

n = 100 #numbr of steps
x0 = (R_O/(R_O+1))*xf
x = np.linspace(x0,xf,n)
dx = x[1] - x[0]
sol = np.zeros(n)
sol[0] = 0 #initial x
for i in range(1,n):
    sol[i] = sol[i-1] + dx*Ec_D(sol[i-1],x[i-1],R_O)
    
    
print("El volumen óptimo del reactor es ",sol[n-1],"Litros")

