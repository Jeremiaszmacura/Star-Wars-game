<!-- Heading -->
## Star Wars Shooter
<!-- Links -->
#### Jeremiasz Macura

 ![game-window](assets/gameplay_window.png)

### Opis
<!-- UL -->
* The home screen shows the title of the game and asks you to select the difficulty level,
* Depending on the selected difficulty level, the appropriate number of enemy spaceships is generated on the screen
 (Tie Fighters), which also, depending on the level of difficulty, have different initial speeds along the x-axis and
  y axis,
* Enemy fighters are generated in random positions on the x axis and a fixed position on the y axis, with the lower limit
 y axis so that they give the effect of coming from the top of the screen towards our ship 
 (which is the Millennium Falcon), which this is generated on the half of the x axis and at the upper 
 y-axis limit (at the bottom of the gameplay screen),
* The goal of the game is to achieve the highest possible score (point = elimination of the enemy ship),
 with the duration of the game, enemy fighters start to accelerate, which makes it difficult for us to shoot them down,
* The condition for losing is the loss of life points. The number of health points is given to the player adequately
to the selected difficulty level. The loss of such a point is caused by crossing our line of defense
 (y-axis upper limit - bottom of screen) by enemy spaceship,
* The ship is controlled using the keyboard buttons on the keyboard that allow you to move around
in all directions and firing missiles at enemy ships (arrow keys, space bar key),
* When you lose all your hitpoints, the main game loop stops and a prompt appears on the screen
 o starting a new game or ending the program.
### Testy
<!-- UL-->
##### Test Modułu screen:
* dropping health points to 0 or less breaks the main gameplay loop, assigning a value
false to the running variable,
* the generated tie_fighters objects are instances of the Tie_fighter class,
* enemy fighters speed up one unit with each subsequent ten seconds,
* the function for calculating ten second periods works fine and after ten seconds it adds one
 value to the time variable in the function main.
 
