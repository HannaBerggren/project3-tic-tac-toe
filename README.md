# TIC TAC TOE
### Play the classic game of Tic Tac Toe. A game for two players who take turns marking the spaces in a three-by-three grid with X's or O's. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner!
&nbsp;
![Game](/assets/images/amiresponsive.png)

## Live Site
---
[Heroku](https://project3-tic-tac-toe.herokuapp.com/)

## Repository
---
[Github](https://github.com/HannaBerggren/project3-tic-tac-toe)
&nbsp;

## Table of Contents
---

- [UX](#ux)
    - [Website owners goals](#website-owners-goals)
    - [Users goals](#users-goals)
    - [Flow Chart](#flow-chart)
- [Existing Features](#existing-features)
    - [Introduction](#introduction)
    - [Game](#game)
    - [Future features](#future-features)
- [Technologies used](#technologies-used)
- [Testing and Validation](#testing-and-validation)
    - [PEP8](#pep8)
    - [Manual testing](#manual-testing)
    - [User stories testing](#user-stories-testing)
    - [Bugs](#bugs)
    - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
    - [How to deploy](#how-to-deploy)
- [Credits](#credits)


&nbsp;

## UX
---

### Website owners goals
- To offer entertainment to the user who wants to play the game.
- Provide simple information about the game.

&nbsp;

### Users goals
For new users:
- To play a game of Tic Tac Toe against the computer.
- To easily navigate in commands and interface.
- To always have reference navigation commands available.

Returning visitors:
- To practice their Tic Tac Toe skills playing against the computer.
- To be able to play Tic Tac Toe as many times as they want.

&nbsp;

### Flow Chart
To create the structure of the game, this diagram was created using [Lucid Charts](https://www.lucidchart.com/) 

&nbsp;
![Flow Chart](/assets/images/flowchart.png)

&nbsp;

[Back to Table of contents](#table-of-contents)

&nbsp;

## Existing Features:

### Introduction

Once the program runs, the user is welcomed to the game and they are asked to enter their name.

![Introduction](/assets/images/welcome.png) 

### Instructions


Here the player sees the instructions on how to play and is asked to press "p" to play the game.

![Instructions](/assets/images/instructions.png) 


### Error message

Thanks to the validation applied, the terminal will accept any "P" format, uppercase or lowercase, if the element typed by the user is different that "P" they will get an error message stating to type "p" again, correctly.

![Start Game](/assets/images/startgame.png) 


### Game

The player starts and is asked to choose a number between 1-9. The player's symbol is shown with an "X", while the computer will be shown as "O". 

![Play Game 1](/assets/images/game1.png)
![Play Game 2](/assets/images/game2.png)

### Spot is taken

When a spot is taken, a message is shown to choose another number.

![Spot Taken](/assets/images/taken.png)

### You won

If you win the game, a message will appear and you will see your score increase. You will be asked to either press q to stop playing or 1 to play again.

![You Won](/assets/images/won.png)

### Computer won

If you lose, a text is displayed that it was the computer that won and the computer score increase. You will be asked to either press q to stop playing or 1 to play again.

![You lose](/assets/images/lose.png)

### It's a Tie

When it's a tie, a text is displayed. You will be asked to either press q to stop playing or 1 to play again.

![It's a Tie](/assets/images/tie.png)

### Play Again or quit

Once the game is finished, a "Game ended" message is printed, and the user will have the option to start again (keeping the previous score), or quit the game. In case they want to quit, a thank you message will be printed.


![Play Game](/assets/images/playagainquit.png)
 
[Back to top](#table-of-contents)

&nbsp;

### Future features
---
- Give an option to the user to choose the symbol they want.
- Let user decide if they want to go first or second.
- Online multiplayer: the ability to play online with friends.
- Improve the computer difficulties in different levels: easy, intermediate and hard.
&nbsp;

[Back to Table of contents](#table-of-contents)

&nbsp;

## Technologies Used

 - [Python](https://www.python.org/) 
 - [JavaScript](https://www.javascript.com/) provided in the Code Institute Template
 - [CSS](https://en.wikipedia.org/wiki/CSS)  provided in the Code Institute Template
 - [HTML](https://en.wikipedia.org/wiki/HTML)  provided in the Code Institute Template
 - [Markdown](https://www.markdownguide.org/) was used troughout writing the README.md 
&nbsp;

## External Sources Used

- Stack Overflow
- W3 School
- Youtube
- [Am I Responsive](https://ui.dev/amiresponsive?url=https://project3-tic-tac-toe.herokuapp.com/) to create the main image for README file
- Lucidchart

## Python Libraries Used

- [Random](https://docs.python.org/3/library/random.html)  for computer random moves 
- [Time and Sleep](https://realpython.com/python-sleep/) for text animation / disappearence
- [Sys](https://docs.python.org/3/library/sys.html)  for specific parameters and functions

[Back to Table of contents](#table-of-contents)

&nbsp;


## Testing and Validation
---

### PEP8
The code was checked with PEP8 validator and passed with no error found.
&nbsp;

![Pep8](/assets/images/pep8.png)

### Manual testing
- All features have been tested manually with a MacBook Air and a Chromebook with multiple browsers (Chrome, Safari, Firefox).
- Family and friends tested for functionality.
- Tested all scenarios, to win, to get the computer to win, to get a tie.
- Tested writing different letters and symbols.
- Tested to write different numbers then 1-9.
- The game doesn't work on mobile devices.


&nbsp;

### User stories testing
For the program owner:
- The game offers joy to the users and the chance to play it multiple times.
- The game contains informations about the game during every step they play.

For new users and returning visitors:
- The user can improve their skill at the game excercising with this program which puts them against the computer.
- The user can navigate through the game with easy commands.
- Always available reference of the possible choices when making a move, makes it easy to find the right commands.
&nbsp;

[Back to Table of contents](#table-of-contents)
&nbsp;

### Bugs
- No bugs detected.

&nbsp;

### Unfixed Bugs
- None that I'm aware of right now.

&nbsp;

## Deployment
This project was developed through Gitpod, using the template provided by Code Institute. Every step was documented and pushed thoroughly via GitHub.
This version is also deployed live on Heroku.

### How to deploy
To deploy this page to Heroku from it's [GitHub repository](https://github.com/HannaBerggren/tic-tac-toe) the following steps were taken:

- Log into or register a new account at [Heroku](https://www.heroku.com/).
- Click on the button **New** in the top right corner of the dashboard.
- From the drop-down menu then select **Create new app**.
- Enter your app name in the first field, the names must be unique so check that then name you have chosen is available on Heroku, then select your region.
- Click on **Create App**.
- Once the app is created you will see the Overview panel of the application. Now move to the **Settings** tab.
- Once you are in scroll down till you find **Config Vars**.
- Press the button **Reveal Config Vars** and for 'KEY' field, type in 'PORT' and for the value field type in '8000'.
Then press the **Add** button.
- Scroll down to **Buildpacks**. Click the button **Add buildpack** and select 'python'. Do the same step and add 'node.js'.
**Python must be on top of the buildpacks. If in your case NODE.JS is first, click and drag Python to the top and save.**
- Return back to the **Deploy** tab. From the deployment method, select 'Github' as the deployment.
- You will be asked to connect your github account. Confirm and proceed.
- Search for your repository name and connect.
- Once that is done and successfully connected, select how you want to push updates from the following options.

  _Clicking **Enable Automatic Deploys**. This will update once you push updates to your Github._

  _Selecting the correct branch for deployment from drop-down menu and pressing **Deploy Branch** button. This will have to be done everytime manually._

&nbsp;

[Back to Table of contents](#table-of-contents)

&nbsp;

## Credits
---
- Youtube - for great inspiration!
- [Stackoverflow](https://stackoverflow.com/)
- [W3 Schools](https://www.w3schools.com/)
- [Geeksforgeeks](https://www.geeksforgeeks.org/)
- My cousin - for her great support!
- Further help and assistance was provided by Love Sanwiches guided project.

&nbsp;

Hanna Berggren 2023

[Back to Table of contents](#table-of-contents)