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
    print("5 - Média das notas")
    print("0 - Sair")

# ===========================
# FUNÇÕES DO CADASTRO DE ALUNO
# ===========================

alunos = []

aluno = {}

alunos.append(aluno)
def cadastrar_aluno():
    RM = None
    nome = None
    notas = None
    nota = None
    erro = ""
    while True:
        limpar_tela()
        print("1 - Cadastrar aluno")
        if RM != None:
            print("Digite o nome do aluno: ", RM)
        while True:
            limpar_tela()
            print("1 - Cadastrar aluno")
            if erro != "":
                print(erro)
            if RM == None:
                try:
                    RM = float(input("Digite o RM do aluno: "))
                except:
                    erro = "Digite um número. Tente novamente."
                    RM = None

                if type(RM) == float:
                    if RM < 0:
                        erro = "Digite um valor válido para RM. Tente novamente."
                        RM = None
                    else:
                        aluno["RM"] = RM
                        break
        print(aluno["RM"])
        break

# ===========================
# EXECUÇÃO
# ===========================

while True:
    limpar_tela()
    mostrar_menu()
    escolhaMenu = int(input("Digite o número da ação escolhida: "))
    if escolhaMenu == 0:
        limpar_tela()
        print("Encerrado")
        break
    elif escolhaMenu == 1:
        cadastrar_aluno()
        break
    elif escolhaMenu == 2:
        limpar_tela()
        print("2 - Listar alunos")
        break
    elif escolhaMenu == 3:
        limpar_tela()
        print("3 - Buscar aluno")
        break
    elif escolhaMenu == 4:
        limpar_tela()
        print("4 - Remover aluno")
        break
    elif escolhaMenu == 5:
        limpar_tela()
        print("5 - Média das notas")
        break
    else:
        print("Opção inválida! Tente novamente.")




