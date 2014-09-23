import pygame, sys, random
from pygame.locals import *
from Tile import *
from Actor import *

#The LevelHandler class stores all the dungeons in the game and keeps track of whatever map you are currently on.
class LevelHandler:

 def __init__(): #It receives the boardHeight and boardWidth in tiles. Columns = Width, Rows = Height
	
	self.dungeonlist = []
	self.currentlevel = 0
