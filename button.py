# Button.py

from graphics import *

class button:
    def __init__(self, win, center, width, height, label):
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill("lightgray")
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.activate()

    def color(self,color): #Change text to green or red.
        self.rect.setFill(color)
        self.deactivate()

    def coloryellow(self): #Yellow fill.
        x = color_rgb(255,203,5)
        self.rect.setFill(x)

    def outline(self): #Outline of box to blue.
        x = color_rgb(45,112,183)
        self.rect.setOutline(x)
        self.rect.setWidth(10)

    def outline2(self):
        x = color_rgb(45,122,183)
        self.rect.setOutline(x)
        self.rect.setWidth(3)

    def style(self): #Bold Text
        self.label.setStyle("bold")

    def clicked(self, p):
#Return true if button active and p is inside
        return (self.active and
        self.xmin <= p.getX() <= self.xmax and
        self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
#Returns the label string of the button.
        return self.label.getText()

    def activate(self):
        self.label.setFill("black")
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
# Sets the button to False.
        self.label.setFill("darkgrey")
        self.rect.setWidth(1)
        self.active = False

    def undraw(self):
        self.rect.undraw()
        self.label.undraw()

    def boxstylepokemon(self): #Makes a Pokemon Styled box
        self.coloryellow()
        self.outline()
        self.style()

    def boxstylepokemon2(self): #Makes a Pokemon Styled box
        self.coloryellow()
        self.outline2()
        self.style()
