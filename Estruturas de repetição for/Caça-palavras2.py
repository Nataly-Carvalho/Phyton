'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Entrada
Linha 1: uma ou mais palavras na qual a caça ocorre
Linha 2: uma ou mais palavras a serem buscadas
Saída
Uma linha para cada palavra caçada: a palavra e sua posição na linha.
Neste caso, cada caractere conta uma posição..
 e Python sempre começa a contar do zero.

'''
texto= str(input())
procura =[str(i) for i in input().split()]

for i in range(len(procura)):
  print(procura[i],texto.index(procura[i]))