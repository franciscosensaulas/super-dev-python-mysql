import os

import questionary

from src.database.criar_banco_dados import criar_database
from src.telas.produto_tela import executar_produto


if __name__ == "__main__":
    os.system("cls") # Limpar a tela
    criar_database()
    opcoes = ["Clientes", "Produtos", "Sair"] # Lista de opções para o usuário
    opcao_desejada = ""
    while opcao_desejada != "Sair":
        opcao_desejada = questionary.select("Escolha o menu desejado", opcoes).ask()

        if opcao_desejada == "Produtos":
            executar_produto()
