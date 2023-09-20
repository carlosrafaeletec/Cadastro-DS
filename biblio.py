import os

#Exer 1
def cadastroEmail(email) -> None:
  while True:
    if '@' in email and '.' in email:
      vef1 = email.index('@')
      if email.count("@") <= 1:
        vef2 = email.find('.', vef1)
        if len(email[0:vef1]) >= 1:
          if len(email[vef1:vef2]) >= 1:
            if len(email[vef2:]) >= 1:
              if email[vef1:].count('.') <= 2 and len(email[vef2:]) >= 1:
                if email[vef2:][1] != '.':
                  os.system("cls")
                  print(f"\n{email}")
                  break
                else:
                  print('\nNão pode ter dois pontos juntos')
                  email = input("Digite seu email novamente: ")
              else:
                print("\nHá mais de 2 pontos")
                email = input("Digite seu email novamente: ")
            else:
              print("\nTer letras depois do ponto")
              email = input("Digite seu email novamente: ")
          else:
            print("\nDeve conter letras entre o arroba e o ponto")
            email = input("Digite seu email novamente: ")
        else:
          print('\nNão há letras antes do arroba ou tem pontos antes do arroba')
          email = input("Digite seu email novamente: ")
      else:
        print("\nHá mais de um arroba")
        email = input("Digite seu email novamente")
    elif '@' not in email or '.' not in email:
      print('\nColoque um arroba ou ponto no seu email')
      email = input("Digite seu email novamente: ")

#Exer 2
def cadastroSenha(senha) -> None:
    while True:
      if len(senha) >= 6:
          numb = 0
          uppr = 0
          special = 0
          caracSpecial = "!@#$%^&*()_+[]{}|;:'<>,.?/"
          for carac in senha:
              if carac >= 'A' and carac <= 'Z':
                  uppr += 1
              if carac.isdigit():
                  numb += 1
              if carac in caracSpecial:
                  special += 1
          if uppr >= 1 and numb >= 1 and special >= 1:
              os.system("cls")
              print(f"\n{senha}")
              confirm = input("Digite sua senha de novo para confirmar: ")
              if senha == confirm:
                  print("\nCadastrado com sucesso! Bem vindo!")
                  break
              else:
                  print("\nHá algo de errado, verifique se digitou certo")
                  confirm = input("Digite novamente: ")
          else:
              print('\nEsta faltando algum requisito')
              senha = print("Digite sua senha novamente: ")
      else:
          print("\nTenha pelo menos 6 caracteres na senha")
          senha = input("Digite novamente: ")

def login(email, senha) -> None:
  chanc = 0
  while True:
    emailConfir = input("Digite seu email: ")
    if emailConfir == email:
      passw = input("Digite sua senha: ")
      if passw == senha:
        print("\nBem vindo a sua conta!")
        break
      else:
        print("\nSenha incorreta!!")
        chanc += 1
        if chanc == 3:
          print("\nConta bloqueada! Volte daqui algumas horas")
          break
        else:
          continue     
    else:
      print("\nEmail incorreto!!")