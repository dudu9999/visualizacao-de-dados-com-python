## Creciemnto da populacao brasileira 1980-2016
## Dados do site DataSus

import matplotlib.pyplot as plt

dados = open('populacao-brasileira.csv').readlines()

x = []
y = []

for i in range(len(dados)):
	if i !=0:
		linha = dados[i].split(";")
		x.append(int(linha[0]))
		y.append(int(linha[1]))
#print(x)
#print(y)

plt.bar(x,y, color='#e4e4e4')
plt.plot(x,y, color='k', linestyle='--')
plt.title('Crescimento da populacao brasileira')
plt.xlabel('Ano')
plt.ylabel('Populacao x100.000.000')
plt.show()
#plt.savefig('populacao-brasileira.png',dpi=300)