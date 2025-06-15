#Importa Flask, la extensión de base de datos y la configuración.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

#Crea una instancia de SQLAlchemy sin enlazarla aún a la app (esto permite usarla globalmente en models.py).
db = SQLAlchemy()

# Esta función fabrica la app y le aplica la configuración (como la URL de la base de datos desde .env).
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    #Conecta la base de datos a esta app Flask.
    db.init_app(app)

    #Registro de rutas
    #Importa y registra las rutas desde routes.py usando un Blueprint (permite separar las rutas de forma ordenada).
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app