from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from models import db, Member, Player, Match
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///hightackle.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Extensions
CORS(app)
migrate = Migrate(app, db)
db.init_app(app)

# Utils
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route('/')
def home():
    return jsonify({"message": "High Tackle API running"}), 200

#POST Register Member
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not is_valid_email(data.get('email', '')):
        return jsonify({"error": "Invalid email format"}), 400

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

#POST Player
@app.route('/players', methods=['POST'])
def create_player():
    data = request.get_json()

    try:
        age = int(data['age'])
        height = float(data['height'])
        weight = float(data['weight'])
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid age/height/weight"}), 400

    player = Player(
        name=data['name'],
        age=age,
        height=height,
        weight=weight,
        position=data.get('position'),
        member_id=data['member_id']
    )

    db.session.add(player)
    db.session.commit()

    return jsonify({"message": "Player created", "player": player.name}), 201

#POST Match
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

#GET Members
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

#GET All Players
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

#GET All Matches
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

#PATCH  Match
@app.route('/matches/<int:id>', methods=['PATCH'])
def update_match(id):
    match = Match.query.get(id)
    if not match:
        return jsonify({"error": "Match not found"}), 404
    data = request.get_json()
    if 'status' in data:
        match.status = data['status']
    if 'score' in data:
        match.score = data['score']
    db.session.commit()
    return jsonify({"message": "Match updated"}), 200

#PATCH Player
@app.route('/players/<int:id>', methods=['PATCH'])
def update_player(id):
    player = Player.query.get(id)
    if not player:
        return jsonify({"error": "Player not found"}), 404
    data = request.get_json()
    if 'position' in data:
        player.position = data['position']
    if 'height' in data:
        player.height = data['height']
    if 'weight' in data:
        player.weight = data['weight']
    db.session.commit()
    return jsonify({"message": "Player updated"}), 200

#DELETE Player
@app.route('/players/<int:id>', methods=['DELETE'])
def delete_player(id):
    player = Player.query.get(id)
    if not player:
        return jsonify({"error": "Player not found"}), 404
    db.session.delete(player)
    db.session.commit()
    return jsonify({"message": "Player deleted"}), 200

# DELETE Match
@app.route('/matches/<int:id>', methods=['DELETE'])
def delete_match(id):
    match = Match.query.get(id)
    if not match:
        return jsonify({"error": "Match not found"}), 404
    db.session.delete(match)
    db.session.commit()
    return jsonify({"message": "Match deleted"}), 200

if __name__ == "__main__":
    app.run(port=5555, debug=True)
