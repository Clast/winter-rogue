#from Map_Object import *
import pygame
from Map_Object import *
from pygame.locals import *

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
  self.BLACK = (0,0,0)
  pygame.init()
  pygame.font.init()  
  self.menusurface = pygame.Surface((200,200))
  self.menusurface.fill(self.BLACK)
  self.font = pygame.font.SysFont("times new roman", 15)
  
  self.itemName = self.font.render(self.name, 1, (255,255,0))
  self.itemHealth = self.font.render("Health: " + str(self.health), 1, (255,255,0))
  self.itemDamage = self.font.render("Damage: " + str(self.damage), 1, (255,255,0))
  self.itemType = self.font.render("Item Slot: " + self.type, 1, (255,255,0))
  self.itemSell = self.font.render("Sells For: " + str(self.sellgold), 1, (255,255,0))
  
  self.menusurface.blit(self.itemName, (50,20))
  self.menusurface.blit(self.itemHealth, (0,40))
  self.menusurface.blit(self.itemDamage, (0,60))
  self.menusurface.blit(self.itemType, (0,80))
  self.menusurface.blit(self.itemSell, (0,100))
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
 