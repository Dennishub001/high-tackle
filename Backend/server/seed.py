# seed.py

# Import your Flask app and models
from app import app
from models import db, Member, Player, Coach, Match, MatchParticipant
from datetime import datetime, timedelta
import random

# -------------------------------
# Step 1: Create Member accounts
# -------------------------------

def create_members():
    print("🌱 Creating club members...")

    member_info = [
        # Players
        {"username": "kipchoge_15", "phone": "254700123456", "email": "kipchoge@grassroots.ke", "role": "player"},
        {"username": "wanjiru_10", "phone": "254711234567", "email": "wanjiru@grassroots.ke", "role": "player"},
        {"username": "odhiambo_7", "phone": "254722345678", "email": "odhiambo@grassroots.ke", "role": "player"},
        {"username": "akoth_12", "phone": "254733456789", "email": "akoth@grassroots.ke", "role": "player"},
        {"username": "kamau_3", "phone": "254744567890", "email": "kamau@grassroots.ke", "role": "player"},

        # Coaches
        {"username": "coach_mwamba", "phone": "254755678901", "email": "mwamba@grassroots.ke", "role": "coach"},
        {"username": "coach_impala", "phone": "254766789012", "email": "impala@grassroots.ke", "role": "coach"},

        # Executive
        {"username": "manager_kenya", "phone": "254777890123", "email": "manager@grassroots.ke", "role": "executive"},
    ]

    members = []

    for info in member_info:
        member = Member(
            username=info["username"],
            phone=info["phone"],
            email=info["email"],
            role=info["role"],
            status="active"  # default for new members
        )
        # Set password using the method from your API
        default_password = "admin@123" if info["role"] == "executive" else "rugby@123"
        member.set_password(default_password)

        db.session.add(member)
        members.append(member)

    db.session.commit()
    print(f"✅ {len(members)} members created.\n")
    return members

# -------------------------------
# Step 2: Create Players
# -------------------------------

def create_players(members):
    print("🏉 Adding player profiles...")

    players_data = [
        {"name": "Eliud Kipchoge", "age": 22, "height": 182, "weight": 85, "position": "Fullback", "member": members[0]},
        {"name": "Grace Wanjiru", "age": 21, "height": 168, "weight": 65, "position": "Fly-half", "member": members[1]},
        {"name": "James Odhiambo", "age": 24, "height": 178, "weight": 92, "position": "Flanker", "member": members[2]},
        {"name": "Mercy Akoth", "age": 20, "height": 170, "weight": 68, "position": "Center", "member": members[3]},
        {"name": "Paul Kamau", "age": 23, "height": 185, "weight": 110, "position": "Prop", "member": members[4]},
    ]

    players = []

    for data in players_data:
        player = Player(
            name=data["name"],
            age=data["age"],
            height=data["height"],
            weight=data["weight"],
            position=data["position"],
            member_id=data["member"].id
        )
        db.session.add(player)
        players.append(player)

    db.session.commit()
    print(f"✅ {len(players)} players created.\n")
    return players

# -------------------------------
# Step 3: Create Coaches
# -------------------------------

def create_coaches(members):
    print("🧑‍🏫 Adding coaches...")

    coaches = [
        Coach(
            name="John Mwamba",
            specialty="Forwards",
            certification="Kenya Rugby Level 2",
            experience=8,
            member_id=members[5].id
        ),
        Coach(
            name="Sarah Impala",
            specialty="Backs",
            certification="Kenya Rugby Level 2",
            experience=6,
            member_id=members[6].id
        )
    ]

    db.session.add_all(coaches)
    db.session.commit()
    print(f"✅ {len(coaches)} coaches created.\n")
    return coaches

# -------------------------------
# Step 4: Create Matches
# -------------------------------

def create_matches():
    print("📅 Scheduling matches...")

    venues = [
        "Nairobi School Ground", "Kakamega Showground", 
        "Kisumu Polytechnic", "Mombasa Sports Club", 
        "Nakuru Athletic Club"
    ]
    opponents = [
        "Slums Rugby", "Village XV", "School Select", 
        "Community Warriors", "County Combined"
    ]

    matches = []

    for i in range(5):
        date = datetime.now() + timedelta(days=i * 14)
        is_past = i < 3  # mark first 3 as completed
        home_score = random.randint(10, 25)
        away_score = random.randint(10, 25)

        match = Match(
            date=date.strftime("%Y-%m-%d"),
            time="15:00",
            venue=f"{venues[i]} vs {opponents[i]}",
            status="completed" if is_past else "scheduled",
            score=f"{home_score}-{away_score}" if is_past else None
        )

        db.session.add(match)
        matches.append(match)

    db.session.commit()
    print(f"✅ {len(matches)} matches created.\n")
    return matches

# -------------------------------
# Step 5: Add Match Participants
# -------------------------------

def create_match_participants(players, matches):
    print("📊 Logging match performance stats...")

    sample_stats = [
        {"tries": 1, "conversions": 0, "penalties": 0, "tackles": 5, "meters_gained": 20, "turnovers_won": 1},
        {"tries": 0, "conversions": 1, "penalties": 0, "tackles": 3, "meters_gained": 15, "turnovers_won": 0},
        {"tries": 0, "conversions": 0, "penalties": 1, "tackles": 8, "meters_gained": 10, "turnovers_won": 2},
        {"tries": 2, "conversions": 0, "penalties": 0, "tackles": 4, "meters_gained": 40, "turnovers_won": 1},
        {"tries": 0, "conversions": 0, "penalties": 0, "tackles": 10, "meters_gained": 5, "turnovers_won": 1},
    ]

    participants = []

    for match in matches:
        for player in players:
            stats = random.choice(sample_stats) if match.status == "completed" else {k: 0 for k in sample_stats[0]}
            participant = MatchParticipant(
                match_id=match.id,
                player_id=player.id,
                minutes_played=random.choice([40, 50, 60]),
                is_starting=random.choice([True, False]),
                tries=stats["tries"],
                conversions=stats["conversions"],
                penalties=stats["penalties"],
                tackles=stats["tackles"],
                turnovers_won=stats["turnovers_won"]
            )
            db.session.add(participant)
            participants.append(participant)

    db.session.commit()
    print(f"✅ {len(participants)} match participants added.\n")
    return participants

# -------------------------------
# Run everything in order
# -------------------------------

def main():
    with app.app_context():
        print("🔄 Resetting database...")
        db.drop_all()
        db.create_all()

        members = create_members()
        players = create_players(members)
        coaches = create_coaches(members)
        matches = create_matches()
        create_match_participants(players, matches)

        print("🎉 Seeding complete! You are ready to use the High Tackle API.\n")

if __name__ == "__main__":
    main()
