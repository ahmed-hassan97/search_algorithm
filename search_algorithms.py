# Utilities: enum datatype & many classes: Window, FifoQueue,
#            LifoQueue, PriorityQueue, Set
from utilities import *

# Search Utilities: Stats class and Node class
from search_utilities import *

######################################################################
# BFS Tree Search
######################################################################
def bfsTree(problem):
    stats = Stats()
    node = Node(problem.initState,None,None,0)
    if problem.goalTest(node.state): return (node.solution(),stats)
    frontier = FifoQueue()
    frontier.add(node)
    stats.fPlusPlus(node.state) #**
    while True:
        if frontier.isEmpty(): return (None,stats) 
        node = frontier.pop()
        stats.fMinusMinus(node.state) #** 
        stats.ePlusPlus(node.state) #**
        for action in problem.actions(node.state):
            child = node.child(problem,action)
            if problem.goalTest(child.state): return (child.solution(),stats)
            frontier.add(child)
            stats.fPlusPlus(child.state) #**

######################################################################
def dfsTree(problem):
    stats = Stats()
    node = Node(problem.initState,None,None,0)
    if problem.goalTest(node.state): return (node.solution(),stats)
    frontier = LifoQueue()
    frontier.add(node)
    stats.fPlusPlus(node.state) #**
    while True:
        if frontier.isEmpty(): return (None,stats)
        node = frontier.pop()
        stats.fMinusMinus(node.state) #**
        stats.ePlusPlus(node.state) #**
        for action in problem.actions(node.state):
            child = node.child(problem,action)
            if problem.goalTest(child.state): return (child.solution(),stats)
            frontier.add(child)
            stats.fPlusPlus(child.state) #**

######################################################################
# UCS Tree Search
######################################################################
def ucsTree(problem):
    stats = Stats()
    def f (x): return x.pathCost
    node = Node(problem.initState,None,None,0)
    frontier = PriorityQueue()

    frontier.add(node,f(node))
    stats.fPlusPlus(node.state) #**
    while True:
        if frontier.isEmpty(): return (None,stats) 
        node = frontier.pop()
        stats.fMinusMinus(node.state) #**
        if problem.goalTest(node.state): return (node.solution(),stats) 
        stats.ePlusPlus(node.state) #**
        for action in problem.actions(node.state):
            child = node.child(problem,action) 
            frontier.add(child,f(child)) 
            stats.fPlusPlus(child.state) #**

######################################################################
# BFS Graph Search
######################################################################
def bfsGraph(problem):
    stats = Stats()  # **

    # ********************************
    # REPLACE THIS LINE WITH YOUR CODE
    node = Node(problem.initState, None, None, 0)
    if problem.goalTest(node.state): return (node.solution(), stats)
    frontier = FifoQueue()
    explored = FifoQueue()
    frontier.add(node)
    stats.fPlusPlus(node.state)  # **
    while True:
        if frontier.isEmpty(): return (None, stats)
        node = frontier.pop()
        explored.add(node)
        stats.fMinusMinus(node.state)  # **
        stats.ePlusPlus(node.state)  # **
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            if (not (frontier.find(child.state)) and not (explored.find(child.state))):

                if problem.goalTest(child.state): return (child.solution(), stats)
                frontier.add(child)
                stats.fPlusPlus(child.state)

######################################################################
# DFS Graph Search       
######################################################################
def dfsGraph(problem):
    stats = Stats()
    node = Node(problem.initState, None, None, 0)
    if problem.goalTest(node.state): return (node.solution(), stats)
    frontier = LifoQueue()
    explored =LifoQueue()
    frontier.add(node)
    stats.fPlusPlus(node.state)  # **
    while True:
        if frontier.isEmpty(): return (None, stats)
        node = frontier.pop()
        explored.add(node.state)
        stats.fMinusMinus(node.state)  # **
        stats.ePlusPlus(node.state)  # **
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            if (not (frontier.find(child.state)) and not (explored.find(child.state))):
                if problem.goalTest(child.state): return (child.solution(), stats)

                frontier.add(child)
                stats.fPlusPlus(child.state)


    return (None,stats)
    # ********************************

######################################################################
# DFS Graph Search       
######################################################################
def ucsGraph(problem):
    stats = Stats()

    def f(x):
        return x.pathCost

    node = Node(problem.initState, None, None, 0)
    frontier = PriorityQueue()
    explored =PriorityQueue()
    frontier.add(node, f(node))
    stats.fPlusPlus(node.state)  # **
    while True:
        if frontier.isEmpty(): return (None, stats)
        node = frontier.pop()
        explored.add(node)
        stats.fMinusMinus(node.state)  # **
        if problem.goalTest(node.state): return (node.solution(), stats)
        stats.ePlusPlus(node.state)  # **
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            if (not (frontier.find(child.state)) and not (explored.find(child.state))):
                if problem.goalTest(child.state): return (child.solution(), stats)
            frontier.add(child, f(child))
            stats.fPlusPlus(child.state)  # **
    return (None,stats)
    # ********************************

######################################################################
# GBFS Graph Search
######################################################################
def gbfsGraph(problem):
    stats = Stats()

    node = Node(problem.initState, None, None, 0)
    frontier = PriorityQueue()
    explored = Set()
    x = problem.heuristic(node.state, problem.goalState);

    frontier.add(node, x)
    stats.fPlusPlus(node.state)  # **
    while True:
        node = frontier.pop()
        explored.add(node.state)
        stats.fMinusMinus(node.state)  # **
        if problem.goalTest(node.state): return (node.solution(), stats)
        stats.ePlusPlus(node.state)  # **
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            if (not (frontier.find(lambda x: x == child)) and not (explored.find(lambda x: x.state == child))):
                if problem.goalTest(child.state): return (child.solution(), stats)
            cost = problem.heuristic(child.state, problem.goalState)
            frontier.add(child, cost)
            stats.fPlusPlus(child.state)  # **





######################################################################
# A* Graph Search
######################################################################
def aStarGraph(problem):
    stats = Stats()

    def f(m):
        return m.pathCost

    node = Node(problem.initState, None, None, 0)
    frontier = PriorityQueue()
    explored = Set()
    x = problem.heuristic(node.state, problem.goalState);
    y=x+f(node)

    frontier.add(node, y)
    stats.fPlusPlus(node.state)  # **
    while True:
        node = frontier.pop()
        explored.add(node.state)
        stats.fMinusMinus(node.state)  # **
        if problem.goalTest(node.state): return (node.solution(), stats)
        stats.ePlusPlus(node.state)  # **
        for action in problem.actions(node.state):
            child = node.child(problem, action)
            if (not (frontier.find(lambda x: x == child)) and not (explored.find(lambda x: x.state == child))):
                if problem.goalTest(child.state): return (child.solution(), stats)
            cost = problem.heuristic(child.state, problem.goalState)
            finalcost = cost+f(child)
            frontier.add(child, finalcost)
            stats.fPlusPlus(child.state)


   # return (None,stats)

