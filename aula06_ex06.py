def multiplo (x, y):
    if x % y == 0:
        return "Sim"
    else:
        return "Não"

print("É Múltiplo? ", multiplo (10, 5))
print("É Múltiplo? ", multiplo (12, 5))
print("É Múltiplo? ", multiplo (15, 3))