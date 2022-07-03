'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Entrada

Linha 1: valor inteiro para dimensão
Próximas n linhas: valores inteiros para cada linha da matrix

Saída
True ou False: se a matriz é nula ou não, respectivamente
'''
TamRange = int(input())
cont=0

for i in range(TamRange):
  lista=[int(i) for i in input().split()]
  for g in range(len(lista)):
   if lista [g]!=0:
     cont += 1

if cont == 0:
  print("True")
else:
  print("False")