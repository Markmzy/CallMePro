---
layout: default
title: Status
---

### Sample Video

<video id="video" controls="" preload="none">
      <source id="mp4" src="https://www.youtube.com/watch?v=gO7Sl99GDOo&t=1s" type="video/mp4">
      </video>
<br />

### Summary

At the very beginning, our initial idea was to make a mini-game similar to flappy bird in minecraft and train AI to reach the destination. But we found that with our current knowledge, this is a very challenging thing. So we changed from avoiding vertical obstacles to avoiding horizontal obstacles. There is deadly lava on both sides of the road, which prevents players from getting around these obstacles from both sides. We also add some random diamonds with bonus points to the map. In fact, if you look down from the air, the map design is similar to flappy bird. Now the player will not die when hitting the wall, but the more steps used, the lower the reward will be. It player not complete within a certain number of steps, it will be considered a failure too. The difficulty of the map can be changed in the future, such as increasing the complexity of obstacles, laying deadly lava on the floor, making the path longer, etc. We may continue to add interesting elements to make this project more complete.

![1](1.png){:height="70%" width="70%"}
![2](2.png){:height="70%" width="70%"}



### Approach

TBD

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

* Qualitative:<br>
For our project, the goal for the agent is approaching the end with the least number of steps to avoid more deductions. Because the less deduction the agent gain, the much rewards he has. During learning, the agent’s initial movement looked a bit silly, since he would get stuck in front of the obstacle and move left and right repeated. And in many cases, he would swam in lava. And even if he passes the obstacle, it is difficult to reach the end within the prescribed number of steps. Might after half hour with learning, the agent may approach the end sometimes, but reward he got was still not good. Therefore, the agent should try to reduce his steps to approach, since the more steps he used, the more rewards he lost because every second before reaching the end, the agent will be punished. After 1 hour with learning, he could appraoch in most times, and gain more and more rewards. 


* Quantitative:<br>
From the following three pictures, we know that the purpose of this program is to allow agents to get more rewards. Through them, we can clearly see that after a lot of learning, agents are getting more and more rewards. In the agent's course of action, the agent can be rewarded by passing gold blocks and get diamonds, and every step the agent takes and falling into the lava will also cause corresponding punishment to the agent. The most important thing is that passing the finish line will give the agent the highest reward, so the agent is motivated to pass each gold blocks, get more diamonds, and use the fewest steps to reach the finish line. Through the three return pictures, we can see that the speed of the agent's advance is increasing, and the more rewards he gets. However, in some periods of time, the income of the agents is decreasing, which may be that the agents are trying to find other ways to increase their income.

### After trainning 6000 steps:
![6000](6000.png){:height="50%" width="50%"}
### After trainning 14000 steps:
![14000](14000.png){:height="50%" width="50%"}
### After trainning 20000 steps:
![20000](20000.png){:height="50%" width="50%"}


<br />

### Remaining Goals
Until this status report, we have not implement more maps with different difficulty. For example, the length of the path is a constant 100 now, and we may increase it in the future. Furthermore, the only obstacle is the brisk block now, so we may add some other obstacles to increase the difficulty of completion. We may also add some penalties policy to improve the performance of the agent. We may also put some interesting element. For example, traps on the ground or arrows from both sides of the path. On the other hand, we also hope to implement some more useful algorithms to make the agent's actions more smooth and realistic.  
The ultimate goal of this project is to approach the score of human control as much as possible, or even exceed the score of human control. Therefore, we should have completed the optimization of all algorithms, and passed enough time and steps to train the agent, in order to make him reach the best condition. After that, we may invite some friends to play it and get the mean score. Then see whether the agent can approach it or exceed it.

### Challenges
The challenge we are facing right now is when the agent collected some diamonds and he dead when he swam in lava, these diamonds he collected would left in where he dead, and when the map reset, these diamonds were still in here. We need to fix this error to make these diamonds disappear when map reset. Because reseting map should clear all the items in the previous map, and then generate a brand new map without leaving anything from the previous map.  
The another problem we need to fix is the agents will not take the initiative to pick up diamonds on the gold block yet. Because each diamond worth 10 points, if the agent wants to gain more and more rewards, he should pick up more diamonds after learning. But right now, even after a long time to learn, the agent still can not pick up any diamonds initiatively to improve his reward. This problem might be more diffucult, so we should change alforithm to let the agent pick up diamond initative.  
The most diffucult part is wrtitting a new machine learning method. The current machine learning method is still PPO which from the assignment2. We are learning Deep Q-learning and will use it in our project. With our understanding, Deep Q-learning might be a better algorithm for our project, but is hard to achieve it, since we do not know whether we can use it by importing a library. If we can use it by importing a library, we aloso do not knwo which library we can import from. And furthermore, if this machine learning algorithm is not good for our agent to learn to finish his mission better, we may still need to find a better one.


### Resources Used

#### The following resourse is useful when we doing our project.

1. [XML Schema Documentation](https://microsoft.github.io/malmo/0.21.0/Schemas/MissionHandlers.html)
2. [Pytorch Reinforcement Learning](https://github.com/bentrevett/pytorch-rl)
3. [Q-Learning in Python](https://www.geeksforgeeks.org/q-learning-in-python/)
4. [Math of Q-Learning — Python](https://towardsdatascience.com/math-of-q-learning-python-code-5dcbdc49b6f6)
5. [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
6. [Enjoy AI in Minecraft (Malmo and MineRL)](https://tsmatz.wordpress.com/2020/07/09/minerl-and-malmo-reinforcement-learning-in-minecraft/)
7. [Deep Q-Learning Tutorial: minDQN](https://towardsdatascience.com/deep-q-learning-tutorial-mindqn-2a4c855abffc)

