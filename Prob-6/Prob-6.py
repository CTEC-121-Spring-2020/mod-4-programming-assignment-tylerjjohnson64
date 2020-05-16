# Module 5
#   Programming Assignment 6
#       Prob-6.py

# <YOUR NAME>
from graphics import *
def main():
    win = GraphWin("Legos",1500,1000)
    # draw basic brick
    blueBrick = Rectangle(Point(10,150), Point(510, 100))
    blueBrick.setFill("blue")
    blueBrick.setOutline("black")
    blueBrick.setWidth(5)
    blueBrick.draw(win) 
    
    # draw first nib
    blueBrickNib = Rectangle(Point(35, 100), Point(85, 80))
    blueBrickNib.setFill("blue")
    blueBrickNib.setOutline("black")
    blueBrickNib.setWidth(5)
    blueBrickNib.draw(win)
    #replicate Nib
    for i in range(1, 5):
        blueBrickNextNib = blueBrickNib.clone()
        blueBrickNextNib.move(100 *i, 0)
        blueBrickNextNib.draw(win)

    
    nextlego = blueBrick.clone()
    nextlego.move(600,0)
    nextlego.draw(win)

    nextnib = blueBrickNib.clone()
    nextnib.move(600,0)
    nextnib.draw(win)
    for i in range(1, 5):
        nextnextnib = nextnib.clone()
        nextnextnib.move(100 *i, 0)
        nextnextnib.draw(win)

    secondrowbrick = blueBrick.clone()
    secondrowbrick.move(0,150)
    secondrowbrick.setFill('red')
    secondrowbrick.draw(win)

    secondnib = blueBrickNib.clone()
    secondnib.move(0,150)
    secondnib.setFill('red')
    secondnib.draw(win)
    for i in range(1,5):
        secondnextnib = secondnib.clone()
        secondnextnib.move(100*i,0)
        secondnextnib.draw(win)
    
    secondrownextbrick = secondrowbrick.clone()
    secondrownextbrick.move(600,0)
    secondrownextbrick.draw(win)
    
    secondrownextbricknib =secondnib.clone()
    secondrownextbricknib.move(600,0) 
    secondrownextbricknib.draw(win)
    for i in range(1,5):
        secondrowsecondbricknib=secondrownextbricknib.clone()
        secondrowsecondbricknib.move(100*i,0)
        secondrowsecondbricknib.draw(win)

    thirdrowbrick=secondrowbrick.clone()
    thirdrowbrick.move(0,150)
    thirdrowbrick.setFill('green')
    thirdrowbrick.draw(win)

    thirdrowbricknib = secondnib.clone()
    thirdrowbricknib.move(0,150)
    thirdrowbricknib.setFill('green')
    thirdrowbricknib.draw(win)
    for i in range(1,5):
        thirdrownextnib = thirdrowbricknib.clone()
        thirdrownextnib.move(100*i,0)
        thirdrownextnib.draw(win)
    
    lastbrick=thirdrowbrick.clone()
    lastbrick.move(600,0)
    lastbrick.draw(win)

    lastnib = thirdrowbricknib.clone()
    lastnib.move(600,0)
    lastnib.draw(win)
    for i in range(1,5):
        lastnibnext=lastnib.clone()
        lastnibnext.move(100*i,0)
        lastnibnext.draw(win)
    win.getMouse()
    win.close()


main()