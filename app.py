from flask import Flask
from routes import api_routes
from flask_talisman import Talisman
from flask_jwt_extended import JWTManager
from datetime import timedelta

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # This has to be strong
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
jwt = JWTManager(app)
Talisman(app)
api_routes(app, jwt)

if __name__ == '__main__':
    app.run(debug=True)
