# Module 5
#   Programming Assignment 6
#       Prob-2.py

# <Tyler Johnson>

from graphics import *

def main():
     win = GraphWin()
 
     for i in range(5):   #creates a loop 
          p = win.getMouse()
          ax = p.getX()  
          ay = p.getY()
          bx = p.getX()+25 #creates a second point 25 pixels above users click
          by = p.getY()-25 #creates second Y point 
          
          shape2 = Rectangle(Point(ax,ay),Point(bx,by)) #takes above points and draws/fills the rectangles
          shape2.setOutline('red')
          shape2.setFill('red')
          shape2.draw(win)

     for i in range(5):
          p = win.getMouse()
          cx = p.getX()-25    #using equal increments creats the user's click as the center of the square created
          cy = p.getY()-25
          dx = p.getX()+25
          dy = p.getY()+25

          shape3 = Rectangle(Point(cx,cy),Point(dx,dy))
          shape3.setOutline('red')
          shape3.setFill('red')
          shape3.draw(win)

     qt = Text(Point(100,100),'Click to exit!')
     qt.setStyle('bold')
     qt.draw(win) #draws the above text 
     win.getMouse() #waits for user mouse input, wont close program until is clicked 
     win.close()
     
main()