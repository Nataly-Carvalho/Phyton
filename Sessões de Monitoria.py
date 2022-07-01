'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Dado o tempo que uma aluna ficou em uma sessão, seu programa deve calcular o número de sessões de monitoria correspondentes, para que os monitores registrem na planilha semanal.

Lembrete: o tempo mínimo para considerar participação em uma sessão é de 30 minutos. 
'''
Horas = int(input())
Minutos = int(input())
Horas = Horas * 2

if Minutos >= 30:
    Minutos = 1
else:
    Minutos < 30
    Minutos = 0

print(Horas + Minutos)