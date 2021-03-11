---https://github.com/Markmzy
layout: default
title: Final Report
---

## **Video**

<iframe width="720" height="480" src="https://www.youtube.com/embed/gO7Sl99GDOo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<br />

## **Project Summary** 

#### TBD

<br />

## **Approaches**
#### TBD


<br />

## **Evaluation**


#### ***Qualitative***
For the goal of the entire project, we need to pass through each gap made up of gold nuggets, and bypass or smash obstacles to reach the end. In the whole process, try to get the highest score possible. In the first half an hour, it was very difficult for the agent to pass through wall and obstacles, since he would always fall into the lava and die. However, after half hour, he began to pass through the gap skillfully and greatly reduced the number of times he fell into the lava, and began to work towards the finish line. When he could reach the finish line, he began trie to learn how to pass the obstacles, bypass or smash. During this time, he began to think about how to get a higher score on the premise of reaching the end. Because not only each step will pay a certain price, but the rewards obtained by breaking different blocks and picking up different items are different.

#### ***Quantitative***
Once again clarify the agent's goal, the agent needs to get the highest possible score in the process of reaching the end. In this progress, the most important thing is reach the end line and finish the mission, so the reward he gain when he reach the finish line is the most highest. There are wall and lava in the map, and he will gain a negative reward if he touch the wall, and gain a more negative reward if he died when he touch lava. Therefore, he needs to reach the end in as few steps as possible, and try to avoid falling into the lava and death. And after he can reach the end line he should pay more attention on two obstacles: coal_ore and diamond_ore, and he would get coal and diamond if he smash them. The reward of these two itmes are different, so he should learn which he should smash to get a higher score. 

At the first beginning 10 minuts around 1000 steps, we can see that the agent learns very fast at the beginning, so the score rises quickly. But then it may also be because of studying over, which led to some other points deducted, so the score has dropped. So he changed his strategy and his score rebounded.

returns1000.png![image](https://user-images.githubusercontent.com/57329825/110741857-55101f00-8270-11eb-9370-ddb2306dc4ea.png)

After half hour and 4000 steps, the agent may meet a bottleneck, since the score seems to be stuck at 500, and it stays at 500 for 10 minutes. It may be that the agent has reached the end once and is trying to improve the score through other projects.

returns6000.png![image](https://user-images.githubusercontent.com/57329825/110742151-d071d080-8270-11eb-86ad-8058f5cce668.png)

After one hour again and the number of steps reaches 8000 to 12000, the score stay at 800, and slightly decreased during this period. This may be because 800 is already the highest score that the agent can obtain through long-term learning, so when trying other methods, the score for decreasing. 

returns12000.png![image](https://user-images.githubusercontent.com/57329825/110742518-7cb3b700-8271-11eb-96ac-413945fdf58f.png)


After two hours, we can see from the figure that the agent has always maintained a high score which is 800, so we can guess and infer that the current agent has mastered the best skills and maintained his highest score range.

![image](https://user-images.githubusercontent.com/57329825/110620832-758a9b80-81d4-11eb-9048-6a39541a97cd.png)


<br />
## **References**
