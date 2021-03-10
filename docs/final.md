---
layout: default
title: Final Report
---

## **Video**

<iframe width="720" height="480" src="https://www.youtube.com/embed/gO7Sl99GDOo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<br />

## **Project Summary** 

The goal of our project is to train an agent through a dangerous zone surrounded by magma and there are many obstacles on the path that the agent needs to avoid to reach the end. While passing through obstacles, the agent needs to obtain diamonds from the diamond mine as much as possible to gain points, or it may lose points by digging coal by mistake. Compared with the map in the status report, the length of the map has been expanded from the original 100 blocks to 200 blocks, which effectively prevents the agent from reaching the destination line every time after training for a while. The agent will break the diamond mine or coal mine to move forward or bypass it. There are three different results, which are bonus points and minus points, and remain unchanged. The purpose of this is to use the rewards obtained from different behaviors to guide the agent to make the most correct choice. Obstacles on the map are randomly generated, and every gap is guaranteed to leave at least three blocks. Because the agent does not retreat, we will not set obstacles in front of the gap, or the agent will fall into an infinite loop.<br />

Because this map is very complicated for ai, trivial algorithms like brute force or greedy will not be able to guarantee that the agent will complete within a limited number of steps. So reinforcement learning is the best solution. We still decided to use the PPO algorithm. Determines the future behavior of the agent by recording the observation results and the reward value. Our agent has made significant progress after learning 20,000 steps, and it has become smarter than the one in the status report. It learned to cross the gap and destroy the correct ore block and finally reached the destination line.

<br />

## **Approaches**

#### **Map constraints**
```math
Width: 10 blocks
Length: 200 blocks
Maximum step per episode: 400 steps
Percentage of diamond mine: 15%
Percentage of coal mine: 15%
```

#### **Actions of agent**
```math
1. Moving forward for 1 block.
2. Moving left for 1 block.
3. Moving right for 1 block.
4. Break mine block
```

#### **Reward functions**
```math
1. Reward = 10 when agent collecting a diamond from breaking a diamond mine.
2. Reward = 10 when agent through a gap.
3. Reward = 100 when agent touchs destination line.
4. Reward = -1 for every steps agent move on stone.
5. Reward = -10 when agent collecting a coal from breaking a coal mine.
6. Reward = -10 when agent die from lava.
```

#### **Reinforcement learning algorithm**
![approach](approach.png){:height="50%" width="50%"}
<br />

## **Evaluation**


#### ***Qualitative***

#### ***Quantitative***


<br />
## **References**

#### The following resourses is useful when we doing our project.

1. [XML Schema Documentation](https://microsoft.github.io/malmo/0.21.0/Schemas/MissionHandlers.html)
2. [Pytorch Reinforcement Learning](https://github.com/bentrevett/pytorch-rl)
3. [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
4. [Enjoy AI in Minecraft (Malmo and MineRL)](https://tsmatz.wordpress.com/2020/07/09/minerl-and-malmo-reinforcement-learning-in-minecraft/)
5. [Proximal Policy Optimization explanation](https://blog.csdn.net/qq_30615903/article/details/86308045)
6. [Interpretation of PPO reinforcement learning algorithm](https://zhuanlan.zhihu.com/p/31005035)
7. [How to record video on Mac](https://support.apple.com/en-us/HT208721)
