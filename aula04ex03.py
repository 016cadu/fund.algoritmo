A = int(input("Escreva o primeiro número: "))
B = int(input("Escreva o segundo número: "))
C = int(input("Escreva o terceiro número: "))
if A > B > C:
    print("A ordem decrescente é: %d, %d, %d" % (A, B, C))
elif A > C > B:
    print("A ordem decrescente é: %d, %d, %d" % (A, C, B))
elif B > A > C:
    print("A ordem decrescente é: %d, %d, %d" % (B, A, C))
elif B > C > A:
    print("A ordem decrescente é: %d, %d, %d" % (B, C, A))
elif C > A > B:
    print("A ordem decrescente é: %d, %d, %d" % (C, A, B))
elif C > B > A:
    print("A ordem decrescente é: %d, %d, %d" % (C, B, A))