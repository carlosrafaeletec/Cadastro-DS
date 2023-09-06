'''
EXERCÍCIO: [UTILIZAR OS RECURSOS ENSINADOS EM AULA]

PARTE I:
Um usuário necessita se cadastrar para entrar em um sistema.
Para tal ele deve digitar um e-mail e uma senha.

Pedir a digitação do e-mail.
Requisito:
- a string ter ao menos um arroba e um ponto 
	- ao menos uma letra antes do arroba
	- ao menos uma letra entre o arroba e ponto.
	- ao menos uma letra depois do ponto
	- no máximo dois pontos depois do arroba

PARTE II:
Pedir a digitação da senha.
Requisitos:
- Ao menos 6 caracteres
- Ao menos uma letra maiúscula
- Ao menos um número
- Ao menos um caractere especial

Depois da digitação, caso não atenda aos requisitos, exibir uma mensagem dizendo o que está faltando.

Caso a senha seja validada, pedir a redigitação da senha para conferir.
[neste momento não se preocupe em aparecer a senha e não o *]
'''

ema = input("Digite seu email: ")

def cadastro(ema) -> str:
    while True: 
        if '@' in ema and '.' in ema:
            if ema[0:] != '@':
                ind = ema.index('@')
                if ema[ind + 1:] != '.':
                    ind2 = ema.index('.')
                    if ema[ind2 + 1]:
                        if ema[ind + 1:] and ema.count('.') <= 2:
                            return ema 
                        elif ema.count('.') <= 0 and ema.count('.') > 2:
                            print("Passou de dois pontos ou não tem")
                    elif ema[-1] != '.':
                        
                else:
                    print("não tem letras entre o arroba e ponto")
            else:
                print("Não tem letras antes do arroba")
        elif not '@' in ema or not '.' in ema:
            print("Esta faltando arroba e ponto no email")         

result = cadastro(ema)
print(result)

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