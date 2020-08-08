# MazeMaker


### Introduction


MazeMaker is a simple python algorithm that creates a procedurally generated solvable maze. This was created in the time span of a week, and I decided to upload it because I am quite happy with it.


### How the algorithm works


The algorithm itself is quite simple, and follows a 4 step process:

1. Create the maze border

This step simply creates a border around the outer edges, and also makes the entry and exit points at the bottom right and top left corners.

2. Create the solution

This step is a workaround for having to validate if the maze is solvable, since the entire maze is built around the solution in the first place. It’s a simple algorithm that makes its way from the bottom right corner to the top left, while following a certain set of rules such as not going into the walls or falling back on itself. Additionally, the algorithm will remake a solution if it gets stuck or doesn’t fulfill the minimum length requirement.

3. Create the solution border

This is another simple step, and it simply draws a border around the solution to prepare for the final step.

4. Create the extra paths

The final step for creating the maze, this step repeats until the maze is complete. It creates a path that follows similar rules to the solution path, except choosing from any valid starting point and ending once stuck. Once there are no valid starting points available, the algorithm is finished.
