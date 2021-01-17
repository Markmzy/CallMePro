---
layout: default 
title: Proposal
---

## Summary of the Project<br>
Flappy bird is a popular game around the world. In the game, the player needs to control a bird to overcome obstacles composed of various lengths of water pipes above and below. We are going to make a minigame in Minecraft that similar to the Flappy bird, and use some algorithms to control our agent to pass that game automatically.
We simulate the player moving forward by making the obstacle move backward. Therefore, we only need to consider the vertical movement of the bird. The only action that player can do is 'Fly' which will make the bird move a block higher while 'No action' causes the bird to move a block lower. Every time the bird passes an obstacle will obtain 1 point, and if the bird hits a water pipe, the game is over.
* Input: The position information of obstacles<br>
* Output: The movement list of the bird ('Fly' or 'No action')

## AI/ML Algorithms
We are planning to implement a Deep Q Network that uses Q-learning to train our agent. We will learn this method during this quarter.

## Evaluation Plan
* Quantitative:<br>
  We will build 5 maps with different difficulty. 3 are easy maps and the remain 2 will be much harder. We will optimize the map as much as possible to ensure that the location of each water pipe is reasonable that no map is impossible to pass. For quantitative evaluation, our agent must pass all easy maps to be considered as succeed. This can rule out coincidences and also verify the correctness of the algorithm. 
* Qualitative:<br>
  However, for hard maps, our agent may not pass them all but should at least pass as much as pipes they can. For qualitative evaluation, the points obtained in the game would be the data we evaluate. Our initial sanity check is to see if our agent can get 20 points which means it can pass 20 pipes. We will change this baseline during implement time depending on how hard the minigame in Minecraft is. 

## Appointment with the Instructor
Thursday, January 21st, 2021, 3:15 pm
