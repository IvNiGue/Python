import math
import matplotlib.pyplot as plt

print("/////////////////////")
print(" Metodo de Proporciones ")
print("///////////////////// \n")

#funcion
def f_x(x):
    return pow(x,0.5) - math.cos(x)

#varibles fundamentales

bandera = 0     #Varible fundamental para parar los ciclos del algoritmo

intmax = 5      #Variables para el ciclo de eleccion del intervalo de la raiz
c_int = 0

error = 10      #Varible guardada para la determinacion del error en base a la varible del error propuesto
ep = pow(10, -10)

imax = 200      #Varibles que ayudan en el ahorro de tiempo de la busqueda de la raiz
iteraciones = 0

puntos = 600    #Varibles para la graficacion
inter_ga = 0
inter_gb = 5
dx = (inter_gb - inter_ga)/puntos
cor_x = []
cor_y = []

#graficacion y determinacion del intervalo

for i in range(puntos):
    nuevax = inter_ga + (dx*i)
    cor_x.append(nuevax)

    nuevay = f_x(nuevax)
    cor_y.append(nuevay)

plt.plot(cor_x, cor_y, linestyle='-', color='g', label='F(x)')
plt.grid(axis='both', color='black', linestyle='-')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.title('Grafica de una funcion')
plt.legend()


auxa = 0
auxb = 0
while c_int < intmax and bandera == 0:
    plt.show()
    a = float(input("Ingrese el intervalo a donde se encuentra su raiz: "))
    b = float(input("Ingrese el intervalo b donde se encuentra su raiz: "))
    print()

    fun_a = f_x(a)
    fun_b = f_x(b)

    
    if fun_a*fun_b < 0:
        bandera = 1

        auxa = a
        auxb = b


    elif fun_a*fun_b == 0:
        if fun_a == 0:
            print(f"La funcion evaluada en {a} es igual a {fun_a}, por lo que {a} es raiz \n")

        else:
            print(f"La funcion evaluada en {b} es igual a {fun_b}, por lo que {b} es raiz \n")

        bandera = 1
        error = 0

    else:
        bandera = 0

    c_int += 1

#calculo de la raiz

xant = auxa
raiz = 0
while bandera == 1 and error>ep and iteraciones<imax:
    
    fun_a = f_x(auxa)
    fun_b = f_x(auxb)
    xprop = auxa - ((fun_a*(auxb-auxa))/(fun_b-fun_a))
    xbis = (auxb+auxa)/2

    #fun_prop = f_x(xprop)
    #fun_bis = f_x(xbis)

    #cada 5 iteraciones el metodo cambia a biseccion
    xact = xprop
    if (iteraciones%5) == 0:
        xact=xbis

    #compara que valor se acerca mas a la raiz, y elige como candidiato al valor mas pequeño
    """if abs(fun_prop) < abs(fun_bis):
        xact = xprop

    else:
        xact = xbis"""

    fun_act = f_x(xact)
    

    if fun_a*fun_act < 0:
        auxb = xact

    elif fun_a*fun_act > 0:
        auxa = xact

    elif fun_a*fun_act == 0:
        error = 0

    if error != 0:
        error = abs((xact-xant)/xact)

    iteraciones += 1
    xant = xact

raiz = xact

#presentar reultados
print(f"La raiz encontrada es {raiz}")
print(f"La funcion evaluada con la raiz encontrada es {fun_act}")
print(f"El error de la raiz encontrada es: {error}, y la cantidad de interaciones que se realizo fue: {iteraciones}")
