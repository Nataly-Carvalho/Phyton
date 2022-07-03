'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Entrada
Zero ou mais frases, uma por linha. A última linha contém um ponto (.)

Saída
Cada uma das frases, uma por linha, como repetida por um loud parrot (ver exemplos)
'''
texto = str()
while texto != '.':
  texto = input()
  texto = texto.upper()
  if texto != '.':
   print(texto)
  else:
    print("BYE")