'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Qual problema você tem que resolver?

Dados dois pontos no espaço 2D, qual a distância entre eles?

O que seu programa recebe como entrada?

São dadas duas linhas, cada um com as coordenadas de um ponto no plano 2D

O que seu programa deve informar?

A distância entre os dois pontos no plano 2D, apresentada com uma casa decimal

'''
from math import sqrt

c=[int(i) for i in input().split()]
d=[int(i) for i in input().split()]

cx = c[0]
cy = c[1]
dx = d[0]
dy = d[1]

result = (dx - cx) ** 2 + (dy - cy) ** 2

N = sqrt(result)
print('{:.1f}'.format(N))