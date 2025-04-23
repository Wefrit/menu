from sistema.lib.interface import *
from sistema.lib.arquivo import *
from time import sleep

arq = 'arquivo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Cadastrar Pessoa','Excluir Pessoa','Exibir Lista', 'Sair'])
    if resposta == 1:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 2:
        cabeçalho('EXCLUIR PESSOA')
        excluirPessoa(arq)
    elif resposta == 3:
        lerArquivo(arq)
    elif resposta == 4:
        cabeçalho('Saindo do sistema...Até logo!')
        break
    else:
        erro()
    sleep(2)
