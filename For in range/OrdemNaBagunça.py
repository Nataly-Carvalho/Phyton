'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Entrada
Uma linha com as notas das alunas da turma

Saída
Lista de notas em ordem decrescente
'''
nota = [float(i) for i in input().split()]

nota.sort()
nota.reverse()
print(nota)