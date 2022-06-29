'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Você sabe o que amor da sua vida curte muito Vinicius de Moraes.
Por isso, você fez um programa que criptografa mensagens para você enviar de modo que pessoas que estejam por
 perto tenham dificuldade em ler cada uma delas...
Para isso, você estudou e viu que as três letras mais frequentes na língua portuguesa são a, e e o.
 Assim, seu programa transforma uma frase lida em uma nova frase com essas letras trocadas.
Para dificultar mais um pouquinho a leitura das mensagens, você usa apenas letra minúsculas.

Entrada
Uma string contendo letras e sinais de pontuação
'''

texto= input()
texto = texto.lower()
palavra = texto.replace('a', '@')
novo = palavra.replace('o', '*')
print (novo)