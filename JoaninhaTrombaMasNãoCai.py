'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Quando a Joaninha é ligada, o programa captura da bateria um valor inteiro entre 0 e 100, correspondente à porcentagem de carga disponível

A Joaninha só funciona com carga mínima maior que 5%

Antes de cada movimento, o programa obtém informações de dois sensores. O primeiro sensor informa B de bateu ou L se a área livre à frente. O segundo sensor informa A se tem um Abismo, ou P se há Piso para avançar

Para controlar a Joaninha, seu programa emite os comandos virar, em caso de necessidade, ou avançar, sempre que possível. Quando não há bateria disponível para trabalhar, seu programa avisa que é hora de recarregar.  Junto com cada comando, seu sempre programa informa o quanto de bateria resta na Joaninha.

Cada movimento de avançar consome 1% de bateria. Cada movimento de virar consome  5% de bateria.

Entrada

Primeira linha: um valor inteiro entre 0 e 100

A seguir, um número indeterminado de pares de linhas com uma letra cada

- o primeiro valor do par contém B ou L

- o segundo valor do par contém A ou P

Saída

Enquanto houver carga mínima na bateria suficiente, a joaninha avança ou vira, de acordo com os dados obtidos dos sensores

Ao final, o programa informa a porcentagem de bateria restante. 
'''

carga = int(input())

while  carga > 5:
  p1 = str(input())
  s2 = str(input())

  if p1 == "B" or s2 =="A":
    carga = carga -5
    print("virar:", carga )

  elif p1 == "L" or s2 == "P":
    carga = carga -1
    print ("avançar:", carga)


print("recarregar:", carga)