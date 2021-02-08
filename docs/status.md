---
layout: default
title: Status
---

### Sample Video

<iframe width="560" height="315" src="TBD" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<br />

### Summary

<h4>At the very beginning, our initial idea was to make a mini-game similar to flappy bird in minecraft and train AI to reach the destination. But we found that with our current knowledge, this is a very challenging thing. So we changed from avoiding vertical obstacles to avoiding horizontal obstacles. There is deadly lava on both sides of the road, which prevents players from getting around these obstacles from both sides. We also add some random diamonds with bonus points to the map. In fact, if you look down from the air, the map design is similar to flappy bird. Now the player will not die when hitting the wall, but the more steps used, the lower the reward will be. It player not complete within a certain number of steps, it will be considered a failure too. The difficulty of the map can be changed in the future, such as increasing the complexity of obstacles, laying deadly lava on the floor, making the path longer, etc. We may continue to add interesting elements to make this project more complete.</h4>

![1](1.png){:height="70%" width="70%"}
![2](2.png){:height="70%" width="70%"}


<br />

### Approach

#### TBD

**Actions of agent**

```math
1. Moving forward for 1 block.
2. Moving left for 1 block.
3. Moving right for 1 block.
```
**Reward Functions**

```math
1. Reward = 10 when agent collecting a diamond on the floor.
2. Reward = 10 when agent through a gap.
3. Reward = 100 when agent touchs destination line.
4. Reward = -1 for every steps agent move on stone.
5. Reward = -10 when agent die from lava.
```

### Evaluation

#### Qualitative

<h4></h4>



#### Quantitative

<h4></h4>



<br />

### Remaining Goals

<h4></h4>

<h4></h4>

<br />

### Challenges

<h4></h4>

<h4></h4>

<h4></h4>

<br />

### Resources Used

#### The following resourse is useful when we doing our project.

1. [XML Schema Documentation](https://microsoft.github.io/malmo/0.21.0/Schemas/MissionHandlers.html)
2. [Pytorch Reinforcement Learning](https://github.com/bentrevett/pytorch-rl)
3. [Q-Learning in Python](https://www.geeksforgeeks.org/q-learning-in-python/)
4. [Math of Q-Learning — Python](https://towardsdatascience.com/math-of-q-learning-python-code-5dcbdc49b6f6)
5. [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
6. [Enjoy AI in Minecraft (Malmo and MineRL)](https://tsmatz.wordpress.com/2020/07/09/minerl-and-malmo-reinforcement-learning-in-minecraft/)
7. [Deep Q-Learning Tutorial: minDQN](https://towardsdatascience.com/deep-q-learning-tutorial-mindqn-2a4c855abffc)

