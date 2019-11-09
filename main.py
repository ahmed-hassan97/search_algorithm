from search_algorithms import *

from problem_maze import Problem
if __name__ == '__main__':


    #define an object of the problem class
    problem = Problem()


    # ----------------------
    # Run BFS (tree version)
    # ----------------------
    #print("** Using BFS - Tree **")
    #(bfsSolution,bfsStats) = bfsTree(problem)
    #if bfsSolution==None:
    #    print("Sorry, I can't find a solution!!")
    #else:
    #   problem.drawSolution("bfsTree",bfsSolution,bfsStats.data)
    # Run DFS (tree version)
    # ----------------------
    #print("** Using dfS - Tree **")
    #(dbsSolution,dbsStats) = dfsTree(problem)
    #if dbsSolution==None:
    #    print("Sorry, I can't find a solution!!")
    #else:
    #  problem.drawSolution("dbsTree",dbsSolution,dbsStats.data)
    ##################################################################################
    #print("** Using dfS - graph **")
    #(dfsSolution,dfsStats) = dfsGraph(problem)
    #if dfsSolution==None:
    #  print("Sorry, I can't find a solution!!")
    #else:
    #  problem.drawSolution("dfsGraph",dfsSolution,dfsStats.data)
    # ----------------------
    # Run UCS (tree version)
    # ----------------------
    #print("** Using UCS - Tree **")
    #(ucsSolution,ucsStats) = ucsTree(problem)
    #if ucsSolution==None:
    #    print("Sorry, I can't find a solution!!")
    #else:
    #    problem.drawSolution("ucsTree",ucsSolution,ucsStats.data)


    # -----------------------
    # Run BFS (graph version)
    # -----------------------
    #print("** Using BFS - Graph **")
    #(bfsSolution, bfsStats) =bfsGraph(problem)
    #if bfsSolution == None:
    #    print("Sorry, I can't find a solution!!")
    #else:
    #    problem.drawSolution("bfsGraph", bfsSolution, bfsStats.data)


    # -----------------------
    # Run DFS (graph version)
    # -----------------------
    #print("** Using DFS - Graph **")
    #(dfsSolution,dfsStats) = dfsGraph(problem)
    #if dfsSolution==None:
    #    print("Sorry, I can't find a solution!!")
    #else:
    #    problem.drawSolution("dfsGraph",dfsSolution,dfsStats.data)


    # ----------------------
    # Run UCS (graph version)
    # ----------------------
    print("** Using UCS - Graph **")
    (ucsSolution,ucsStats) = ucsTree(problem)
    if ucsSolution==None:
       print("Sorry, I can't find a solution!!")
    else:
     problem.drawSolution("ucsGraph",ucsSolution,ucsStats.data)


    # ------------------------
    # Run GBFS (graph version)
    # ------------------------
    #print("** Using GBFS - Graph **")
    #(gbfsSolution,gbfsStats) = gbfsGraph(problem)
    #if gbfsSolution==None:
    #    print("Sorry, I can't find a solution!!")
    #else:
    #   problem.drawSolution("gbfsGraph",gbfsSolution,gbfsStats.data)

    # ----------------------
    # Run A* (graph version)
    # ----------------------
    #print("** Using A* - Graph **")
    #(aStarSolution,aStarStats) = aStarGraph(problem)
    #if aStarSolution==None:
    #    print("Sorry, I can't find a solution!!")
    #else:
    #    problem.drawSolution("AStarGraph",aStarSolution,aStarStats.data)
