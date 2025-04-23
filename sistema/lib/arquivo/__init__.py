from fileinput import close

from sistema.lib.interface import cabeçalho, leiaInt


def arquivoExiste(nome):
    try:
        with open(nome,'rt'):
            pass
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        with open(nome, 'wt+'):
            pass
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo criado com sucesso')

def lerArquivo(nome):
    try:
       with open(nome, 'rt') as a:
           cabeçalho('PESSOAS CADASTRADAS')
           for i, pessoa in enumerate(a, 1):
               nome, idade = pessoa.strip().split(';')
               print(f"{i:<2}.{nome:<25}{idade:>3}")
    except:
        print('Erro ao ler o arquivo')

def cadastrar(arq,nome = 'desconhecido', idade = '0'):
    try:
        with open(arq, 'at') as a:
            a.write(f'{nome};{idade}\n')
        print('Pessoa cadastrada com sucesso')
    except:
        print('Erro ao manipular o arquivo!')

def excluirPessoa(arq):
    try:
        with open(arq, 'r') as a:
            pessoas = a.readlines()
        if not pessoas:
            print("Nenhuma pessoa cadastrada.")
            return
        for i, pessoa in enumerate(pessoas, 1):
            nome, idade = pessoa.strip().split(';')
            print(f"{i}. {nome} - {idade}")
        numero = int(input('Digite o número da pessoa que deseja excluir: '))
        if numero > 0 and numero <= len(pessoas):
            pessoa_a_excluir = pessoas[numero - 1].strip()
            nome, idade = pessoa_a_excluir.split(';')
            with open(arq, 'w') as a:
                for i, pessoa in enumerate(pessoas, 1):
                    if i != numero:
                        a.write(pessoa)
            print(f"Pessoa {nome} ({idade}) excluída com sucesso.")
        else:
            print("Número inválido.")
    except Exception as e:
        print(f"Erro ao listar ou excluir a pessoa")