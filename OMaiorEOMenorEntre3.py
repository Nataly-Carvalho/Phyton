'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Para resolver este problema, você deve usar no máximo nove comparações simples
Não serão consideradas soluções que utilizem comandos de repetição (while ou for-in)
Não serão consideradas soluções que utilizem funções prontas para identificação dos valores maiores/menores
Essa verificação é manual! mesmo com 'accepted' no beecrowd, sua solução só vai ser aceita pela professora se atender o requisito especificado!
'''
n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 > n2 and n1 > n3:
    print("Maior:", n1)
elif n2 > n1 and n2 > n3:
    print("Maior:", n2)
else:
    print("Maior:", n3)

if n1 < n2 and n1 < n3:
    print("Menor:", n1)
elif n2 < n1 and n2 < n3:
    print("Menor:", n2)
else:
    print("Menor:", n3)
