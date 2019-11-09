# useful stuff: enum datatype & many classes: Window, FifoQueue,
#               LifoQueue, PriorityQueue, Set
from utilities import *
import math
######################################################################
# A class to define the maze problem
# Public variables/functions: initState, actions, results, goalTest,
#                             stepCost, pathCost,
#                             drawSolution, heuristic
######################################################################
class Problem:
    def __init__(self):
        #Basic:
        #######
        self.initState = (10,1)
        #Problem-specific:
        ##################
        self.actionType = enum("left","right","up","down")
        self.goalState = (14,4)
        self.maze = [
            [0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
            [0,0,0,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
            [0,0,0,1,1,1,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
            [0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
            [1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
            [0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1,1,1],
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1],
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,1,0,0,1],
            [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0],
            [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0],
            [0,0,1,1,1,0,1,1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0],
            [0,0,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0],
            [1,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0],
            [1,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0],
            [0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            ]

    # calculate the legal actions that could be taken at a given state
    def actions(self,state) :
        (row,col) = state
        legalActions = []
        if col>0 and self.maze[row][col-1]!=1: 
            legalActions += [self.actionType.left]
        if col<24 and self.maze[row][col+1]!=1: 
            legalActions += [self.actionType.right]
        if row>0 and self.maze[row-1][col]!=1: 
            legalActions += [self.actionType.up]
        if row<24 and self.maze[row+1][col]!=1: 
            legalActions += [self.actionType.down]
        return legalActions

    # calculate the next state resulting by taking a specific action
    def result(self,state,action) :
        (row,col) = state
        if action==self.actionType.left: return (row,col-1)
        if action==self.actionType.right: return (row,col+1)
        if action==self.actionType.up: return (row-1,col)
        if action==self.actionType.down: return (row+1,col)

    # check whether the goal is satisfied/reached in a given state
    def goalTest(self,state):
        return state==self.goalState

    # calculate the step cost
    def stepCost(self,state,action): 
        return 1

    # calculate the path cost
    def pathCost(self,state,actionList):
        if actionList==[]: return 0
        return self.stepCost(state,actionList[0]) + \
            pathCost(self.result(state,actionList[0]),actionList[1:])

    #Draw solution and visualize search state space
    def drawSolution(self,title,solution,stateMap={}):
        # Initialize a window
        window = Window(title,(70,70),260,260,"#0000FF")

        # Draw maze, and highlight initial/goal states
        for r in range(25):
            for c in range(25):
                if self.maze[r][c]==0:
                    window.rectangle((75+c*10,75+r*10),10,10,"#FFFFFF")
                else: # self.maze[r][c]==1:
                    window.rectangle((75+c*10,75+r*10),10,10,"#000000")

        # Mark initial
        (r,c)=self.initState
        window.rectangle((75+c*10,75+r*10),10,10,"#00FF00")

        # Mark goal
        (r,c)=self.goalState
        window.rectangle((75+c*10,75+r*10),10,10,"#FF0000")

        # Determine maximum value in state map
        maximum = 1
        for s in stateMap: 
            if stateMap[s]>maximum: 
                maximum = stateMap[s]
        if maximum==1: maximum = 10
        # Visualize search state space by filling squares with 
        # ... shades of grey color
        if self.initState in stateMap: del stateMap[self.initState]
        for (r,c) in stateMap:
            color = 240 - int(float(stateMap[(r,c)]) / maximum * 75)
            window.rectangle((75+c*10,75+r*10),10,10,\
                             "#" + "%x"%color + "%x"%color + "%x"%color)
        # Draw solution
        (r,c)=self.initState
        for a in solution:
            if a==self.actionType.left: #<
                window.line((77+c*10,80+r*10),(80+c*10,78+r*10))
                window.line((77+c*10,80+r*10),(80+c*10,82+r*10))
                (r,c)=(r,c-1)
            elif a==self.actionType.right: #>
                window.line((80+c*10,78+r*10),(83+c*10,80+r*10))
                window.line((80+c*10,82+r*10),(83+c*10,80+r*10))
                (r,c)=(r,c+1)
            elif a==self.actionType.up: #^
                window.line((78+c*10,80+r*10),(80+c*10,77+r*10))
                window.line((82+c*10,80+r*10),(80+c*10,77+r*10))
                (r,c)=(r-1,c)
            else: #a==self.actionType.down: #v
                window.line((78+c*10,80+r*10),(80+c*10,83+r*10))
                window.line((82+c*10,80+r*10),(80+c*10,83+r*10))
                (r,c)=(r+1,c)
        window.display()

    # A heuristic function to estimate how far the goal is from a given state
    def heuristic(self,currentNode, targetNode):

        cost = ((targetNode[0]-currentNode[0])**2 +(targetNode[1]-currentNode[1])**2)

        return cost





        # ********************************
