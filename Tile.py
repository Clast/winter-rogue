import pygame, sys, os

#A dungeon map is made up of a list of Tiles. Each tile contains a set of coordinates, an image, and a case which tells you what type of terrain it is and whether or not it is passable.
#A tile is typically created automatically through the creation of a Dungeon object.
#You can change a tile's type by tile.set_case(case) where case is an integer.
class Tile:

 def __init__(self, xcoordinate, ycoordinate, case):
  self.xcoordinate = xcoordinate
  self.ycoordinate = ycoordinate
  self.case = case
  self.Img = None
  self.imgpath = 'blank'
  self.isPassable = 1 #1 means passable
  
  #Note that you do not pass an image directly to tile, but rather it's case determines which image file is assigned to it in the set_case function.
  self.set_case(case)
 

  
#Since set_case is called on Tile creation, all terrain types can be added here before the code runs.
 def set_case(self, case):
  if case == 0:
   self.imgpath = 'images/grass.png'
   self.Img = pygame.image.load(self.imgpath)
   self.isPassable = 1
  elif case == 1:
   self.imgpath = 'images/brick_wall.png'
   self.Img = pygame.image.load(self.imgpath)
   self.isPassable = 0
  else:
   print "Terrain type %s is not defined! Errors may occur!" % self.case
    
 def get_terrain(self):
  print "Returning terrain case: %s" % self.case
  return self.case
  

 def get_xcoordinate(self):
  print "Returning Coordinate-X %s" % self.xcoordinate
  return self.xcoordinate
  

 def get_ycoordinate(self):
  print "Returning Coordinate-Y %s" % self.ycoordinate
  return self.ycoordinate
  

 def get_coordinates(self):
  tuple = (self.xcoordinate, self.ycoordinate)
  print "Returning Coordinates (Tuple) %s" % (tuple,)
  return tuple
  

 def get_image(self):
  print "Returning Image %s" % self.imgpath
  return self.Img
  
  
 def get_isPassable(self):
  print "Returning isPassable value of: %s" % self.isPassable
  return self.isPassable
  

#Test code
#newtile = Tile(1,1,0)

#newtile.get_xcoordinate()
#newtile.get_ycoordinate()
#newtile.get_coordinates()
#newtile.get_image()
#newtile.get_isPassable()
