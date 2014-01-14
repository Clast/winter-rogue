#from Map_Object import *
import pygame
from Map_Object import *

class Item(Map_Object):

 def __init__(self, itemNumber,name, health, attackdamage, picture, type, buygold, sellgold):#All of these stats are specific to the item class
  self.number=itemNumber
  self.name=name
  self.health = health
  self.damage = attackdamage
  self.image = pygame.image.load(picture)
  self.type=type
  self.sellgold=sellgold
  self.buygold=buygold
  
 #Accessor functions to all variables in the item class
 def get_number(self):
  return self.number
  
 def get_name(self):
  return self.name
  
 def get_health(self):
  return self.health
  
 def get_damage(self):
  return self.damage
  
 def get_image(self):
  return self.image
  
 def get_type(self):
  return self.type
 