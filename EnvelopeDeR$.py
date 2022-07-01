'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.As crianças da creche perto da sua casa estão aprendendo a contar. A professora pediu para você fazer um programa que ajude as crianças a contarem dinheiro em notas. Você topou na hora, é claro!
Cada criança recebe um envelope com um conjunto de notas de brinquedo. Ninguém sabe quantas notas tem em um envelope, mas sabe-se que:
- o envelope contém entre 0 e 5 notas
- a criança tira uma nota de cada vez
- a última nota tem valor 0, que indica que acabaram-se as notas do envelope
A partir do valor das notas contidas em um envelope, seu programa deve informar quanto de dinheiro tinha no envelope.

'''

notas = int(input())
soma =  0
while (notas != 0):
  soma += notas
  notas = int(input())

print(soma)