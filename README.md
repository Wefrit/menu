# 📋 Sistema de Cadastro de Pessoas (Terminal)

Este projeto é um sistema simples de cadastro de pessoas desenvolvido em Python. Ele funciona diretamente no terminal e permite **cadastrar**, **excluir** e **listar pessoas**, utilizando um arquivo `.txt` como base de dados.
Caso não tenha um arquivo criado ele cria o arquivo ja na pasta.
Criado a partir de um projeto do Curso em Vídeo (Exercício Python #115) com opção adicionada de excluir pessoa cadastrada.
---

## 📁 Estrutura do Projeto

Sistema/
├── lib/
│ ├── arquivo/
│ │ └── init.py # Funções de manipulação de arquivo
│ └── interface/
│ └── init.py # Interface de entrada (menu, cabeçalhos, validações)
├── menu_cadastro.py # Arquivo principal que executa o sistema

---

## ✅ Funcionalidades

- Cadastrar pessoas com nome e idade
- Excluir pessoas da lista
- Exibir lista de pessoas cadastradas
- Validação de entradas numéricas
- Armazenamento de dados em arquivo `.txt`

---

## ⚙️ Requisitos

- Python 3.6 ou superior

> 📦 O projeto não utiliza bibliotecas externas. Apenas recursos nativos do Python.

---

## 🚀 Como Executar

1. **Clone o repositório** (ou copie os arquivos para sua máquina):

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```
---
## Acesse a pasta do projeto:

Execute o programa principal:

```bash
python menu_cadastro.py
```

O arquivo arquivo.txt será criado automaticamente, caso não exista.

## 💡 Exemplo de Uso

---------- MENU PRINCIPAL ----------
1 - Cadastrar Pessoa
2 - Excluir Pessoa
3 - Exibir Lista
4 - Sair
-----------------------------------
Sua Opção: 1

---------- NOVO CADASTRO ----------
Nome: Ana Clara
Idade: 25
Pessoa cadastrada com sucesso

# 🧠 Organização do Código

lib/arquivo/__init__.py → Funções que manipulam o arquivo: leitura, escrita, cadastro e exclusão.

lib/interface/__init__.py → Funções para exibir menu, cabeçalhos, e validar entradas do usuário.

menu_cadastro.py → Controlador principal que exibe o menu e chama as funções de acordo com a escolha do usuário.

👨‍💻 Autor
Desenvolvido por Nathan Lopes.
