######################################################################
# A class representing a node in the search tree/graph
# Public functions: child, solution
######################################################################
class Node:
    # Create a node
    def __init__(self,state,parent,action,pathCost):
        self.state = state
        self.parent = parent
        self.action = action
        self.pathCost = pathCost

    # Calculate the child node resulting by taking a given action
    def child (self,problem,action):
        newstate = problem.result(self.state,action)
        g  = self.pathCost+problem.stepCost(self.state,action)
        return Node(newstate, self,action,g)

    # Calculate the list of actions taken to reach the node
    def __solution__(node):
        if node.parent==None: return []
        return Node.__solution__(node.parent) + [node.action]
    
    def solution (self): return Node.__solution__(self)

######################################################################
# A class to display info about the frontier states & the explored stats
# Public functions: fPlusPlus, fMinusMinus, fMinusPlus, ePlusPlus
######################################################################
class Stats:
    # Initialize the statistics counters
    def __init__(self):
        self.data = {}
        self.frontier=0
        self.explored=0

    # a state is added to frontier
    def fPlusPlus(self,state):
        self.frontier += 1
        print("[F++] ", state, " -  F=", self.frontier, " -  E=", self.explored)

    # a state is removed from frontier
    def fMinusMinus(self,state):
        self.frontier -= 1
        print("[F--] ", state, " -  F=", self.frontier, " -  E=", self.explored)

    # a state is removed from frontier and another is added instead
    def fMinusPlus(self,state,pathCost1,pathCost2):
        print("[F-+] ", state, " -  C=", pathCost1,">>", pathCost2,\
            " -  F=", self.frontier, " -  E=", self.explored)

    # a state is added to the explored set
    def ePlusPlus(self,state):
        if state in self.data: 
            self.data[state] += 1
        else: 
            self.data[state] = 1
        self.explored += 1
        print("[E++] ", state, " -  F=", self.frontier, " -  E=", self.explored)
