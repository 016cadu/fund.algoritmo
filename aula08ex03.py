lista = []
maior = -99999999
indiceM = -1

for i in range(10):
    nro = float(input("Digite um número: "))
    lista.append(nro)

for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]
        indiceM = i

print(maior)
print(indiceM)