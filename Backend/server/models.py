from config import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin

# 🔐 MEMBER: Can be player, coach, executive, or just member
class Member(db.Model, SerializerMixin):
    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    role = db.Column(db.String, nullable=False)           # e.g., "player", "coach", "executive"
    status = db.Column(db.String, default="active")       # e.g., "active", "inactive"
    _password_hash = db.Column(db.String, nullable=False)

    players = db.relationship('Player', backref='member')
    coaches = db.relationship('Coach', backref='member')

    serialize_rules = ('-players', '-coaches', '-_password_hash',)

    def set_password(self, password):
        self._password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self._password_hash, password)


# 🏉 PLAYER: Linked to a member
class Player(db.Model, SerializerMixin):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Float, nullable=False)          # in cm
    weight = db.Column(db.Float, nullable=False)          # in kg
    position = db.Column(db.String)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))

    participations = db.relationship('MatchParticipant', backref='player')

    serialize_rules = ('-participations', '-member',)


# 🧠 COACH: Linked to a member
class Coach(db.Model, SerializerMixin):
    __tablename__ = 'coaches'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    specialty = db.Column(db.String)
    certification = db.Column(db.String)
    experience = db.Column(db.Integer, nullable=False)    # in years
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))

    serialize_rules = ('-member',)


# 📅 MATCH: A scheduled match
class Match(db.Model, SerializerMixin):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)           # e.g., "2025-07-01"
    time = db.Column(db.String, nullable=False)           # e.g., "15:00"
    venue = db.Column(db.String, nullable=False)
    score = db.Column(db.String, nullable=True)           # e.g., "15-10"
    status = db.Column(db.String, default="scheduled")    # e.g., "scheduled", "completed"

    participants = db.relationship('MatchParticipant', backref='match', cascade="all, delete-orphan")

    serialize_rules = ('-participants',)


# 🤝 MATCH PARTICIPANT: Player involvement in a match
class MatchParticipant(db.Model, SerializerMixin):
    __tablename__ = 'match_participants'

    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    score = db.Column(db.Integer, default=0)              # individual score
    minutes_played = db.Column(db.Integer, default=0)
    is_starting = db.Column(db.Boolean, default=True)
