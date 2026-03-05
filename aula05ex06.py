somatoria = 0

while True:
    entrada = int(input("Digite um número ou 0 para sair: "))
    if entrada == 0:
        break
    somatoria += entrada
    qtde = entrada
print("números digitados: ", qtde)
print("somatória: ", somatoria)
print("média: ", somatoria / qtde)

# -- arrumar em casa --