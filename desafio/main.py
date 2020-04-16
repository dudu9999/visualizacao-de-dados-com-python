import json
import matplotlib.pyplot as plt

z = []
y = []
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
a = ['#800000', '#B0E0E6', '#D8BFD8', '#E6E6FA', '#A52A2A', '#FF1493', '#FFE4E1', '#FFFF00', '#FF0000', '#F5F5DC', '#F0F8FF', '#FFA500', '#FF8C00', '#FF6347', '#DC143C', '#DDA0DD','#7CFC00', '#DAA520', '#F4A460', '#BC8F8F', '#00FFFF', '#008080', '#4682B4', '#6A5ACD', '#FF00FF']

try:
        arquivo_json = json.load(open('cursos/page_1.json', encoding='utf-8'))
        dados = arquivo_json['results']        
        for x in range(len(dados)):
                if x < 25:
                        z.append( str(dados[x]['title'] ))
                if x > 25:
                        break
except:
        print('Deu erro 1')


try:
        arquivo_json = json.load(open('cursos/page_1.json', encoding='utf-8'))
        dados = arquivo_json['results']
        for v in range(len(dados)):
                linha = dados[v]['price'].split("R$")
                if v < 25:
                        y.append(float(linha[1]))
                if v > 25:
                        break        
except:
        print('Deu erro 2')
e = len(y)
soma = 0
for d  in range(len(y)):
        soma = soma + y[d]
        
media = soma/e

plt.scatter(6,579.99 ,label = 'Maior valor R$ 579,99', color='#FF1493', marker='o', s=200)
plt.scatter(23,39.99 ,label = 'Menor valor R$ 39.99', color='#4682B4', marker='o', s=200)
plt.bar(b,y, color=a)
plt.plot(b,y, color='k', linestyle='--')
plt.title('valor dos cursos da udemy')
plt.xlabel('Numero de cursos no grafico ( 25 )')
plt.ylabel('valor  0 x 600')
plt.legend()
#plt.show()
plt.savefig('Desafio.png', dpi=300)

