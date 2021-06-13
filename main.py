from graphics import *
from sprite import Sprite

win = GraphWin(width = 1024, height = 512)
win.setCoords(0, 0, 1024, 512)
win.setBackground("cyan3")
#mySquare = Rectangle(Point(200, 200), Point(400, 400)) 
#mySquare.draw(win)
sprit = Sprite([(200,200), (400,200), (400,400), (200, 400)])
sprit.translate(200,50)
sprit.draw(win)
win.getMouse()