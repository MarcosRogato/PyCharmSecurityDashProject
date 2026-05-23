# Security Dashboard

Dashboard web desenvolvido em Python com foco em monitoramento e gerenciamento de logs de segurança. O projeto permite importar logs, visualizar eventos em tempo real, realizar operações CRUD e organizar registros através de uma interface simples e intuitiva.

---

## 🚀 Funcionalidades

- Importação de arquivos `.log` para banco de dados SQLite
- Dashboard web com visualização dos logs
- CRUD completo de registros
- Filtro visual por categorias:
  - 🔴 ERROR
  - 🟡 WARNING
  - 🟢 INFO
- Inserção manual de novos logs
- Edição e exclusão de registros
- Interface inspirada em terminais de segurança

---

## 🛠 Tecnologias utilizadas

- Python 3.13
- Flask
- SQLite
- HTML5
- CSS3
- Jinja2

---

## 📂 Estrutura do projeto

```bash
Security-Dashboard/
│
├── app.py
├── database.py
├── database.db
├── logs_v2.log
│
└── templates/
    ├── index.html
    └── editar.html
```

---

## ▶️ Como executar o projeto

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/security-dashboard.git
```

Acesse a pasta do projeto:

```bash
cd security-dashboard
```

Instale as dependências:

```bash
pip install flask
```

Execute o servidor:

```bash
python app.py
```

Abra no navegador:

```bash
http://127.0.0.1:5000
```

---

## 📌 Rotas principais

| Rota | Método | Descrição |
|------|--------|------------|
| `/` | GET | Dashboard principal |
| `/importar` | GET | Importa logs para o banco |
| `/inserir` | POST | Adiciona novo log |
| `/editar/<id>` | GET | Página de edição |
| `/atualizar/<id>` | POST | Atualiza registro |
| `/deletar/<id>` | GET | Remove registro |

---

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido para praticar:

- Desenvolvimento web com Flask
- Integração com banco de dados SQLite
- Operações CRUD
- Organização de logs de segurança
- Estruturação de aplicações backend em Python

---

## 👨‍💻 Autor

Desenvolvido por **Marcos Rogato** 🚀