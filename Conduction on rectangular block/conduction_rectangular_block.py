# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 23:41:38 2021

@author: Y.Emre
"""
import numpy as np
import matplotlib.pyplot as plt

##### Parameters #####

Lx = 1.5            # cm
Ly = 0.5            # cm
a = 0.25            # cm
k = 0.011           # W/cm.K
h = 0.001           # W/cm^2.K
N = 100             # number of pieces
dx = 2*Lx/N         # distance between nodes in x-direction
dy = Ly/N           # distance between nodes in y-direction
T_infinity = 300    # K

A = np.zeros(((N+1)**2,(N+1)**2))   # initialize Coefficient Matrix A
b = np.zeros(((N+1)**2,1))          # initialize Output Matrix b
C = np.zeros(((N+1),(N+1)))         # initialize Temperature Distribution Matrix C

##### Boundary Conditions #####

# internal nodes #

for j in range(1,N):
    for i in range(1,N):
        n=(j)*(N+1)+i
        A[n,n]=-2*(1/dx**2+1/dy**2)
        A[n,n+1]=1/dx**2
        A[n,n-1]=1/dx**2
        A[n,n+(N+1)]=1/dy**2
        A[n,n-(N+1)]=1/dy**2
        b[n,0]=0
        
# edge nodes @ x=0 #

for j in range(1,N):
    i=0
    n=(j)*(N+1)+i
    A[n,n]=-2*(1/dx**2+1/dy**2)
    A[n,n+1]=2/dx**2
    A[n,n+(N+1)]=1/dy**2
    A[n,n-(N+1)]=1/dy**2
    b[n,0]=0
    
# edge nodes @ x=2*Lx #

for j in range(1,N):
    i=N
    n=(j)*(N+1)+i
    A[n,n]=-2*(1/dx**2+1/dy**2)
    A[n,n-1]=2/dx**2
    A[n,n+(N+1)]=1/dy**2
    A[n,n-(N+1)]=1/dy**2
    b[n,0]=0
    

# edge nodes @ y=0 #

for i in range(1,N):
    j=0
    n=(j)*(N+1)+i
    A[n,n]=-2*(1/dx**2+1/dy**2)
    A[n,n+1]=1/dx**2
    A[n,n-1]=1/dx**2
    A[n,n+(N+1)]=2/dy**2
    if (i*dx)>=Lx-a and (i*dx)<=Lx+a:
        q_s=-0.2
    else:
        q_s=0
        
    b[n,0]=2*q_s/(k*dy)
    
# edge nodes @ y=Ly #

for i in range(1,N):
    j=N
    n=(j)*(N+1)+i
    A[n,n]=-2*(1/dx**2+1/dy**2+h/(k*dy))
    A[n,n+1]=1/dx**2
    A[n,n-1]=1/dx**2
    A[n,n-(N+1)]=2/dy**2
    b[n,0]=((-2*h)/(k*dy))*T_infinity
    
# Bottom-Left Corner Node #

j=0
i=0

n=(j)*(N+1)+i
A[n,n]=-2*(1/dx**2+1/dy**2)
A[n,n+1]=2/dx**2
A[n,n+(N+1)]=2/dy**2
b[n,0]=0

# Bottom-Right Corner Node #

j=0
i=N

n=(j)*(N+1)+i
A[n,n]=-2*(1/dx**2+1/dy**2)
A[n,n-1]=2/dx**2
A[n,n+(N+1)]=2/dy**2
b[n,0]=0

# Upper-Left Corner Node #

j=N
i=0

n=(j)*(N+1)+i
A[n,n]=-2*(1/dx**2+1/dy**2+h/(k*dy))
A[n,n+1]=2/dx**2
A[n,n-(N+1)]=2/dy**2
b[n,0]=(-2*h/(k*dy))*T_infinity

# Upper-Right Corner Node #

j=N
i=N

n=(j)*(N+1)+i
A[n,n]=-2*(1/dx**2+1/dy**2+h/(k*dy))
A[n,n-1]=2/dx**2
A[n,n-(N+1)]=2/dy**2
b[n,0]=(-2*h/(k*dy))*T_infinity

##### Solution #####

# A x T = b

T=np.linalg.solve(A,b)      # linear system solver 

# Placing temperature values from T to C Matrix

for j in range (0,N+1):
    for i in range (0,N+1):
        C[j,i] = T[i+j*(N+1)]

# Contour Plot

X=np.linspace(0,2*Lx,N+1)
Y=np.linspace(0,Ly,N+1)

contour=plt.contour(X,Y,C)
plt.clabel(contour, colors = 'k', fmt = '%2.1f', fontsize=12)
plt.title("Temperature Distribution")
plt.xlabel('X-direction')
plt.ylabel('Y-direction')
plt.colorbar(contour)
plt.grid()
plt.show()



    



        
    