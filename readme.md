# Coder Academy - Soccer Mania API Project by Nasir Ruslan


## R1. Identification of the problem you are trying to solve by building this particular app.

There are many types of soccer forums that provide a place for fans of different soccer teams to come on and talk about anything related to their teams. Examples can be Reddit, Facebook, Twitter, Instagram and others. However, most of these platforms only provide a forum for fans to gather and discuss about any issues or news related to soccer, be it their team rosters, team schedules, team transfer news, upcoming opponent team rosters or tactics, the team tactics and other soccer-related matters. Others like Reddit do offer a way to view player stats, though this is only via clicking to view other links from the Reddit platform. Statistics are not really integrated into the platform. Furthermore, such statistics may be biased and not show the entire picture of recent team performances. Fans need to know the entire picture before they can make sound discussions, without having skewed statistics that may paint a different picture. As such, my application will be trying to solve this problem by providing an online forum that allows fans to view statistics that are relevant to their teams and players as well as other teams and players. As a matter of fact, the forum will be a small part of the overall application, which will put more emphasis on the statistics and ensuring the data is as accurate as possible. By doing this, this application will package everything a soccer fan needs to make valid discussions online and also help them analyse the data provided for their own personal needs.

## R2. Why is it a problem that needs solving?

It is a problem that needs solving because the current popular social platforms that fans use to hold discussions with their own team fans or fans of other teams often are very biased and not necessarily accurate. For example, Reddit works on upvotes making threads more visible. The thread may contain statistis about a certain player or team or anything football-related. However, users of Reddit will only upvote threads they like, and by relation, statistics that they find relevant to them. This, however, does not necessarily paint the correct picture of the soccer-related issue. The same can be said about Instagram, where users will follow certain people who post certain statistics that they find relevant, or Facebook, where posts that have more likes, will draw others to view those posts that has certain statistics as well as others like Twitter or Threads. An application where statistics can be accessed by any user and which cannot be modified except by the administrators will ensure that users will be able to make informed opinions about anything football-related and help them to have more meaningful discussions with other users. Users can also use these statistics that will be very thorough and detailed to help them make better analysis about anything football-related for their own personal use. This will help to stem issues such as useless information, skewed or fake statistics and fake news that is becoming more relevant due to the presence of popular social media.

## R3. Why have you chosen this database system. What are the drawbacks compared to others?


### The reason behind choosing PostgreSQL

The system I will be using is PostgreSQL or PSQL for short. I have chosen this database system since it has many features that I find to be useful for my application. Although my application might potentially contain a lot of data due to additional statistics that it will source from data from a third-party api, PSQL is scalable so it should not matter much. The features that PSQL possess is also something that I am after such as creating access tokens, jwt authentication, blueprints, functools and decorators, datetime module, bcrpyt, psycopg2, errorcodes and integrityerror, marshmallow and its validate function amd Flask. It also has integration with github and other third-party applications, which makes it useful for me. 

### PostgreSQL advantages

It is well-supported and is the most advanced open-source database system that is available. PostgreSQL is also easy to use and does not require much training. It has a long history of being developed(25 years). It has extensive functionality as well since it is open-source and very reliable. It also has good scalability(Advantages of PostgreSQL - CYBERTEC | Data Science & PostgreSQL n.d.). 

### PostgreSQL drawbacks compared to others

While PostgreSQL is open-source, it is not owned by any one organization so it is unable to become more featured compared to other paid database software systems. It also has some limitations when it comes to its database structure. It also has a slower performance when compared to other database management systems(DBMS). As the more data is stored inside its library, the slower the performance gets, even if it is scalable(Dhruv 2019).

#### Reference List:

1) Advantages of PostgreSQL - CYBERTEC | Data Science & PostgreSQL n.d., Cybertec, accessed 30 July 2023, <https://www.cybertec-postgresql.com/en/postgresql-overview/advantages-of-postgresql/>
2) Dhruv, S 2019, Pros and Cons of using PostgreSQL for Application Development, Aalpha., accessed 30 July 2023, <https://www.aalpha.net/blog/pros-and-cons-of-using-postgresql-for-application-development/>


## R4. Identify and discuss the key functionalities and benefits of an ORM


### What is ORM?

Object-relational Mapping or ORM for short, is a method of aligning programming code with database structures. It helps code find a way of storing data into databases, making programming a very useful tool when learning how to manipulate relational databases. ORM uses descriptors, created using metadata or code, to create a layer between programming and database structures, essentially acting as a middleman between those two parties. It is based on the idea of abstraction. ORM allows users to access and manipulate data objects without having to consider how those objects relate to their data sources.

### Key functionalities

One of the many advantages of using an ORM is that it allows the user to perform CRUD operations in relational databases without even using SQL. That makes it a huge advantage as the user need not possess the technical knowledge and terminology behind SQL to operate in a relational database.  This makes it very newbie-friendly to new users who want to step into the world of relational databases and performing vital CRUD - create, read, update, delete operations without knowing how to use SQL(What is object-relational mapping (ORM)? – TechTarget Definition n.d.).

ORMs generate objects which are then kept in database tables in the database system. Once the objects are up, users are able to access and manipulate the object fields easily. It makes accessing and manipulating object data easy without learning complex SQL queries. It has libraries that help it understand the code that we use to generate objects and map it to tables. As such, ORMs is very versatile and not limited to a specific language, making it very appealing to new users who might not want to invest time in learning a new language. Instead, users can invest time in making better code to have faster performances.

As ORMs make the application independent of the database system, it allows the user to write generic queries without relying on being connected to a database system. Furthermore, with ORMs, when migrating to a new database, ORMs make it much easier to interact with new databases easily without having to write new complex queries. The user can easily change databases with the application so long as he has ORMs and the generic queries written.

ORM will allow the user to manipulate data, big or small, with no restrictions or hassles. Other databases may have a lot of restrictions when it comes to accessing small datasets, manipulating them and recommitting them to the database. This makes ORM more appealing(What is ORM? | How ORM Works? | A Quick Glance of ORM Features 2020).

#### Reference List

1) What is object-relational mapping (ORM)? – TechTarget Definition n.d., TheServerSide.com, accessed 30 July 2023, <https://www.theserverside.com/definition/object-relational-mapping-ORM#:~:text=ORM%20uses%20metadata%20descriptors%20to>.
2) What is ORM? | How ORM Works? | A Quick Glance of ORM Features 2020, EDUCBA, accessed 30 Jul 2023, <https://www.educba.com/what-is-orm/>


## R5. Document all endpoints for your API

### user_controller.py - @users_bp.route('/')

This endpoint route has the function get_all_users().
As indicated in the function, it is using the GET request or READ in CRUD.
It requires the User models in the database and all the data it has in those models. The function will query at the back-end, which is the database system, all the User models and their relevant data and then arranges the User models by descending order of their ids. 
The function will then execute the query and then return the results as a list of user objects, arranged by descending order of their ids. Finally, the function will serialize the list of user objects using users_schema and return as a JSON response to the front-end for the viewer to view in JSON format.

### user_controller.py - @users_bp.route('/<int:id>')

This endpoint route has the function get_one_user(id).
As indicated in the function, it is using the GET request or READ in CRUD.
It again requires the User models in the database and all the data tied to the User models. The function will query at the back-end, which is the database system, all the User models and their relevant data. The query will be to look for a specific user id which matches the <int:id> that was indicated at the front end when the query was made. 
The function will then return the result as a single user object using db.session.scalar(). The function will check if the user id matches the query made. 
If there is a match, it will serialize the user object using user_schema and return to the front end a JSON response for the viewer to see in JSON format. 
Otherwise, if there is no user id that matches the query id made, the back-end will return an error message that says there is no user with that id in the database system, along with an status code 404.

### team_thread_controller.py - @team_threads_bp.route('/')

This endpoint route has the function get_all_team_threads().
As indicated in the function, it is using the GET request or READ in CRUD.
It requires the Team_thread models in the database and all the data it has in those models. The function will query at the back-end, which is the database system, all the Team_thread models and their relevant data and then arranges the Team_thread models by descending order of their ids. 
The function will then execute the query and then return the results as a list of team_thread objects, arranged by descending order of their ids. 
Finally, the function will serialize the list of team_thread objects using team_threads_schema and return as a JSON response to the front-end for the viewer to view in JSON format.

### team_thread_controller.py - @team_threads_bp.route('/<int:id>')

This endpoint route has the function get_one_team_thread().
As indicated in the function, it is using the GET request or READ in CRUD.
It again requires the Team_thread models in the database and all the data tied to the Team_thread models. The function will query at the back-end, which is the database system, all the Team_thread models and their relevant data. The query will be to look for a specific team_thread id which matches the <int:id> that was indicated at the front end when the query was made. The function will then return the result as a single team_thread object using db.session.scalar(). 
The function will check if the team_thread id matches the query made. If there is a match, it will serialize the team_thread object using team_thread_schema and return to the front end a JSON response for the viewer to see in JSON format. 
Otherwise, if there is no team_thread id that matches the query id made, the back-end will return an error message that says there is no team_thread with that id in the database system, along with an error code 404.

### team_thread_controller.py - @team_threads_bp.route('/', methods=['POST'])

This endpoint route has the function create_team_thread().
As indicated in the function, it is using the POST request or CREATE in CRUD.
The function requires a valid JWT token. The user must first log in and display his JWT token as a bearer token to show that he is logged in, if he wants to perform this operation. This is done by the decorator function @jwt_required. 
The function will first change the JSON input that was received from the front end and make it readable by the database by changing it using Marshmallow into a readable Python type. This process is known as deserialization. The data is stored as body_data. 
The function then gets the user_id from the JWT token. When a user logins, he generates a JWT token, which the function can use to verify the user is in the database and retrieve the user_id. It will then query the database(back-end) for the user object based on the user_id and retrieve it. 
If the function is unable to retrieve the user object because the user_id does not exist, it returns an error saying the user is not found with status code 404. 
It also performs a check to see if the user has a team associated with it and if there is no team, it returns an error saying user team not found with status code 404. 
If those conditional checks pass, it will then start to create a new Team_thread model instance in the database by using the body_data to fill the appropriate fields. The title of the team_thread will be filled up with the body_data's title which is done with body_data.get('title'). The description of the team_thread will be filled up with the body_data's description which is done with body_data.get('description'). The date field will be set to the current date, obtained using the date.today() function from the datetime module. The function will then fill up the user field of the Team_thread model instance with the user who created the team_thread. The team field of the Team_thread instance will be filled up with the team of the user who created the team_thread. 
Afterwards, the db.session.add(team_thread) will add the new Team_thread model instance to the session, and the commit will insert and save it into the database. The newly created Team_thread model instance is then serialized using Marshmallow and changed into a JSON response which is viewable at the front-end as a JSON format, with status code 201.

### team_thread_controller.py - @team_threads_bp.route('/<int:id>', methods=['DELETE'])

This endpoint route has the function delete_one_team_thread().
As indicated in the function, it is using the DELETE request, same in CRUD.
The function requires a valid JWT token. The user must first log in and display his JWT token as a bearer token to show that he is logged in, if he wants to perform this operation. This is done by the decorator function @jwt_required. 
The function gets the user_id from the JWT token. When a user logins, he generates a JWT token, which the function can use to verify the user is in the database and retrieve the user_id. It will then query the database(back-end) for the user object based on the user_id and retrieve it. 
The function then queries the back-end for the team_thread id that matches the <int:id> sent by the front-end user. The result is stored as a single team_thread object. 
If there is a match, it goes to the next check. The function checks if the id of the user object matches the team_thread.user_id or if the user.is_admin is True, which is one of the fields of the User model(default is false). 
If it passes this check as well, the team_thread is deleted based on its team_thread id and gives a message saying the team thread with its title has been deleted successfully. 
If the id of the user object does not match the team_thread.user_id or if the user.is_admin is False, then an error message is given, which says that only the admin or the user who created the team_thread can delete the team_thread, with status code 403. If the first check, which is to check whether there is a team_thread id that matches the <int:id> fails, then the error message is returned to the front-end saying that there is no team_thread with that id and hence, it cannot be deleted, with status code 404.

### team_thread_controller.py - @team_threads_bp.route('/<int:id>', methods=['PUT', 'PATCH'])

This endpoint route has the function update_one_team_thread().
As indicated in the function, it is using the PUT or PATCH request, known as UPDATE in CRUD.
The function requires a valid JWT token. The user must first log in and display his JWT token as a bearer token to show that he is logged in, if he wants to perform this operation. This is done by the decorator function @jwt_required. 
The function will first change the JSON input that was received from the front end and make it readable by the database by changing it using Marshmallow into a readable Python type. This process is known as deserialization. The data is stored as body_data. The partial=True argument indicates that not all fields must be filled in the JSON input as some fields can be missing and the function will still perform the deserialization process. 
The function then gets the user_id from the JWT token. When a user logins, he generates a JWT token, which the function can use to verify the user is in the database and retrieve the user_id. It will then query the database(back-end) for the user object based on the user_id and retrieve it. 
The function then queries the back-end for the team_thread id that matches the <int:id> sent by the front-end user. The result is stored as a single team_thread object. 
If there is a match, it goes to the next check. The function checks if the id of the user object matches the team_thread.user_id. 
If there is no match, then the error message will show up saying only the user who created the team_thread can update the team_thread, with the status code 403. 
If there is a match for the second check(id of user object matches team_thread_user_id), the function will continue as per normal. It will then start to update the exisiting Team_thread model instance with that user_id in the database by using the body_data to fill the indicated fields that have data. For example, the title of the team_thread will be filled up with the body_data's title which is done with body_data.get('title') if the body data has the title field filled. If not, the following code 'or team_thread.title' sets the team_thread.title field to the existing data in the database for team_thread.title. The function does this with the other fields of the body_data and fills up the attributes in the Team_thread model accordingly. The date field will be set to the current date, obtained using the date.today() function from the datetime module. This will show when the team_thread was updated. 
The function will then commit the newly updated Team_thread model instance to be re-inserted into the database and saved. The newly updated Team_thread model instance is then serialized using Marshmallow and changed into a JSON response which is viewable at the front-end as a JSON format. 
If the check where team_thread id matches the <int:id> fails, the error message shows up saying the team_thread with that id does not exist and cannot be updated with status code 404.

### team_controller.py - @teams_bp.route('/')

This endpoint route has the function get_all_teams().
As indicated in the function, it is using the GET request, or READ in CRUD.
It requires the Team models in the database and all the data it has in those models. The function will query at the back-end, which is the database system, all the Team models and their relevant data and then arranges the Team models by descending order of their ids. 
The function will then execute the query and then return the results as a list of team objects, arranged by descending order of their ids. Finally, the function will serialize the list of team objects using teams_schema and return as a JSON response to the front-end for the viewer to view in JSON format.

### team_controller.py - @teams_bp.route('/<int:id>')

This endpoint route has the function get_one_team(id).
As indicated in the function, it is using the GET request, or READ in CRUD.
It again requires the Team models in the database and all the data tied to the Team models. The function will query at the back-end, which is the database system, all the Team models and their relevant data. The query will be to look for a specific team id which matches the <int:id> that was indicated at the front end when the query was made. 
The function will then return the result as a single team object using db.session.scalar(). 
The function will check if the team id matches the query made. 
If there is a match, it will serialize the team object using team_schema and return to the front end a JSON response for the viewer to see in JSON format. 
Otherwise, if there is no team id that matches the query id made, the back-end will return an error message that says there is no team with that id in the database system, along with an status code 404.

### team_controller.py - @teams_bp.route('/', methods=['POST'])

This endpoint route has the function create_team().
As indicated in the function, it is using the POST request or CREATE in CRUD.
The function requires a valid JWT token. The user must first log in and display his JWT token as a bearer token to show that he is logged in, if he wants to perform this operation. This is done by the decorator function @jwt_required. 
The function will first change the JSON input that was received from the front end and make it readable by the database by changing it using Marshmallow into a readable Python type. This process is known as deserialization. The data is stored as body_data. 
It will then start to create a new Team model instance in the database by using the body_data to fill the appropriate fields. For example, the team_name of the team will be filled up with the body_data's team_name which is done with body_data.get('team_name'). The fields that will be filled up are team_name and trophies_won. 
Afterwards, the db.session.add(team) will add the new Team model instance to the session, and the commit will insert and save it into the database. The newly created Team model instance is then serialized using Marshmallow and changed into a JSON response which is viewable at the front-end as a JSON format, with a 201 status code.

### team_controller.py - @teams_bp.route('/<int:id>', methods=['DELETE']) 

This endpoint route has the function delete_one_team(id).
As indicated in the function, it is using the DELETE request, same in CRUD.
The function requires a valid JWT token. The user must first log in and display his JWT token as a bearer token to show that he is logged in, if he wants to perform this operation. This is done by the decorator function @jwt_required. 
The function gets the user_id from the JWT token. When a user logins, he generates a JWT token, which the function can use to verify the user is in the database and retrieve the user_id. It will then query the database(back-end) for the user object based on the user_id and retrieve it. 
The function will then check to see if the is_admin field is True for the User model instance it retrieved from the database. 
If so, it will execute the decorated function with its arguments and key word arguments. 
If not, the backend will return to the front end an error message saying that only admins are able to perform this action with a status code 403. This is performed by the decorator function known as @authorise_as_admin. 
The function then queries the back-end for the team id that matches the <int:id> sent by the front-end user. The result is stored as a single team object. 
If there is a match, the team is then deleted based on its team id and gives a message saying the team with its team_name has been deleted successfully. 
If there is no match, then the error message is returned to the front-end saying that there is no team with that id and hence, it cannot be deleted, with status code 404.

### team_controller.py - @teams_bp.route('/<int:id>', methods=['PUT', 'PATCH'])

This endpoint route has the function update_one_team(id).
As indicated in the function, it is using the PUT or PATCH request, known as UPDATE in CRUD.
The function requires a valid JWT token. The user must first log in and display his JWT token as a bearer token to show that he is logged in, if he wants to perform this operation. This is done by the decorator function @jwt_required. 
The function gets the user_id from the JWT token. When a user logins, he generates a JWT token, which the function can use to verify the user is in the database and retrieve the user_id. It will then query the database(back-end) for the user object based on the user_id and retrieve it. 
The function will then check to see if the is_admin field is True for the User model instance it retrieved from the database. 
If so, it will execute the decorated function with its arguments and key word arguments. 
If not, the backend will return to the front end an error message saying that only admins are able to perform this action with a status code 403. This is performed by the decorator function known as @authorise_as_admin. 
The function will then first change the JSON input that was received from the front end and make it readable by the database by changing it using Marshmallow into a readable Python type. This process is known as deserialization. The data is stored as body_data. The partial=True argument indicates that not all fields must be filled in the JSON input as some fields can be missing and the function will still perform the deserialization process. 
The function then queries the back-end for the team id that matches the <int:id> sent by the front-end user. The result is stored as a single team object. If there is a match, it will then start to update the existing Team model instance by using the body_data to fill the indicated fields that have data. For example, the team_name of the team will be filled up with the body_data's team_name which is done with body_data.get('team_name') if the body data has the team_name field filled. If not, the following code 'or team.team_name' sets the team.team_name field to the existing data in the database for team.team_name. The function does this with the other fields of the body_data and fills up the attributes in the Team model accordingly. The attributes are team_name and trophies_won. 
The function will then commit the newly updated Team model instance to be re-inserted into the database and saved. The newly updated Team model instance is then serialized using Marshmallow and changed into a JSON response which is viewable at the front-end as a JSON format. 
If the check where team id matches the <int:id> fails, the error message shows up saying the team with that id does not exist and cannot be updated with status code 404.

### stadium_controller.py - @stadiums_bp.route('/')

This endpoint route has the function get_all_stadiums().
As indicated in the function, it is using the GET request, or READ in CRUD.
It requires the Stadium models in the database and all the data it has in those models. The function will query at the back-end, which is the database system, all the Stadium models and their relevant data and then arranges the Stadium models by descending order of their ids. 
The function will then execute the query and then return the results as a list of stadium objects, arranged by descending order of their ids. Finally, the function will serialize the list of stadium objects using stadiums_schema and return as a JSON response to the front-end for the viewer to view in JSON format.

### stadium_controller.py - @stadiums_bp.route('/<int:id>')

This endpoint route has the function get_one_stadium(id).
As indicated in the function, it is using the GET request, or READ in CRUD.
It again requires the Stadium models in the database and all the data tied to the Stadium models. The function will query at the back-end, which is the database system, all the Stadium models and their relevant data. 
The query will be to look for a specific stadium id which matches the <int:id> that was indicated at the front end when the query was made. The function will then return the result as a single stadium object using db.session.scalar(). 
The function will check if the stadium id matches the query made. 
If there is a match, it will serialize the stadium object using stadium_schema and return to the front end a JSON response for the viewer to see in JSON format. 
Otherwise, if there is no stadium id that matches the query id made, the back-end will return an error message that says there is no existing stadium with that id in the database system, along with an status code 404.

### stadium_controller.py - @stadiums_bp.route('/', methods=['POST'])

This endpoint route has the function create_stadium().
As indicated in the function, it is using the POST request, known as CREATE in CRUD.
The function requires a valid JWT token. The user must first log in and display his JWT token as a bearer token to show that he is logged in, if he wants to perform this operation. This is done by the decorator function @jwt_required. 
The function will first change the JSON input that was received from the front end and make it readable by the database by changing it using Marshmallow into a readable Python type. This process is known as deserialization. The data is stored as body_data. 
It will then start to create a new Stadium model instance in the database by using the body_data to fill the appropriate fields. For example, the stadium_name of the stadium will be filled up with the body_data's stadium_name which is done with body_data.get('stadium_name'). The fields that will be filled up are stadium_name, location, year_built and team. 
Afterwards, the db.session.add(stadium) will add the new Stadium model instance to the session, and the commit will insert and save it into the database. The newly created Stadium model instance is then serialized using Marshmallow and changed into a JSON response which is viewable at the front-end as a JSON format, with a 201 status code.

### stadium_controller.py - @stadiums_bp.route('/<int:id>', methods=['DELETE'])

This endpoint route has the function delete_one_stadium(id).
As indicated in the function, it is using the DELETE request, the same in CRUD.
The function requires a valid JWT token. The user must first log in and display his JWT token as a bearer token to show that he is logged in, if he wants to perform this operation. This is done by the decorator function @jwt_required. 
The function gets the user_id from the JWT token. When a user logins, he generates a JWT token, which the function can use to verify the user is in the database and retrieve the user_id. It will then query the database(back-end) for the user object based on the user_id and retrieve it. 
The function will then check to see if the is_admin field is True for the User model instance it retrieved from the database. 
If so, it will execute the decorated function with its arguments and key word arguments. 
If not, the backend will return to the front end an error message saying that only admins are able to perform this action with a status code 403. This is performed by the decorator function known as @authorise_as_admin. 
The function then queries the back-end for the stadium id that matches the <int:id> sent by the front-end user. The result is stored as a single stadium object. 
If there is a match, the stadium is then deleted based on its stadium id and gives a message saying the stadium with its stadium_name has been deleted successfully. 
If there is no match, then the error message is returned to the front-end saying that there is no stadium with that id and hence, it cannot be deleted, with status code 404.

### stadium_controller.py - @stadiums_bp.route('/<int:id>', methods=['PUT', 'PATCH'])

This endpoint route has the function update_one_stadium(id).
As indicated in the function, it is using the PUT or PATCH request, known as UPDATE in CRUD.
The function requires a valid JWT token. The user must first log in and display his JWT token as a bearer token to show that he is logged in, if he wants to perform this operation. This is done by the decorator function @jwt_required. 
The function gets the user_id from the JWT token. When a user logins, he generates a JWT token, which the function can use to verify the user is in the database and retrieve the user_id. 
It will then query the database(back-end) for the user object based on the user_id and retrieve it. 
The function will then check to see if the is_admin field is True for the User model instance it retrieved from the database. 
If so, it will execute the decorated function with its arguments and key word arguments. 
If not, the backend will return to the front end an error message saying that only admins are able to perform this action with a status code 403. This is performed by the decorator function known as @authorise_as_admin. 
The function will then first change the JSON input that was received from the front end and make it readable by the database by changing it using Marshmallow into a readable Python type. This process is known as deserialization. The data is stored as body_data. The partial=True argument indicates that not all fields must be filled in the JSON input as some fields can be missing and the function will still perform the deserialization process. 
The function then queries the back-end for the stadium id that matches the <int:id> sent by the front-end user. The result is stored as a single stadium object. 
If there is a match, it will then start to update the existing stadium model instance by using the body_data to fill the indicated fields that have data. For example, the stadium_name of the stadium will be filled up with the body_data's stadium_name which is done with body_data.get('stadium_name') if the body data has the stadium_name field filled. If not, the following code 'or stadium.stadium_name' sets the stadium.stadium_name field to the existing data in the database for stadium.stadium_name. The function does this with the other fields of the body_data and fills up the attributes in the Stadium model accordingly. The attributes are stadium_name, location, year_built and team. 
The function will then commit the newly updated Stadium model instance to be re-inserted into the database and saved. The newly updated Stadium model instance is then serialized using Marshmallow and changed into a JSON response which is viewable at the front-end as a JSON format. 
If the check where stadium id matches the <int:id> fails, the error message shows up saying the stadium with that id does not exist and cannot be updated with status code 404.

### player_controller.py - @players_bp.route('/')

This endpoint route has the function get_all_players().
As indicated in the function, it is using the GET request, or READ in CRUD.
It requires the Player models in the database and all the data it has in those models. The function will query at the back-end, which is the database system, all the Player models and their relevant data and then arranges the Player models by descending order of their ids. 
The function will then execute the query and then return the results as a list of player objects, arranged by descending order of their ids. Finally, the function will serialize the list of player objects using players_schema and return as a JSON response to the front-end for the viewer to view in JSON format.

### player_controller.py - @players_bp.route('/<int:id>')

This endpoint route has the function get_one_player(id).
As indicated in the function, it is using the GET request, or READ in CRUD.
It again requires the Player models in the database and all the data tied to the Player models. The function will query at the back-end, which is the database system, all the Player models and their relevant data. The query will be to look for a specific player id which matches the <int:id> that was indicated at the front end when the query was made. 
The function will then return the result as a single player object using db.session.scalar(). The function will check if the player id matches the query made. 
If there is a match, it will serialize the player object using player_schema and return to the front end a JSON response for the viewer to see in JSON format. 
Otherwise, if there is no player id that matches the query id made, the back-end will return an error message that says there is no existing player with that id in the database system, along with an status code 404.

### player_controller.py - @players_bp.route('/', methods=['POST'])

This endpoint route has the function create_player().
As indicated in the function, it is using the POST request, known as CREATE in CRUD.
The function requires a valid JWT token. The user must first log in and display his JWT token as a bearer token to show that he is logged in, if he wants to perform this operation. This is done by the decorator function @jwt_required. 
The function will first change the JSON input that was received from the front end and make it readable by the database by changing it using Marshmallow into a readable Python type. This process is known as deserialization. The data is stored as body_data. 
It will then start to create a new Player model instance in the database by using the body_data to fill the appropriate fields. For example, the name field of the player will be filled up with the body_data's name which is done with body_data.get('name'). The fields that will be filled up are name, date_of_birth, position, contract_period, current_salary and team. 
Afterwards, the db.session.add(player) will add the new Player model instance to the session, and the commit will insert and save it into the database. The newly created Player model instance is then serialized using Marshmallow and changed into a JSON response which is viewable at the front-end as a JSON format, with a 201 status code.

### player_controller.py - @players_bp.route('/<int:id>', methods=['DELETE'])

This endpoint route has the function delete_one_player(id).
As indicated in the function, it is using the DELETE request, the same in CRUD.
The function requires a valid JWT token. The user must first log in and display his JWT token as a bearer token to show that he is logged in, if he wants to perform this operation. This is done by the decorator function @jwt_required. 
The function gets the user_id from the JWT token. When a user logins, he generates a JWT token, which the function can use to verify the user is in the database and retrieve the user_id. 
It will then query the database(back-end) for the user object based on the user_id and retrieve it. 
The function will then check to see if the is_admin field is True for the User model instance it retrieved from the database. 
If so, it will execute the decorated function with its arguments and key word arguments. 
If not, the backend will return to the front end an error message saying that only admins are able to perform this action with a status code 403. This is performed by the decorator function known as @authorise_as_admin. 
The function then queries the back-end for the player id that matches the <int:id> sent by the front-end user. The result is stored as a single player object. 
If there is a match, the player is then deleted based on its player id and gives a message saying the player with its name has been deleted successfully. 
If there is no match, then the error message is returned to the front-end saying that there is no player with that id and hence, it cannot be deleted, with status code 404.

### player_controller.py - @players_bp.route('/<int:id>', methods=['PUT', 'PATCH'])

This endpoint route has the function update_one_player(id).
As indicated in the function, it is using the PUT or PATCH request, known as UPDATE in CRUD.
The function requires a valid JWT token. The user must first log in and display his JWT token as a bearer token to show that he is logged in, if he wants to perform this operation. This is done by the decorator function @jwt_required. 
The function gets the user_id from the JWT token. When a user logins, he generates a JWT token, which the function can use to verify the user is in the database and retrieve the user_id. 
It will then query the database(back-end) for the user object based on the user_id and retrieve it. 
The function will then check to see if the is_admin field is True for the User model instance it retrieved from the database. 
If so, it will execute the decorated function with its arguments and key word arguments. 
If not, the backend will return to the front end an error message saying that only admins are able to perform this action with a status code 403. This is performed by the decorator function known as @authorise_as_admin. 
The function will then first change the JSON input that was received from the front end and make it readable by the database by changing it using Marshmallow into a readable Python type. This process is known as deserialization. The data is stored as body_data. The partial=True argument indicates that not all fields must be filled in the JSON input as some fields can be missing and the function will still perform the deserialization process. 
The function then queries the back-end for the player id that matches the <int:id> sent by the front-end user. The result is stored as a single player object. 
If there is a match, it will then start to update the existing Player model instance by using the body_data to fill the indicated fields that have data. For example, the name field of the player will be filled up with the body_data's name which is done with body_data.get('name') if the body data has the name field filled. If not, the following code 'or player.name' sets the player.name field to the existing data in the database for player.name. The function does this with the other fields of the body_data and fills up the attributes in the Player model accordingly. The attributes are name, date_of_birth, position, contract_period, current_salary and team.
The function will then commit the newly updated Player model instance to be re-inserted into the database and saved. The newly updated Player model instance is then serialized using Marshmallow and changed into a JSON response which is viewable at the front-end as a JSON format.
If the check where player id matches the <int:id> fails, the error message shows up saying the player with that id does not exist and cannot be updated with status code 404.

### manager_controller.py - @managers_bp.route('/')

This endpoint route has the function get_all_managers().
As indicated in the function, it is using the GET request, or READ in CRUD.
It requires the Manager models in the database and all the data it has in those models. The function will query at the back-end, which is the database system, all the Manager models and their relevant data and then arranges the Manager models by descending order of their ids. 
The function will then execute the query and then return the results as a list of manager objects, arranged by descending order of their ids. 
Finally, the function will serialize the list of manager objects using managers_schema and return as a JSON response to the front-end for the viewer to view in JSON format.

### manager_controller.py - @managers_bp.route('/<int:id>')

This endpoint route has the function get_one_manager().
As indicated in the function, it is using the GET request, or READ in CRUD.
It again requires the Manager models in the database and all the data tied to the Manager models. The function will query at the back-end, which is the database system, all the Manager models and their relevant data. The query will be to look for a specific manager id which matches the <int:id> that was indicated at the front end when the query was made. 
The function will then return the result as a single manager object using db.session.scalar(). 
The function will check if the manager id matches the query made. 
If there is a match, it will serialize the manager object using manager_schema and return to the front end a JSON response for the viewer to see in JSON format. 
Otherwise, if there is no manager id that matches the query id made, the back-end will return an error message that says there is no existing manager with that id in the database system, along with an status code 404.

### manager_controller.py - @managers_bp.route('/', methods=['POST'])

This endpoint route has the function create_manager().
As indicated in the function, it is using the POST request, known as CREATE in CRUD.
The function requires a valid JWT token. The user must first log in and display his JWT token as a bearer token to show that he is logged in, if he wants to perform this operation. This is done by the decorator function @jwt_required. 
The function will first change the JSON input that was received from the front end and make it readable by the database by changing it using Marshmallow into a readable Python type. This process is known as deserialization. The data is stored as body_data. 
It will then start to create a new Manager model instance in the database by using the body_data to fill the appropriate fields. For example, the name field of the manager will be filled up with the body_data's name which is done with body_data.get('name'). The fields that will be filled up are name, date_of_birth, teams_managed_previously, trophies_won and team. 
Afterwards, the db.session.add(manager) will add the new Manager model instance to the session, and the commit will insert and save it into the database. The newly created Manager model instance is then serialized using Marshmallow and changed into a JSON response which is viewable at the front-end as a JSON format, with a 201 status code.

### manager_controller.py - @managers_bp.route('/<int:id>', methods=['DELETE'])

This endpoint route has the function delete_one_manager(id).
As indicated in the function, it is using the DELETE request, the same in CRUD.
The function requires a valid JWT token. The user must first log in and display his JWT token as a bearer token to show that he is logged in, if he wants to perform this operation. This is done by the decorator function @jwt_required. 
The function gets the user_id from the JWT token. When a user logins, he generates a JWT token, which the function can use to verify the user is in the database and retrieve the user_id. 
It will then query the database(back-end) for the user object based on the user_id and retrieve it. 
The function will then check to see if the is_admin field is True for the User model instance it retrieved from the database. 
If so, it will execute the decorated function with its arguments and key word arguments. 
If not, the backend will return to the front end an error message saying that only admins are able to perform this action with a status code 403. This is performed by the decorator function known as @authorise_as_admin. 
The function then queries the back-end for the manager id that matches the <int:id> sent by the front-end user. The result is stored as a single manager object. 
If there is a match, the manager is then deleted based on its manager id and gives a message saying the manager with its name has been deleted successfully. 
If there is no match, then the error message is returned to the front-end saying that there is no manager with that id and hence, it cannot be deleted, with status code 404.

### manager_controller.py - @managers_bp.route('/<int:id>', methods=['PUT', 'PATCH'])

This endpoint route has the function update_one_manager(id).
As indicated in the function, it is using the PUT or PATCH request, known as UPDATE in CRUD.
The function requires a valid JWT token. The user must first log in and display his JWT token as a bearer token to show that he is logged in, if he wants to perform this operation. This is done by the decorator function @jwt_required. 
The function gets the user_id from the JWT token. When a user logins, he generates a JWT token, which the function can use to verify the user is in the database and retrieve the user_id. It will then query the database(back-end) for the user object based on the user_id and retrieve it. 
The function will then check to see if the is_admin field is True for the User model instance it retrieved from the database. 
If so, it will execute the decorated function with its arguments and key word arguments. 
If not, the backend will return to the front end an error message saying that only admins are able to perform this action with a status code 403. This is performed by the decorator function known as @authorise_as_admin. 
The function will then first change the JSON input that was received from the front end and make it readable by the database by changing it using Marshmallow into a readable Python type. This process is known as deserialization. The data is stored as body_data. The partial=True argument indicates that not all fields must be filled in the JSON input as some fields can be missing and the function will still perform the deserialization process. 
The function then queries the back-end for the manager id that matches the <int:id> sent by the front-end user. The result is stored as a single manager object. 
If there is a match, it will then start to update the existing Manager model instance by using the body_data to fill the indicated fields that have data. For example, the name field of the manager will be filled up with the body_data's name which is done with body_data.get('name') if the body data has the name field filled. If not, the following code 'or manager.name' sets the manager.name field to the existing data in the database for manager.name. The function does this with the other fields of the body_data and fills up the attributes in the Manager model accordingly. The attributes are name, date_of_birth, teams_managed_previously, trophies_won and team. 
The function will then commit the newly updated Manager model instance to be re-inserted into the database and saved. The newly updated Manager model instance is then serialized using Marshmallow and changed into a JSON response which is viewable at the front-end as a JSON format. 
If the check where manager id matches the <int:id> fails, the error message shows up saying the manager with that id does not exist and cannot be updated with status code 404.

### comment_controller.py - @comments_bp.route('/', methods=['POST'])

This endpoint route has the function create_comment(team_thread_id).
As indicated in the function, it is using the POST request, known as CREATE in CRUD.
The function requires a valid JWT token. The user must first log in and display his JWT token as a bearer token to show that he is logged in, if he wants to perform this operation. This is done by the decorator function @jwt_required. 
The function will first change the JSON input that was received from the front end and make it readable by the database by changing it using Marshmallow into a readable Python type. This process is known as deserialization. The data is stored as body_data. 
It will then query the database, specifically the Team_thread model instances and search the id of those instances using team_thread_id. It will then return the result as a team_thread object. 
If there is a successful match, it will then start to create a new Comment model instance in the database by using the body_data to fill the appropriate fields. For example, the message field of the comment will be filled up with the body_data's name which is done with body_data.get('name'). The fields that will be filled up are message, date, user_id and team_thread_id. The date field will be set to the current date, obtained using the date.today() function from the datetime module. The user_id field will be filled with the user_id retrieved from the get_jwt_identity() function. The team_thread_id field will be filled with id of the Team_thread model instance that was found.
Afterwards, the db.session.add(comment) will add the new Comment model instance to the session, and the commit will insert and save it into the database. 
The newly created Comment model instance is then serialized using Marshmallow and changed into a JSON response which is viewable at the front-end as a JSON format, with a 201 status code. 
If there is no match, the error message will pop up saying there is no team_thread with that id and therefore cannot be commented on, with status code 404.

### comment_controller.py - @comments_bp.route('<int:comment_id>', methods=['DELETE'])

This endpoint route has the function delete_comment(team_thread_id, comment_id).
As indicated in the function, it is using the DELETE request, the same in CRUD.
The function requires a valid JWT token. The user must first log in and display his JWT token as a bearer token to show that he is logged in, if he wants to perform this operation. This is done by the decorator function @jwt_required. 
The function gets the user_id from the JWT token. When a user logins, he generates a JWT token, which the function can use to verify the user is in the database and retrieve the user_id. It will then query the database(back-end) for the user object based on the user_id and retrieve it. 
The function will also query the database for a comment object based on its comment_id and retrieve the comment object. The function will then check to see if the comment object was retrieved. 
If so, the function will then check to see if the is_admin field is True for the User model instance it retrieved from the database or the function will check to see if the user_id attribute of the comment field matches the user_id. 
If there is a match, the comment is then deleted based on its comment id and gives a message saying the comment with its message has been deleted successfully. 
If there is no match between user_id attribute of comment field with user_id or the is_admin attribute of the user is False, the backend will return an error message saying only the admin or the creator of the message is able to delete the comment with a status code 403. 
If the comment object was not retrieved due to the comment object not existing, the error message is returned to the front-end saying that there is no comment with that id, with status code 404.

### comment_controller.py - @comments_bp.route('/<int:comment_id>', methods=['PUT', 'PATCH'])

This endpoint route has the function update_comment(team_thread_id, comment_id).
As indicated in the function, it is using the PUT or PATCH request, known as UPDATE in CRUD.
The function requires a valid JWT token. The user must first log in and display his JWT token as a bearer token to show that he is logged in, if he wants to perform this operation. This is done by the decorator function @jwt_required. 
The function gets the user_id from the JWT token. When a user logins, he generates a JWT token, which the function can use to verify the user is in the database and retrieve the user_id. 
The function will then first change the JSON input that was received from the front end and make it readable by the database by changing it using Marshmallow into a readable Python type. This process is known as deserialization. The data is stored as body_data. The partial=True argument indicates that not all fields must be filled in the JSON input as some fields can be missing and the function will still perform the deserialization process. 
The function will then query the database for a specific comment object by searching for its id attribute and matching it with the id inputted by the user and then retrieving the comment object. 
If the comment object was retrieved, it will then do the next check to see if the is_admin field is True for the User model instance it retrieved from the database or the function will check to see if the user_id attribute of the Comment model instance matches the user_id field of the User model instance. 
If both checks pass, it will then start to update the existing Comment model instance by using the body_data to fill the indicated fields that have data. The message field of the comment will be filled up with the body_data's message which is done with body_data.get('message') if the body data has the message field filled. If not, the following code 'or comment.message' sets the comment.message field to the existing data in the database for comment.message. The date field is not updated as this application will only consider when the user originally made the comment, not when it was updated. 
The function will then commit the newly updated Comment model instance to be re-inserted into the database and saved. The newly updated Comment model instance is then serialized using Marshmallow and changed into a JSON response which is viewable at the front-end as a JSON format. 
If the check where the User model instance has its is_admin attribute set to False, or the user_id attribute of the Comment model instance does not match the user_id attribute of the User model instance, the error message is given, saying only an admin or the creator of the comment can update the comment, with status code 403.
If the check where the Comment model instance cannot be retrieved as there is no match, an error message is given saying there is no comment with that specific id, with status code 404.

### auth_controller.py - @auth_bp.route('/register', methods=['POST'])

This endpoint route has the function auth_register().
As indicated in the function, it is using the POST request, known as CREATE in CRUD.
The function will first try to get the JSON data from the request put in by the front-end user in the form of a JSON input. The data is stored as body_data. 
It will then start to create a new User model instance in the database by using the body_data to fill the appropriate fields. For example, user.name will be filled up with the body_data's name which is done with body_data.get('name'). The fields that will be filled up are name, email, username, favourite_player, password and team. The is_admin field will be set to False by default. The password field will be encrypted using the bcrypt.generate_password_has(body_data.get('password')).decode('utf-8') if the password is inputted.
Afterwards, the db.session.add(user) will add the new User model instance to the session, and the commit will insert and save it into the database. 
The newly created User model instance is then serialized using Marshmallow and changed into a JSON response which is viewable at the front-end as a JSON format, with a 201 status code.
Except if the function encounters an integrity error which comes when the email and username is not unique, or when the not null requirements are violated as the field is left empty. These will return the error codes respectively.

### auth_controller.py - @auth_bp.route('/login', methods=['POST'])

This endpoint route has the function auth_login().
As indicated in the function, it is using the POST request, known as CREATE in CRUD.
This route is for the user to login. The function will first get the JSON data from the request put in by the front-end user in the form of a JSON input. The data is stored as body_data. 
A login_identifier variable is created by retrieving the email or username details of the body_data. The function will then start to search the user in the database by searching the email or username attributes of the User model instances in the database and comparing them with the login_identifier variable's email or username details. It will take the first match of either the email or username attributes found in the database and retrieve it and set it as a user object.
The function will then check to see if the user object exists and the password attribute of the user object that was retrieved matches the password field in the body_data, after the bcrypt.generate_password_hash. If both conditions are met, the backend will generate a JWT token and return it to the front-end along with other details such as the username, email and whether the user is an admin.
If the username or email or password does not match the username, email or password attributes of the User model instances in the database, an error message will be given saying 'Invalid email, username or password. Please try again', with status code 401.

### auth_controller.py - @auth_bp.route('/users/<int:id>', methods=['DELETE'])

This route is for admins to delete users.
This endpoint route has the auth_delete_one_user(id).
As indicated in the function, it is using the DELETE request, also known as DELETE in CRUD.
The function requires a valid JWT token. The user must first log in and display his JWT token as a bearer token to show that he is logged in, if he wants to perform this operation. This is done by the decorator function @jwt_required. 
It will then query the database(back-end) for the user object based on the user_id and retrieve it. 
The function will then check to see if the is_admin field is True for the User model instance it retrieved from the database. 
If so, it will execute the decorated function with its arguments and key word arguments. 
If not, the backend will return to the front end an error message saying that only admins are able to perform this action with a status code 403. This is performed by the decorator function known as @authorise_as_admin.
The function gets the user_id from the JWT token. When a user logins, he generates a JWT token, which the function can use to verify the user is in the database and retrieve the user_id. It will then query the database(back-end) for the user object based on the user<int:id> and retrieve it and set it as user_to_delete variable.
If the user_to_delete variable exists as the user<int:id> has a match in the User model instances in the system, the user_to_delete variable is removed from the session and then committed so the removal is saved into the database system. A message will appear saying the user with the username has been deleted succesfully.
Else, the function will return the error message that there is no user with that id and cannot be deleted, with status code 404.

### auth_controller.py - @auth_bp.route('/users/<int:id>', methods=['PUT', 'PATCH'])

This endpoint route has the update_one_user(id).
As indicated in the function, it is using the PUT or PATCH request, known as UPDATE in CRUD.
The function requires a valid JWT token. The user must first log in and display his JWT token as a bearer token to show that he is logged in, if he wants to perform this operation. This is done by the decorator function @jwt_required. 
The function gets the user_id from the JWT token. When a user logins, he generates a JWT token, which the function can use to verify the user is in the database and retrieve the user_id.
The function will then first change the JSON input that was received from the front end and make it readable by the database by changing it using Marshmallow into a readable Python type. This process is known as deserialization. The data is stored as body_data. The partial=True argument indicates that not all fields must be filled in the JSON input as some fields can be missing and the function will still perform the deserialization process. 
The function will then query the database for a specific user object by searching for its id attribute and matching it with the id inputted by the user and then retrieving the user object and setting it as user_to_update variable. 
If the user_to_update variable exists, it will then do the next check to see if the id of the user_to_update variable matches the id of the user object(user_id).
If both checks pass, it will then start to update the existing User model instance by using the body_data to fill the indicated fields that have data. For example, the name field of the user object will be filled up with the body_data's name which is done with body_data.get('name') if the body data has the name field filled. If not, the following code 'or user.name' sets the user.name field to the existing data in the database for user.name. The function does this with the other fields of the body_data and fills up the attributes in the User model accordingly. The attributes are name, email, username, date_of_birth, favourite_player, password and team. The password will be encrypted using bcrypt.generate_password_hash() if the password field is filled up. Otherwise, it will use the existing password attribute of the User model instance.
The function will then commit the newly updated User model instance to be re-inserted into the database and saved. The newly updated User model instance is then serialized using Marshmallow and changed into a JSON response which is viewable at the front-end as a JSON format. 
If the check to see if the id of the user_to_update variable does not match the id of the user object(user_id), the error message is given, saying that only the user can edit his own details, with status code 403.
If the user_to_update variable does not exist, an error message is given saying there is no user with that specific id and cannot be updated, with status code 404.

## R6. An ERD for your app

![Alt text](<ERD diagram for soccer mania app.jpeg>)

## R7. Detail any third party services that your app will use

