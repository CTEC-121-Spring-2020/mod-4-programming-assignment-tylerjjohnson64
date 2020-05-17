# Module 5
#   Programming Assignment 6
#       Prob-7.py

# <YOUR NAME>

from graphics import *
def main():
    win = GraphWin("Face",600,600)
    
    ear=Oval(Point(130,275),Point(80,220))
    ear.setOutline('black')
    ear.setFill('yellow')
    otherear=ear.clone()
    otherear.move(390,0)
    otherear.setFill('yellow')
    ear.draw(win)
    otherear.draw(win)

    hair=Line(Point(150,200),Point(150,90))
    hair.setFill('brown')
    hair.draw(win)
    for i in range(1,300):
        nexthair=hair.clone()
        nexthair.move(1*i,0)
        nexthair.draw(win)

    shape = Circle(Point(300,300), 200)
    shape.setOutline("black")
    shape.setFill("yellow")
    shape.draw(win)

    leftEye = Circle(Point(220,250), 45)
    leftEye.setFill("white")
    leftEye.setOutline("black")
    rightEye = leftEye.clone()
    rightEye.move(160,0)
    
    leftEye.draw(win)
    rightEye.draw(win)

    iris = Circle(Point(220,250),10)
    iris.setFill('blue')
    iris.draw(win)
    iris2=iris.clone()
    iris2.move(160,0)
    iris2.draw(win)

    
    mouth=Oval(Point(250,350),Point(350,450))
    mouth.setFill('Black')
    mouth.draw(win)
    
    nose=Polygon(Point(300,270),Point(280,320),Point(320,320))
    nose.setFill('yellow')
    nose.setOutline('black')
    nose.draw(win)
    
    teeth=Rectangle(Point(300,350),Point(310,360))
    teeth.setOutline("black")
    teeth.setFill("white")
    teeth.draw(win)
    tooth=teeth.clone()
    tooth.move(-10,90)
    tooth.draw(win)
    for i in range(1,3):
        nexttooth=tooth.clone()
        nexttooth.move(10*i,-1*i)
        nexttooth.draw(win)
    
    
   
    
    input()
    


    

    

main()


