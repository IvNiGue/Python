import math
import matplotlib.pyplot as plt
import random

print("####################")
print("Método de Montecarlo")
print("#################### \n")

#funcion
def f_x(x):
    p1 = (pow(1-pow(math.cos(x),3),0.5))/(pow(math.e,pow(x,2)+math.sin(x)))
    p2 = (math.sin((5*x)+2-pow(x,2)))/(pow(x,3)+2)
    return p1 + p2 +1

# pow(x,2) * math.log(x) // (2*x*math.cos(2*x))-pow(x-2,2) // pow(1 + pow(math.cos(x),3),0.5)

#Varaibles fundamentales
inter_a = 0
inter_b = 3
n_tir = 1000
puntos = 500
cor_x = []
cor_y = []
dx = (inter_b - inter_a)/puntos
hmax1 = 0
xmax1 = 0
hmax2 = 0
xmax2 = 0

#Generacion de puntos de la funcion
for i in range(puntos):
    nuevax = inter_a + (dx*i)
    cor_x.append(nuevax)

    nuevay = f_x(nuevax)
    cor_y.append(nuevay)

    if nuevay > hmax1:
        hmax1 = nuevay
        xmax1 = nuevax

    else:
        hmax1 = hmax1

    if nuevay < hmax2:
        hmax2 = nuevay
        xmax2 = nuevax

    else:
        hmax2 = hmax2

#area
amax = (inter_b - inter_a)*(hmax1+hmax2)
print(hmax1)
print(hmax2)

#Tiradas
contador = 0

for i in range(n_tir):
    xaux = random.uniform(inter_a, inter_b) #x generada de manera random(intervalo)
    yaux = random.uniform(hmax2, hmax1) #generada de random(0 , hmax)

    aux = f_x(xaux)
    #print(aux)
    #print(yaux)

    if abs(yaux) < abs(aux):
        contador += 1

#Calculo del area y del error
prob = contador/n_tir
a_int = prob*amax

error = abs((3.25202-a_int)/3.25202)

print(contador)
print(f"El resultado de la integral es: {a_int}")
print(f"Error de calculo: {error*100}%")

#Graficar
plt.plot(cor_x, cor_y, linestyle='-', color='y', label='F(x)')
plt.plot(xmax1, hmax1, marker='o', color='r', label='Punto Maximo')
plt.plot(xmax2, hmax2, marker='o', color='b', label='Punto Minimo')
plt.grid(axis='both', color='black', linestyle='-')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.title('Grafica de una funcion')
plt.legend()

plt.show()
