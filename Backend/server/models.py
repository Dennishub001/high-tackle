from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s"
})

db = SQLAlchemy(metadata=metadata)


class Member(db.Model, SerializerMixin):
    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    role = db.Column(db.String, nullable=False)          
    status = db.Column(db.String, default="active")    
    _password_hash = db.Column(db.String, nullable=False)

    
    player = db.relationship('Player', backref='member', uselist=False)
    coach = db.relationship('Coach', backref='member', uselist=False)

    serialize_rules = ('-player', '-coach', '-_password_hash',)

    @property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, value):
        self._password_hash = value

    def set_password(self, password):
        self._password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self._password_hash, password)



class Player(db.Model, SerializerMixin):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Float, nullable=False)          # in cm
    weight = db.Column(db.Float, nullable=False)          # in kg
    position = db.Column(db.String)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'), unique=True)  

    participations = db.relationship('MatchParticipant', backref='player', cascade="all, delete-orphan")

    serialize_rules = ('-participations', '-member',)


class Coach(db.Model, SerializerMixin):
    __tablename__ = 'coaches'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    specialty = db.Column(db.String)
    certification = db.Column(db.String)
    experience = db.Column(db.Integer, nullable=False)    # in years
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'), unique=True)  # 1-to-1

    serialize_rules = ('-member',)


class Match(db.Model, SerializerMixin):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)           
    time = db.Column(db.String, nullable=False)          
    venue = db.Column(db.String, nullable=False)
    score = db.Column(db.String, nullable=True)           
    status = db.Column(db.String, default="scheduled")    

    participants = db.relationship('MatchParticipant', backref='match', cascade="all, delete-orphan")

    serialize_rules = ('-participants',)


class MatchParticipant(db.Model, SerializerMixin):
    __tablename__ = 'match_participants'

    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), primary_key=True)
    minutes_played = db.Column(db.Integer, default=0)  
    tries = db.Column(db.Integer, default=0)
    is_starting = db.Column(db.Boolean, default=False)  
    conversions = db.Column(db.Integer, default=0)
    penalties = db.Column(db.Integer, default=0)
    tackles = db.Column(db.Integer, default=0)
    turnovers_won = db.Column(db.Integer, default=0)

    serialize_rules = ('-match', '-player',)