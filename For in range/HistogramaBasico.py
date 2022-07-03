'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Problema
Seu programa lê um conjunto de inteiros do teclado. Para cada valor inteiro positivo e par lido, seu programa imprime uma linha com um conjunto de asteriscos correspondente ao valor lido. Para cada número ímpar lido, ele imprime um número de pontos (i.e., o ponto final .) correspondente a esse valor.
Entrada
Uma sequencia de valores inteiros entre 0 e 20

Saída
O histograma conforme explicado acima e ilustrado nos exemplos.
'''
C=[int(i)for i in input().split()]

for end in range(len(C)):
  make= ""
  if C[end]%2== 0:
   for M in range(C[end]):
      make += '*'
   print(make)
  else:
   for M in range(C[end]):
    make += "."
   print(make)