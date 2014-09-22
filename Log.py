import random, sys, pygame

class Log():

  def __init__(self):
   self.events = []
   pygame.init()
   self.WHITE = (255, 255, 255)
   self.GREEN = (0, 255, 0)
   self.BLUE = (0, 0, 255)
   self.BLACK = (0,0,0)
   self.width=640
   self.height=160
   #X,Y coordinates of the surface itself
   self.xcoord = 0
   self.ycoord = 800
   #X,Y location on the display
   pygame.font.init()  
   self.menusurface = pygame.Surface((self.width,self.height))
   self.menusurface.fill(self.BLACK)
   self.font = pygame.font.SysFont("times new roman", 15)
   
  def addEvent(self, event):
   type, text = event
   
   tempEvent = self.font.render(text, 1, (255,255,0))
   self.events.append(tempEvent)
   i=0
   i = len(self.events)-1
   x=0
   self.menusurface.fill(self.BLACK)
   while(x<9):
	self.menusurface.blit(self.events[i], (0,self.height-20-x*20))
	if (i-1)>=0:
	 i=i-1
	 x=x+1
	else:
	 x=9
	
   
  
   
   
   