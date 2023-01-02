DESCRIPTION:

This project is called "War Restful API". It is RESTful service that allows a
user to simulate a game of war between two CPUS's and retrieve the
number of lifetieme wins for each player that is stored in a database.
Note: The game of war is played according to Bicycle Cards's rules.

INSTRUCTIONS:

To start a game between two players:
Send a POST request to the "https://war-restful-api.herokuapp.com/war/start" endpoint.
As a response, you will receive the winner of the game as well as the outcomes for
each round of the game.

To retreive the lifetime wins for a certain player:
Send a GET request to the "https://war-restful-api.herokuapp.com//user/<int:user_id>" endpoint, 
replacing "<int:user_id>" with the user id of the desired player.
To get player 1's lifetime wins, use 1 as the user_id. For player 2, use 2 as the user_id.

To the run the unit tests included in the API:
  1. Install all the requirements specified using "pip install -r requirements.txt"
  2. Install MongoDB community edition according to instructions specified on thier website;
     https://www.mongodb.com/docs/manual/administration/install-community/.
  3. Start a MongoDB database server by inputting "mongod" into the command line.
  4. In a separate terminal, cd into this project directory and
     run the tests by inputting "pytest" into the command line.


FUTURE WORK:

To further develop this project in the future, I would create simple web application/UI. 
In the web app, a user could click a button to start a game of War and 
see the game being played out round by round. The lifetime wins for each player would 
be displayed on the screen before and after the game.

