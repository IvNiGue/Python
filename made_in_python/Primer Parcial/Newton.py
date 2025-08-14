import math
import matplotlib.pyplot as plt

print("//////////////////////")
print(" Metodo de Newton ")
print("////////////////////// \n")

dx = 0.001      #diferencial para la derivada

n = 0.045
Q = 50
B = 35
S = math.tan((0.1*math.pi)/180)

#funcion
def fun_x(x):
    return ((1/n)*(pow(B*x,5/3)/pow(B+(2*x),2/3))*pow(S,1/2)) - Q

#derivada de f(x)
def dev_fx(x):
    return (fun_x(x+dx)-fun_x(x))/dx

#funcion g(x)
def fung_x(x):
    return x - (fun_x(x)/dev_fx(x))

#derivada de g(x)
def dev_gx(x):
    return (fung_x(x+dx)-fung_x(x))/dx

#varibles fundamentales

bandera = 0     #Varible fundamental para parar los ciclos del algoritmo

intmax = 10     #Variables para el ciclo de eleccion del intervalo de la raiz
c_int = 0

error = 10      #Varible guardada para la determinacion del error en base a la varible del error propuesto
ep = pow(10, -8)

imax = 200      #Varibles que ayudan en el ahorro de tiempo de la busqueda de la raiz
iteraciones = 0


#ciclo para determinar el valor inicial

a = 0
while bandera == 0 and c_int < intmax:
    a = float(input("Ingrese el valor inicial: "))
    fx = fun_x(a) #math.exp(-a) - a
    dg = fung_x(a)
    ddg = dev_gx(a) #((math.exp(-a+dx))-math.exp(-a))/dx

    if abs(ddg) < 1:
        bandera = 1

    if fx == 0:
        error = 0
        bandera = 1

    c_int += 1

#calculo de la raiz

xant = a
xact = 0
while bandera == 1 and error > ep and iteraciones < imax:
    xact = fung_x(xant)
    fx = fun_x(xact)
    ddg = dev_gx(xact) #((math.exp(-xact+dx))-math.exp(-xact))/dx

    if fx == 0:
        error = 0

    if abs(ddg) >= 1:
        bandera = 0
        print("Fallo por convergencia \n")

    if error != 0:
        error = abs((xact-xant)/xact)

    xant = xact
    iteraciones += 1

#presentar datos
fx = fun_x(xact)

print()
print(f"La raiz encontrada es: {xact}")
print(f"Evaluacion: {fx}")
print(f"Error final: {error}")
print(f"La cantidad de iteraciones fue: {iteraciones}")
