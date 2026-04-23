par = open("pares.txt", "r")
m4 = open("m4.txt", "w")

for linha in par.readlines():
    if int(linha) %4 == 0:
        m4.write("%d\n" % int(linha))

par.close()
m4.close()