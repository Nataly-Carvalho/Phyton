'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Para passar o tempo, você programou um jogo no qual você "escolhe" um valor e depois deixa uma colega chutar valores até acertar o valor que você "escolheu". As regras são
primeiro você digita o número-alvo a ser encontrado
depois você deixa sua amiga chutar um valor até que ela acerte
Portanto, depois do número-alvo escolhido inicialmente, seu programa deve iniciar um bloco de repetição que só termina quanto o valor que sua amiga chutou for igual ao que você escolheu inicialmente.
Ou seja, para cada chute
se for igual ao número-alvo, o seu programa imprime 'igual' e seu programa termina
se o número-alvo for maior, seu programa imprime 'maior' e espera um novo palpite
se o número-alvo for for menor, seu programa imprime 'menor' e espera um novo palpite
Note que não há penalidades caso os palpites sejam "chutes" que ignoram o que deveria se aprender com as respostas anteriores
'''


numero = int(input())
chute = int()

while chute != numero:
  chute = int(input())
  if chute > numero:
    print("menor")
  elif chute < numero:
      print("maior")
  else:
      print("igual")
