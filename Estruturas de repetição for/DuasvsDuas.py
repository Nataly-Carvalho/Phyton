'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Entrada
Quatro linhas informando os valores das cartas na seguinte ordem:
carta da 1a menina da 1a dupla
carta da 1a menina da 2a dupla
carta da 2a menina da 1a dupla
carta da 2a menina da 2a dupla
Saída
Valor da carta vencedora. Em caso de empate, imprima empate

'''

menina1_1 = int(input())
menina1_2 = int(input())
menina2_1 = int(input())
menina2_2= int(input())

if (menina1_1 >menina2_1):
  maior1= menina1_1
else:
  maior1=menina2_1

if(menina1_2>menina2_2):
  maior2= menina1_2
else:
  maior2=menina2_2

if(maior1==maior2):
 print('empate')
elif(maior2>maior1):
  print(maior2)
else:
 print(maior1)
