from app import app
from models import db, Member, Player, Coach, Match, MatchParticipant
from werkzeug.security import generate_password_hash
import random
from datetime import datetime, timedelta

def create_members():
    members = [
        # Players
        Member(
            username="kipchoge_15",
            phone="254700123456",
            email="kipchoge@grassroots.ke",
            role="player",
            _password_hash=generate_password_hash("rugby@123")
        ),
        Member(
            username="wanjiru_10",
            phone="254711234567",
            email="wanjiru@grassroots.ke",
            role="player",
            _password_hash=generate_password_hash("rugby@123")
        ),
        Member(
            username="odhiambo_7",
            phone="254722345678",
            email="odhiambo@grassroots.ke",
            role="player",
            _password_hash=generate_password_hash("rugby@123")
        ),
        Member(
            username="akoth_12",
            phone="254733456789",
            email="akoth@grassroots.ke",
            role="player",
            _password_hash=generate_password_hash("rugby@123")
        ),
        Member(
            username="kamau_3",
            phone="254744567890",
            email="kamau@grassroots.ke",
            role="player",
            _password_hash=generate_password_hash("rugby@123")
        ),
        
        # Coaches
        Member(
            username="coach_mwamba",
            phone="254755678901",
            email="mwamba@grassroots.ke",
            role="coach",
            _password_hash=generate_password_hash("coach@123")
        ),
        Member(
            username="coach_impala",
            phone="254766789012",
            email="impala@grassroots.ke",
            role="coach",
            _password_hash=generate_password_hash("coach@123")
        ),
        
        # Team Manager
        Member(
            username="manager_kenya",
            phone="254777890123",
            email="manager@grassroots.ke",
            role="executive",
            _password_hash=generate_password_hash("admin@123")
        )
    ]
    
    db.session.add_all(members)
    db.session.commit()
    return members

def create_players(members):
    positions = [
        "Prop", "Hooker", "Lock", "Flanker", 
        "Number 8", "Scrum-half", "Fly-half",
        "Center", "Wing", "Fullback"
    ]
    
    players = [
        Player(
            name="Eliud Kipchoge",
            age=22,
            height=182.0,
            weight=85.0,
            position="Fullback",
            member_id=members[0].id
        ),
        Player(
            name="Grace Wanjiru",
            age=21,
            height=168.0,
            weight=65.0,
            position="Fly-half",
            member_id=members[1].id
        ),
        Player(
            name="James Odhiambo",
            age=24,
            height=178.0,
            weight=92.0,
            position="Flanker",
            member_id=members[2].id
        ),
        Player(
            name="Mercy Akoth",
            age=20,
            height=170.0,
            weight=68.0,
            position="Center",
            member_id=members[3].id
        ),
        Player(
            name="Paul Kamau",
            age=23,
            height=185.0,
            weight=110.0,
            position="Prop",
            member_id=members[4].id
        )
    ]
    
    db.session.add_all(players)
    db.session.commit()
    return players

def create_coaches(members):
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
    return coaches

def create_matches():
    matches = []
    venues = [
        "Nairobi School Ground", "Kakamega Showground", 
        "Kisumu Polytechnic", "Mombasa Sports Club",
        "Nakuru Athletic Club"
    ]
    opponents = [
        "Slums Rugby", "Village XV", "School Select",
        "Community Warriors", "County Combined"
    ]
    
    for i in range(1, 6):
        match_date = datetime.now() + timedelta(days=i*21) 
        is_completed = i < 3 
        

        home_score = random.randint(5, 25)
        away_score = random.randint(5, 25)
        
        matches.append(
            Match(
                date=match_date.strftime("%Y-%m-%d"),
                time="15:00",
                venue=f"{venues[i%5]} vs {opponents[i%5]}",
                status="completed" if is_completed else "scheduled",
                score=f"{home_score}-{away_score}" if is_completed else None
            )
        )
    
    db.session.add_all(matches)
    db.session.commit()
    return matches

def create_match_participants(players, matches):

    rugby_stats = [
        {"tries": 1, "conversions": 0, "penalties": 0, "tackles": 5, "meters_gained": 25, "turnovers_won": 1},
        {"tries": 0, "conversions": 1, "penalties": 0, "tackles": 3, "meters_gained": 15, "turnovers_won": 0},
        {"tries": 0, "conversions": 0, "penalties": 1, "tackles": 8, "meters_gained": 10, "turnovers_won": 2},
        {"tries": 0, "conversions": 0, "penalties": 0, "tackles": 10, "meters_gained": 5, "turnovers_won": 1},
        {"tries": 2, "conversions": 0, "penalties": 0, "tackles": 4, "meters_gained": 40, "turnovers_won": 1}
    ]
    
    participants = []
    
    for match in matches:
        for player in players:
            stats = random.choice(rugby_stats) if match.status == "completed" else {
                "tries": 0,
                "conversions": 0,
                "penalties": 0,
                "tackles": 0,
                "meters_gained": 0,
                "turnovers_won": 0
            }
            
            participants.append(
                MatchParticipant(
                    match_id=match.id,
                    player_id=player.id,
                    score=stats["tries"] * 5 + stats["conversions"] * 2 + stats["penalties"] * 3,
                    minutes_played=random.choice([40, 50, 60, 70]),
                    is_starting=random.choice([True, False]),
                    tries=stats["tries"],
                    conversions=stats["conversions"],
                    penalties=stats["penalties"],
                    tackles=stats["tackles"],
                    meters_gained=stats["meters_gained"],
                    turnovers_won=stats["turnovers_won"]
                )
            )
    
    db.session.add_all(participants)
    db.session.commit()
    return participants

def main():
    with app.app_context():
        print("Clearing db...")
        db.drop_all()
        db.create_all()
        
        print("Seeding members...")
        members = create_members()
        
        print("Seeding players...")
        players = create_players(members)
        
        print("Seeding coaches...")
        coaches = create_coaches(members)
        
        print("Seeding  matches...")
        matches = create_matches()
        
        print("Seeding match participants...")
        participants = create_match_participants(players, matches)
        
        print(" High tackle seeding complete!")

if __name__ == "__main__":
    main()