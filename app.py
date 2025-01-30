from flask import Flask
from routes import api_routes
from flask_talisman import Talisman

app = Flask(__name__)

Talisman(app)
api_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
