# Rllib docs: https://docs.ray.io/en/latest/rllib.html

try:
    from malmo import MalmoPython
except:
    import MalmoPython

import sys
import time
import json
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint
import random

import gym, ray
from gym.spaces import Discrete, Box
from ray.rllib.agents import ppo


class CallMePro(gym.Env):

    def __init__(self, env_config):
        # Static Parameters
        self.penalty_density = .02
        self.obs_size = 5
        self.log_frequency = 10
<<<<<<< HEAD
        self.max_episode_steps = 400
=======
        self.max_episode_steps = 200
>>>>>>> d6624e565e9a53a840f5951e2e48a0c34cdfae2e
        self.action_dict = {
            0: 'move 0',  # Stop
            1: 'strafe 1',  # Move one block left
            2: 'strafe -1',  # Move one block right
<<<<<<< HEAD
            3: 'attack 1',
=======
>>>>>>> d6624e565e9a53a840f5951e2e48a0c34cdfae2e
        }

        # Rllib Parameters
        self.action_space = Discrete(len(self.action_dict))
        self.observation_space = Box(0, 1, shape=(2 * self.obs_size * self.obs_size, ), dtype=np.float32)

        # Malmo Parameters
        self.agent_host = MalmoPython.AgentHost()
        try:
            self.agent_host.parse( sys.argv )
        except RuntimeError as e:
            print('ERROR:', e)
            print(self.agent_host.getUsage())
            exit(1)

        # CallMePro Parameters
        self.obs = None
        self.face_brick_move = False
        self.face_gold_move = False
<<<<<<< HEAD
        self.face_diamond_move = False
        self.face_stone_move = False
        self.face_diamondblock_move = False
        self.face_coal_move = False
=======
>>>>>>> d6624e565e9a53a840f5951e2e48a0c34cdfae2e
        self.episode_step = 0
        self.episode_return = 0
        self.returns = []
        self.steps = []

    def reset(self):
        """
        Resets the environment for the next episode.

        Returns
            observation: <np.array> flattened initial obseravtion
        """
        # Reset Malmo
        world_state = self.init_malmo()

        # Reset Variables
        self.returns.append(self.episode_return)
        current_step = self.steps[-1] if len(self.steps) > 0 else 0
        self.steps.append(current_step + self.episode_step)
        self.episode_return = 0
        self.episode_step = 0

        # Log
        if len(self.returns) > self.log_frequency + 1 and \
            len(self.returns) % self.log_frequency == 0:
            self.log_returns()

        # Get Observation
        #self.obs = self.get_observation(world_state)
<<<<<<< HEAD
        self.obs, self.face_brick_move, self.face_gold_move, self.face_diamond_move, self.face_stone_move, self.face_diamondblock_move, self.face_coal_move = self.get_observation(world_state)
=======
        self.obs, self.face_brick_move, face_gold_move = self.get_observation(world_state)
>>>>>>> d6624e565e9a53a840f5951e2e48a0c34cdfae2e

        return self.obs

    def step(self, action):
        """
        Take an action in the environment and return the results.

        Args
            action: <int> index of the action to take

        Returns
            observation: <np.array> flattened array of obseravtion
            reward: <int> reward from taking action
            done: <bool> indicates terminal state
            info: <dict> dictionary of extra information
        """

        # Get Action
<<<<<<< HEAD
        if(self.face_stone_move == True):
            self.agent_host.sendCommand('move 1')
            time.sleep(.2)

        if(self.face_diamondblock_move == True):
            self.agent_host.sendCommand('move 1')
            time.sleep(.2)
            self.agent_host.sendCommand('move 1')
            time.sleep(.2)

        # if(self.face_stone_move == False and self.face_diamondblock_move == False and self.face_brick_move == False and self.face_gold_move == False and self.face_diamond_move == False and self.face_coal_move == False):
        #     print("im here")
        #     if(action != 0):
        #         if(action != 3):
        #             command = 'move 1'
        #             self.agent_host.sendCommand(command)
        #             command = self.action_dict[action]
        #             self.agent_host.sendCommand(command)
        #             time.sleep(.2)
        #             self.episode_step += 1
        
        #self.obs, self.allow_break_action = self.get_observation(world_state)
        #print("true or false: ", self.select_move_action)

        if(self.face_brick_move == True):
            if(action != 0):
                if(action != 3):
                    command = 'move 1'
                    self.agent_host.sendCommand(command)
                    command = self.action_dict[action]
                    self.agent_host.sendCommand(command)
                    time.sleep(.2)
                    self.episode_step += 1
            
        if(self.face_gold_move == True):
            if(action != 3):
                command = 'move 1'
                self.agent_host.sendCommand(command)
=======
        self.agent_host.sendCommand('move 1')
        time.sleep(.2)
        
        #self.obs, self.allow_break_action = self.get_observation(world_state)
        #print("true or false: ", self.select_move_action)
        if(self.face_brick_move == True):
            if(action != 0):
>>>>>>> d6624e565e9a53a840f5951e2e48a0c34cdfae2e
                command = self.action_dict[action]
                self.agent_host.sendCommand(command)
                time.sleep(.2)
                self.episode_step += 1
<<<<<<< HEAD

        if(self.face_diamond_move == True):
            if(action != 0):
                if(action == 3):
                    command = self.action_dict[action]
                    self.agent_host.sendCommand(command)
                    time.sleep(0.8)
                    self.agent_host.sendCommand('move 1')
                else:
                    command = self.action_dict[action]
                    self.agent_host.sendCommand(command)
                time.sleep(.2)
                self.episode_step += 1

        if(self.face_coal_move == True):
            if(action != 0):
                if(action == 3):
                    command = self.action_dict[action]
                    self.agent_host.sendCommand(command)
                    time.sleep(0.8)
                    self.agent_host.sendCommand('move 1')
                else:
                    command = self.action_dict[action]
                    self.agent_host.sendCommand(command)
                time.sleep(.2)
                self.episode_step += 1
=======
            
        if(self.face_gold_move == True):
            command = 'move 1'
            self.agent_host.sendCommand(command)
            command = self.action_dict[action]
            self.agent_host.sendCommand(command)
            time.sleep(.2)
            self.episode_step += 1
>>>>>>> d6624e565e9a53a840f5951e2e48a0c34cdfae2e

        # Get Observation
        world_state = self.agent_host.getWorldState()
        for error in world_state.errors:
            print("Error:", error.text)
        #self.obs = self.get_observation(world_state)
<<<<<<< HEAD
        self.obs, self.face_brick_move, self.face_gold_move, self.face_diamond_move, self.face_stone_move, self.face_diamondblock_move, self.face_coal_move = self.get_observation(world_state)
=======
        self.obs, self.face_brick_move, self.face_gold_move = self.get_observation(world_state)
>>>>>>> d6624e565e9a53a840f5951e2e48a0c34cdfae2e

        # Get Done
        done = not world_state.is_mission_running

        # Get Reward
        reward = 0
        for r in world_state.rewards:
            reward += r.getValue()
        self.episode_return += reward

        return self.obs, reward, done, dict()

    def get_mission_xml(self):
        # def setLava():
        #     my_xml = ""
        #     for j in range(0, 25):
        #         for i in range(-5, 6):
        #             lavaNumber = random.choice(range(0, 100))
        #             if(lavaNumber < 5):
        #                 #my_xml += '<DrawBlock x=\'' + str(x) + '\' y=\'1\' ' + 'z=\'' + str(z*4+1) + '\' type=\'lava\'/>\n'
        #                 my_xml += "<DrawBlock x='{}' y='1' z='{}' type='lava' />".format(i, randint(4*j+1, 4*j+3))
        #     return my_xml

        def initmap():
            my_xml = ""
            for z in range(0, 201):
                for y in range(2, 11):
                    my_xml += '<DrawBlock y=\'' + str(y) + '\' x=\'-10\' ' + 'z=\'' + str(z) + '\' type=\'lava\'/>\n'
                    my_xml += '<DrawBlock y=\'' + str(y) + '\' x=\'10\' ' + 'z=\'' + str(z) + '\' type=\'lava\'/>\n'

            for x in range(-5,6):
<<<<<<< HEAD
                my_xml += '<DrawBlock x=\'' + str(x) + '\' y=\'1\' ' + 'z=\'201\' type=\'diamond_block\'/>\n'
                for z in range(0, 51):
=======
                my_xml += '<DrawBlock x=\'' + str(x) + '\' y=\'1\' ' + 'z=\'101\' type=\'diamond_block\'/>\n'
                for z in range(0, 26):
>>>>>>> d6624e565e9a53a840f5951e2e48a0c34cdfae2e
                    my_xml += '<DrawBlock x=\'' + str(x) + '\' y=\'1\' ' + 'z=\'' + str(4 * z) + '\' type=\'gold_block\'/>\n'
            return my_xml

        def obstacle():
            my_xml = ""
            for x in range(-5,6):
                if(x < -1 or x > 1):
                    for y in range(2, 3):
                        my_xml += '<DrawBlock x=\'' + str(x) + '\' y=\'' + str(y) + '\' ' + 'z=\'0\' type=\'brick_block\'/>\n'
<<<<<<< HEAD

            for z in range(1, 51):
                nblocks = random.choice(range(1, 7))
                probdiamond = random.choice(range(1, 201))

=======

            for z in range(1, 26):
                nblocks = random.choice(range(1, 7))
                probdiamond = random.choice(range(1, 101))

>>>>>>> d6624e565e9a53a840f5951e2e48a0c34cdfae2e
                for x in range(-5, -5+nblocks):
                    for y in range(2, 3):
                        my_xml += '<DrawBlock x=\'' + str(x) + '\' y=\'' + str(y) + '\' ' + 'z=\'' + str(4 * z) + '\' type=\'brick_block\'/>\n'

                for x in range(max(-2+nblocks, 0), 6):
                    for y in range(2, 3):
                        my_xml += '<DrawBlock x=\'' + str(x) + '\' y=\'' + str(y) + '\' ' + 'z=\'' + str(4 * z) + '\' type=\'brick_block\'/>\n'

<<<<<<< HEAD
                if(z != 50):
                    coal_number = random.choice(range(0, 3))
                    for h in range(0, coal_number):
                        my_xml += "<DrawBlock x='{}' y='2' z='{}' type='coal_ore' />".format(randint(-5+nblocks, max(-2+nblocks, 0)), randint(4*z+1, 4*z+3))

                    diamond_number = random.choice(range(0, 3))
                    for h in range(0, diamond_number):
                        my_xml += "<DrawBlock x='{}' y='2' z='{}' type='diamond_ore' />".format(randint(-5+nblocks, max(-2+nblocks, 0)), randint(4*z+1, 4*z+3))

                # if probdiamond > 75:
                #     diamondpos = random.choice(range(-5+nblocks, -2+nblocks))
                #     my_xml += '<DrawItem x=\'' + str(diamondpos) + '\' y=\'2\' ' + 'z=\'' + str(4 * z) + '\' type=\'diamond\'/>\n'

            # for i in range(60):
            #     j = random.choice(range(1, 101))
            #     if(j % 4 != 0):
            #         my_xml += "<DrawBlock x='{}' y='2' z='{}' type='diamond_ore' />".format(randint(-5, 6), j)

            # for i in range(30):
            #     j = random.choice(range(1, 101))
            #     if(j % 4 != 0):
            #         my_xml += "<DrawBlock x='{}' y='2' z='{}' type='coal_ore' />".format(randint(-5, 6), j)
=======
                if probdiamond > 75:
                    diamondpos = random.choice(range(-5+nblocks, -2+nblocks))
                    my_xml += '<DrawItem x=\'' + str(diamondpos) + '\' y=\'2\' ' + 'z=\'' + str(4 * z) + '\' type=\'diamond\'/>\n'
>>>>>>> d6624e565e9a53a840f5951e2e48a0c34cdfae2e

            return my_xml

        return '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
                <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

                    <About>
                        <Summary>CallMePro</Summary>
                    </About>

                    <ServerSection>
                        <ServerInitialConditions>
                            <Time>
                                <StartTime>12000</StartTime>
                                <AllowPassageOfTime>false</AllowPassageOfTime>
                            </Time>
                            <Weather>clear</Weather>
                        </ServerInitialConditions>
                        <ServerHandlers>
                            <FlatWorldGenerator generatorString="3;7,2;1;"/>
                            <DrawingDecorator>
                                ''' + \
                                "<DrawCuboid x1='{}' x2='{}' y1='2' y2='2' z1='{}' z2='{}' type='air'/>".format(-6, 6, 0, 201) + \
                                "<DrawCuboid x1='{}' x2='{}' y1='1' y2='1' z1='{}' z2='{}' type='stone'/>".format(-6, 6, 0, 201) + \
                                initmap() + \
                                obstacle() + \
                                '''
                            </DrawingDecorator>
                            <ServerQuitWhenAnyAgentFinishes/>
                        </ServerHandlers>
                    </ServerSection>

                    <AgentSection mode="Survival">
                        <Name>CallMePro</Name>
                        <AgentStart>
                            <Placement x="0.5" y="2" z="-0.5" pitch="45" yaw="0"/>
                            <Inventory>
                                <InventoryItem slot="0" type="diamond_pickaxe"/>
                            </Inventory>
                        </AgentStart>
                        <AgentHandlers>
                            <RewardForCollectingItem>
                            <Item reward = "10" type = "diamond" />
<<<<<<< HEAD
                            <Item reward = "-10" type = "coal" />
=======
>>>>>>> d6624e565e9a53a840f5951e2e48a0c34cdfae2e
                            </RewardForCollectingItem>
                            <RewardForTouchingBlockType>
                            <Block reward = "10" type = "gold_block" />
                            <Block reward = "-10" type = "lava" />
                            <Block reward = "100" type = "diamond_block" />
                            <Block reward = "-1" type = "stone" />
                            </RewardForTouchingBlockType>
                            <DiscreteMovementCommands/>
                            <ObservationFromFullStats/>
                            <ObservationFromRay/>
                            <ObservationFromGrid>
                                <Grid name="floorAll">
                                    <min x="-'''+str(int(self.obs_size/2))+'''" y="-1" z="-'''+str(int(self.obs_size/2))+'''"/>
                                    <max x="'''+str(int(self.obs_size/2))+'''" y="0" z="'''+str(int(self.obs_size/2))+'''"/>
                                </Grid>
                            </ObservationFromGrid>
                            <AgentQuitFromTouchingBlockType>
                                <Block type="diamond_block" />
                            </AgentQuitFromTouchingBlockType>
                            <AgentQuitFromReachingCommandQuota total="'''+str(self.max_episode_steps)+'''" />
                        </AgentHandlers>
                    </AgentSection>
                </Mission>'''

    def init_malmo(self):
        """
        Initialize new malmo mission.
        """
        my_mission = MalmoPython.MissionSpec(self.get_mission_xml(), True)
        my_mission_record = MalmoPython.MissionRecordSpec()
        my_mission.requestVideo(800, 500)
        my_mission.setViewpoint(1)

        max_retries = 3
        my_clients = MalmoPython.ClientPool()
        my_clients.add(MalmoPython.ClientInfo('127.0.0.1', 10000)) # add Minecraft machines here as available

        for retry in range(max_retries):
            try:
                self.agent_host.startMission( my_mission, my_clients, my_mission_record, 0, 'CallMePro' )
                break
            except RuntimeError as e:
                if retry == max_retries - 1:
                    print("Error starting mission:", e)
                    exit(1)
                else:
                    time.sleep(2)

        world_state = self.agent_host.getWorldState()
        while not world_state.has_mission_begun:
            time.sleep(0.1)
            world_state = self.agent_host.getWorldState()
            for error in world_state.errors:
                print("\nError:", error.text)

        return world_state

    def get_observation(self, world_state):
        """
        Use the agent observation API to get a flattened 2 x 5 x 5 grid around the agent.
        The agent is in the center square facing up.

        Args
            world_state: <object> current agent world state

        Returns
            observation: <np.array> the state observation
            allow_break_action: <bool> whether the agent is facing a diamond
        """
        obs = np.zeros((2 * self.obs_size * self.obs_size, ))
        face_brick_move = False
        face_gold_move = False
<<<<<<< HEAD
        face_diamond_move = False
        face_stone_move = False
        face_diamondblock_move = False
        face_coal_move = False
=======
>>>>>>> d6624e565e9a53a840f5951e2e48a0c34cdfae2e

        while world_state.is_mission_running:
            time.sleep(0.1)
            world_state = self.agent_host.getWorldState()
            if len(world_state.errors) > 0:
                raise AssertionError('Could not load grid.')

            if world_state.number_of_observations_since_last_state > 0:
                # First we get the json from the observation API
                msg = world_state.observations[-1].text
                observations = json.loads(msg)

                # Get observation
                grid = observations['floorAll']
                for i, x in enumerate(grid):
                    if x == 'brick_block' or x == 'lava':
                        obs[i] = 1
                    else:
                        obs[i] = 0

                # Rotate observation with orientation of agent
                obs = obs.reshape((2, self.obs_size, self.obs_size))
                yaw = observations['Yaw']
                if yaw >= 225 and yaw < 315:
                    obs = np.rot90(obs, k=1, axes=(1, 2))
                elif yaw >= 315 or yaw < 45:
                    obs = np.rot90(obs, k=2, axes=(1, 2))
                elif yaw >= 45 and yaw < 135:
                    obs = np.rot90(obs, k=3, axes=(1, 2))
                obs = obs.flatten()
                
                face_brick_move = observations['LineOfSight']['type'] == 'brick_block'
                face_gold_move = observations['LineOfSight']['type'] == 'gold_block'
<<<<<<< HEAD
                face_diamond_move = observations['LineOfSight']['type'] == 'diamond_ore'
                face_stone_move = observations['LineOfSight']['type'] == 'stone'
                face_diamondblock_move = observations['LineOfSight']['type'] == 'diamond_block'
                face_coal_move = observations['LineOfSight']['type'] == 'coal_ore'

                break

        return obs, face_brick_move, face_gold_move, face_diamond_move, face_stone_move, face_diamondblock_move, face_coal_move
=======

                break

        return obs, face_brick_move, face_gold_move
>>>>>>> d6624e565e9a53a840f5951e2e48a0c34cdfae2e

    def log_returns(self):
        """
        Log the current returns as a graph and text file

        Args:
            steps (list): list of global steps after each episode
            returns (list): list of total return of each episode
        """
        box = np.ones(self.log_frequency) / self.log_frequency
        returns_smooth = np.convolve(self.returns[1:], box, mode='same')
        plt.clf()
        plt.plot(self.steps[1:], returns_smooth)
        plt.title('CallMePro')
        plt.ylabel('Reward')
        plt.xlabel('Steps')
        plt.savefig('returns.png')

        with open('returns.txt', 'w') as f:
            for step, value in zip(self.steps[1:], self.returns[1:]):
                f.write("{}\t{}\n".format(step, value))


if __name__ == '__main__':
    ray.init()
    trainer = ppo.PPOTrainer(env=CallMePro, config={
        'env_config': {},           # No environment parameters to configure
        'framework': 'torch',       # Use pyotrch instead of tensorflow
        'num_gpus': 0,              # We aren't using GPUs
        'num_workers': 0            # We aren't using parallelism
    })

    while True:
        print(trainer.train())
