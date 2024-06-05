# RACING GAME DONE USING NEAT ALGORITH

## Table of Contents

1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Usage](#usage)
4. [Project Structure](#project-structure)
5. [Game Mechanics](#game-mechanics)
6. [AI Training](#ai-training)
7. [Conclusion/Results](#conclusion-result)

## Introduction

This project is an AI-powered car racing game made in pygame that uses the NEAT algorithm to train computer-controlled cars. Players can race against 2 AI models I personaly trained.

## Setup

To set up the project, follow these steps:

1. Clone this repository to your local machine.
2. Make sure you have at least Python version 3.6 (that is the earliest version that neat library supports).
3. Install the needed packages `pip install -r requirements. txt`.
4. Run the program and enjoy.

## Usage

The idea behind the project is to see if ai will have any similarites in positioning to the real formula 1 drivers (right now it might be harder to get any good results since the car movement and the physics are very basic but I plan on updating the project to have more sophisticated mechanics).

## Project Structure

Project contains 3 folders:

1. AIGameModel - this is a folder containg all the files that allow you to train the ai using NEAT algorithm. The config.txt contains all the configuration needed for the NEAT algorithm to work.
2. game - this is a folder containg all the code for the game, menu, etc.
3. Models - this folder contains the models best.pkl and worst.pkl as well as neat checkpoints (the best.pkl was trained using 50 generations and worst using 8 generations).

## Game Mechanics

When you start the game you will be presented with a game menu.
![startScreen](documentationsImgs\startScreen.png)
Pressing Exit will close the app, while pressing Start will allow you to pick a model you want to play against.
![pickScreen](documentationsImgs\pickScreen.png)
Pressing one of the images will start the game and will allow you to play against 1 of the 2 pre-trained models (You can probably realize which one is the better model if you have any knowledge about formula 1).
![gameScreen](https://github.com/szbytniewski/ReinforcmentTraningInAGame/blob/351bf826832895babe2d5608d943a7f49fb1f895/documentationsImgs/gameScreen.png)
Above is an image of how the game looks. The images for the track and track outline were taken from this youtube video description https://www.youtube.com/watch?v=L3ktUWfAMPg&t as well as some of the basic code needed for the game.
The controls for the player car are as follows:

1. W - move forward
2. S - move backward
3. A - rotate left
4. D - rotate right

In the left down corner you have a counter of current laps count. To win the game you have to be the first to finish 3 laps around the track. After the first person reaches 3/3 laps a message will appear on the screen saying who won. Upon pressing any button on the keyboard the game will close(this will be changed later on to return to the game menu).

## AI Training

The model has 7 inputs 5 for rays/pointers which allow them to observe their surrounding, and 2 more inputs for their velocity and angle, while having 8 outputs. The model can make 2 choices turn left or turn right(0 and 1). If you look into the config file you will see the numer of outputs equals 8. It is 8 because during intense traning 2 outputs made the model traning very slow since and inefficient and while playing around I relised that it was doing better when the ammount fo outputs was larger.

![traningScreen](documentationsImgs\traningScreen.png)
Above you can see an example of how the ai is trained. On the picture you can see a few cars, each car has 5 rays pointing into 5 diffrent directions(2 to their sides, 1 to the front, and 2 in-between the front and the sides). This allows them to adapt based on how far they are from the track's walls. As for rewarding the cars there are a few options. The first one is given for reaching the finish line which adds 500 to their fitness score, it is made this way since it should be a big achievement for a car to reach finish line. Next rewarding system is given for reaching the finish line the fastest as possible which is `1000 / (time.time() - start_time)`. The last positive rewards is for the distance which is the smallest and calculated as `car.vel / 10` the reason for this kind of small reward is so that they cars get awarded for moving which will be usefull for the version where car has full control but it is small becuase otherwise the car will try to strafe as much as possible in order to travel the most distance. The negative reward is for hitting the wall which is made so that the car aboid hitting the walls and slowing down.

## Conclusion/Results

During the traning of the models and play testing the game/models, I realised that there are a few similarities between the ai and real drivers and that was in the way the position for turning. Below is a link to a youtube video which explains the turning lines that are in formula 1 and from my observations the ai is trying to do the same thing. Even though, our game and cars are much more simplified and lack some of the physics that real drivers have, we can see similarities which is very suprising. I belive that we could get more accurate results if the game and mechanic were more sophisticated but for the current version I can say I achieved a success in recreating some bacis behaviours from real life.

Link to the video:
https://www.youtube.com/watch?v=uIbTPvHFf-w

Link to the NEAT-Python documentation: https://neat-python.readthedocs.io/en/latest/

Link to an introduction to the NEAT algorithm which I used to understand the subject more: https://www.youtube.com/watch?v=VMQOa4-rVxE
