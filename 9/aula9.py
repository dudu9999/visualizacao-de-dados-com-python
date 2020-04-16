import matplotlib.pyplot as plt
import random
dados = open('populacao-brasileira.csv').readlines()

vetor = []

for i in range(10):
	numero_aleatorio = random.randint(0,5)
	vetor.append(numero_aleatorio)


#plt.bar(vetor, color='#e4e4e4')
plt.boxplot(vetor)
#plt.boxplot(vetor, color='k', linestyle='--')
plt.title('Boxplot')
#plt.xlabel('Ano')
#plt.ylabel('Populacao x100.000.000')
plt.show()
#plt.savefig('populacao-brasileira.png',dpi=300)