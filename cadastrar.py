import mysql.connector


def menu():
    opcao = int(input('(1)CADASTRAR \n(2)LISTAR\n ESCOLHA UMA OPÇÃO: '))
    if (opcao == 1):
        cadastrar_cliente()
    elif (opcao == 2):
        listar_clientes()
    else:
        print('opção invalida!!!\n  Tente novamente ;)')
        menu()


def listar_clientes():
    listar = 'SELECT * FROM clientes'
    cursor.execute(listar)
    resultado = cursor.fetchall()
    print(resultado)


def cadastrar_cliente():
    nomecl = str(input('digite o nome: '))
    cpf = int(input('digite o cpf: '))
    numero = int(input('digite o telefone: 55+ '))
    conta = int(input('digite o valor : '))
    cadastrar = f'INSERT INTO clientes (nome, cpf, numero, conta) VALUES("{nomecl}","{cpf}","{numero}","{conta}")'
    cursor.execute(cadastrar)
    conexao.commit()


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password=None,
    database='banco',
)

cursor = conexao.cursor()

print('conectado\n')
menu()

# cadastrar_cliente()
# listar_clientes()
conexao.close
cursor.close
