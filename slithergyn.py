import gym
import slither_api
from gym import spaces
import numpy as np
import time

class SlitherEnv(gym.Env):

  def __init__(self):
    #inint
    n_actions=8
    self.action_space = spaces.Discrete(n_actions)
    self.height =515
    self.width = 956
    self.observation_space = spaces.Box(low = 0 ,high =255,shape = (self.height,self.width,1),dtype = np.uint8)
    self.lastscore = 0
    self.initTime = time.time()
    #self.reset()


  def reset(self):
    self.initTime = time.time()
    slither_api.begingame()
    self.lastscore = 0
    observation = self.getobservation()
    return observation

  def step(self, action):
    self.takeaction(action)
    done = slither_api.endedgame()
    currentTime = time.time()
    difftime = currentTime -  self.initTime
    if (difftime<10):
      done = False
    currentscore = slither_api.readcurrentscore()
    reward = currentscore - self.lastscore
    self.lastscore = currentscore
    observation = self.getobservation()
    print("current score: ",currentscore,"Reward: ",reward ,"Done",done)

    return observation,reward,done,{}

  def takeaction(self,action):
    if action == 0:
      slither_api.movetoTop()
    elif action == 1:
      slither_api.movetoDown()
    elif action == 2:
      slither_api.movetoLeft()
    elif action == 3:
      slither_api.movetoRight()
    elif action == 4:
      slither_api.movetoTopLeft()
    elif action == 5:
      slither_api.movetoTopRight()
    elif action == 6:
      slither_api.movetoBottomLeft()
    elif action == 7:
      slither_api.movetoBottomRight()

  def getobservation(self):
    return slither_api.returngamescreen(self.width,self.height)




  def render(self, mode='human'):
    pass


