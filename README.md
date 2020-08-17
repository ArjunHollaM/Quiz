# Quiz
This is a Science and Technology Quiz.
Execute the 'main.py' file to sart the quiz.
All you have to do is to respond for the questions that are asked.
You can use lifelines if you are unsure about an answer.Just type 'life' instead of the answer.
The instructions,lifelinees,no. of players are explained in the Quiz itself.
# Description
In this project you will be testing your knowledge on the topic 'Science and Technology'
You will have to select the no. of players(Single player or Double player).
Accordingly your name has to be submitted.
10 questions will be put forth randomly from a set of questions which are defined beforehand. 
For every question the player has to type a response which he/she feels is correct from a given set of 4 options.
If the player is unsure about an answer he/she can type 'life' or 'LIFE' in place of the response.
Three lifelines are provided which can be activated for any question.
Every question carries 10 points. If a wrong response is given , 5 points will be deducted.
In case of 2 players, the second player will recieve his 10 questions after the first player has completed his/her 10 questions.Standings will be printed.  
Finally a bar graph is plotted as a review.

LIFELINES:
(i)50-50--Eliminates two wrong options from the given set of 4 options.---- Holds 5 points.
(ii)Pass--The question will be skipped.---- Holds 3 points.
(iii)Eliminate One-- Eliminates one wrong option from the given set of 4.---- Holds 7 points.
# Implementation
Libraries like matplotlib.pyplot,time,numpy have been used.
main.py has to be run after cloning the repository on your PC.
When the main.py file is run..it starts off with "Welcome to the Science and Technology quiz!" followed by instructions to the game.
It will ask each player if they are ready ...if the response then, is not what is desired ..then it prints "It's ok. Try later".
If the player types 'ok' ..the first question is randomly printed and waits for the player to give a response. An invalid response is considered as a wrong response and hence points will be deducted.

