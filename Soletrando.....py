'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Entrada

- Primeira linha: uma palavra simples  (sem espaços)

- Linhas seguintes: uma letra por linha. 

- Última linha: um ponto final.

Saída

True ou False

'''
linha = input()
soletra = input()
while True:

    soletra = str(input())
    if soletra == ".":
        break

    linha += soletra
if linha == soletra:
    print("True")
else:
    print("False")