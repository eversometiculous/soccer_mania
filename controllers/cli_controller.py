from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.team_thread import Team_thread
from datetime import date
from models.team import Team
from models.comment import Comment
from sqlalchemy import text
from models.stadium import Stadium
from models.manager import Manager
from models.player import Player

# Creates commands tied to the blueprint instance. __name__ specifies the current module, which is cli_controller, where the blueprint
# is defined.
db_commands = Blueprint('db', __name__)

# Decorator created to define CLI commands, in this case, create. The decorator helps to register the create_db() function. 
# When running Flask CLI and using command flask db create, it executes the create_db() function.
@db_commands.cli.command('create')
def create_db():
    # It will create all the database tables defined in the application. 
    db.create_all()
    # Prints Tables Created after creating all the database tables to notify user process is done,
    print("Tables Created")

# Decorator created to define CLI commands, in this case, drop. The decorator helps to register the drop_db() function. 
# When running Flask CLI and using command flask db drop, it executes the drop_db() function.
@db_commands.cli.command('drop')
def drop_db():
    # It will drop/delete all the database tables and their corresponding data defined in the application. 
    db.drop_all()
    # After completing the process, tables dropped will be printed to notify user that theprocess is done.
    print("Tables dropped")

# Decorator created to define CLI commands, in this case, seed. The decorator helps to register the seed_db() function. 
# When running Flask CLI and using command flask db seed, it executes the seed_db() function.
@db_commands.cli.command('seed')
def seed_db():
    # Creates a new list in the database called teams that contains instances of Team models. Each element of the list is an attribute
    # of the Team model. The attributes are team_name and trophies_won.
    teams = [
        Team(
            team_name='Arsenal',
            trophies_won='Kent Senior Cup – 1889–90 (1), London Charity Cup – 1889–90 (1), London Challenge Cup – 1921–22, 1923–24, 1930–31, 1933–34, 1935–36, 1953–54, 1954–55, 1957–58, 1961–62, 1962–63, 1969–70 (11), London Senior Cup – 1890–91 (1), Inter-Cities Fairs Cup – 1969–70 (1), UEFA Cup Winners’ Cup – 1993–94 (1), FA Community Shield – 1930, 1931, 1933, 1934, 1938, 1948, 1953, 1991, 1998, 1999, 2002, 2004, 2014, 2015, 2017, 2020 (16), FA Cup – 1929–30, 1935–36, 1949–50, 1970–71, 1978–79, 1992–93, 1997–98, 2001–02, 2002–03, 2004–05, 2013–14, 2014–15, 2016-17, 2019-2020 (14), First Division (until 1992) and Premier League – 1930–31, 1932–33, 1933–34, 1934–35, 1937–38, 1947–48, 1952–53, 1970–71, 1988–89, 1990–91, 1997–98, 2001–02, 2003–04 (13), League Cup – 1986–87, 1992–93 (2), Mercantile Credit Centenary Trophy –  1988–89 (1), Southern Professional Floodlit Cup – 1958-59 (1)'
        ),
        Team(
            team_name='Manchester United',
            trophies_won='English 2nd Tier Champion - 1974-75,  1935-36 (2), Intercontinental Cup Winner - 1999-2000 (1), English Supercup Winner - 2016-17, 2013-14, 2011-12, 2010-11, 2008-09, 2007-08, 2003-04, 1997-98, 1996-97, 1994-95, 1993-94, 1990-91, 1983-84, 1977-78, 1967-68, 1965-66, 1957-58, 1956-57, 1952-53, 1911-12, 1908-09 (21), English League Cup Winner - 2022-23, 2016-17, 2009-10, 2008-09, 2005-06, 1991-92 (6), FA Cup Winner - 2015-16, 2003-04, 1998-99, 1995-96, 1993-94, 1989-90, 1984-85, 1982-83, 1976-77, 1962-63 , 1947-48, 1908-09 (12), Cup Winners Cup Winner - 1990-91 (1), Europa League Winner - 2016-17 (1), UEFA Supercup Winner - 1991-92 (1), English League Champions - 2012-13, 2010-11, 2008-09, 2007-08, 2006-07, 2002-03, 2000-01, 1999-00, 1998-99, 1996-97, 1995-96, 1993-94, 1992-93, 1966-67, 1964-65, 1956-57, 1955-56, 1951-52, 1910-11, 1907-08 (20), FIFA Club World Cup Winner - 2008-09 (1), European Champions Club Cup Winner - 1967-68 (1), Champions League Winner - 2007-08, 1998-99 (2)'
        ),
    ]

    # Adds all Team models and its elements and data to the database session. Added to the session to be saved(committed) later.
    db.session.add_all(teams)

    # Creates a new list in the database called users that contains instances of User models. Each element of the list is an attribute
    # of the User model. The attributes are name, email, username, password, is_admin, favourite_player and team.
    users = [
        User(
            name='Administrator',
            email='admin@admin.com',
            username='OGAdmin',
            password=bcrypt.generate_password_hash('admin123').decode('utf-8'),
            is_admin=True,
            favourite_player='Thierry Henry',
            team=teams[0]
        ),
        User(
            name='User1',
            email='user1@email.com',
            username='OGUser',
            password=bcrypt.generate_password_hash('user1pw').decode('utf-8'),
            favourite_player='Wayne Rooney',
            team=teams[0]
        ),
        User(
            name='User2',
            email='user2@email.com',
            username='ManUtdFan',
            password=bcrypt.generate_password_hash('user2pw').decode('utf-8'),
            favourite_player='Christiano Ronaldo',
            team=teams[1]
        )
    ]
    # Adds all User models and its element and data to the database session. Added to the session to be saved(committed) later.
    db.session.add_all(users)

    # Creates a new list in the database called team_threads that contains instances of Team_thread models. Each element of the list is an attribute
    # of the Team_thread model. The attributes are title, description, date, user and team.
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
    # Adds all Team_thread models and its elements and data to the database session. Added to the session to be saved(committed) later.
    db.session.add_all(team_threads)

    # Creates a new list in the database called stadiums that contains instances of Stadium models. Each element of the list is an attribute
    # of the Stadium model. The attributes are stadium_name, location. year_built and team.
    stadiums = [
        Stadium(
            stadium_name='Emirates Stadium',
            location='Ashburton Grove',
            year_built='2006',
            team=teams[0]
        ),
        Stadium(
            stadium_name='Old Trafford',
            location='Trafford',
            year_built='1910',
            team=teams[1]
        )
    ]

    # Adds all Stadium models and its elements and data to the database session. Added to the session to be saved(committed) later.
    db.session.add_all(stadiums)

    # Creates a new list in the database called managers that contains instances of Manager models. Each element of the list is an attribute
    # of the Manager model. The attributes are name, date_of_birth, teams_managed_previously, trophies_won and team.
    managers = [
        Manager(
            name='Mikel Arteta',
            date_of_birth=date(1982, 3, 26),
            teams_managed_previously='None',
            trophies_won='FA Cup Trophy - 2019-20 (1), FA Community Shield - 2020 (1)',
            team=teams[0]
        ),
        Manager(
            name='Erik Ten Hag',
            date_of_birth=date(1970, 2, 2),
            teams_managed_previously='Go Ahead Eagles - 2012-13, Bayern Munich II - 2013-15, Utrecht - 2015-17, Ajax - 2017-22',
            trophies_won='Regionalliga Bayern - 2013-14 (1), Eredivisie - 2018-19, 2020-21, 2021-22 (3), KNVB Cup - 2018-19, 2020-21 (2), Johan Cryuff Shield - 2019 (1), English League Cup - 2022-23 (1)',
            team=teams[1]
        )
    ]

    # Adds all Manager models and its elements and data to the database session. Added to the session to be saved(committed) later.
    db.session.add_all(managers)

    # Creates a new list in the database called players that contains instances of Player models. Each element of the list is an attribute
    # of the Player model. The attributes are name, date_of_birth, position, contract_period, current_salary and team.
    players = [
        Player(
            name='Bukayo Saka',
            date_of_birth=date(2001, 9, 5),
            position='Right Forward, midfielder, fullback',
            contract_period='2023-2027',
            current_salary='£300,000-per-week',
            team=teams[0]
        ),
        Player(
            name='Aaron Ramsdale',
            date_of_birth=date(1998, 5, 14),
            position='Goalkeeper',
            contract_period='2022-2026',
            current_salary='£120,000-per-week',
            team=teams[0]
        ),
        Player(
            name='Marcus Rashford',
            date_of_birth=date(1997, 10, 31),
            position='Forward',
            contract_period='2023-2028',
            current_salary='£300,000-per-week',
            team=teams[1]
        )
    ]

    # Adds all Player models and its elements and data to the database session. Added to the session to be saved(committed) later.
    db.session.add_all(players)

    # Creates a new list in the database called comments that contains instances of Comment models. Each element of the list is an attribute
    # of the Comment model. The attributes are message, team_thread, user and date.
    comments = [
        Comment(
            message="First post",
            user=users[0],
            team_thread=team_threads[0],
            date=date.today()
        ),
        Comment(
            message="Test post",
            user=users[1],
            team_thread=team_threads[1],
            date=date.today()
        ),
        Comment(
            message="Arsenal signed Declan Rice!!!",
            user=users[0],
            team_thread=team_threads[0],
            date=date.today()
        ),
        Comment(
            message="Out of topic, but how is everyone feeling about the Women's World Cup?",
            user=users[1],
            team_thread=team_threads[2],
            date=date.today()
        )
    ]

    # Adds all Comment models and its elements and data to the database session. Added to the session to be saved(committed) later.
    db.session.add_all(comments)

    # Commits all additions to the session to be saved into the database.
    db.session.commit()

    # Once the process is done, "Tables Seeded" will be printed to notify the user that the process is done.
    print("Tables Seeded")