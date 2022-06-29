'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Uma espiã que se encontra em perigo enviou uma mensagem codificada para seu grupo.
 Ela enviou porque sabe que você escreveu um programa que consegue identificar se uma mensagem de texto contém,
escondida nela, o sinal universal de pedido de ajuda SOS  usando o código Morse.
O ---
S ...
'''

SOS = '...---...'
texto = input()
if SOS in texto:
  print ("S")
else:
  print("N")