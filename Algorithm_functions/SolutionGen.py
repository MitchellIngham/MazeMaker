import random

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
        #eliminate D and R
        moves = elimmove(moves, 'D')
        moves = elimmove(moves, 'R')
    
    #if it's near the left border
    if x == 1:
        #eliminate D and L
        moves = elimmove(moves, 'D')
        moves = elimmove(moves, 'L') 

    #if it's near the top border
    if y == 1:
        #eliminate U and R
        moves = elimmove(moves, 'U')
        moves = elimmove(moves, 'R')
    
    #if it's near the right border
    if x == 59:
        #eliminate D and R
        moves = elimmove(moves, 'D')
        moves = elimmove(moves, 'R')
        
    #eliminate moves that will trap it between the border and itself
    #check bottom
    if y == 58:
        moves = elimmove(moves, 'R')
    
    #check left
    if x == 2:
        moves = elimmove(moves, 'D')
        
    #check up
    if y == 2:
        moves = elimmove(moves, 'R')
    
    #check right
    if x == 58:
        moves = elimmove(moves, 'D')
    
    return moves

#eliminates moves that make the solution go back on itself
def backtrackmove(maze, moves, x, y):
    
    #check down (x, y + 1)
    if y < 59: #prevent out of bounds error
        if maze[y + 2][x] == 2:
            moves = elimmove(moves, 'D')
    if maze[y + 1][x - 1] == 2 or maze[y + 1][x + 1] == 2:
        moves = elimmove(moves, 'D')
    
    #check left (x - 1, y)
    if x > 1: #prevent out of bounds error
        if maze[y][x - 2] == 2:
             moves = elimmove(moves, 'L')
    if maze[y - 1][x - 1] == 2 or maze[y + 1][x - 1] == 2:
        moves = elimmove(moves, 'L')
    
    #check up (x, y - 1)
    if y > 1: #prevent out of bounds error
        if maze[y - 2][x] == 2:
             moves = elimmove(moves, 'U')
    if maze[y - 1][x - 1] == 2 or maze[y - 1][x + 1] == 2:
        moves = elimmove(moves, 'U')
        
    #check right (x + 1, y)
    if x < 59: #prevent out of bounds error
        if maze[y][x + 2] == 2:
             moves = elimmove(moves, 'R')
    if maze[y - 1][x + 1] == 2 or maze[y + 1][x + 1] == 2:
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
    
    #next eliminate moves that go back on itself
    moves = backtrackmove(maze, moves, x, y)
    
    nextmove = [0, 0, 'D']
    
    #if the algorithm gets stuck, just start over
    if len(moves) == 0:
        stuck = True
    else:
        #choose a random move from the ones that haven't been eliminated
        nextmove = choosemove(moves, previousmove, x, y)
        
    nextmove.append(stuck)
    
    return nextmove

#makes the solution of the maze
def makeSolution(maze):
    
    #starting values
    x, y = 59, 59
    previousmove = ''
    stuck = False
    
    #save block
    maze[y][x] = 2
    
    #loop until done
    done = False
    while done == False:
        
        #find the next move
        move = findnext(maze, previousmove, stuck, x, y)
        
        #if it's stuck restart the algorithm
        stuck = move[3]
        if stuck == True:
            done = True
        else:
            #use the move
            x, y = move[0], move[1]
            previousmove = move[2]
            maze[y][x] = 2
        
        #find if done
        if (x == 2 and y == 1) or (x == 1 and y == 2):
            
            #put in the last block
            maze[1][1] = 2
            done = True
    
    return [maze, stuck]