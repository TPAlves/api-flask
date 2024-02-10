from flask import request
from flask_restx import Resource, fields
from models.hero import HeroModel
from schemas.hero import HeroSchema
from server.intance import server

hero_ns = server.hero_ns
hero_schema = HeroSchema()
hero_list_schema = HeroSchema(many=True)

message = 'Hero not found'

item = hero_ns.model('Hero', {
        'name_hero': fields.String(description='Hero name'),      
         'name_civil': fields.String(description='Civil name'),
         'superpower': fields.String(description='Super Power')
    })

class Hero(Resource):

    def get(self, id):
        hero_data = HeroModel.find_by_id(id)
        if hero_data:
            return hero_schema.dump(hero_data), 200
        return {'message': message}, 404
    
    @hero_ns.expect(item)
    @hero_ns.doc('Update Hero')
    def put(self, id):
        hero_data = HeroModel.find_by_id(id)
        json = request.get_json()

        hero_data.name_hero = json['name_hero']
        hero_data.name_civil = json['name_civil']
        hero_data.superpower = json['superpower']
    
        HeroModel.save_to_db(hero_data)
        return hero_schema.dump(hero_data), 200

    def delete(self, id):
        hero_data = HeroModel.find_by_id(id)
        if hero_data:
            hero_data.delete_from_db()
            return '', 204
        return {'message': message}, 404

class HeroList(Resource):

    def get(self):
        return hero_list_schema.dump(HeroModel.find_all()), 200 
    
    @hero_ns.expect(item)
    @hero_ns.doc('Add Hero')
    def post(self):
        json = request.get_json()
        data = hero_schema.load(json)
        HeroModel.save_to_db(data)
        
        return hero_schema.dump(data), 201