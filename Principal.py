from Modelos import Aluno, listar_alunos

def exibir_menu():
    print("=====================")
    print("MENU ALUNOS")
    print("0 - sair")
    print("1 - cadastrar aluno")
    print("2 - Listar aluno")
    print("=====================")

def cadastrar():
    nome_aluno = input("Digite o nome do aluno: ")

    nome_aluno = Aluno (nome_aluno)
    nome_aluno.salvar()

def mostrar():
    for nome_aluno in listar_alunos():
        nome_aluno.exibir()

while True:
    exibir_menu()
    opcao = input("Digite um opção: ")

    if opcao == "0":
        print=input("programa finalizado")
        break
    elif opcao == "1":
        cadastrar()
    elif opcao == "2":
        mostrar()
    else:
        print ("Opção invalida! Tente novamente. ")  

