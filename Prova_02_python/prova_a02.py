# FAÇA UM PROGRAMA QUE SOLICITE AO USUARIO QUE DIGITE 10 VALORES PARA PREENCHER UMA LISTA.
# EM SEGUIDA, O PROGRAMA DEVE SEPARAR OS NUMEROS PARES E IMPARES EM LISTAS DIFERENTES. 
# POR FIM, EXIBA NA TELA OS NUMEROS PARES E OS IMPARES EM TUPLA, A QUANTIDADE DE NUMEROS
# PARES E IMPARES PRESENTES NA LISTA E A SOMA DE TODOS OS NUMEROS PARES E IMPARES, RESPECTIVAMENTE.    

numeros_pares = []
numeros_impares = []

# Solicite ao usuário que insira 10 valores e preencha a lista
for i in range(10): 
    valor = int(input("Digite um numero: "))
    
    if valor % 2 == 0:
        numeros_pares.append(valor)
    else:
        numeros_impares.append(valor)

# Crie uma tupla com os números pares e ímpares
tupla_numeros_pares = (numeros_pares)
tupla_numeros_impares = (numeros_impares)

# Calcule a quantidade e a soma dos números pares e ímpares
quantidade_pares = len(numeros_pares)
quantidade_impares = len(numeros_impares)
soma_pares = sum(numeros_pares)
soma_impares = sum(numeros_impares)

# Exiba os resultados
print(f"Números pares: {tupla_numeros_pares}")
print(f"Números ímpares: {tupla_numeros_impares}")
print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")
print(f"Soma dos números pares: {soma_pares}")
print(f"Soma dos números ímpares: {soma_impares}")
