# Module 5
#   Programming Assignment 6
#       Prob-3.py

# <YOUR NAME>

from graphics import *
def main():
    win = GraphWin('Archery Target',300,300)
    center = Point(150,150)

    w = Circle(center,100)
    w.setFill('white')
    w.draw(win)

    bl = Circle(center,80)
    bl.setFill('black')
    bl.draw(win)

    b = Circle(center,60)
    b.setFill('blue')
    b.draw(win)

    r = Circle(center,40)
    r.setFill('red')
    r.draw(win)

    y = Circle(center,20)
    y.setFill('yellow')
    y.draw(win)

    input()
    
main()    