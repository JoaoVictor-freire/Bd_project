# 📌 Projeto CRUD de Clínica Médica em Python

Este é um projeto de um **CRUD (Create, Read, Update, Delete)** para gerenciamento de uma **clínica médica**, desenvolvido em **Python**. O sistema permite o cadastro, consulta, atualização e remoção de **médicos, pacientes e exames**, além de listar informações importantes para administração da clínica.

## 🚀 Objetivo do Projeto
Criar um sistema eficiente para gerenciamento de consultas médicas, utilizando Python e futuramente integrando um **banco de dados PostgreSQL** para armazenamento persistente.

---

## 📂 Estrutura do Projeto
```
📦 clinic-crud-python
 ┣ 📜 doctor.py         # Classe para gerenciamento de médicos
 ┣ 📜 patient.py        # Classe para gerenciamento de pacientes
 ┣ 📜 exam.py           # Classe para agendamento e gestão de exames
 ┣ 📜 main.py           # Arquivo principal para testes e execução
 ┗ 📜 README.md         # Documentação do projeto
```

---

## 🛠 Tecnologias Utilizadas
✅ **Python** → Linguagem principal do projeto  
✅ **PostgreSQL (futuro)** → Banco de dados relacional para armazenamento persistente  
✅ **VS Code** → IDE recomendada para desenvolvimento  

---

## 📌 Funcionalidades
### 👨‍⚕️ Médicos (`doctor.py`)
- `cadastrar()` → Cadastra um novo médico.
- `update()` → Atualiza os dados de um médico.
- `list_all()` → Lista todos os médicos cadastrados.
- `listOne(name)` → Exibe um médico pelo nome.
- `search_Name(name)` → Retorna um médico pelo nome.
- `remove(doctor_id)` → Remove um médico pelo ID.

### 👤 Pacientes (`patient.py`)
- `cadastrar()` → Cadastra um novo paciente.
- `update()` → Atualiza os dados de um paciente.
- `list_all()` → Lista todos os pacientes cadastrados.
- `listOne(name)` → Exibe um paciente pelo nome.
- `search_Name(name)` → Retorna um paciente pelo nome.
- `remove(patient_id)` → Remove um paciente pelo ID.

### 📝 Exames (`exam.py`)
- `register_exam()` → Cadastra um novo exame.
- `schedule()` → Agendar um exame para um paciente.
- `confirm()` → Confirma um exame.
- `cancel()` → Cancela um exame.
- `list_all()` → Lista todos os exames agendados.

---

## 💾 Configuração do Ambiente
### 1️⃣ Instalar o Python
Certifique-se de ter o **Python 3.10+** instalado.  
[Download do Python](https://www.python.org/downloads/)

### 2️⃣ Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/clinic-crud-python.git
cd clinic-crud-python
```

### 3️⃣ Criar e Ativar um Ambiente Virtual (Opcional, mas Recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate  # Windows
```

### 4️⃣ Instalar Dependências
```bash
pip install psycopg2  # Biblioteca para PostgreSQL (futuramente utilizada)
```

### 5️⃣ Executar o Sistema
```bash
python main.py
```

---

## 🔗 Futuras Implementações
✅ **Integração com PostgreSQL** → Armazenamento persistente dos dados.  
✅ **Interface Gráfica (GUI) ou API REST** → Melhor experiência do usuário.  
✅ **Autenticação de Usuários** → Segurança e controle de acesso.  
✅ **Histórico Médico dos Pacientes** → Melhor gerenciamento de consultas.  

---
