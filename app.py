# Importação
from flask import Flask

app = Flask(__name__)

# Definir uma rota raiz (pagina incial) e a função que será executada ao requisitar
@app.route('/')
def index():
    return 'Olá, mundo!'

if __name__ == '__main__':
    app.run(debug=True)
