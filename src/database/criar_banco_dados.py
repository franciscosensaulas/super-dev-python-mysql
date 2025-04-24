import sys
from mysql.connector import connect

def criar_database():
    """
    Verifica se o banco de dados existe, caso contrário, será criado com as tabelas necessárias
    """
    conexao = None
    try:
        conexao = __abrir_conexao()

        nome_banco_dados="super_empresa"

        cursor = conexao.cursor()
        if __existe_banco_dados(cursor, nome_banco_dados) == True:
            return
        
        __criar_banco_dados(cursor, nome_banco_dados)

        conexao.database = nome_banco_dados
        __criar_tabela_produto(cursor)
        __popular_tabela_produtos(cursor)
    except Exception as erro:
        print("Ocorreu um erro ao tentar criar o banco de dados")
        print(erro)
        sys.exit(1)
    finally:
        if conexao is not None:
            conexao.close()

def __abrir_conexao():
    return connect(
        host="127.0.0.1", # host é a máquina q está o banco de dados
        port=3306, # porta padrão do MySQL
        user="root",
        password="admin",
        autocommit=True
    )

def __existe_banco_dados(cursor, nome_banco_dados) -> bool:
    cursor.execute("SHOW DATABASES LIKE %s", (nome_banco_dados,))
    existe = cursor.fetchone()

    if existe:
        return True
    return False

def __criar_banco_dados(cursor, nome_banco_dados):
    cursor.execute(f"CREATE DATABASE {nome_banco_dados}")

def __criar_tabela_produto(cursor):
    cursor.execute("""
    create table produtos(
        id int primary key auto_increment,
        nome varchar(50)
    );
    """)

def __popular_tabela_produtos(cursor):
    cursor.execute("""
                   INSERT INTO produtos (nome) VALUES
                   ('Uva'),
                   ('Maçã'), 
                   ('Abacate'),
                   ('Sorvete')
                   """)
