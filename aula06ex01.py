qtde = int(input("Digite a quantidade de números a serem testados: "))
primos = 0

for i in range(1, qtde + 1):
    num = int(input(f"Digite o número {i}:  "))

    divisores = 0

    for j in range(1, num + 1):
        if num % j == 0:
            divisores += 1

    if divisores == 2:
        primos += 1
print(f"você digitou {primos} números primos de {i} números testados.")