from flask import Flask, Blueprint
from flask_restx import Api
import os

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint, doc='/doc', title='CRUD - Heros')
        self.app.register_blueprint(self.blueprint)


        self.app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('USER_DB')}:{os.getenv('PS_DB')}@localhost/heros"
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
        
        self.hero_ns = self.hero_ns()

    def hero_ns(self):
        return self.api.namespace(name='Heros', description='Flask API for Heros', path='/')


    def run(self):
        self.app.run(
            port=5000,
            debug=True,
            host='localhost'
        )


server = Server()