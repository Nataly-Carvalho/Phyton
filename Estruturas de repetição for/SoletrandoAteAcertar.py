'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Entrada
- Primeira linha: uma palavra simples (sem espaços)
- Linhas seguintes: uma letra por linha, terminadas com ponto.
- Se as letras corresponderem corretamente à palavra da primeira linha, seu programa imprime 8-) e termina
- Caso contrário,  seu programa imprime 8-| e lê um novo conjunto de linhas terminado por ponto.
Saída
- uma sequencia de zero ou mais linhas com 8-|
- ultima linha: 8-)

'''
linha = input()
soletra = input()
while True:

    letra = str(input())

    if letra == "." and (soletra == linha):
        print('8-)')
        break

    elif letra == ".":
        soletra = ""
        print('8-|')
    else:
        soletra += letra
