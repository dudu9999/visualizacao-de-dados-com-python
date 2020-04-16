import matplotlib.pyplot as plt
import random
entrada = open('bacteria.fasta').read()
saida = open('bacteria.html','w')

entrada2 = open('human.fasta').read()
saida2 = open('human.html','w')

cont = {}
cont2 = {}

for a in     ['A' ,'T' ,'C' ,'G']:
	for b in ['A', 'T' ,'C' ,'G']:
		cont[a+b] = 0

for c in     ['A' ,'T' ,'C' ,'G']:
	for d in ['A', 'T' ,'C' ,'G']:
		cont2[c+d] = 0


entrada = entrada.replace("\n","")
#entrada2 = entrada.replace("\n","")

for e in range(len(entrada)-1):
	cont[entrada[e]+entrada[e+1]] += 1
print('cont ',cont)
print('len ',len(entrada))

for f in range(len(entrada2)-1):
	cont2[entrada2[f]+entrada2[f+1]] += 1
print('cont2',cont2)
print('len',len(entrada2))

### HTML ####
i = 1
saida.write("<p>DNA - Humano</p>")

for l in cont2:
	transparence = cont2[l]/max(cont2.values())
	saida.write("<div style='width:100px; border:1px solid #111; color:#fff; height: 100px; float:left; background-color: rgba(0,0,0,"+str(transparence)+"')>"+l+"</div>")
	#if i % 4 == 0:
	#	saida.write("<div style='clear:both'></div>")
	i+=1

saida.write("<br><br><br><br><br><br>")
saida.write("<p>DNA - bacteria</p>")

i = 1
for g in cont:
	transparence = cont[g]/max(cont.values())
	saida.write("<div style='width:100px; border:1px solid #111; color:#fff; height: 100px; float:left; background-color: rgba(0,0,0,"+str(transparence)+"')>"+g+"</div>")
	#if i % 4 == 0:
	#	saida.write("<div style='clear:both'></div>")
	i+=1




saida.close()

'''
i = 1
for l in cont2:
	transparence = cont2[l]/max(cont2.values())
	saida2.write("<br><br><div style='width:100px; border:1px solid #111; color:#fff; height: 100px; float:left; background-color: rgba(0,0,0,"+str(transparence)+"')>"+l+"</div>")
	if i % 4 == 0:
		saida2.write("<div style='clear:both'></div>")
	i+=1
		
saida2.close()

'''