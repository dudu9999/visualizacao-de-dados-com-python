import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]

x2 = [2,4,6,8,10]
y2 = [5,1,3,7,4]

titulo = 'Scatterplot: grafico de dispersão'
eixox = 'Eixo X'
eixoY = 'Eixo Y'

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoY)



plt.scatter(x1, y1, label = 'Usuarios 1', color='r')
plt.plot(x1, y1,)

plt.legend()
plt.show()
