'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Seu programa recebe os pontos de um set, um por linha: o valor 1 indica ponto do time 1, e o valor dois indica ponto do time 2.

Seu programa deve aceitar pontos até que o set acabe, e imprimir o placar final do set.

Dica: projete sua solução limitando o set a um numero de pontos bem menor que 25, por exemplo 5, mas mantendo a diferença mínima de dois pontos para vitória no set... depois de pronto, é só mudar a pontuação para 25  >;-)
'''

placar = 0
placar2 = 0

time = 0
while True:
    time = int(input())

    if (time == 1):
        placar = placar + 1
    elif (time == 2):
        placar2 = placar2 + 1

    if (placar > 24 or placar2 > 24) and ((placar - placar2 >= 2) or (placar2 - placar >= 2)):
        print(placar, 'x', placar2)
        break
