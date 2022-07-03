'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Vamos contar? desta vez, números pares a partir do 0 (zero)

Entrada
Valor inteiro entre 1 e 1000

Saída
Imprima apenas os valores pares a partir de 0 até o valor par anterior ao valor lido
'''
VesesRodar = int(input())
for contador in range(VesesRodar + 0):
    if contador % 2 == 0:
        print(contador)
        contador += 1
