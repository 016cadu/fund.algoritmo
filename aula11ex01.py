def procuraChave(dicionario, valor):
    chaves = []

    for chave, valor_dict in dicionario.items():
        if valor_dict == valor:
            chaves.append(chave)

    return chaves

d = {
    'alpha': 1,
    'bravo': 2,
    'charlie': 1,
    'delta': 3,
    'echo': 1
}

print("Dicionário:")
print(d)

print("\nProcurando chaves com valor 1:")
print(procuraChave(d, 1))

print("\nProcurando chaves com valor 3:")
print(procuraChave(d, 3))

print("\nProcurando chaves com valor 4:")
print(procuraChave(d, 4))