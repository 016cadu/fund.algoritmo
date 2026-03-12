def calc (n1, n2, n3):
    res = n1**0.5 + n2**0.5 + n3**0.5 + (n1 + n2) / 2 + (n2 + n3) / 2 + (n1 + n3) / 2
    return res

print("Resultado: = ", calc(7, 8, 9))
print("Resultado: = ", calc(4, 9, 16))
print("Resultado: = ", calc(4, 10, 12))