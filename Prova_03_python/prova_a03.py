# CRIE  UM PROGRAMA EM PYTHON QUE PERMITA ADICIONAR, REMOVER E VISUALIZAR ALUNOS E SEUS NUMEROS DE MATRICULA
# USANDO UM DICIONARIO. O PROGRAMA DEVE FORNECER AS SEGUINTES FUNCIONALIDADES: 
# 1- ADICIONAR UM ALUNO: O USUARIO PODERA ADICIONAR O NOME E O NUMERO DE MATRICULA DE UM ALUNO AO DICIONARIO.
# 2- REMOVER UM ALUNO: O USUARIO PODERA REMOVER UM ALUNO DO DICIONARIO INFORMANDO O NUMERO DE MATRICULA.
# 3- VISUALIZAR TODOS OS ALUNOS: O USUARIO PODERA VISUALIZAR TODOS OS ALUNOS REGISTRADOS NO DICIONARIO,
#                                 EXIBINDO SEUS RESPECTIVOS NUMEROS DE MATRICULA.
# 4- O PROGRAMA DEVE SER EXCUTADO EM UM LOOP CONTINUO ATÉ QUE O USUARIO ESCOLHA SAIR.


alunos = {}

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite o numero de matricula do aluno: ")
    alunos[matricula] = nome
    print("Aluno adicionado com sucesso! ")

def remove_aluno():
    matricula = input("Digite o numero de matricula do aluno que deseja remover: ")
    if matricula in alunos:
        del alunos[matricula]
        print("Aluno removido com sucesso! ")
    else:
        print("Matricula não encontrada! Nenhum aluno removido. ")

def visualizar_aluno():
    print("Lista de alunos: ")
    for matricula, nome in alunos.items():
        print(f"Matricula: {matricula}, Nome: {nome}")

while True:
    print("\nEscolha uma Opção: ")
    print("1. Adicionar Aluno")
    print("2. Remover Aluno")
    print("3. Visualizar Todos Os Alunos")
    print("4. Sair")

    opcao = input("Digite o Número da Opção Desejada: ")

    if opcao =='1':
        adicionar_aluno()
    elif opcao =='2':
        remove_aluno()
    elif opcao =='3':
        visualizar_aluno()
    elif opcao =='4':
        print("Saindo do programa.")
        break
    else:
        print("Opção Invalida. Por favor, escolha uma opção valida! ")