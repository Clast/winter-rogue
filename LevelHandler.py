import pygame, sys, random
from pygame.locals import *
from Tile import *
from Actor import *
from Dungeon import *

#The LevelHandler class stores all the dungeons in the game and keeps track of whatever map you are currently on.
class LevelHandler:

 def __init__(self):
	
	
	self.dungeonlist = []
	self.currentlevel = -1

 def move_floor(self,i):
	if (len(self.dungeonlist)	> 0):
		self.currentlevel = self.currentlevel + i
		
levelhandler = LevelHandler()
levelhandler.dungeonlist.append('a')