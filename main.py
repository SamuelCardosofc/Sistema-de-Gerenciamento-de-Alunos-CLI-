import cadastro
import utils

alunos = []

# massa de teste
aluno = {}
aluno["RM"] = 123
aluno["nome"] = "Samuel"
aluno["notas"] = [10, 5]
alunos.append(aluno)
aluno = {}
aluno["RM"] = 234
aluno["nome"] = "Marcos"
aluno["notas"] = [2, 4]
alunos.append(aluno)

while True:

    utils.limpar_tela()
    cadastro.mostrar_menu()

    try:
        escolhaMenu = int(input("Digite o número da ação escolhida: "))

        if escolhaMenu == 0:
            cadastro.encerrar()
            break
        elif escolhaMenu == 1:
            cadastro.cadastrar_aluno(alunos)
        elif escolhaMenu == 2:
            utils.limpar_tela()
            cadastro.listar_alunos(alunos)
        elif escolhaMenu == 3:
            cadastro.buscar_aluno(alunos)
        elif escolhaMenu == 4:
            cadastro.remover_aluno(alunos)
    except:
        print("erro")