'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Primeira linha: numero de notas
Proximas linhas: o valor de cada nota
'''

quantidade = int(input())
contador =0

while quantidade !=0:
  nota = int(input())
  contador = contador + nota
  quantidade = quantidade - 1

print(contador)
