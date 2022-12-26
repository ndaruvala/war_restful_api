DESCRIPTION:
This project is called "War Restful API". It is RESTful service that allows a
user to simulate a game of war between two CPUS's and retrieve the
number of lifetieme wins for each player that is stored in a database.
Note: The game of war is played according to Bicycle Cards's rules.

SETUP:
Install all the requirements specified using "pip install -r requirements.txt"

INSTRUCTIONS:
To the run the unit tests included in the API:
 1. Install MongoDB community edition
 2. Start a MongoDB server by inputting "mongod" into the command line
 2. In a separate terminal, run the tests by inputting "pytest" into the command line.

To start the application server:
 1. Run the "flask run" command in your terminal
 2. Open another terminal and use CURL to send get and post requests
    your localhost:5000.

To start a game between two players:
Send a POST request to the "/war/start" endpoint.
As a response, you will receive the winner of the game as well as the outcomes for
each round of the game.

To retreive the lifetime wins for a certain player, 
send a GET request to the "/user/<int:user_id>" endpoint, 
replacing "<int:user_id>" with the user id of the desired player.

FUTURE WORK:
If I had additional time, I would create either a simple web application/UI or 
deploy this API with documentation to Heroku. In the web app, a user could click a button 
to start a game of War and see the game being played out. 
The lifetime wins for each player would be displayed on the screen.

TRADE OFFS:
In developing this app, I traded off ease of development for organization. I created
an organized structure to store the logic and classes for the War resource and User resource 
instead of merely placing everything in app.py. I also created a dedicated package for tests 
so that we can utilize the pytest library. These design choices allow developers
to add many additional endpoints easily in the app.py file and add the logic for which
these resources depend on to the resources folder. Creating more tests is as simple as 
adding more functions with the name "test_*.py" to the tests folder.