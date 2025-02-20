# 🛍️ API de E-commerce com Flask

## 📋 Sobre o Projeto
Este é um projeto de API RESTful para um e-commerce desenvolvido com Flask. A aplicação implementa funcionalidades essenciais de uma loja virtual, incluindo autenticação de usuários, gerenciamento de produtos e carrinho de compras.

## 🚀 Funcionalidades Principais

### 👤 Autenticação
- Sistema de login e logout de usuários
- Proteção de rotas com autenticação obrigatória
- Gerenciamento de sessões de usuário

### 📦 Gerenciamento de Produtos
- Cadastro de produtos
- Listagem completa do catálogo
- Visualização de detalhes individuais
- Atualização de informações
- Remoção de produtos

### 🛒 Carrinho de Compras
- Adição de produtos ao carrinho
- Remoção de itens
- Visualização do carrinho
- Processo de checkout

## 🛠️ Tecnologias Utilizadas
- **Flask**: Framework web em Python
- **SQLAlchemy**: ORM para banco de dados
- **Flask-Login**: Gerenciamento de autenticação
- **Flask-CORS**: Suporte a requisições cross-origin
- **SQLite**: Banco de dados relacional

## 🗄️ Estrutura do Banco de Dados

### Modelos:
- **User**: Armazena informações dos usuários
- **Product**: Cadastro de produtos
- **CartItem**: Gerencia itens no carrinho

## ⚙️ Instalação e Configuração

1. **Instale as dependências:**
```shell
pip3 install -r requirements.txt
```

2. **Configure o banco de dados:**

Abra o terminal Flask:
```shell
flask shell
```

Execute os comandos:
```shell
# Limpar banco de dados (se necessário)
db.drop_all()

# Criar tabelas
db.create_all()

# Criar usuário administrador
user = User(username="admin", password="123")
db.session.add(user)
db.session.commit()
```

3. **Inicie o servidor:**
```shell
python app.py
```
O servidor iniciará na porta 8080.

## 🔒 Endpoints da API

### Autenticação
- `POST /login`: Realiza login
- `POST /logout`: Realiza logout

### Produtos
- `GET /api/products`: Lista todos os produtos
- `GET /api/products/<id>`: Obtém detalhes de um produto
- `POST /api/products/add`: Adiciona novo produto
- `PUT /api/products/update/<id>`: Atualiza produto
- `DELETE /api/products/delete/<id>`: Remove produto

### Carrinho
- `GET /api/cart`: Visualiza carrinho
- `POST /api/cart/add/<product_id>`: Adiciona item ao carrinho
- `DELETE /api/cart/remove/<product_id>`: Remove item do carrinho
- `POST /api/cart/checkout`: Finaliza compra

## 👨‍💻 Autor
Abner Colman