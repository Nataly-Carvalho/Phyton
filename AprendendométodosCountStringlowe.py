'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Seu programa deve ler um padrão e uma linha, e verificar quantas vezes o padrão ocorre na linha de duas maneiras: com a mesma capitalização ou não
'''
pesquisa = str(input())
msg = str(input())

print(msg.count(pesquisa))

pesquisa = pesquisa.upper()
msg = msg.upper()

print(msg.count(pesquisa))