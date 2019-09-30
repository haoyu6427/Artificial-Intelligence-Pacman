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

class OneStepLookAheadAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # get all legal actions for pacman
        legal = state.getLegalPacmanActions()
        # get all the successor state for these actions
        successors = [(state.generatePacmanSuccessor(action), action) for action in legal]
        # evaluate the successor states using scoreEvaluation heuristic
        scored = [(admissibleHeuristic(state), action) for state, action in successors]
        # get best choice
        bestScore = min(scored)[0]
        # get all actions that lead to the highest score
        bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
        # return random action from the list of the best actions
        return random.choice(bestActions)

class BFSAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write BFS Algorithm instead of returning Directions.STOP
        stack = []
        visit = {}
        win = []
        limit = []
        if(state.isWin() == 1):
            return Directions.STOP
        legal = state.getLegalPacmanActions()
        for action in legal:
            if(state.generatePacmanSuccessor(action) != None and state.isLose()!= 1):
                stack.append([state.generatePacmanSuccessor(action), action])
        while(len(stack)>0):
            node,tempaction = stack.pop(0)
            if(node.isWin() == 1):
                win.append([admissibleHeuristic(node),tempaction])
                continue
            if(node.isLose() == 1):
                continue
            if node not in visit:
                visit[node] = 1
                legal = node.getLegalPacmanActions()
                successors = [(node.generatePacmanSuccessor(action), action) for action in legal]
                for success in successors:
                    if(success[0] not in visit):
                        if(success[0] != None):
                            stack.append([success[0],tempaction])
                        else:
                            limit.append([admissibleHeuristic(node),tempaction])
        if(len(win)>0):
            minHeu = min(win)[0]
            for score,action in win:
                if(score == minHeu):
                    return action
        elif(len(limit)>0):
            minHeu = min(limit)[0]
            for score,action in limit:
                if(score == minHeu):
                    return action
        return Directions.STOP
class DFSAgent(Agent):
    visit = {}
    def registerInitialState(self, state):
        self.visit = {}
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        stack = []
        visit = {}
        win = []
        limit = []
        if(state.isWin() == 1):
            return Directions.STOP
        legal = state.getLegalPacmanActions()
        for action in legal:
            if(state.generatePacmanSuccessor(action) != None and state.isLose()!= 1):
                stack.append([state.generatePacmanSuccessor(action), action])
        while(len(stack)>0):
            node,tempaction = stack.pop()
            if(node.isWin() == 1):
                win.append([admissibleHeuristic(node),tempaction])
                continue
            if(node.isLose() == 1):
                continue
            if node not in visit:
                visit[node] = 1
                legal = node.getLegalPacmanActions()
                successors = [(node.generatePacmanSuccessor(action), action) for action in legal]
                for success in successors:
                    if(success[0] not in visit):
                        if(success[0] != None):
                            stack.append([success[0],tempaction])
                        else:
                            limit.append([admissibleHeuristic(node),tempaction])
        if(len(win)>0):
            minHeu = min(win)[0]
            for score,action in win:
                if(score == minHeu):
                    return action
        elif(len(limit)>0):
            minHeu = min(limit)[0]
            for score,action in limit:
                if(score == minHeu):
                    return action
        return Directions.STOP


class AStarAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write A* Algorithm instead of returning Directions.STOP
        return Directions.STOP
