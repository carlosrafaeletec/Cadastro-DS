import os
from biblio import *
while True:
    print("\nBem vindo ao Menu de cadastro!\n")
    print("Escolha qual você quer cadastrar primeiro!")
    print("1 - Cadastre-se")
    print("2 - Faça seu login")
    print("0 - Sair")
    opc = input("\nDigite qual opcao você quer fazer: ")

    match(opc):
        case '1':
            os.system("cls")
            email = input("Digite seu email: ")
            cadastroEmail(email)
            senha = input("Digite a senha: ")
            cadastroSenha(senha)
        
        case '2':
            os.system("cls")
            login(email, senha)
        
        case '0':
            print("\nDesligando...")
            break