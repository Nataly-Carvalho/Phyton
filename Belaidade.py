'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras 
   Turma: Modulo 1 A

Q.Seu programa deve ler a idade de uma aluna e dar uma mensagem apropriada

- a partir de 60, é a melhor idade

- entre 18 e 59, é a maioridade

- antes dos 18, é a tenra idade
'''
idade = int(input())

if idade >= 60:
  print('melhor idade')
elif idade < 18:
  print('tenra idade')
else:
  print('maioridade')