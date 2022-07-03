'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Qual problema você tem que resolver?

 Use o comando condicional if-elif-else para responder se uma passageira paga ou não paga, a partir de sua idade.

Entrada
Um valor inteiro

Saída
Responda 'Gratis' ou 'Gratis no colo' ou 'Pago' 
'''
Idade= int(input())

if Idade >= 60:
  print("Gratis")
elif Idade <= 6:
  print("Gratis no colo")
else:
  print("Pago")