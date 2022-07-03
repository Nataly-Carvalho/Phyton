'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: Modulo 1 A

Q.Para inúmeros fins, uma pessoa precisa apresentar um conjunto de documentos, por exemplo

- RG

- Título de Eleitor

- Certificado de Reservista ou equivalente, em caso do sexo masculino
'''

sexo = input()
if (sexo == "M"):
    CR = input()

RG = input()
TE = input()

if (sexo == "M") and (RG == "S") and (TE == "S") and (CR == "S"):
    print("Completa")

elif (sexo == "F") and (RG == "S") and (TE == "S"):
    print("Completa")
else:
    print("Incompleto")