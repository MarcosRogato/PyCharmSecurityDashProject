# 🛡️ Security Dashboard

Dashboard web desenvolvido em **Python** para monitoramento, gerenciamento e análise inteligente de logs de segurança. A aplicação permite importar diferentes formatos de arquivos, visualizar eventos em tempo real, gerenciar registros por meio de operações CRUD e utilizar Inteligência Artificial para gerar análises automáticas sobre os dados armazenados.

---

# 🚀 Funcionalidades

## 📥 Importação de Arquivos

O sistema permite importar diferentes formatos para o banco de dados:

* ✅ `.log`
* ✅ `.txt`
* ✅ `.csv`
* ✅ `.md`

Os arquivos são processados automaticamente e seus registros são armazenados no banco SQLite para consulta e análise.

---

## 📊 Dashboard Interativo

* Visualização dos logs em tempo real
* Organização dos registros por categoria
* Interface intuitiva inspirada em centrais de monitoramento de segurança (SOC)
* Consulta rápida aos eventos registrados
* Painel responsivo e de fácil navegação

---

## 🤖 Análise Inteligente com IA

O projeto integra um módulo de Inteligência Artificial utilizando **Groq API** e modelos **LLaMA**, responsável por analisar automaticamente os logs armazenados no sistema, oferecendo:

* Resumo inteligente dos eventos
* Identificação de padrões e comportamentos suspeitos
* Destaque para eventos críticos
* Apoio na investigação de incidentes de segurança
* Geração automática de insights sobre o ambiente monitorado

---

## 📝 Gerenciamento de Logs (CRUD)

* Inserção manual de registros
* Edição de logs existentes
* Exclusão de registros
* Consulta completa ao banco de dados

---

## 🎯 Classificação dos Eventos

Os logs são organizados visualmente por nível de severidade:

* 🔴 ERROR
* 🟡 WARNING
* 🟢 INFO

---

# 🛠️ Tecnologias Utilizadas

* Python 3.13
* Flask
* Flask-Login
* SQLite
* HTML5
* CSS3
* JavaScript
* Jinja2
* Groq API
* LLaMA (Large Language Model)

---

# 📂 Estrutura do Projeto

```text
Security-Dashboard/
│
├── app.py
├── database.py
├── database.db
├── groq_analyzer.py
├── README.md
│
└── templates/
    ├── index.html
    └── editar.html
```

---

# ▶️ Como Executar

## Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/security-dashboard.git
```

Entre na pasta:

```bash
cd security-dashboard
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Caso não exista um arquivo `requirements.txt`, instale manualmente:

```bash
pip install flask
```

Execute a aplicação:

```bash
python app.py
```

Acesse pelo navegador:

```text
http://127.0.0.1:5000
```

---

# 📌 Rotas Principais

| Rota              | Método | Descrição                                       |
| ----------------- | ------ | ----------------------------------------------- |
| `/`               | GET    | Dashboard principal                             |
| `/upload`         | POST   | Importa arquivos `.log`, `.txt`, `.csv` e `.md` |
| `/analisar`       | GET    | Executa a análise inteligente dos logs          |
| `/inserir`        | POST   | Adiciona um novo registro                       |
| `/editar/<id>`    | GET    | Página de edição                                |
| `/atualizar/<id>` | POST   | Atualiza um registro                            |
| `/deletar/<id>`   | GET    | Remove um registro                              |

---

# 📊 Fluxo da Aplicação

```text
Arquivos (.log, .txt, .csv, .md)
                │
                ▼
         Importação dos Dados
                │
                ▼
        Banco de Dados SQLite
                │
        ┌───────┴────────┐
        ▼                ▼
 Dashboard Web      IA (Groq + LLaMA)
        │                │
        └───────┬────────┘
                ▼
      Análise Inteligente dos Logs
```

---

# 🎯 Objetivos do Projeto

Este projeto foi desenvolvido para consolidar conhecimentos em:

* Desenvolvimento Web com Flask
* Banco de Dados SQLite
* Operações CRUD
* Processamento e importação de arquivos
* Organização de logs de segurança
* Desenvolvimento de dashboards
* Integração com Inteligência Artificial
* Análise automatizada de eventos utilizando LLMs

---

# 🔮 Próximas Funcionalidades

* 📄 Exportação de relatórios em PDF
* 📊 Exportação de dados em Excel
* 🔔 Sistema de notificações em tempo real
* 🔗 Integração com plataformas SIEM
* 🗄️ Suporte a PostgreSQL e MySQL
* 📚 Histórico de análises realizadas pela IA
* ⚙️ Dashboard com métricas e widgets personalizáveis
* 📡 Monitoramento em tempo real via WebSockets
* 📈 Geração automática de indicadores de segurança

---

# 👨‍💻 Autor

**Marcos Rogato**

Projeto desenvolvido com foco em monitoramento, gerenciamento e análise inteligente de logs de segurança utilizando **Python**, **Flask**, **SQLite**, **Groq API** e modelos **LLaMA**.

---

## ⭐ Contribuições

Contribuições são bem-vindas!

Caso tenha sugestões de melhorias, encontre algum problema ou queira adicionar novas funcionalidades, sinta-se à vontade para abrir uma **Issue** ou enviar um **Pull Request**.


