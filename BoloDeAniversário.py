'''
Nome: Nataly Carvalho da Silva
  Curso: Meninas programadoras
   Turma: 9

Q.Para cada sopro dado, uma mensagem correspondente como indicado nos exemplos
Ao final, a mensagem de parabéns pelo aniversário

EX:
Entrada     Saida
5

fuuuuuuu    bom sopro!
fuuuuuuu    bom sopro!
fuuuuuuu    bom sopro!
fuuuuuuu    bom sopro!
fuuuuuuu    bom sopro!

Parabéns para pelo seu aniversário de 5 anos!
'''

aniversario = int(input())
bolo = aniversario
while bolo != 0:
    velas = str(input())

    if velas == "fuuuuuuu":
        bolo = bolo - 1
        print("bom sopro!")

    elif velas == "fuuu":
        print("um pouco mais de força no sopro!")

    else:
        print("precisa de muito mais força no sopro!")

print("Parabéns para pelo seu aniversário de ", aniversario, "anos!")