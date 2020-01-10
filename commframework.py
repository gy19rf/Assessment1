# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 13:48:18 2019

@author: gy19rf (Richard Frimpong) Student ID:201377095
"""
"""
Module name: Programming for Geographical Information Analysis (Core skills) 
Module code: GEOG5990
"""
"""
commframework is imported as agentframework to create agents. The agents were to move in the environment, 
eat the grasses in the enviroment, share and interact well with the environment
"""
"""Note: The import operator function is very useful in the building agents to interact  
with the environment because it allows useful data files to be imported to the model.

"""

import random
class Agent():
   
    def __init__(self,i,agents,environment, y, x):
        self.i = i
        self.x = x
        self.y = y
        self.environment = environment
        self.agents =agents
        self.store = 0
       
       
        
        """
        Moving the agents 
        """
    def __str__(self):
        return "Agent(i=" + str(self.i)+ ", store=" + str(self.store) + ", x=" + str(self.x) + ", y=" + str(self.y) + ")"  
    
    def move(self):
                                                                                                                                                                        
        
        """
         #Moving agent y
        """
       
        test = random.random()
        # Either:
        # Increase y by 1 if test is less than 0.5
        # Decrease y by 1 if test is greater than or equal to 0.5
        if test < 0.5:
            #print("y + 1")
            self.y = (self.y+1)%300
        else:
            #print("y - 1")
            self.y = (self.y-1)%300
        
        
        #print("y", y)
        
        
        """
        # Moving agent x
        """
        test = random.random()
        # Either:
        # Increase x by 1 if test is less than 0.5
        # Decrease x by 1 if test is greater than or equal to 0.5
        if test < 0.5:
            
            #print("x + 1")
             self.x = (self.x-1)%300
        else:
            
            #print("x - 1")
              self.x = (self.x+1)%300
       
        #print("x", x)

    """Making agents to eat the grass left from the environment
    """
    def eat(self): 
        
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
       
    """
       Calculating the distance between agents in the environment
       """
    def get_neighbourhood(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
    """
    Making the agents to share what is in the environment with neighbours
    """
    def share(self, d):
        for agent in self.agents:
            if agent != self:
                neighbourhood = self.get_neighbourhood(agent)
                if (neighbourhood < d):
                    print(self, "is sharing with", agent,  "as neighbourhood is", neighbourhood)
                    total = self.store + agent.store
                    ave = total/2
                    self.store = ave 
                    agent.store = ave
