import utils

# ===========================
# FUNÇÕES DE MENU
# ===========================

def mostrar_menu():
    print(" --- Sistema de alunos ---")
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
    RM = None
    nome = None
    notas = []
    nota = None
    erro = ""
    jaTem = False
    aluno = {}

    #loop do cadastrar
    while True:
        utils.limpar_tela()
        print("1 - Cadastrar aluno")
        if RM != None:
            print("Digite o nome do aluno: ", RM)

        # loop de validação e adição do RM
        while True:
            utils.limpar_tela()
            print("1 - Cadastrar aluno")
            if erro != "":
                print(erro)
                erro = ""

            if RM == None:
                #validações do RM
                try:
                    RM = float(input("Digite o RM do aluno: "))
                except:
                    erro = "Digite um número pro RM. Tente novamente."
                    RM = None

                if type(RM) == float:
                    if RM <= 0:
                        erro = "Digite um valor válido para RM. Tente novamente."
                        RM = None
                    else:
                        for i in range(0, len(alunos)):
                            if RM == alunos[i]["RM"]:
                                jaTem = True
                                RM = None
                                erro = "Esse RM já existe. Tente novamente."
                                break
                        if not jaTem:
                            aluno["RM"] = RM
                        else:
                            jaTem = False
            else:
                print("Digite o RM do aluno: %d" % aluno["RM"])

                if nome == None :
                    #validações do nome

                    nome = input("Digite o nome do aluno: ")
                    if nome == "":
                        nome = None
                        erro = "Nome do aluno não pode estar vazio. Tente novamente."
                    else:
                        aluno["nome"] = nome

                else:
                    print("Digite o nome do aluno: %s" % aluno["nome"])

                    if notas:
                        print("Notas do aluno:", ", ".join(map(str, notas)))

                    nota = input("Digite a nota do aluno ou 'n' para parar: ")

                    if nota.lower() == "n":
                        break

                    try:
                        nota = float(nota)

                        if nota < 0 or nota > 10:
                            erro = "Digite uma nota válida (0 a 10)."
                        else:
                            notas.append(nota)
                            aluno["notas"] = notas

                    except:
                        erro = "Entrada inválida. Digite um número ou 'n'."
        utils.alunos.append(aluno)
        break

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
    while True:
        utils.limpar_tela()
        print("3 - Buscar aluno")

        if not alunos:
            print("Nenhum aluno cadastrado.")
            input("Pressione Enter para voltar...")
            break

        if erro != "":
            print(erro)
            erro = ""

        if RM == None:
            # validações do RM
            try:
                RM = float(input("Digite o RM do aluno: "))
            except:
                erro = "Digite um número pro RM. Tente novamente."
                RM = None

            if type(RM) == float:
                if RM <= 0:
                    erro = "Digite um valor válido para RM. Tente novamente."
                    RM = None
                else:
                    for i in range(0, len(alunos)):
                        if RM == alunos[i]["RM"]:
                            encontrado = True
                            nome = alunos[i]["nome"]
                            notas = alunos[i]["notas"]
                            break
                    if not encontrado:
                        RM = None
                        erro = "Esse RM não existe. Tente novamente."
        else:
            print("Digite o RM do aluno: %d" % RM)
            print("Nome do aluno: %s" % nome)
            print("Notas do aluno:", ", ".join(map(str, notas)))
            input("Pressione <enter> para continuar...")
            break

# ===========================
# FUNÇÕES DO REMOVER ALUNO
# ===========================

def remover_aluno(alunos):
    erro = ""
    while True:
        encontrado = False
        utils.limpar_tela()
        print("4 - Remover aluno")
        if erro != "":
            print(erro)
            erro = ""

        if not alunos:
            print("Nenhum aluno cadastrado.")
            input("Pressione Enter para voltar...")
            break

        try:
            RM = float(input("Digite o RM do aluno a remover: "))
        except:
            erro = "RM deve ser numérico."
            RM = None

        if type(RM) == float:
            if RM <= 0:
                erro = "Digite um valor válido para RM. Tente novamente."
                RM = None
            else:
                for i in range(0, len(alunos)):
                    if alunos[i]["RM"] == RM:
                        encontrado = True
                        alunos.pop(i)
                        print("Aluno removido com sucesso.")
                        input("Pressione Enter para voltar...")
                        break
                if not encontrado:
                    erro = "Aluno não encontrado"
                    RM = None
                else:
                    break