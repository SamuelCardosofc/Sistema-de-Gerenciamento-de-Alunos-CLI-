import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def calcular_media_e_situacao(notas):
    if not notas:
        return 0, "Sem notas"

    media = sum(notas) / len(notas)
    situacao = "Reprovado" if media < 6 else "Aprovado"

    return media, situacao
