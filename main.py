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
# FUNÇÕES DO ENCERRAMENTO
# ===========================

def encerrar():
    limpar_tela()
    print("0 - Sair")
    print("Programa encerrado")

# ===========================
# FUNÇÕES DO CADASTRO DE ALUNO
# ===========================

# teste do loop
# remover no futuro
alunos = []

alunos.append({
    "RM": 123,
    "nome": "Ana",
    "notas": [7.5, 8.0, 9.0]
})

alunos.append({
    "RM": 456,
    "nome": "Beatriz",
    "notas": [7.5, 8.0, 9.0]
})


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
                    aluno["nome"] = nome

                else:
                    print("Digite o nome do aluno: %s" % aluno["nome"])

                    if notas:
                        print("Notas do aluno: ", end=" ")
                        for i in range(0, len(notas)):
                            if i == len(notas)-1:
                                print(notas[i])
                            else:
                                print(notas[i], end=", ")

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
    main()

# ===========================
# EXECUÇÃO
# ===========================

def main():
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
        except:
            print("erro")

main()