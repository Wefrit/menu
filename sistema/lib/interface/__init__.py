def erro():
    print ('\33[31mErro! Por favor digite um número válido.\33[m')

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 0:
                erro()
                continue
        except (ValueError, TypeError):
            erro()
        except (KeyboardInterrupt):
            erro()
        else:
            return n

def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\33[33m{c} - \33[34m{item}\33[m')
        c += 1
    print (linha())
    opc = leiaInt('\33[32mSua Opção: \33[m')
    return opc