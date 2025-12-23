import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

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
    limpar_tela()
    print("0 - Sair")
    print("Programa encerrado")

# ===========================
# FUNÇÕES DO CADASTRO DE ALUNO
# ===========================

alunos = []

def cadastrar_aluno():
    RM = None
    nome = None
    notas = []
    nota = None
    erro = ""
    jaTem = False
    aluno = {}

    #loop do cadastrar
    while True:
        limpar_tela()
        print("1 - Cadastrar aluno")
        if RM != None:
            print("Digite o nome do aluno: ", RM)

        # loop de validação e adição do RM
        while True:
            limpar_tela()
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
        alunos.append(aluno)
        break

# ===========================
# FUNÇÕES DO LISTAR ALUNOS
# ===========================

def listar_alunos():
    limpar_tela()
    print("2 - Listar alunos")

    if len(alunos) != 0:
        for i in range(0, len(alunos)):
            media = 0
            situacao = ""
            print("%d" % alunos[i]["RM"], end=" ")
            print(alunos[i]["nome"], end=" ")

            for j in range(0, len(alunos[i]["notas"])):
                media += alunos[i]["notas"][j]
            if media <6:
                situacao = "reprovado"
            else:
                situacao = "aprovado"

            print(situacao)
    else:
        print("Nenhum aluno cadastrado.")

    input("Pressione Enter para continuar...")

# ===========================
# FUNÇÕES DO BUSCAR ALUNO
# ===========================

def buscar_aluno():
    RM = None
    nome = None
    notas = []
    erro = ""
    encontrado = False
    while True:
        limpar_tela()
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

def remover_aluno():
    erro = ""
    while True:
        encontrado = False
        limpar_tela()
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

# ===========================
# EXECUÇÃO
# ===========================

while True:

    limpar_tela()
    mostrar_menu()

    try:
        escolhaMenu = int(input("Digite o número da ação escolhida: "))

        if escolhaMenu == 0:
            encerrar()
            break
        elif escolhaMenu == 1:
            cadastrar_aluno()
        elif escolhaMenu == 2:
            limpar_tela()
            listar_alunos()
        elif escolhaMenu == 3:
            limpar_tela()
            buscar_aluno()
        elif escolhaMenu == 4:
            limpar_tela()
            remover_aluno()
    except:
        print("erro")