somatoria = 0
while True:
    numero = int(input("Digite um número (ou 0 para sair): "))
    if numero == 0:
        break
    else:
        somatoria = somatoria + numero
print("A soma dos números é:", somatoria)