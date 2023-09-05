import random

def sorteio_adicional(numeros_base, qtd_adicional):
    numeros_possiveis = list(range(1, 26))
    for numero in numeros_base:
        numeros_possiveis.remove(numero)
    
    numeros_sorteados_adicionais = random.sample(numeros_possiveis, qtd_adicional)
    return numeros_sorteados_adicionais

# Solicitar 9 números do usuário
numeros_base = []
for i in range(9):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros_base.append(numero)

qtd_adicional = 6
numeros_sorteados_adicionais = sorteio_adicional(numeros_base, qtd_adicional)

print("\nNúmeros base:", numeros_base)
print("Números sorteados adicionais:", numeros_sorteados_adicionais)

