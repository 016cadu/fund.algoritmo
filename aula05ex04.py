x=0
maior = -999999999999
while x<6:
    nro = int(input("Digite um número inteiro: "))
    if nro > maior:
        maior = nro
    x =  x + 1
print("O maior número digitado foi:", maior)