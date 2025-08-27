from flask import Flask, render_template
from products.controllers.product_controller import product_controller
from db.db import db
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DB_URI", "mysql+pymysql://root:root@db:3306/myflaskapp"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Registrando el blueprint del controlador de usuarios
app.register_blueprint(product_controller)

if __name__ == '__main__':
    app.run()
