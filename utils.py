import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def calcular_media_e_situacao(notas):
    if not notas:
        return 0, "Sem notas"

    media = sum(notas) / len(notas)
    situacao = "Reprovado" if media < 6 else "Aprovado"

    return media, situacao

def mostra_erro(erro):
    if erro != "":
        print(erro)

def validar_rm_basico(rm):
    try:
        rm = int(rm)
    except ValueError:
        return False, None, "Digite um número positivo pro RM."

    if rm <= 0:
        return False, None, "Digite um número positivo pro RM."

    return True, rm, ""

def validar_cadastro_rm(rm, alunos):
    valido, rm, erro = validar_rm_basico(rm)
    if not valido:
        return False, None, erro

    for aluno in alunos:
        if rm == aluno["RM"]:
            return False, None, "Esse RM já existe. Tente novamente."

    return True, rm, ""

def aluno_existe(rm,alunos):
    for aluno in alunos:
        if rm == aluno["RM"]:
            return True, aluno, ""

    erro = "Esse RM não existe. Tente novamente."
    return False, None, erro

def validar_nome(nome):
    if nome == "":
        erro = "Nome do aluno não pode estar vazio. Tente novamente."
        return False, None, erro
    else:
        return True, nome, ""

def validar_nota(nota):

    try:
        nota = float(nota)

        if nota < 0 or nota > 10:
            erro = "Digite uma nota válida (0 a 10)."
            return False, None, erro
        else:
            return True, nota, ""

    except:
        erro = "Entrada inválida. Digite um número ou 'n'."
        return False, None, erro
