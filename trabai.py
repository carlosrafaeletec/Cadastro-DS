ema = input("Digite seu email: ")

def cadastro(ema) -> str:
    cont = 0
    while True: 
        if '@' in ema and '.' in ema:
            if ema[cont + 1:] != '@':
                ind = ema.index('@')
                if ema[ind + 1:] != '.':
                    ind2 = ema.index('.')
                    if ema[ind2 + 1]:
                        if ema[ind + 1:] and ema.count('.') <= 2:
                            return ema 
                        elif ema.count('.') <= 0 and ema.count('.') > 2:
                            print("Passou de dois pontos ou não tem")
                    else:         

x = cadastro(ema)
print(x)

'''
if len(sen) < 6:
    if len(sen) == sen.upper():
        if sen.numeric():
            if sen.digit():
                print(len(sen.replace(sen, '*')))
            else:
                print("Esta faltando um caracter especial")
        else:
            print("Esta faltando numeros")
    else:
        print("Falta uma letra maiuscula")
else:
    print("tem menos de 6 caracteres")
break
'''