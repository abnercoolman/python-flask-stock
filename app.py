# Importação
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '4*q%0Da?2r#,'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

login_manager = LoginManager()
db = SQLAlchemy(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
CORS(app)

# Modelagem
# Usuário (id, username, password)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


# Produto (id, name, price, description)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

# Rotas
# Autenticação
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get("username")).first()
    if user and data.get("password") == user.password:
        login_user(user)
        return jsonify({"message": "Logado com sucesso."})
    return jsonify({"message": "Não autorizado! Credenciais inválidas."}), 401

# Deslogar
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Deslogado com sucesso."})

# Adicionar Produto
@app.route('/api/products/add', methods=['POST'])
@login_required
def add_product():
    data = request.json
    if 'name' in data and 'price' in data:
        product = Product(
            name=data['name'], price=data['price'], description=data.get('description', ''))
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Produto cadastrado com sucesso."})
    return jsonify({"message": "Dados do produto inválidos"}), 400

# Deletar Produto
@app.route('/api/products/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    # Recuperar o produto da base de dados
    # Verificar se o produto existe
    # Se existir, remover da base de dados
    # Se não existir, retornar 404 não encontrado
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Produto removido com sucesso"})
    return jsonify({"message": "Produto não encontrado"}), 404

# Recuperar detalhes de um Produto
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_details(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
        })
    return jsonify({"message": "Produto não encontrado"}), 404

# Atualizar detalhes de um Produto
@app.route('/api/products/update/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Produto não encontrado"}), 404

    data = request.json
    if 'name' in data:
        product.name = data['name']

    if 'price' in data:
        product.price = data['price']

    if 'description' in data:
        product.description = data['description']

    db.session.commit()
    return jsonify({"message": "Produto atualizado com sucesso."})

# Recuperar detalhes de todos os Produto
@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = []
    for product in products:
        product_data = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
        }
        product_list.append(product_data)
    return jsonify(product_list)

# Definir uma rota raiz (pagina incial) e a função que será executada ao requisitar
@app.route('/')
def index():
    return 'Olá, mundo!'


if __name__ == '__main__':
    app.run(debug=True, port=8080)
