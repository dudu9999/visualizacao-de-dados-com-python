import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]
z  = [200, 25, 400, 330, 100]

x2 = [2,4,6,8,10]
y2 = [5,1,3,7,4]

titulo = 'Scatterplot: grafico de dispersão'
eixox = 'Eixo X'
eixoY = 'Eixo Y'

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoY)



plt.plot(x1, y1, color='k', linestyle='-.')
plt.scatter(x1, y1, label = 'Usuarios 1', color='k', marker='o', s=z)

plt.legend()
#plt.show()
#plt.savefig('aula7.png')
#plt.savefig('aula7.pdf')
#plt.savefig('aula7_300.png', dpi=300)
plt.savefig('aula7_1200DPI.png', dpi=1200)
'''
cores: color=''
'b' azul blue
'g' verde green
'r' vermelho red
'c' azul fraco cyan
'm' rosa magenta
'y' amarelo yellow
'k' preto black
'w' banco white

macadores  marker='h'
'.' ponto
',' pixel
'o' ciculo
'v' triangulo para baixo
'^' triangulo para cima
'<' triangulo para esquerda
'>' triangulo para direita
'1' tri para baixo
'2' tri para cima
'3' tri para esquerda
'4' tri para direita
's' quadrado
'p' pentagono
'*' estrela
'h' hexagono 1
'H' hexagono 2
'+' mais
'x' xis 
'D' diamante
'd' thin diamante
'|' linha vertical 
'-' linha horizontal

Tipos de linha (linest='-')
'-' linha solida
'--' linha solida separada = dashed
'-.' linha solida e ponto
':' linha pontilhada

'''

#['#800000', '#B0E0E6', '#D8BFD8', '#E6E6FA', '#A52A2A', '#FF1493', '#FFE4E1', '#FFFF00', '#FF0000', '#F5F5DC', '#F0F8FF', '#FFA500', '#FF8C00', '#FF6347', '#DC143C', '#DDA0DD',
#'#7CFC00', '#DAA520', '#F4A460', '#BC8F8F', '#00FFFF', '#008080', '#4682B4', '#6A5ACD', '#FF00FF']