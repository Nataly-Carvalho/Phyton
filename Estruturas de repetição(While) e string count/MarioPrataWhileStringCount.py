'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Dada uma palavra, seu programa deve ler um conjunto de linhas e verificar quantas vezes aquela palavra se repete no texto
'''

pesquisar = str(input())
soma =  0
while True:
  texto = str(input())
  pesquisar_texto = texto.count(pesquisar)
  soma += pesquisar_texto

  if texto == ".":
    break


print(soma)