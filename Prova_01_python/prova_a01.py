# FAÇA UM PROGRAMA EM PYTHON QUE DETERMINE EM DUAS VARIAVEIS (SENHA E EMAIL) E QUE CONTENHA UMA SENHA E UM EMAIL
# CADASTRADOS ANTECIPADAMENTE, EM SEGUIDA SOLICITE AO USUARIO UMA SENHA E EMAIL E UTILIZE O LAÇO DE REPETICAO
# JUNTAMENTE COM A ESTRUTURA DE CONDICAO PARA VERIFICAR SE O EMAIL E SENHA DIGITADA PELO USUARIO É IGUAL AO EMAIL
# E SENHA CADASTRADOS ANTECIPADAMENTE. E ENQUANTO A SENHA E O EMAIL QUE O USUARIO DIGITOU NAO FOR IGUAL AO EMAIL
# E SENHA CADASTRADOS ELE CONTINUE EM UM LOOP. 

email = "argalmeida@gmail.com"
senha = 123456

while True:
        i_1 = str(input("Digite o email: "))
        i_2 = int(input("Digite a senha numerica de 6 digitos: "))
        if i_1 == email and i_2 == senha:
            print("Parabéns, estaremos encaminhando para a pagina inicial!")
            break
        else:
            print("Email ou senha inválida, tente novamente ")

