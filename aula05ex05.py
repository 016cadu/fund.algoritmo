nro = int(input("Digite um número entre 0 e 10: "))
while nro < 0 or nro > 10:
    print("Número inválido. Digite um número entre 0 e 10.")
    nro = int(input("Digite um número entre 0 e 10: "))
print("Número aceito")