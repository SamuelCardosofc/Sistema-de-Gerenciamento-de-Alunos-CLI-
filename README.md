# Sistema de Gerenciamento de Alunos (CLI)

Este projeto consiste em um **sistema de gerenciamento de alunos em modo terminal (CLI)**,
desenvolvido em Python, com foco no aprendizado e na prática de conceitos fundamentais
da linguagem e da lógica de programação.

> ⚠️ **Observação:** Este sistema funciona exclusivamente no **terminal**, não possuindo
interface gráfica.

> 📚 **Projeto educacional**: desenvolvido com fins de estudo e prática de programação.

---

## Conceitos utilizados
- Variáveis
- Entrada e saída de dados (`input`, `print`)
- Estruturas condicionais (`if`, `elif`, `else`)
- Laços de repetição (`while`, `for`)
- Listas
- Dicionários
- Funções
- Tratamento simples de erros (`try/except`)

---

## Funcionalidades

### 1️⃣ Cadastrar aluno
Cada aluno possui as seguintes informações:
- Nome
- RM (RA ou matrícula)
- Lista de notas

Os dados são armazenados utilizando:
- Um **dicionário** para cada aluno
- Uma **lista** contendo todos os alunos cadastrados

---

### 2️⃣ Listar alunos
Mostra, para cada aluno:
- RM
- Nome
- Média final das notas
- Situação do aluno (aprovado/reprovado)

---

### 3️⃣ Buscar aluno
- Busca realizada pelo **RM**
- Exibe os dados do aluno e suas notas
- Caso o aluno não exista, o sistema exibe uma mensagem de aviso

---

### 4️⃣ Remover aluno
- Remoção realizada pelo **RM**
- Solicita confirmação antes de apagar o aluno

---

### 0️⃣ Sair do sistema
- Encerra a execução do programa

---

## Execução do projeto
Para executar o sistema, utilize o comando abaixo no terminal:

```bash
python main.py
