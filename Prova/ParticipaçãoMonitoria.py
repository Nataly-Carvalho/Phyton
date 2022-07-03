'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Primeira linha: número de alunas
Para cada aluna, 5 linhas
nome da aluna
numero de minutos de monitoria na semana 1
numero de minutos de monitoria na semana 2
numero de minutos de monitoria na semana 3
numero de minutos de monitoria na semana 4
'''
QuatidadeAluna = int(input())

for i in range(QuatidadeAluna):
  nome = str(input())
  semana1= int(input())
  semana2= int(input())
  semana3= int(input())
  semana4= int(input())
  if semana1 >=120 and semana2>=120 and semana3>=120 and semana4>=120:
   print(nome,"tem monitorias OK! :-)")
  else:
   print(nome,"não tem monitorias suficientes :-(")