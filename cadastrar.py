import mysql.connector


def menu():
    opcao = int(
        input('(1)CADASTRAR \n(2)LISTAR \n(3)PROCURAR UM CLIENTE\nESCOLHA UMA OPÇÃO: '))
    if (opcao == 1):
        cadastrar_cliente()
    elif (opcao == 2):
        listar_clientes()
    elif (opcao == 3):
        procura_cliente()
    else:
        print('opção invalida!!!\n  Tente novamente ;)')
        menu()


def voltar():
    input("Pressione ENTER para voltar ao menu ")
    print('\n \n \n \n \n \n')
    menu()


def procura_cliente():
    try:
        nome = input("Digite o nome do cliente: ")
        nome = nome.upper()
        procurar = "SELECT * FROM `clientes` WHERE nome = '"+nome+"'"
        cursor.execute(procurar)
        resultado = cursor.fetchall()
        print(resultado)
        voltar()
    except:
        print('ERRO! NENHUM CLIENTE ENCONTRADO. TENTE NOVAMENTE!')
        voltar()


def listar_clientes():
    listar = 'SELECT * FROM clientes'
    cursor.execute(listar)
    resultado = cursor.fetchall()
    print(resultado)
    voltar()


def cadastrar_cliente():
    try:
        nomecl = str(input('digite o nome: '))
        cpf = int(input('digite o cpf: '))
        numero = int(input('digite o telefone: 55+ '))
        conta = int(input('digite o valor : '))
        cadastrar = f'INSERT INTO clientes (nome, cpf, numero, conta) VALUES("{nomecl.upper()}","{cpf}","{numero}","{conta}")'
        cursor.execute(cadastrar)
        conexao.commit()
        print('cadastro feito com sucesso!\n')
        voltar()
    except:
        print('ERRO! VALORES NÃO APROPRIADOS')
        voltar()


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password=None,
    database='banco',
)

cursor = conexao.cursor()

print('conectado\n')
menu()


conexao.close
cursor.close
