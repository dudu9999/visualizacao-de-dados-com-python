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



plt.plot(x1, y1, color='m', linestyle=':')
plt.scatter(x1, y1, label = 'Usuarios 1', color='r', marker='1', s=500)

plt.legend()
plt.show()

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