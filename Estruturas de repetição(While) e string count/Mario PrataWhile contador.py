'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Neste problema, os exemplos são de autoria de Mario Prata

Seu programa deve ler entradas do usuário continuamente e imprimir o total de linhas lidas.

deve parar apenas quando quando receber o caractere ponto final '.'

ao final, deve imprimir o número de linhas lidas, incluindo a que sinaliza a parada do programa
'''

i = 0
while True:
    texto = str(input())
    i = i + 1
    if texto == '.':
        break

print(i)