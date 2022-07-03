'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Problema
Você deve ler um conjunto de valores correspondentes a pagamentos
(valores negativos) e recebimentos (valores positivos) e informar o balanço final.
Entrada
Primeira linha: inteiro positivo com o número de movimentações financeiras a serem processadas
Próximas linhas: um total de linhas que correspondente ao número de movimentações financeiras
(cada valor pode ter até duas casas decimais)
Saída
Valor do balanço final, informado com duas casas decimais

'''

tamanho_l = int(input())
plus = 0

for i in range(tamanho_l):
    V = float(input())
    plus = plus + V

print('{:.2f}'.format(plus))
