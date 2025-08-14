import math
import matplotlib.pyplot as plt

#plt.figure(figsize=()) --- tamaño de la figura

x = [2016, 2017, 2018, 2019, 2020, 2021]
y = [45, 47, 47, 47, 49, 50]

plt.plot(x, y, marker='o', linestyle='--', color='y', label='Argentina')
plt.xlabel('Años')
plt.ylabel('Poblacon (M)')
plt.title('Años vs Poblacion')
plt.legend()

#plt.yticks([rango]) --- tamaños de ejes
#plt.savefig('nombre del grafico')

plt.show()
