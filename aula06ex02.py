A = int(input("Digite a altura do retângulo: "))
L = int(input("Digite a largura do retângulo: "))
if A > 0 and L > 0:
    for i in range(1, A + 1):
        for j in range(1, L + 1):
            if i == 1 or i == A or j == 1 or j == L:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
else:
    print("A altura e a largura devem ser maiores que zero.")