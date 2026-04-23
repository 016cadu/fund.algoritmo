par = open("pares.txt", "w")
impar = open("impares.txt", "w")

for num in range(1000):
    if num % 2 == 0:
        par.write(f"{num}\n")
    else:
        impar.write(f"{num}\n")

par.close()
impar.close()