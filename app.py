from ma import ma 
from flask import jsonify 
from marshmallow import ValidationError
from db import db 
from server.intance import server
from controllers.hero import Hero, HeroList

api = server.api
app = server.app 


api.add_resource(Hero, '/heros/<int:id>')
api.add_resource(HeroList, '/heros')


if __name__ == '__main__':
    db.init_app(app)
    with app.test_request_context():
        db.create_all()
    ma.init_app(app)
    server.run()
