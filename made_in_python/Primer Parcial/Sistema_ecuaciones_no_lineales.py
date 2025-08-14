import math
import matplotlib.pyplot as plt

print("/////////////////////////////")
print(" Resolucion de un sitema 2x2 ")
print("//////////////////////////// \n")
dt = 0.001

def z_xy(x, y):
    return (3 - (10*math.pi) - (3*pow(math.e, -x*y)))/60

def fz(x,y,z):
    return pow(math.e, -x*y) + (20*z) + (((10*math.pi) - 3)/3)


#funciones
def u_xy(x, y):
    return (3*x) - (math.cos(y*z_xy(x,y))) - 0.5

def v_xy(x, y):
    return (4*pow(x,2)) - (625*pow(y,2)) + (2*y) -1

#derivadas parciales
def dux(x, y):
    return (u_xy(x+dt,y) - u_xy(x,y))/dt

def duy(x, y):
    return (u_xy(x,y+dt) - u_xy(x,y))/dt

def dvx(x, y):
    return (v_xy(x+dt,y) - v_xy(x,y))/dt

def dvy(x, y):
    return (v_xy(x,y+dt) - v_xy(x,y))/dt

#jacobiano
def jac(x, y):
    return (dux(x,y)*dvy(x,y)) - (duy(x,y)*dvx(x,y))

#variables fundamentales
intentos = 0
intmax = 10

error = 10
ep = pow(10,-6)

bandera = 0

ite = 0
itmax = 100

#valores iniciales
while bandera == 0 and error > ep and intentos < intmax:
    xin = float(input("Ingrese la x inicial: "))
    yin = float(input("Ingrese la y inicial: "))

    if jac(xin,yin) != 0:
        bandera = 1

    if u_xy(xin,yin) == 0 and v_xy(xin,yin) == 0:
        error = 0

    intentos += 1

#calculo de las raices
print()
xant = xin
yant = yin

while bandera == 1 and error > ep and ite < itmax:
    xact = xant - ((u_xy(xant, yant)*dvy(xant, yant)) - (v_xy(xant, yant)*duy(xant, yant)))/jac(xant,yant)
    yact = yant - ((v_xy(xant, yant)*dux(xant, yant)) - (u_xy(xant, yant)*dvx(xant, yant)))/jac(xant,yant)

    if u_xy(xact,yact) == 0 and v_xy(xact,yact) == 0:
        error = 0

    if error != 0:
        errorx = abs((xact-xant)/xact)
        errory = abs((yact-yant)/yact)

        if errorx < ep and errory < ep:
            error = errorx

        else:
            if errorx > errory:
                error = errorx

            else:
                error = errory

    if jac(xact,yact) == 0:
        bandera = 0
        print("Falla por convergencia")

    xant = xact
    yant = yact
    ite += 1

zact = z_xy(xact,yact)
#presentar datos
print("Raices encontradas")
print(f"x: {xact}, y: {yact}, z:{zact}\n")

print("Evaluacion de las raices")
print(f"u: {u_xy(xact,yact)}, v: {v_xy(xact,yact)}\n")
print(f"z: {fz(xact,yact,zact)}\n")

print(f"Error final: {error}\n")
print(f"Iteraciones: {ite}")
        
