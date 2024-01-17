# CONSIDERE UMA LISTA DE NUMEROS INTEIROS
# NUMEROS = [1,2,3,4,5,6,7,8,9,10]

# UTILIZANDO AS FUNÇÕES MAP(), FILTER() E REDUCE(), ESCREVA UM CÓDIGO QUE EXECUTE AS SEGUINTES OPERAÇÕES:

# FUNÇÃO MAP() PARA OBTER UMA NOVA[1,4,9,16,25,36,49,64,81,100]
# LISTA COM O QUADRADO DE CADA NUMERO DA LISTA NUMEROS
# FUNÇÃO FILTER() PARA OBTER UMA NOVA LISTA COM NUMEROS PARES DA LISTA NUMEROS  
# FUNÇÃO REDUCE() PARA OBTER A SOMA DE TODOS OS NUMEROS DA LISTA NUMEROS
# QUAL O RESULTADO OBTIDO APÓS A EXECUÇÃO DAS OPERAÇÕES ACIMA?


numeros = [1,2,3,4,5,6,7,8,9,10]
quadrado = list (map(lambda x: x **2, numeros))
print (quadrado) 

# [1,4,9,16,25,36,49,64,81,100]

numeros = [1,2,3,4,5,6,7,8,9,10]
par = list(filter(lambda x: x %2==0, numeros))
print (par)

# [2,4,6,8,10]

from functools import reduce

numeros = [1,2,3,4,5,6,7,8,9,10]
soma = reduce(lambda x,y: x+y, numeros)
print (soma)

# 55
