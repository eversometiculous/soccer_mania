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

As seen from requirements.txt, here are the packages.

### bcrypt

This is v4.0.1. Bcrypt serves as a modern password hashing service for softwares and servers. While it is relatively safe as it encrypts data such as passwords using an utf-8 encoding system. UTF-8 is an encoding system for Unicode. It can translate any Unicode character to a matching unique binary string, and can also translate the binary string back to a Unicode character. This is the meaning of “UTF”, or “Unicode Transformation Format.”

It is relatively secure as UTF-8 converts characters from one to four bytes. It also helps to save up space and memory, as common ASCII characters requies less space(one byte). This results in spatial efficiency. It is also backward-compatible with ASCII(Juviler n.d.).

There are more secure options such as scrypt or argon2id.

### greenlet

This is v2.0.2. Greenlet is a lightweight library that can occur concurrently in real-time. It allows for the writing of efficient and cooperative multitasking code. It allows the user to create coroutines or greenlets that are small and lightweight. Greenlets can run cooperatively. They do not rely on the operating system unlike threads, making them faster and more memory-efficient.

Greenlets can be thought of as mini-threads. Greenlets run cooperatively, meaning that they need to give an ouput or other greenlets wont run. It is also limited to one operating system thread. It is a lower-level concurrency library compared to asyncio, which is a higher-level concurrency library.

### itsdangerous

This is v2.1.2. Itsdangerous, helps to safely pass data to unsafe environments and back. It provides various utilites for data serialization, salting and signing to securely transmit and store data. Commonly used in creating and verifying tokens.

Itsdangerous can serialize python types into a compact URL-safe string representation that helps to securely transmit and store data. The module also allows the user to add a crytographic signature to the data, making it more secure and authentic. It can also create signatures with a time limit that causes signatures to expire once the time limit is reached. Useful for creating access tokens with a time limit. Salting is another feature itsdangerous does. It adds another layer of security by adding a layer before the serialized data. 

### Jinja2

This is v3.1.2. Jinja2 is a popular templating engine for Python. It provides a powerful way to generate dynamic content by combining templates with data. Jinja2 templates are text files that contain placeholders, expressions and control structure, which are then later replaced by actual values.

Jinja2 uses a simple template language with placeholders.
Jinja2 supports template inheritance, which allows you to create a base template and have child templates inherit the base template features. Jinja2 also allows filters and macros.

### MarkUpSafe

This is v2.1.3. MarkupSafe is a Python module that provides functions and classes for escaping and manipulating strings. It is often used in conjunction with templating engines like Jinja2 to help prevent Cross-Site Scripting (XSS) attacks by escaping potentially dangerous characters in user-generated or untrusted content

When working with strings that have user-generated content, concatenating them directly can lead to security issues. MarkupSafe provides the .join() method, which safely joins a list of strings as a new Markup object. T It also includes error classes to handle situations where markup is not valid or improperly used. This helps in providing informative error messages during development.

### packaging

This is v23.1. While it is not a Python module per se, it is part of Python's packaging ecosystem that helps to create, distribute and install Python packages.

### PyJWT

This is v2.7.0. As it says, it is a Python library that provides support for encoding and decoding JSON Web Tokens or JWT. A JWT is a secure way to represent information and share it between two parties. JWT is often used for authentication and authorisation in web applications. It supports various algorithms for signing and verifying tokens such as HMAC and RSA algorithms.

### python-dotenv

This module is v1.0.0. It is a Python module that allows the user to load environment variables specified in the .env file into a Python application. Sometimes when working on an application, the application requires access to databases, which in turn requires sensitive data to access them. This module helps to solve that by loading the environment variables from the .env file into the Python application itself. When used in conjunction with .gitignore where your .env file is listed, this will help to prevent your sensitive data from being leaked online.

### typing_extensions

This python module is v4.6.3. It extends the functionality of the typing module, giving extra hints to what to input into your code based on what your previous code is. It also helps to catch potential type-related errors.  The typing extension module is even more useful as it helps to bridge the gap between older and newer versions of Python by giving out hints as to whether a function or command or some lines of code is derelict,

### Werkzeug

This python module is v2.3.6. It is a part of the Flask web framework  and provides tools and utilities for web development. Werkzeug provides a simple and consistent way to work with HTTP requests and responses. The Request and Response objects encapsulate the data associated with an HTTP request and response, making it easy to read and manipulate headers, cookies, query parameters, form data, and other aspects of an HTTP message.

It also has URL routing. It allows developers to define URL patterns and associate them with corresponding view functions.

### Flask

This is currently at v2.3.2. Flask is a web framework for Python that is popular and lightweight.  It helps to simplify the process of developing web applications or APIs. It can handle HTTP requests, manage routing and render templates.

Flask, in conjunction with Werkzeug, allows developers to define routes for different URLs and associate them with corresponding view functions. It also provides easy access to the data of incoming HTTP requests. Developers can easily access query parameters, form data, headers, and cookies associated with the request. Flask also makes it simple to create and return HTTP responses. Developers can return HTML pages, JSON data, or other types of responses from view functions.

### Flask-Bcrypt

This is currently at v1.0.1. This is an extension that allows the user to integrate the bcrypt functions into the application by initializing the Bcrypt to run in the application. This is done by writing some specific code.

### Flask-JWT-Extended

This is currently at v4.5.2. This is an extension that allows the user to integrate the JWT-Extended functions into the application by initializing the JWT-Extended to run in the application. This is done by writing some specific code.

### flask-marshmallow

This is currently at v0.15.0. This is an extension that allows the user to integrate the marshmallow functions into the application by initializing the marshmallow to run in the application. This is done by writing some specific code.

### flask-SQLAlchemy

This is currently at v3.0.3. This is an extension that allows the user to integrate the SQLAlchemy functions into the application by initializing the SQLAlchemy to run in the application. This is done by writing some specific code.

### marshmallow

This is currently at v3.19.0. Marshmallow is a popular Python library that is mainly used for serialization and deseriallization purposes. It converts complex data types into native Python types and vice versa.

Serialization is the act of converting complex data types into native Python types that PostgreSQL can understand using SQLAlchemy. For example, when a user sends a JSON input into our application, our application will first use Marshmallow to serialize the JSON data into Python code that SQLAlchemy can use to look up and manipulate data in the PostgreSQL database. Deserialization does the exact same thing but in reverse.

### marshmallow-sqlalchemy

This is currently at v0.29.0. This extension helps to integrate the bridge between Marshmallow and SQLAlchemy. When working with SQLAlchemy, database models exist as Python classes. However, when building applications, you have to convert these models into JSON output.

Marshmallow will help to create schemas from your Python classes. They are written in JSON format so they can be used as output for your web application.

### psycopg2-binary

This is currently at v2.9.6. This is an adapter that helps to provide an Python interface to PostgreSQL databases. It acts like a bridge between Python applications and the PostgreSQL database.

With the adapter, a user can conduct queries into PostgreSQL databases using their python code from their python application instead of using the native PostgreSQL language. It can also convert PostgreSQL data types to Python and vice versa.

### SQLAlchemy

This is currently at v2.0.16. This is an open-source Python ORM system that acts like a middleman between PostgreSQL and the Python application. By writing Python classes and objects, the user can use SQLAlchemy to access and manipulate data in the PostgreSQL database without using SQL language.

SQLAlchemy provides a high-level API for building database queries, including SELECT, INSERT, UPDATE, DELETE, and more. The user can filter, join, and aggregate data using intuitive Python language. SQLAlchemy supports defining and managing relationships between database tables, such as one-to-one, one-to-many, and many-to-many relationships. This makes it easier to work with related data in the application.

The difference between psycopg2-binary and SQLAlchemy is that psycopg2-binary is a PostgresQL-specific adapter whilst SQLAlchemy is more of a higher-level ORM library. They do work together, though. Psycopg2-binary provides the direct connection to PostgreSQL and SQLAlchemy offers a higher-level interface to work with PostgreSQL and other databases(ChatGPT, 2023).


#### Reference List

1) Juviler, J n.d., What is UTF-8 Encoding? A Guide for Non-Programmers, blog.hubspot.com., accessed 30 July 2023, <https://blog.hubspot.com/website/what-is-utf-8#:~:text=UTF%2D8%20is%20an%20encoding,or%20%E2%80%9CUnicode%20Transformation%20Format.%E2%80%9D>

2) ChatGPT n.d., chat.openai.com, accessed 31 July 2023, <https://chat.openai.com/c/f67d87b7-2117-41f7-a560-b997cef90984>

## R8. Describe your projects models in terms of the relationships they have with each other

This answer will talk about the database relations using SQLAlchemy and the Flask code itself.

### Model user.py(db.Model)

In the User class, I have 1 foreign key and 3 relationships that I will go up in more detail.

#### Foreign Key

"team_id" is a foreign key for the "users" table. It essentially establishes a many-to-one relationship between the one Team model and many User models. Each user will belong to one team, and this is done by referencing the id of the "teams" table.

####  Relationships

"team_threads" will be represented by a one-to-many relationship between the one User model and many Team_thread models. A user can create as many "team_threads" as he wants but in reverse, a "team_thread" can only belong to one and only one user. This is defined with db.Relationship. As for back_populates='user', the Team_thread model's attribute called 'user' will represent the user relationship back to the team_threads he created. In essence, it means that the team_threads will show the user who created them. The cascade='all, delete-orphan' parameter will essentially mean that any changes made to the User model will cascade to its relevant team_threads. If a user is deleted, all team_threads created by the user are deleted as well. The deleted records will be removed from the database immediately once disassociated.

"team" will be represented by a one-to-many relationship between the one Team model and many User models. A team can have as many users as it can represent but a user can only be tied on one team. This is defined by db.Relationship. As for back_populates='users', the Team model's attribute called 'user' will represent the user relationship back to the user's favourite team.

"comment" will be represented by a one-to-many relationsip between the one User model and many Comment models. A user can have as many comments as he made, by each comment represents one unique user. The back_populates='user' parameter is an attribute of the Comment model called 'user' and will represent the user relationship back to the comments he created. In essence, the comments will show the user who made them. The cascade='all, delete-orphan' parameter will essentially mean that any changes made to the User model will cascade to its relevant comments. If a user is deleted, all comments created by the user are deleted as well. The deleted records will be removed from the database immediately once disassociated.

### Model team.py(db.Model)

In the Team class, we have 5 relationships that will be discussed.

#### Relationships

"team_threads" will be represented by a one-to-many relationship between the one Team model and many Team_thread models. A team can have as many "team_threads" as it can but in reverse, a "team_thread" can only belong to one and only one team. This is defined with db.Relationship. As for back_populates='team', the Team_thread model's attribute called 'team' will represent the team relationship back to the team_threads he created. In essence, it means that the team_threads will show the team who they belong to. The cascade='all, delete' parameter will essentially mean that any changes made to the team model will cascade to its relevant team_threads. If a team is deleted, all team_threads belonging to the team are deleted as well. Since there is no delete-orphan, the records will still be orphaned in the database, but will be removed once the session is committed.

"managers" will be represented by a zero to one-to-a zero to one relationship between the one Team model and one Manager model. A team can be managed by zero to one manager and in reverse, a manager can only belong to zero to one team. This is defined with db.Relationship. As for back_populates='team', the Manager model's attribute called 'team' will represent the team relationship back to the manager who manages it. In essence, this means that the manager will show the team that he belongs to. The cascade='all, delete' parameter will essentially mean that any changes made to the team model will cascade to its relevant manager. If a team is deleted, the manager belonging to the team is deleted as well. Since there is no delete-orphan, the records will still be orphaned in the database, but will be removed once the session is committed.

"stadiums" will be represented by a zero to many-to-a zero to many relationship between the one to many Team models and one to many Manager models. A stadium can be be the base for zero-to-many teams and in reverse, a team can have zero to many stadiums. This is defined with db.Relationship. As for back_populates='team', the Stadium model's attribute called 'team' will represent the team relationship back to the stadium which acts as the base for the team. In essence, this means that the stadium will show the team that it is hosting. The cascade='all, delete' parameter will essentially mean that any changes made to the team model will cascade to its relevant stadium. If a team is deleted, the stadium belonging to the team is deleted as well. Since there is no delete-orphan, the records will still be orphaned in the database, but will be removed once the session is committed.

"players" will be represented by a zero to one-to-a zero to many relationship between the zero to one Team model and zero to many Player models. A team can have zero to many players and in reverse, a player can only belong to zero to one team. This is defined with db.Relationship. As for back_populates='team', the Player model's attribute called 'team' will represent the team relationship back to the player who plays for the team. In essence, this means that the player will show the team that he plays for. The cascade='all, delete' parameter will essentially mean that any changes made to the team model will cascade to its relevant players. If a team is deleted, the players belonging to the team is deleted as well. Since there is no delete-orphan, the records will still be orphaned in the database, but will be removed once the session is committed.

"users" will be represented by a zero to one-to-a zero to one relationship between the one Team model and one User model. A team can have zero to one users and in reverse, a user can only belong to zero to one teams. This is defined with db.Relationship. As for back_populates='team', the User model's attribute called 'team' will represent the team relationship back to the user who it belongs to. In essence, this means that the user will show the team that he belongs to. The cascade='all, delete-orphan' parameter will essentially mean that any changes made to the team model will cascade to its relevant user. If a team is deleted, the user belonging to the team is deleted as well. The deleted records will be removed from the database immediately once disassociated.

### Model team_thread.py(db.Model)

In the Team_thread class, we have two foreign keys and 3 relationships that will be talked in detail.

#### Foreign Keys

"team_id" is a foreign key for the "team_threads" table. It essentially establishes a many-to-one relationship between the one Team model and many Team_thread models. Each team_thread will belong to one team, and this is done by referencing the id of the "teams" table.

"user_id" is a foreign key for the "team_threads" table. It essentially establishes a many-to-one relationship between the one User model and many team_threads models. Each team_thread will belong to one user, and this is done by referencing the id of the "users" table.

#### Relationships

"user" will be represented by a one and only one-to-zero to many relationship between the one User model and zero to many Team_thread models. A user can have zero to many team_threads and in reverse, a team_thread can only belong to one and only one user. This is defined with db.Relationship. As for back_populates='team_threads', the User model's attribute called 'team_thread' will represent the team_thread relationship back to the user who created it. In essence, this means that the user id will be shown on the team_thread that created it. The parameter foreign_keys=[user_id] is used when there is more than one foreign key in the relationship. In this case, user_id is the foreign key in the Team_thread model that refers to the id column of the User model. 

"team" will be represented by a one and only one-to-zero to many relationship between the one Team model and zero to many Team_thread models. A team can have zero to many team_threads and in reverse, a team_thread can only belong to one and only one team. This is defined with db.Relationship. As for back_populates='team_threads', the Team model's attribute called 'team_thread' will represent the team_thread relationship back to the team it belongs to. In essence, this means that the team id will be shown on the team_thread that belongs to it. The parameter foreign_keys=[team_id] is used when there is more than one foreign key in the relationship. In this case, team_id is the foreign key in the Team_thread model that refers to the id column of the Team model. 

"comments" will be represented by a one and only one-to-zero to many relationship between the one Team_thread model and zero to many Comment models. A team_thread can have zero to many comments but in reverse, a comment can only belong to one and only one team_thread. This is defined with db.Relationship. As for back_populates='team_thread', the Comment model's attribute called 'team_thread' will represent the team_thread relationship back to the comment. In essence, this means that the comment will show the team_thread that it belongs to. The cascade='all, delete-orphan' parameter will essentially mean that any changes made to the team_thread model will cascade to its relevant comments. If a team_thread is deleted, the comments belonging to it are deleted as well. The deleted records will be removed from the database immediately once disassociated.

### Model stadium.py(db.Model)

The Stadium class has one foreign key and one relationship which will be discussed in detail.

#### Foreign keys

"team_id" is a foreign key for the "stadiums" table. It essentially establishes a zero to one-to-zero to many relationship between the zero to one Team model and zero to many Stadium models. Each stadium will belong to zero to one team, and this is done by referencing the id of the "teams" table.

#### Relationships

"team" will be represented by a zero to one-to-zero to many relationship between the zero to one Team model and zero to many Stadium models. A stadium can belong to zero to one team but in reverse, a team can play in zero to many stadiums. This is defined with db.Relationship. As for back_populates='stadium', the Team model's attribute called 'stadium' will represent the stadium relationship back to the team. In essence, this means that the team will show the stadium that plays in it.

### Model player.py(db.Model)

The Player class has one foreign key and one relationship which will be discussed in detail.

#### Foreign keys

"team_id" is a foreign key for the "stadiums" table. It essentially establishes a zero to one-to-zero to many relationship between the zero to one Team model and zero to many Player models. Each player will belong to zero to one team, and this is done by referencing the id of the "teams" table.

#### Relationships

"team" will be represented by a zero to one-to-zero to many relationship between the zero to one Team model and zero to many Player models. A player can belong to zero to one team but in reverse, a team can have zero to many players. This is defined with db.Relationship. As for back_populates='players', the Team model's attribute called 'player' will represent the player relationship back to the team. In essence, this means that the team will show the player that plays in it.

### Model manager.py(db.Model)

The Manager class has one foreign key and one relationship which will be discussed in detail.

#### Foreign keys

"team_id" is a foreign key for the "managers" table. It essentially establishes a zero to one-to-zero to one relationship between the zero to one Team model and zero to one Stadium model. Each manager will belong to zero to one team, and this is done by referencing the id of the "teams" table.

#### Relationships

"team" will be represented by a zero to one-to-zero to one relationship between the zero to one Team model and zero to one Stadium model. A manager can belong to zero to one team but in reverse, a team can have zero to one manager. This is defined with db.Relationship. As for back_populates='manager', the Team model's attribute called 'manager' will represent the manager relationship back to the team. In essence, this means that the team will show the manager that manages it.

### Model comment.py(db.Model)

The Comment class has two foreign keys and two relationships which will be discussed in detail.

#### Foreign keys

"team_thread_id" is a foreign key for the "comments" table. It essentially establishes a one and only one-to-zero to many relationship between the one and only Team_thread model and zero to many Comment models. Each comment will belong to one unique team_thread, and this is done by referencing the id of the "teams" table.

"user_id" is a foreign key for the "comments" table. It essentially establishes a zero to many-to-one and only one relationship between the one and only one User model and zero to many Comment models. Each comment will belong to one unique user, and this is done by referencing the id of the "users" table.

#### Relationships

"team_thread" will be represented by a one and only one-to-zero to many relationship between the one and only Team_thread model and zero to many Comment models. A comment can belong to one unique team_thread but in reverse, a team_thread can have zero to many comments. This is defined with db.Relationship. As for back_populates='comments', the Team_thread model's attribute called 'comments' will represent the comments relationship back to the team_thread. In essence, this means that the team_thread will show the many comments belonging to it. The parameter foreign_keys=[team_thread_id] is used when there is more than one foreign key in the relationship. In this case, team_thread_id is the foreign key in the Comment model that refers to the id column of the Team_thread model. The cascade='all, delete' parameter will essentially mean that any changes made to the Team_thread model will cascade to its relevant comments. If a team_thread is deleted, the comments belonging to it are deleted as well. Since there is no delete-orphan, the records will still be orphaned in the database, but will be removed once the session is committed.

"user" will be represented by a zero to many-to-one and only one relationship between the one unique User model and zero to many Comment models. A comment can belong to one unique user but in reverse, a user can have zero to many comments. This is defined with db.Relationship. As for back_populates='comments', the User model's attribute called 'comments' will represent the comments relationship back to the user. In essence, this means that the user will show the many comments belonging to him. The parameter foreign_keys=[user_id] is used when there is more than one foreign key in the relationship. In this case, user_id is the foreign key in the Comment model that refers to the id column of the User model. The cascade='all, delete' parameter will essentially mean that any changes made to the User model will cascade to its relevant comments. If a user is deleted, the comments belonging to him are deleted as well. Since there is no delete-orphan, the records will still be orphaned in the database, but will be removed once the session is committed.

## R9. Discuss the database relations to be implemented in your application

![Alt text](<ERD diagram for soccer mania app.jpeg>)

Please note that discussions held here will be done in terms of the ERD diagram show above.

### User table

The User table has one user_id, which serves as the primary key. Since there is only one primary key, the table is normalized. There is also one foreign key, which is "team_id". "team_id" represents a foreign key that ties the User table to the id of the Team. 
The relationship line shows a zero to one-to-zero-to-many relationship between the zero to one User table and zero to many Team table. This means that a user can have zero to one team and a team can have zero to many users registered to it. 
It also has a relationship with the Team_thread and Comment table, which will be discussed in their respective tables.

### Team table

The Team table has one team_id, which serves as the primary key. Since there is only one primary key, the table is normalized. There is no foreign keys to speak of. 
The Team table also has relationships with the Manager, Player, Stadium, and Team_thread table, which will be discussed in their respective tables.

### Team_thread table

The Team_thread table has one team_thread_id, which serves as the primary key. Since there is only one primary key, the table is normalized. 
There are two foreign keys, which are team_id and user_id. Team_id represents a foreign key that ties the Team_thread table to the id of the Team table. 
The relationship line shows a zero to many-to-one and only one relationship between the zero to many Team_thread table and one and only one Team table. This means that a team_thread can belong to one unique team but a team can have zero to many team_threads. 
The user_id represents a foreign key that ties the Team_thread table to the id of of the User table. 
The relationship line shows a zero to many-to-one and only one relationship between the zero to many Team_thread table and one and only one User table.
This means that a team_thread can belong to one unique user but a user can have zero to many team_threads.

### Comment table

The Comment table has one comment_id, which serves as the primary key. Since there is only one primary key, the table is normalized.
There are two foreign keys, which are team_thread_id and user_id. Team_thread_id represents a foreign key that ties the Comment table to the id of the Team_thread table. 
The relationship line shows a zero to many-to-one unique relationship between the zero to many Comment tables and one unique Team_thread table. This means that a comment can only belong to one unique team_thread, but a team_thread can have zero to many comments.
The user_id represents a foreign key that ties the Comment table to the id of of the User table. 
The relationship line shows a zero to many-to-one unique relationship between the zero to many Comment table and one unique User table. This means that a comment can only belong to one unique user, but a user can have zero to many comments.
Since it has two foreign keys to both the Team_thread table and User table, the Comment table also acts as a join table. This essentially means each team_thread can have multiple users, and each users can create multiple team_threads.

### Player table

The Player table has one player_id, which serves as the primary key. Since there is only one primary key, the table is normalized.
There is one foreign key, which is the team_id. Team_id represents a foreign key that ties the Player table to the id of the Team table.
The relationship line shows a zero to many-to-zero to one relationship between the zero to many Player tables and zero to one Team table. This means that a player can belong to zero to one team, and a team can have zero to many players.

### Manager table

The Manager table has one manager_id, which serves as the primary key. Since there is only one primary key, the table is normalized.
There is one foreign key, which is the team_id. Team_id represents a foreign key that ties the Manager table to the id of the Team table.
The relationship line shows a zero to one-to-zero to one relationship between the zero to one Manager tables and zero to one Team table. This means that a manager can belong to zero to one team, and a team can have zero to one manager.

### Stadium table

The Stadium table has one stadium_id, which serves as the primary key. Since there is only one primary key, the table is normalized.
There is one foreign key, which is the team_id. Team_id represents a foreign key that ties the Stadium table to the id of the Team table.
The relationship line shows a zero to many-to-zero to one relationship between the zero to many Stadium tables and zero to one Team table. This essentially means that a stadium can belong to zero to one team, and a team can have zero to many stadiums hosting it.

## R10