from GUI_functions.InitGUI import initgui
from Algorithm_functions.MazeGen import makemaze

#debug options
showsolution = False
showextrapaths = False

#make the maze
maze = makemaze()

#display it on screen
initgui(maze, showsolution, showextrapaths)