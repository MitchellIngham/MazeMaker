import turtle

#converts coordinates from list format to turtle format
def convcoords(num, isy = False):
    
    if isy == True:
        return (300 - (num * 10))
    else:
        return (-300 + (num * 10))

#makes a square at a certain point
def makesquare(x, y, color, t):
    
    #set color and go to location
    t.color(color)
    t.fillcolor(color)
    t.goto(convcoords(x) - 4, convcoords(y, isy = True) + 4)
    
    #draw the square
    t.pendown()
    t.begin_fill()
    t.shape('square')
    t.stamp()

    #tidy up
    t.end_fill()
    t.penup()
    
#draws every square
def drawmaze(maze, showsolution, showextrapaths, t):
    
    #loop through the whole maze
    for y in range(61):
        for x in range(61):
            #if there's a block
            if maze[y][x] == 1:
                #draw it
                makesquare(x, y, 'black', t)
            #if there's a solution block
            elif maze[y][x] == 2:
                #draw it only if showsolution is true
                if showsolution == True:
                    makesquare(x, y, 'green', t)
            #if there's an extra path block
            elif maze[y][x] == 3:
                #draw it only if showextrapaths is true
                if showextrapaths == True:
                    makesquare(x, y, 'blue', t)

#Initializes the gui and displays the maze
def initgui(maze, showsolution, showextrapaths):
    
    #set up turtle
    try:
        t = turtle.Turtle()
    except:
        t = turtle.Turtle()
    wn = turtle.Screen()
    
    #turtle settings
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.shapesize(0.45, 0.45, 0)
    
    #screen settings
    wn.tracer(0, 0)
    wn.setup(width = 621, height = 621)
    wn.title('MazeMaker')
    
    #draw the maze
    drawmaze(maze, showsolution, showextrapaths, t)
    
    #done
    wn.update()
    wn.exitonclick()
    turtle.done()