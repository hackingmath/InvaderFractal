'''Invader Fractal
Peter Farrell
August 29, 2017'''

from random import choice

sz = 3
dim = 5 # Invader is a dim x dim grid
screensize = 30 #output window

class Invader:
    def __init__(self):
        self.gridList = []
        #4 x 7 matrix
        self.blockList = []
        for i in range(dim//2+1):
            self.blockList.append([])
            for j in range(dim):
                self.blockList[i].append(choice([0,1]))
        #now copy the rows at the end to the beginning
        #rows 0,1,2,3,2,1,0
        for rownum in range(dim//2+1):
            self.gridList.append(self.blockList[rownum])
        for rownum in range(dim//2-1,-1,-1):
            self.gridList.append(self.blockList[rownum])
            
    def update(self):
        for y in range(dim):
            for x in range(dim):
                if self.gridList[y][x] == 1:
                    fill(0)
                else: fill(255)
                rect(x*sz,y*sz,sz,sz)
        
invaderList = []
for x in range(screensize**2):
   invaderList.append(Invader())

def setup():
    size(600,600)
    rectMode(CENTER)
    noStroke()
    
def draw():
    global invaderList
    background(255)
    #translate(width/2,height/2)
    
    for x in range(screensize):
        for y in range(screensize):
            pushMatrix()
            translate((dim+2)*x*sz,(dim+2)*y*sz)
            rotate(radians(90))
            invaderList[screensize*x+y].update()
            popMatrix()