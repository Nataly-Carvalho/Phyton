'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Entrada
linha 1: dimensão de uma matriz quadrada de valores inteiros
Próximas n linhas: cada uma das linhas da matriz

Saída
A matriz impressa na forma de uma lista por linha, que é como está sendo representada em nosso programa...
'''
TamMatriz = int(input())
Matriz = [ ]

for i in range(TamMatriz):
 CMatriz = [int(i) for i in input().split ()]
 Matriz.append(CMatriz)

for i in range(TamMatriz):
 print(Matriz[i])