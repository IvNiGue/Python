import math
import matplotlib.pyplot as plt

print("/////////////////////////////")
print("     Integrales Numericas    ")
print("//////////////////////////// \n")

def f_x(x):
    return (math.sin((math.sin(3*x))+((pow(math.e,-2*pow(x,2)+1)))))*(math.cos(4*pow(x,2)-3))

#Valores fundamentales

a = 0
b = 3
n = 1000
dx = (b-a)/n

#Suma de Riemann
print("Suma de Riemann \n")

suma = 0

for i in range(n):
    suma = suma + f_x(a+(dx*i))

iriem = suma * dx

print(iriem)
print()

#Suma de Trapecios
print("Suma de Trapecios \n")

suma = 0

for i in range(1,n):
    suma = suma + f_x(a + dx*i)

itrap = (dx/2) * (f_x(a) + 2*suma + f_x(b))

print(itrap)
print()

#Simpson
print("Simpson \n")

sumpar = 0
sumimp = 0


for i in range(1,int((n/2)+1)):
    sumimp = sumimp + f_x(a + dx*(2*i-1))

for i in range(1,int(n/2)):
    sumpar = sumpar + f_x(a + dx*(2*i))

isimp = (dx/3) * (f_x(a) + 4*sumimp + 2*sumpar + f_x(b))

print(isimp)

