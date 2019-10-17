# pacmanAgents.py
# ---------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from pacman import Directions
from game import Agent
from heuristics import *
import random
import math

class RandomAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # get all legal actions for pacman
        actions = state.getLegalPacmanActions()
        # returns random action from all the valide actions
        return actions[random.randint(0,len(actions)-1)]

class RandomSequenceAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        self.actionList = [];
        for i in range(0,10):
            self.actionList.append(Directions.STOP);
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # get all legal actions for pacman
        possible = state.getAllPossibleActions();
        for i in range(0,len(self.actionList)):
            self.actionList[i] = possible[random.randint(0,len(possible)-1)];
        tempState = state;
        for i in range(0,len(self.actionList)):
            if tempState.isWin() + tempState.isLose() == 0:
                tempState = tempState.generatePacmanSuccessor(self.actionList[i]);
            else:
                break;
        # returns random action from all the valide actions
        return self.actionList[0];

class HillClimberAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        self.actionList = [];
        for i in range(0,5):
            self.actionList.append(Directions.STOP);
        return;


    # GetAction Function: Called with every frame
    def getAction(self, state):
        mark = 0
        # TODO: write Hill Climber Algorithm instead of returning Directions.STOP
        possible = state.getAllPossibleActions();
        for i in range(0,len(self.actionList)):
            self.actionList[i] = possible[random.randint(0,len(possible)-1)];
        tempState = state;
        for i in range(0,len(self.actionList)):
            if tempState.isWin() + tempState.isLose() == 0:
                if(tempState.generatePacmanSuccessor(self.actionList[i]) == None):
                    break
                else:
                    tempState = tempState.generatePacmanSuccessor(self.actionList[i]);
            else:
                break;
        score = gameEvaluation(state, tempState)
        while(mark == 0):
            newSeq = self.actionList[:]
            for i in range(0, len(newSeq)):
                if (random.randint(0, 1) == 1):
                    newSeq[i] = possible[random.randint(0, len(possible) - 1)]
            tempState = state;
            for i in range(0,len(self.actionList)):
                if tempState.isWin() + tempState.isLose() == 0:
                    check = tempState.generatePacmanSuccessor(self.actionList[i]) == None
                    if(check):
                        mark = 1
                        break
                    else:
                        tempState = check
                    break;
            newscore = gameEvaluation(state, tempState)
            if(newscore >= score):
                score = newscore
                self.actionList = newSeq[:]
        return self.actionList[0];

class GeneticAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        self.actionList = [];
        for i in range(0,5):
            self.actionList.append(Directions.STOP);
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        mark = 0
        # TODO: write Genetic Algorithm instead of returning Directions.STOP
        popSeq = []
        score = [[],0]
        possible = state.getAllPossibleActions();
        for j in range(8):
            for i in range(0,len(self.actionList)):
                self.actionList[i] = possible[random.randint(0,len(possible)-1)]
            popSeq.append(self.actionList[:])
        while(mark == 0):
            rankpop = []
            for i in range(len(popSeq)):
                tempState = state
                for j in range(len(self.actionList)):
                    if tempState.isWin() + tempState.isLose() == 0:
                        check = tempState.generatePacmanSuccessor(popSeq[i][j])
                        if(check == None):
                            mark = 1
                            break
                        else:
                            tempState = check
                    else:
                        break;
                tempscore = gameEvaluation(state, tempState)
                rankpop.append((popSeq[i][:], tempscore))
            rankpop = sorted(rankpop, key = lambda x:x[1])
            if(rankpop[-1][1] >= score[1]):
                score = (rankpop[-1][0][0], rankpop[-1][1])
            newpop = []
            for i in range(4):
                candchro = []
                for j in range(2):
                    test = random.randint(1, 36)
                    if(test >=1 and test <=8):
                        candchro.append(rankpop[7][0][:])
                    elif(test >=9 and test <=15):
                        candchro.append(rankpop[6][0][:])
                    elif(test >=16 and test <=21):
                        candchro.append(rankpop[5][0][:])
                    elif(test >=22 and test <=26):
                        candchro.append(rankpop[4][0][:])
                    elif(test >=27 and test <=30):
                        candchro.append(rankpop[3][0][:])
                    elif(test >=31 and test <=33):
                        candchro.append(rankpop[2][0][:])
                    elif(test >=34 and test <=35):
                        candchro.append(rankpop[1][0][:])
                    else:
                        candchro.append(rankpop[0][0][:])
                test2 = random.randint(0, 10)
                if(test2 <= 7):
                    for j in range(len(candchro)):
                        test3 = random.randint(0, 1)
                        if(test3 == 1):
                            temp = candchro[0][j]
                            candchro[0][j] = candchro[1][j]
                            candchro[1][j] = temp
                newpop.append(candchro[0][:])
                newpop.append(candchro[1][:])
            for i in range(len(newpop)):
                test4 = random.randint(0, 10)
                if(test4 <= 1):
                    newpop[i][random.randint(0, len(newpop[i])-1)] = possible[random.randint(0, len(possible) - 1)]
            popSeq = newpop
        return score[0]

class MCTSAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write MCTS Algorithm instead of returning Directions.STOP
        return Directions.STOP
