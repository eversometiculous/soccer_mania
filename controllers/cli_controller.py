from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.team_thread import Team_thread
from datetime import date
from models.team import Team

db_commands = Blueprint('db', __name__)


@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables Created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables Dropped")

@db_commands.cli.command('seed')
def seed_db():
    users = [
        User(
            name='Administrator',
            email='admin@admin.com',
            username='OGAdmin',
            password=bcrypt.generate_password_hash('admin123').decode('utf-8'),
            is_admin=True
        ),
        User(
            name='User1',
            email='user1@email.com',
            username='OGUser',
            password=bcrypt.generate_password_hash('user1pw').decode('utf-8')
        ),
    ]

    db.session.add_all(users)

    teams = [
        Team(
            team_name='Arsenal',
            user=users[0]
        ),
        Team(
            team_name='Manchester United',
            user=users[1]
        ),
    ]

    db.session.add_all(teams)

    team_threads = [
        Team_thread(
            title='Arsenal Men transfer news',
            description='Anything related to Arsenal Men transfer news',
            date=date.today(),
            user=users[0],
            team=teams[0]
            # user_id=users[0].id
        ),
        Team_thread(
            title='Arsenal Men team upcoming matches',
            description='For anything related to upcoming matches for Arsenal Men',
            date=date.today(),
            user=users[0],
            team=teams[0]
        ),
        Team_thread(
            title='Arsenal Women transfer news',
            description='For anything related to Arsenal Women transfer news',
            date=date.today(),
            user=users[1],
            team=teams[0]
        ),
        Team_thread(
            title='Arsenal Women team upcoming matches',
            description='For anything related to upcoming matches for Arsenal Women',
            date=date.today(),
            user=users[1],
            team=teams[0]
        ),
    ]

    db.session.add_all(team_threads)
    db.session.commit()

    print("Tables Seeded")