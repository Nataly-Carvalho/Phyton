'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Entrada

Primeira linha: a palavra a caçar

Segunda linha: lista de uma ou mais palavras na qual a palavra que estamos caçando
 pode ou não se encontrar

Saída

Se a palavra caçada estiver na lista, qual a posição da palavra entre o conjunto de palavras.
 Neste caso, cada palavra conta uma posição.
  Ainda: lembre que Python sempre começa a contar do zero.

Se a palavra não estiver na lista, informe que ela está faltando, como no exemplo

Atenção

Note que, na apresentação dos exemplos, uma linha de palavras ocupar o espaço visual
de mais que uma linha na tela.. mas isso é só por causa do navegador..
mude tamanho da janela para ver a linha mudando de tamanho ;-)
'''
procura = str(input())
lista =[str(i) for i in input().split()]
cont=0

for i in range(len(lista)):
  if lista[i] == procura:
    posi = i
    cont +=1

if cont>0:
  print(procura,posi)
else:
  print("falta",procura)