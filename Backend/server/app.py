from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, Member, Player, Coach, Match, MatchParticipant




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rugby.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev-secret-key'

app = Flask(__name__)  


db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "High Tackle API running"})

# 🔐 Register a Member
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if Member.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already exists"}), 409

    member = Member(
        username=data['username'],
        phone=data['phone'],
        email=data['email'],
        role=data['role'],
        status="active"
    )
    member.set_password(data['password'])
    db.session.add(member)
    db.session.commit()
    return jsonify({"message": "Member registered successfully", "member": member.username}), 201

# 🔍 Get All Members
@app.route('/members', methods=['GET'])
def get_members():
    members = Member.query.all()
    return jsonify([{
        "id": m.id,
        "username": m.username,
        "phone": m.phone,
        "email": m.email,
        "role": m.role,
        "status": m.status
    } for m in members]), 200

# 🏉 Create a Player
@app.route('/players', methods=['POST'])
def create_player():
    data = request.get_json()
    player = Player(
        name=data['name'],
        age=data['age'],
        height=data['height'],
        weight=data['weight'],
        position=data.get('position'),
        member_id=data['member_id']
    )
    db.session.add(player)
    db.session.commit()
    return jsonify({"message": "Player created", "player": player.name}), 201

# 📋 Get All Players
@app.route('/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "age": p.age,
        "height": p.height,
        "weight": p.weight,
        "position": p.position,
        "member_id": p.member_id
    } for p in players]), 200

# 📅 Create Match
@app.route('/matches', methods=['POST'])
def create_match():
    data = request.get_json()
    match = Match(
        date=data['date'],
        time=data['time'],
        venue=data['venue'],
        status=data.get('status', 'scheduled'),
        score=data.get('score')
    )
    db.session.add(match)
    db.session.commit()
    return jsonify({"message": "Match created", "match_id": match.id}), 201

# 📆 Get All Matches
@app.route('/matches', methods=['GET'])
def get_matches():
    matches = Match.query.all()
    return jsonify([{
        "id": m.id,
        "date": m.date,
        "time": m.time,
        "venue": m.venue,
        "status": m.status,
        "score": m.score
    } for m in matches]), 200

# ➕ Add Player to Match
@app.route('/match-participants', methods=['POST'])
def add_match_participant():
    data = request.get_json()
    participant = MatchParticipant(
        match_id=data['match_id'],
        player_id=data['player_id'],
        score=data.get('score', 0),
        minutes_played=data.get('minutes_played', 0),
        is_starting=data.get('is_starting', True)
    )
    db.session.add(participant)
    db.session.commit()
    return jsonify({"message": "Player added to match"}), 201

# 📑 Get Match Participants
@app.route('/match-participants', methods=['GET'])
def get_match_participants():
    participants = MatchParticipant.query.all()
    return jsonify([{
        "id": mp.id,
        "match_id": mp.match_id,
        "player_id": mp.player_id,
        "score": mp.score,
        "minutes_played": mp.minutes_played,
        "is_starting": mp.is_starting
    } for mp in participants]), 200

if __name__ == '__main__':
    app.run(debug=True)
