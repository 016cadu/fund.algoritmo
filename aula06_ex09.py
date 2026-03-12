genero = int(input("Digite o gênero (1 para masculino, 2 para feminino): "))
peso = float(input("Digite o peso em kg: "))
if genero == 1:
    if peso >= 60:
        print("Você pode doar sangue.")
    else:
        print("Você não pode doar sangue.")
if genero == 2:
    if peso >= 50:
        print("Você pode doar sangue.")
    else:
        print("Você não pode doar sangue.")