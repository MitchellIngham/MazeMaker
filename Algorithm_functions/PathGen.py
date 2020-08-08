import random
import copy

#eliminates a move if it hasn't been already
def elimmove(moves, m):
    c = moves.count(m)
    if c > 0:
        moves.remove(m)
        
    return moves

#calculates a move near the border
def bordermove(moves, x, y):
    
    #if it's near the bottom border
    if y == 59:
        #eliminate D
        moves = elimmove(moves, 'D')
    
    #if it's near the left border
    if x == 1:
        #eliminate L
        moves = elimmove(moves, 'L') 

    #if it's near the top border
    if y == 1:
        #eliminate U
        moves = elimmove(moves, 'U')
    
    #if it's near the right border
    if x == 59:
        #eliminate R
        moves = elimmove(moves, 'R')
    
    return moves

#eliminates moves that make the solution go back on itself or go onto the solution
def backtrackmove(maze, moves, x, y, target):
    
    #check down (x, y + 1)
    if y < 59: #prevent out of bounds error
        if maze[y + 2][x] == target:
            moves = elimmove(moves, 'D')
    if maze[y + 1][x - 1] == target or maze[y + 1][x + 1] == target:
        moves = elimmove(moves, 'D')
    
    #check left (x - 1, y)
    if x > 1: #prevent out of bounds error
        if maze[y][x - 2] == target:
             moves = elimmove(moves, 'L')
    if maze[y - 1][x - 1] == target or maze[y + 1][x - 1] == target:
        moves = elimmove(moves, 'L')
    
    #check up (x, y - 1)
    if y > 1: #prevent out of bounds error
        if maze[y - 2][x] == target:
             moves = elimmove(moves, 'U')
    if maze[y - 1][x - 1] == target or maze[y - 1][x + 1] == target:
        moves = elimmove(moves, 'U')
        
    #check right (x + 1, y)
    if x < 59: #prevent out of bounds error
        if maze[y][x + 2] == target:
             moves = elimmove(moves, 'R')
    if maze[y - 1][x + 1] == target or maze[y + 1][x + 1] == target:
        moves = elimmove(moves, 'R')
        
    return moves

#sees if a move will run the path into a wall
def wallmove(maze, moves, x, y):
    
    #check down
    if maze[y + 1][x] == 1:
        moves = elimmove(moves, 'D')
    
    #check left
    if maze[y][x - 1] == 1:
        moves = elimmove(moves, 'L')
        
    #check up
    if maze[y - 1][x] == 1:
        moves = elimmove(moves, 'U')
        
    #check right
    if maze[y][x + 1] == 1:
        moves = elimmove(moves, 'R')
    
    return moves

#chooses a random move
def choosemove(moves, previousmove, x, y):
    
    #if the previous move is an option, make it much more likely to use that move
    if moves.count(previousmove) > 0:
        for a in range(8):
            moves.append(previousmove)
    
    #choose a random move
    nextmove = random.choice(moves)
    
    if nextmove == 'D':    #if the move is down
        y += 1
    elif nextmove == 'L':  #if the move is left
        x -= 1
    elif nextmove == 'U':  #if the move is up
        y -= 1
    elif nextmove == 'R':  #if the move is right
        x += 1
    
    return [x, y, nextmove]

#finds the next move
def findnext(maze, previousmove, stuck, x, y):
    
    #all possible moves
    moves = ['U', 'D', 'L', 'R']
    
    #first eliminate moves going into the border or trapping itself
    moves = bordermove(moves, x, y)
    
    #next eliminate moves that go back on itself or the solution
    moves = backtrackmove(maze, moves, x, y, 2)
    moves = backtrackmove(maze, moves, x, y, 3)
    
    #finally, eliminate moves that go into a wall from another path
    moves = wallmove(maze, moves, x, y)
    
    nextmove = [0, 0, 'D']
    
    #if the algorithm gets stuck, just start over
    if len(moves) == 0:
        stuck = True
    else:
        #choose a random move from the ones that haven't been eliminated
        nextmove = choosemove(moves, previousmove, x, y)
        
    nextmove.append(stuck)
    
    return nextmove

#makes a border around the path
def pathborder(maze):
    
    #loop through whole maze excluding borders
    for y in range(59):
        for x in range(59):
            
            #if it's a path block
            if maze[y + 1][x + 1] == 3:
                
                #if any block around it is blank, make it a block
                for a in range(3):
                    for b in range(3):
                        
                        #if it's blank
                        if maze[y + b][x + a] == 0:
                            
                            #make it a block
                            maze[y + b][x + a] = 1
    
    return maze

#finds a random starting location for the next path
def findstart(maze):
    
    #make list of all possible starting points
    startpoints = []
    
    #loop through whole maze excluding walls
    for a in range(59):
        for b in range(59):
            
            #set x and y for simplicity
            x, y = b + 1, a + 1
            
            #if it is a block
            if maze[y][x] == 1:
                #and if it is next to an empty space
                if maze[y - 1][x] == 0 or maze[y + 1][x] == 0 or maze[y][x - 1] == 0 or maze[y][x + 1] == 0:
                    #and if it is next to either a solution or path
                    if maze[y - 1][x] == 2 or maze[y + 1][x] == 2 or maze[y][x - 1] == 2 or maze[y][x + 1] == 2 or maze[y - 1][x] == 3 or maze[y + 1][x] == 3 or maze[y][x - 1] == 3 or maze[y][x + 1] == 3:
                        
                        #mark it
                        startpoints.append([x, y])
    
    #if there are no starting points
    if len(startpoints) == 0:
        
        #return as stuck
        return [0, 0]
    
    #choose a random point to start at
    return random.choice(startpoints)

#makes a single path
def singlePath(maze):
    
    #initial data
    stuck = False
    previousmove = ''
    
    #get starting point
    startpoint = findstart(maze)
    
    #if stuck
    if startpoint[0] == 0:
        return [maze, True]
    else:
        x, y = startpoint[0], startpoint[1]
    
    #save block
    maze[y][x] = 3
    
    #loop until done
    done = False
    while done == False:
        
        #find the next move
        move = findnext(maze, previousmove, stuck, x, y)
        
        #if it's stuck end the algorithm
        if move[3] == True:
            done = True
        else:
            #use the move
            x, y = move[0], move[1]
            previousmove = move[2]
            maze[y][x] = 3
        
    #when stuck add walls to the path
    maze = pathborder(maze)
    
    return [maze, False]

#makes extra paths to finish the maze
def makePaths(maze):
    
    #make paths until the maze is filled in
    done = False
    while done == False:
        
        #make a path
        result = singlePath(copy.deepcopy(maze))
        
        #if there are no starting points end the loop
        if result[1] == True:
            done = True
        else:
            #save the path if it succeeded
            maze = result[0]
    
    #return path data when done
    return maze