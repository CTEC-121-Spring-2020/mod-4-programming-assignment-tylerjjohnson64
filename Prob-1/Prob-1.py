# Module 5
#   Programming Assignment 6
#       Prob-1.py

# <Tyler Johnson>

# INSTRUCTIONS:
#   Insert a comment above each line of code in the program below to describe
#   what the code does

#this imports all of the graphics library
from graphics import *
#creats a set of instructions called main 
def main():
     win = GraphWin()  #creates a shortcut for the GraphWin function
     shape = Circle(Point(50,50), 20) #creates a circle shape but does not draw
     shape.setOutline("red") #outline set to color red
     shape.setFill("red") #fill color set to red
     shape.draw(win) #this step will actually draw the shape with information given above, so a red circle
     for i in range(5): # creates a for loop with 5 iterations 
          p = win.getMouse() # sets the letter p to the getmouse function in the created window, allows moving of circle to mouse click
          c = shape.getCenter() # sets the letter c to the getcenter() function, the center of the circle
          dx = p.getX() - c.getX() #sets dx to the change in x values from original center to pointed position
          dy = p.getY() - c.getY() #similiar to above but change in Y
          shape.move(dx,dy) # moves the shape
     win.close() #closes the created window after the for loop is complete 

main()