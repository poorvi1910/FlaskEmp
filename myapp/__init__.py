from flask import Flask
from flask_talisman import Talisman
from flask_jwt_extended import JWTManager
from datetime import timedelta

def create_app():
    app = Flask(__name__)
    
    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # This has to be strong
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
    
    jwt = JWTManager(app)
    Talisman(app)
    
    from myapp.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app