import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

titulo = 'Grafico de barras'
eixox = 'Eixo X'
eixoY = 'Eixo Y'

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoY)

plt.bar(x, y)
plt.show()
