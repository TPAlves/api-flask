from db import db  

class HeroModel(db.Model):
    table_name = 'heros'

    id = db.Column(db.Integer, primary_key=True)
    name_hero = db.Column(db.String(60), nullable=False, unique=True)
    name_civil = db.Column(db.String(60), nullable=False, unique=True)
    superpower = db.Column(db.String(60), nullable=False, unique=True)

    def __init__(self, name_hero, name_civil, superpower):
        self.name_hero = name_hero
        self.name_civil = name_civil
        self.superpower = superpower
    
    def __repr__(self):
        return f'HeroModel(Hero={self.name_hero}, Civil={self.name_civil}, SuperPower={self.superpower})'

    def json(self):
        return {
        'Hero': self.name_hero,
        'Civil': self.name_civil,
        'SuperPower': self.superpower
        }

    @classmethod 
    def find_by_hero(cls, hero):
        return cls.query.filter_by(name_hero=hero).first()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
    
    def delete_from_db(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            print(e)