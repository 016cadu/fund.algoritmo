T = [11, 7, 2, 4]

menor = 999999

for elemento in T:
    if elemento < menor:
        menor = elemento

print("O menor elemento da lista é:", menor)