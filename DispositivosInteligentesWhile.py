'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Seu programa deve ler um conjunto de valores do sensor e informar se o portador do dispositivo está sedentário ou ativo, assumindo que:

o usuário está ativo quando o número de leituras que indicam movimento é maior que o de leituras que indicam paradonote que o dispositivo já começa parado
'''

p = 1
m = 0
while True:
    a = str(input())

    if a == "f":
        break

    elif a == "m":
        m = m + 1

    else:
        p = p + 1

if p > m or p == m:
    print("sedentário")
else:
    print("ativo")