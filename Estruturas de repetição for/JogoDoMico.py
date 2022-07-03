'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Esta versão do jogo admite muitos jogadores.
  Joga-se com dois baralhos completos (52 cartas cada) e um coringa (mico), de modo que cada carta,
   menos o coringa, tem um par. As cartas são distribuídas entre todos os
   jogadores: o número de cartas de cada jogador varia de acordo com o numero de
   jogadores e nem todos os jogadores têm o mesmo número de cartas na mão.
  O objetivo de um jogador é se livrar de todas as suas cartas.
  Para isso um jogador, estando de posse de um par de cartas iguais, livra-se do par colocando-o na mesa.
 Ganha quem se livrar de todas as cartas primeiro.
'''


nome= input()
cartas = input()
caracter = 'mico'
if  caracter in cartas:
  print(nome, 'mico!')
else:
  print(nome, 'ok')