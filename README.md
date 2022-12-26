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
 2. Run the tests by inputting "pytest" into the command line.

To start a game between two players:
send a POST request to the "/war/start" endpoint.
As a response, you will receive the winner of the game as well as the outcomes for
each round of the game.

To retreive the lifetime wins for a certain player, send a GET request to the "/user/<int:user_id>"
endpoint, replacing "<int:user_id>" with the user id of the desired player.
