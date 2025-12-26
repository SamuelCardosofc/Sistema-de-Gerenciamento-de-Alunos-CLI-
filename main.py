import cadastro
import utils
import storage


CAMINHO_ARQUIVO = "alunos.json"

alunos = storage.carregar_dados(CAMINHO_ARQUIVO)
erro = ""

while True:
    utils.limpar_tela()
    cadastro.mostrar_menu()
    utils.mostra_erro(erro)

    escolhaMenu = input("Digite o escolha: ")
    try:
        escolhaMenu = int(escolhaMenu)
        if escolhaMenu < 0 or escolhaMenu > 4:
            erro = "Escolha entre 0 e 4"
        else:
            erro = ""
            if escolhaMenu == 0:
                cadastro.encerrar()
                break
            elif escolhaMenu == 1:
                cadastro.cadastrar_aluno(alunos)
            elif escolhaMenu == 2:
                cadastro.listar_alunos(alunos)
            elif escolhaMenu == 3:
                cadastro.buscar_aluno(alunos)
            elif escolhaMenu == 4:
                cadastro.remover_aluno(alunos)
    except:
        erro = "Escolha entre 0 e 4"

