# Module 5
#   Programming Assignment 6
#       Prob-5.py

# <YOUR NAME>
from graphics import *
def main():
    win=GraphWin("My car",500,500)
    center = Point(100,400)
    tire = Circle(center,40)
    tire.setFill('black')
    rim = Circle(center,20)
    rim.setOutline("red")
    rim.setFill("red")
    tire2 = tire.clone()
    tire2.move(250,0)
    tire2.setFill('black')
    rim2=rim.clone()
    rim2.move(250,0)
    rim2.setOutline("green")
    rim2.setFill('green')    
    
    body = Rectangle(Point(50,375),Point(400,250))
    body.setFill("yellow")
    body.setOutline('yellow')
    
    window=Polygon(Point(400,250),Point(350,400),Point(350,150))
    window.setFill("black")
    window.draw(win)

    doorline = Line(Point(225,375),Point(225,250))
    doorline.setOutline('black')
    
    bumper = Rectangle(Point(40,350),Point(50,375))
    bumper.setFill("grey")
    frontbump=bumper.clone()
    frontbump.move(350,0)

    #backwin = Line(Point(50,250),Point(50,150))
    #backwin.setFill('black')
    
    roof = Line(Point(50,150),Point(350,150))
    roof.setFill('black')

    drivewindow = Rectangle(Point(225,250),Point(350,220))
    drivewindow.setFill('blue')

    rearpanel = Rectangle(Point(50,150),Point(225,250))
    rearpanel.setFill('yellow')
    rearpanel.setOutline('yellow')

    body.draw(win)
    roof.draw(win)
    rearpanel.draw(win)
    drivewindow.draw(win)
    #backwin.draw(win)
    bumper.draw(win)
    frontbump.draw(win)
    doorline.draw(win)
    tire.draw(win)
    tire2.draw(win)
    rim.draw(win)
    rim2.draw(win)
    
    win.getMouse()
    win.close()


main()