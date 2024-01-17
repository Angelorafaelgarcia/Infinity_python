# DESENVOLVA UM PROGRAMA EM PYTHON QUE PERMITA AO USUARIO DIGITAR VARIAS NOTAS. EM SEGUIDA CRIE UMA FUNÇÃO CHAMADA
# "CALCULAR_MEDIA" QUE IRÁ RECEBER AS NOTAS DIGITADAS E CALCULAR A MEDIA DO ALUNO. TAMBEM CRIE UMA FUNÇÃO CHAMADA
# "VERIFICAR SITUAÇÃO" QUE, COM BASE NA MEDIA CALCULADA, IRA EXIBIR A SITUAÇÃO DO ALUNO: 
# "REPROVADO" SE A MEDIA FOR MENOR QUE 7
# "APROVADO"  SE A MEDIA FOR MAIOR OU IGUAL A 7 
# "PARABENS SUA MEDIA É 10" SE A MEDIA FOR IGUAL A 10.


def obter_notas():
    notas = []
    while True:
        try:
            nota = float(input("Digite uma nota entre 0 e 10 (ou digite -1 para encerrar): "))
            if nota == -1:
                break
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Digite uma nota válida entre 0 e 10.")
        except ValueError:
            print("Digite um valor numérico.")

    return notas

def calcular_media(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

def verificar_situacao(media):
    if media < 7:
        return "Reprovado"
    elif media == 10:
        return "Parabéns, sua média é 10!"
    else:
        return "Aprovado"

# Obtém as notas do usuário
notas_aluno = obter_notas()

# Calcula a média das notas
media_aluno = calcular_media(notas_aluno)

# Verifica a situação do aluno com base na média
situacao_aluno = verificar_situacao(media_aluno)

# Exibe os resultados
print(f"Média do aluno: {media_aluno}")
print(f"Situação do aluno: {situacao_aluno}")
