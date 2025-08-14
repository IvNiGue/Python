import math
import matplotlib.pyplot as plt

print("/////////////////////////////")
print("       Metodo de Euler     ")
print("//////////////////////////// \n")

def f_xy(x, y):
    return -2*pow(x,3) + 12*pow(x,2) - 20*x + (17/2)

#Variables de incializacion

xin = 0
yin = 1
xfin = 5
lasx = [xin]
lasy = [yin]
dx = 0.5

n = int(((xfin-xin)/dx)+1)

print(f"Cantidad de puntos: {n-1}")

#Euler

for i in range(1,n):
    xnueva = xin + dx*i
    lasx.append(xnueva)
    ynueva = lasy[i-1] + f_xy(lasx[i-1],lasy[i-1])*dx
    lasy.append(ynueva)


#Punto medio
lasx1 = [xin]
lasy1 = [yin]

for i in range(1,n):
    xnueva = xin + dx*i
    lasx1.append(xnueva)

    #Correccion
    xaux = lasx1[i-1] + dx/2
    k1 = f_xy(lasx1[i-1],lasy1[i-1])
    yaux = lasy1[i-1] + (k1*dx/2)

    #Prediccion

    k2 = f_xy(xaux,yaux)
    
    ynueva = lasy1[i-1] + k2*dx
    lasy1.append(ynueva)

#Huen
lasx2 = [xin]
lasy2 = [yin]

for i in range(1,n):
    xnueva = xin + dx*i
    lasx2.append(xnueva)

    #Correccion
    xaux = lasx2[i-1] + dx
    k1 = f_xy(lasx2[i-1],lasy2[i-1])
    yaux = lasy2[i-1] + (k1*dx)

    #Prediccion

    k2 = f_xy(xaux,yaux)
    
    ynueva = lasy2[i-1] + ((k2+k1)*dx)/2
    lasy2.append(ynueva)


#Grafica
plt.plot(lasx, lasy, linestyle='-', color='g', label='F_E(x)')
plt.plot(lasx1, lasy1, linestyle='-', color='r', label='F_pm(x)')
plt.plot(lasx2, lasy2, linestyle='-', color='b', label='F_Huen(x)')
plt.grid(axis='both', color='black', linestyle='-')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.title('Grafica de una funcion')
plt.legend()
plt.show()



    

    
