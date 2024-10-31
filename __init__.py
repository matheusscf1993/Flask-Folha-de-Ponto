from flask import Flask
from dotenv import load_dotenv
import os
from routes import register_routes

def create_app():
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()  # Carrega as variáveis do .env para o ambiente

    app = Flask(__name__)

    # Configurações do Flask usando as variáveis de ambiente
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    app.config['DEBUG'] = os.getenv("DEBUG") == "True"  # Converte para booleano

    # Carregar as rotas
    register_routes(app)

    return app

