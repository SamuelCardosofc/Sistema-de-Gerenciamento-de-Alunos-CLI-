import utils

# ===========================
# FUNÇÕES DE MENU
# ===========================

def mostrar_menu():
    print("Sistema de Gerenciamento de Alunos - v0.6.2")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Remover aluno")
    print("0 - Sair")
# ===========================
# FUNÇÕES DO ENCERRAMENTO
# ===========================

def encerrar():
    utils.limpar_tela()
    print("0 - Sair")
    print("Programa encerrado")

# ===========================
# FUNÇÕES DO CADASTRO DE ALUNO
# ===========================


def cadastrar_aluno(alunos):
    aluno = {}
    notas = []
    erro = ""

    # -------- RM --------
    while True:
        utils.limpar_tela()
        print("1 - Cadastrar aluno\n")
        utils.mostra_erro(erro)

        rm_input = input("Digite o RM do aluno: ")
        valido, rm, erro = utils.validar_cadastro_rm(rm_input, alunos)

        if valido:
            aluno["RM"] = rm
            break

    # -------- NOME --------
    while True:
        utils.limpar_tela()
        print("1 - Cadastrar aluno\n")
        print(f"RM: {aluno['RM']}")
        utils.mostra_erro(erro)

        nome_input = input("Digite o nome do aluno: ")
        valido, nome, erro = utils.validar_nome(nome_input)

        if valido:
            aluno["nome"] = nome
            break

    # -------- NOTAS --------
    while True:
        utils.limpar_tela()
        print("1 - Cadastrar aluno\n")
        print(f"RM: {aluno['RM']}")
        print(f"Aluno: {aluno['nome']}")
        utils.mostra_erro(erro)

        if notas:
            print("Notas:", ", ".join(map(str, notas)))

        nota_input = input("Digite a nota ou 'n' para finalizar: ")

        if nota_input.lower() == "n":
            break

        valido, nota, erro = utils.validar_nota(nota_input)
        if valido:
            notas.append(nota)

    aluno["notas"] = notas
    alunos.append(aluno)


# ===========================
# FUNÇÕES DO LISTAR ALUNOS
# ===========================

def listar_alunos(alunos):
    utils.limpar_tela()
    print("2 - Listar alunos\n")

    if not alunos:
        print("Nenhum aluno cadastrado.")
        input("Pressione Enter para voltar...")
        return

    for aluno in alunos:
        media, situacao = utils.calcular_media_e_situacao(aluno["notas"])

        print(f"RM: {aluno['RM']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Média: {media:.1f}")
        print(f"Situação: {situacao}")
        print("-" * 30)

    input("Pressione Enter para voltar...")

# ===========================
# FUNÇÕES DO BUSCAR ALUNO
# ===========================

def buscar_aluno(alunos):
    erro = ""
    utils.limpar_tela()
    print("3 - Buscar aluno\n")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        input("Pressione Enter para voltar...")
        return

    while True:
        utils.limpar_tela()
        print("3 - Buscar aluno\n")
        utils.mostra_erro(erro)

        rm_input = input("Digite o RM do aluno: ")

        valido, rm, erro = utils.validar_rm_basico(rm_input)
        if valido:
            valido, aluno, erro = utils.aluno_existe(rm, alunos)
            if valido:
                break

    media, situacao = utils.calcular_media_e_situacao(aluno["notas"])
    print(f"Nome: {aluno['nome']}")
    print("Notas do aluno:", ", ".join(map(str, aluno["notas"])))
    print(f"Média: {media:.1f}")
    print(f"Situação: {situacao}")
    input("Pressione Enter para continuar...")

# ===========================
# FUNÇÕES DO REMOVER ALUNO
# ===========================

def remover_aluno(alunos):
    erro = ""
    utils.limpar_tela()
    print("4 - Remover Aluno\n")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        input("Pressione Enter para voltar...")
        return

    while True:
        utils.limpar_tela()
        print("4 - Remover aluno\n")
        utils.mostra_erro(erro)

        rm_input = input("Digite o RM do aluno: ")
        valido, rm, erro = utils.validar_rm_basico(rm_input)
        if valido:
            valido, aluno, erro = utils.aluno_existe(rm, alunos)
            if valido:
                break


    alunos.remove(aluno)
    print("Aluno removido com sucesso.")
    input("Pressione Enter para voltar...")