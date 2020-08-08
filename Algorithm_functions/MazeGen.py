from Algorithm_functions.SolutionGen import makeSolution
from Algorithm_functions.PathGen import makePaths
import copy

#makes a border of blocks
def makeborder(maze):
    
    #make the blocks on the border
    for a in range(61):
        maze[0][a] = 1
        maze[60][a] = 1
        maze[a][0] = 1
        maze[a][60] = 1
    
    #make the entrance and exit blocks
    maze[0][1] = 2
    maze[60][59] = 2
    
    return maze

#makes a border around the solution
def solborder(maze):
    
    #loop through whole maze excluding borders
    for y in range(59):
        for x in range(59):
            
            #if it's a solution block
            if maze[y + 1][x + 1] == 2:
                
                #if any block around it is blank, make it a block
                for a in range(3):
                    for b in range(3):
                        
                        #if it's blank
                        if maze[y + b][x + a] == 0:
                            
                            #make it a block
                            maze[y + b][x + a] = 1
    
    return maze

#gets the length of the solution
def sollen(maze):
    
    count = 0
    
    #loop through maze
    for y in range(59):
        for x in range(59):
            #if it's a solution block
            if maze[y + 1][x + 1] == 2:
                #count it
                count += 1
    
    return count

#makes the maze
def makemaze():
    
    #initial data
    maze = [[0 for i in range(61)] for j in range(61)] 
    
    #make the border
    maze = makeborder(maze)
    
    #make the solution of the maze
    stuck = True
    while stuck == True: #redo the algorithm if it gets stuck
        sol = makeSolution(copy.deepcopy(maze))
        
        #if the algorithm didn't get stuck
        if sol[1] == False:
            
            #only exit the loop if the solution meets the minimum length requirement
            if sollen(sol[0]) >= 250:
                stuck = sol[1]
        
    #save solution data when done
    maze = sol[0]
    
    #make a border around the solution
    maze = solborder(maze)
    
    #make extra paths
    maze = makePaths(maze)
    
    #return the maze
    return maze