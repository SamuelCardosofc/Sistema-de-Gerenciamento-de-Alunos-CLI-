Sistema de Gerenciamento de Alunos (CLI)

Este projeto consiste em um sistema de gerenciamento de alunos em modo terminal (CLI),
desenvolvido em Python, com foco no aprendizado, prática de lógica de programação
e organização de código.

⚠️ Observação: Este sistema funciona exclusivamente no terminal e não possui interface gráfica.

📚 Projeto educacional: desenvolvido com fins de estudo, prática e evolução gradual do código.

🎯 Objetivos do projeto

Praticar lógica de programação

Trabalhar com estruturas de dados

Aprender organização e refatoração de código

Simular um sistema simples de gerenciamento

🧠 Conceitos utilizados

Variáveis

Entrada e saída de dados (input, print)

Estruturas condicionais (if, elif, else)

Laços de repetição (while, for)

Listas

Dicionários

Funções

Modularização de código (múltiplos arquivos)

Tratamento simples de erros (try/except)

🧱 Estrutura do projeto (refatoração)

O projeto foi refatorado para melhorar a organização, legibilidade e manutenção do código.

Cada funcionalidade foi separada em funções e arquivos específicos,
seguindo boas práticas de organização.

⚙️ Funcionalidades

1️⃣ Cadastrar aluno

Cada aluno possui as seguintes informações:

Nome

RM (RA ou matrícula)

Lista de notas

Os dados são armazenados utilizando:

Um dicionário para cada aluno

Uma lista contendo todos os alunos cadastrados

Durante o cadastro, o sistema:

Valida o RM

Evita RMs duplicados

Valida as notas inseridas

2️⃣ Listar alunos

Exibe todos os alunos cadastrados, mostrando:

RM

Nome

Média final das notas

Situação do aluno (Aprovado ou Reprovado)

3️⃣ Buscar aluno

Busca realizada pelo RM

Exibe:

Nome

RM

Notas

Média

Situação

Caso o aluno não exista, o sistema exibe uma mensagem de aviso

4️⃣ Remover aluno

Remoção realizada pelo RM

Exibe mensagem de sucesso ou erro

0️⃣ Sair do sistema

Encerra a execução do programa de forma segura

▶️ Execução do projeto

Para executar o sistema, utilize o comando abaixo no terminal:

``` bash
python main.py