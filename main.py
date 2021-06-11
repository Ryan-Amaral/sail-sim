from graphics import *

win = GraphWin(width = 1024, height = 512)
win.setCoords(0, 0, 1024, 512)
win.setBackground("cyan3")
mySquare = Rectangle(Point(200, 200), Point(400, 400)) 
mySquare.draw(win) 
win.getMouse()