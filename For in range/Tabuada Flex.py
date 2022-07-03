'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.As crianças acharam o máximo quando descobriam que você sabe programar! e você está super orgulhosa de pode ajudar, claro! Por conta disso, a professora pediu para você fazer um programa que gera tabuadas flexíveis! vamos lá?

Entrada
Três linhas:
primeira linha: numero do qual queremos calcular a tabuada (valor entre 1 e 99)

segunda linha: primeiro valor da tabuada a ser gerado (valor entre 1 e 999)

terceira linha: último valor da tabuada a ser gerado (valor entre 1 e 999)

Saída

Conforme exemplos
Dica

Lembra que a função range aceita mais que um argumento?
range(start, stop, step)
'''
Tabuada = int(input())
ini = int(input())
fim = int(input())
soma = 0

print("Tabuada do", Tabuada, "de", ini, "até", fim)
for i in range(ini, fim + 1):
    print(Tabuada, " x ", i, "=", Tabuada * i)
