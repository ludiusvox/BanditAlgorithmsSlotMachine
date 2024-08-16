#!/usr/bin/env python3
"""
Sample Stationary Bandit Skeleton.
Author: Dr. Collin F. Lynch

This code probides a basic skeleton for the 
stationary bandit code.  It should be adapted
by the students for their work.
"""
#Solved by Aaron Linder

import csv, random
import sys
import numpy as np
import random
arm1= .25
arm2= .25
arm3= .25
arm4= .25
arms = {}       
class BanditSet(object):
    """
    This object represents a set of arms for a stationary multi-armed 
    bandit problem it will store a fixed set of arms from a set and
    will then maintain them over multiple iterations.
    """
    InitialWeight = .25
    CumulativeReward = 0

    
    def __init__(self, DataRows, ArmNames, ExpRate,
                 DistribParam, DecayRate, RewardWeight):
        """
        This initializes the set of choices by acting as a factory
        class to create one arm instance for each of the choices.
        The names and the rows will come from the file that 
        is read in. 
        """
        
        # Store the Data for later use.
        self.Data = DataRows
        
        self.CumulativeReward = 0
        
        # Initialize the parameters.
        self.ExplorationRate       = ExpRate
        self.DistributionParameter = DistribParam
        self.DecayRate             = DecayRate
        self.RewardWeight          = RewardWeight
        
        # Store items for each of the arms.
        self.Name         = ArmNames
        
        # Store a list for the weights.
        self.Weights       = [-1 for I in len(ArmNames)]

        # Calculate the starting probability and add it.
        StartProb = 1 / float(len([1,2,3,4]))
        self.Probabilities = [StartProb for I in len(ArmNames)]

        # And store the Cumulative Reward
        self.CumulativeReward = 0



    def handleRows(self,Names,data):
        """
        Process each of the rows and update our running reward 
        and the basic probabilies for each one.
        """
        # We initialize the cumulative
        # Reward to be 0
        
        # Now iterate over the rows and make each
        # of the choices.
        Index= 1
        y=0
        CumulativeReward = 0
        rows = data.shape[0]
        cols = data.shape[1]
        it = np.iterable(data)
       
        for Index in range(0, rows):
            number = BanditSet.pickArmIndex(self,arm1, arm2, arm3, arm4, Index)
            print("Choice made: "+ str(number))
            if number == 1:    
            
                value = data[Index, cols-4]
                print("value is: " + str(value))
        
                if value == 1:
                    print("Value Exists:")
                    Names=Names+1
                    print("Iteration: " +str(Names))
                   
                    
                    BanditSet.pickArmIndex(self,arm1+.9,arm2,arm3,arm4, Index)
                    BanditSet.CumulativeReward=BanditSet.CumulativeReward+.9
                    
                    
                elif value == 0:
                    Names=Names+1
                    print("Slot Failed")
                    print("Iteration: " +str(Names))
                    BanditSet.pickArmIndex(self,arm1*.6,arm2*.6,arm3*.6,arm4*.6, Index)
            if number == 2:    
            
                value = data[Index, cols-3]
                print("value is: " + str(value))
        
                if value == 1:
                    print("Value Exists:")
                    Names=Names+1
                    print("Iteration: " +str(Names))
                   
                    BanditSet.pickArmIndex(self,arm1,arm2+.9,arm3,arm4, Index)
                    BanditSet.CumulativeReward=BanditSet.CumulativeReward+.9
                    
                   
                    
                elif value == 0:
                    Names=Names+1
                    print("Slot Failed")
                    print("Iteration: " +str(Names))  
                    BanditSet.pickArmIndex(self,arm1*.6,arm2*.6,arm3*.6,arm4*.6, Index)
            if number == 3:    
            
                value = data[Index, cols-2]
                print("Value is : " + str(value))
        
                if value == 1:
                    print("Value Exists:")
                    Names=Names+1
                    print("Iteration: " +str(Names))
                   
                    BanditSet.pickArmIndex(self,arm1,arm2,arm3+.9,arm4, Index)
                    BanditSet.CumulativeReward=BanditSet.CumulativeReward+.9
                    
                    
                    
                elif value == 0:
                    Names=Names+1
                    print("Slot Failed")
                    print("Iteration: " +str(Names))
                    BanditSet.pickArmIndex(self,arm1*.6,arm2*.6,arm3*.6,arm4*.6, Index)
            if number == 4:    
            
                value = data[Index, cols-1]
                print("Value is : " + str(value))
        
                if value == 1:
                    print("Value Exists:")
                    Names=Names+1
                    print("Iteration: " +str(Names))
                   
                    BanditSet.pickArmIndex(self,arm1,arm2,arm3,arm4 +.9, Index)
                    BanditSet.CumulativeReward=BanditSet.CumulativeReward+.9
                    
                elif value == 0:
                    Names=Names+1
                    print("Slot Failed")
                    print("Iteration: " +str(Names))
                    BanditSet.pickArmIndex(self,arm1*.6,arm2*.6,arm3*.6,arm4*.6, Index)
        # Return the cumulative reward.
                 
        

    def pickArmIndex(self,arm1,arm2,arm3,arm4, Index):
        """
        Pick an index based upon the probabilities
        using the cumulative score approach based
        upon a random value.
        """
        
        arm1 = arm1*(1-(.3*.1))

        arm2 = arm2*(1-(.3*.1))
        arm3 = arm3*(1-(.3*.1))
        arm4 = arm4*(1-(.3*.1))
        arms[Index] = {arm1,arm2,arm3,arm4}
        sum = arm1+arm2+arm3+arm4
        print("Arm1 " +str(arm1)+" Arm2 "  +str(arm2)+" Arm3 "  +str(arm3) +" Arm4 "  +str(arm4))
        print("sum: " + str(sum))
        BanditSet.DistributionParameter = (arm1+arm2+arm3+arm4)
        print("Distribution paremeter "+ str(BanditSet.DistributionParameter))
        normal = BanditSet.DistributionParameter/sum
        print("normal is: "+ str(normal))
        number =normal *sum
        print("probability is: " + str(number))
        numero = [1,2,3,4]
        numbera = random.choices(numero, weights = [arm1,arm2,arm3,arm4])
        if numbera == [1]:
            return 1
        elif numbera == [2]:
            return 2
        elif numbera == [3]:
            return 3
        elif numbera == [4]:
            return 4
        else:
            print("error")
            return


    def getReward(self, Names):
        """
        Use the Armnames to get the rewrd for the 
        chosen arm.
        """
        self.RewardWeight = self.RewardWeight+.9
        
        return self.RewardWeight
        
    
    def UpdateWeight(self, Names, Reward):
        uprob = BanditSet.DecayRate * BanditSet.RewardWeight * BanditSet.InitialWeight
        
        return uprob


    def updateProbability(self, Names):
        uprob2 = BanditSet.UpdateWeight(self,Names,Reward=.9)*.25
        return uprob2


    def normalizeProbabilities(self, Names, Reward):
        """
        Normalize the probability values.
        """
        
        pprob = BanditSet.UpdateWeight(self,Names, Reward)/BanditSet.updateProbability(self,Names)
        return pprob

def main():
        
        file = sys.argv[1]
        firstarray = np.genfromtxt(file, dtype=int, delimiter=",")
       
        
        
        Names=0
        BanditSet.DecayRate = .6
        BanditSet.ExplorationRate = .1
        BanditSet.DistributionParameter = .3
        BanditSet.RewardWeight = .9
        InitialWeight = .25
       
        BanditSet.handleRows(BanditSet,Names,firstarray)
        print("total reward: " + str(BanditSet.CumulativeReward))
        print("Done")
        
          
if __name__=="__main__":
   main() 
