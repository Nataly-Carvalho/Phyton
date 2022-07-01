'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: Modulo 1 A

Q.Seu programa deve ler três linhas, cada uma com uma parte do nome, e imprimir o nome completo.

Caso não exista nome do meio, e entrada correspondente é indicada com um ponto final.
'''

nome = input()
nome_do_meio = input()
sobrenome = input ()

if (nome_do_meio == "."):
 print(nome, sobrenome)
else:
 print(nome, nome_do_meio,sobrenome)