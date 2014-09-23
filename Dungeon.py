import pygame, sys, random
from pygame.locals import *
from Tile import *
from Actor import *

#The Dungeon class makes up the board of any particular level.
#The meat of the Dungeon Class is the map[] list. When the Dungeon class is called, it will create a map[] list of blank tiles with the given parameters. It will then assign the correct coordinates to each tile so that they can be drawn on the screen.

class Dungeon:

 def __init__(self,boardWidth,boardHeight): #It receives the boardHeight and boardWidth in tiles. Columns = Width, Rows = Height
  self.boardHeight = boardHeight
  self.boardWidth = boardWidth
  self.objectlist = []
  curx = 0
  cury = 0
  
  #Here we create the map[] list which is the actual storage location of all the tiles. This creates a blank list of dimensions boardWidth and boardHeight of blank tiles.
  self.map = [[ Tile(0,0,0) for y in range(self.boardHeight) ] for x in range(self.boardWidth) ]

#Here we assign the correct coordinates to each Tile so that they can be printed to the screen. For instance:
#Tile[0][1] will have coordinate x = 0,  y = 32
#Tile[1][2] will have coordinate x = 32 y = 64
  for y in xrange(self.boardHeight):
    for x in xrange(self.boardWidth):
        self.map[x][y].xcoordinate = curx
        self.map[x][y].ycoordinate = cury
        curx += 32
    curx = 0
    cury += 32
        
 def spawn_Monsters(self,boardWidth,boardHeight,Rarity_Database,Item_Database, objectlist):#This function posts a random number of monsters throughout the current map
  amount=random.randint(10,20)#For now, we are creating a random number of monsters between 1 and 20
  while (amount != 0):
   MapLVL=1#Setting this defaultly, once multiple levels of the map exist, this will be modified through that
   name='monster'#Generic monster name, will be adjustable later
   xcoord = random.randint(0,(boardWidth-2))#Ensures that we stay within the map
   ycoord = random.randint(0,(boardHeight-2))#Ensures that we stay within the map
   monsterLVL = random.randint(MapLVL,MapLVL+1)#Monster level is randomly generated
   filename=name+"lvl"+str(monsterLVL)
   image='images/' + filename + '.png'#Allows a customized image link based on the name of the Actor
   empty=True
   for object in objectlist:
    if object.xcoordinate==xcoord and object.ycoordinate==ycoord:
     empty=False
   if self.map[xcoord][ycoord].isPassable == True and empty:#If there is no wall at the current X,Y coordinates
    objectlist.append(Monster(xcoord*32, ycoord*32, name,monsterLVL*100,monsterLVL*10,monsterLVL,image, Rarity_Database, Item_Database))
    amount=amount-1
 
 def room_Generation(self,width,height):#This function generates a completely random mapLVL with rooms of varying sizes
  numberofRooms=100#random.randint(1,(width-1)/5)
  numberofAttempts=1000
  
  while(numberofRooms!=0 and numberofAttempts != 0):#Try to generate rooms while there are still rooms to create and you haven't used up all of your attempts
   
   canPost=True#Used to determine if the room can be posted to the map
   #These variables are used to determine if a door can be added to a room, this is based on surrounding rooms and the map height/width
   north_door=True
   east_door=True
   south_door=True
   west_door=True
   roomsize=random.randint(5,width/2)#Rooms are created with a random size, starting with 5 and up to half the room width
                                     #This is to ensure that all rooms have space to contain items/monsters/NPCs and also has walls
   
   while (roomsize%2!=1):#The room size can not be odd or calculations will become difficult and is asthetically less pleasing
    roomsize=random.randint(5, width/2)
    #Roomx and Roomy are used to denote the top left-hand corner of the room 
   roomx=random.randint(1,width-1-roomsize)
   roomy=random.randint(1,height-1-roomsize)
   #Check to see if the box rests on the border of the map, if they do no doors will be created on that wall
   if roomx==1:
    west_door=False
   if roomy==1:
    north_door=False
   if roomx+roomsize==(width-1):
    east_door=False
   if roomy+roomsize==(height-1):
    south_door=False       
   #Check to see if the room you are currently placing does not overlap any other room on the map
   for x in range(0,roomsize):
    for y in range(0,roomsize):
     if self.map[roomx+x][roomy+y].isPassable==False:
      canPost=False#If the room overlaps, do not post the room and restart the room creation process
      
   if canPost:
           
    #This for loop places the four walls up for a room
    for number in range(0,roomsize):
     self.map[roomx][roomy+number].set_case(1)
     self.map[roomx+number][roomy].set_case(1)
     self.map[roomx+roomsize-1][roomy+number].set_case(1)
     self.map[roomx+number][roomy+roomsize-1].set_case(1)
     
    #This will be used to determine placement of the walls of a room
    
    
    
    #Each of the following four if statements determine where on the wall that a door will be placed
    #Generally, the door will be placed in the middle of the wall.
    #This is different when the placed room is adjacent to another room.
    #If the current room is being placed next to a room that already exists, extend the doorway from the initial room into the room that is currently being posted
    if west_door:
     ydoorloc=roomsize/2+roomy
     for pos in range (0,roomsize):      
      if self.map[roomx-1][roomy+pos].isPassable and self.map[roomx-1][roomy+pos-1].isPassable==False and self.map[roomx-1][roomy+pos+1].isPassable==False:
       ydoorloc=roomy+pos
     self.map[roomx][ydoorloc].set_case(0)
     
    if north_door:
     xdoorloc=roomsize/2+roomx
     for pos in range (0,roomsize):
      if self.map[roomx+pos][roomy-1].isPassable and self.map[roomx+pos-1][roomy-1].isPassable==False and self.map[roomx+pos+1][roomy-1].isPassable==False:
       xdoorloc=roomx+pos
     self.map[xdoorloc][roomy].set_case(0)
     
     
    if east_door:
     ydoorloc=roomsize/2+roomy
     for pos in range (0,roomsize):
      if self.map[roomx+roomsize][roomy+pos].isPassable and self.map[roomx+roomsize][roomy+pos-1].isPassable==False and self.map[roomx+roomsize][roomy+pos+1].isPassable==False:
       ydoorloc=roomy+pos
     self.map[roomx+roomsize-1][ ydoorloc].set_case(0)
     
    if south_door:   
     xdoorloc=roomsize/2+roomx    
     for pos in range (0,roomsize):
      if self.map[roomx+pos][roomy+roomsize].isPassable and self.map[roomx+pos-1][roomy+roomsize].isPassable==False and self.map[roomx+pos+1][roomy+roomsize].isPassable==False:
       xdoorloc=roomx+pos
     self.map[xdoorloc][roomy+roomsize-1].set_case(0)
    numberofRooms=numberofRooms-1
   numberofAttempts=numberofAttempts-1
          


    
