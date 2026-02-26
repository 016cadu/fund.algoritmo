pre = float(input("Digite o preço do produto: "))
cod = int(input("Digite o código de origem: "))
if cod == 1:
    ori="Sul"
elif cod == 2:
    ori="Norte"
elif cod == 3:
    ori="Leste"
elif cod == 4:
    ori="Oeste"
elif cod == 5 or cod== 6:
    ori="Nordeste"
elif cod == 7 or cod == 8 or cod == 9:
    ori="Sudeste"
elif cod >= 10 and cod <= 20:
    ori="Centro-Oeste"
elif cod >= 25 and cod <= 30:
    ori="Noroeste"
else:
    ori="importado"

print("Preço.....: %2f" % pre)
print("Origem....: %s" % ori)