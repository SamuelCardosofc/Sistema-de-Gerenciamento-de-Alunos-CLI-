import json
import os

def salvar_dados(dicionario, caminho):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dicionario, arquivo, indent=4, ensure_ascii=False)


def carregar_dados(caminho):
    if not os.path.exists(caminho):
        return []

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except json.JSONDecodeError:
        return []