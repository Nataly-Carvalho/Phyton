'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Vamos contar? desta vez, números divisíveis por 3

Entrada
Valor inteiro entre 0 e 100

Saída
Imprima, em uma única linha, o valor da soma de todos os múltiplos de 3 entre 0 e o valor dado, inclusive o valor dado.
'''
VesesRodar= int(input())
soma=0
for contador in range(VesesRodar +1):
  if contador % 3 == 0:
     soma = soma+ contador
print(soma)