import pygame, sys, random
from pygame.locals import *
from Tile import *
from Dungeon import *
from Actor import *
from Menu import *


class Menu(pygame.Surface):

    def __init__(self, Player,xloc,yloc):
        
        #pygame.init()

        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.BLACK = (0,0,0)

        #pygame.font.init()
        

        self.Player = Player
        #X,Y coordinates of the surface itself
        self.xcoord = 0
        self.ycoord = 0
        #X,Y location on the display
        self.xloc=xloc
        self.yloc=yloc
        self.menusurface

    def Inventory(self):
        self.menusurface = pygame.Surface((500,300))
        self.menusurface.fill(self.BLACK)
        
       
        
        fontObj = pygame.font.Font('freesansbold.ttf', 16) 
        
        iteminformationnumber = fontObj.render("No.", True, self.WHITE, self.BLACK)
        iteminformationname = fontObj.render("Name", True, self.WHITE,self.BLACK)
        iteminformationdamage = fontObj.render("Damage", True, self.WHITE, self.BLACK)
        iteminformationhealth = fontObj.render("Health", True, self.WHITE, self.BLACK)
        iteminformationtype = fontObj.render("Type", True, self.WHITE, self.BLACK)
        
        
        
        xcoord = 50
        ycoord = 30
        itemindex = 1
        
        self.menusurface.blit(iteminformationnumber, (xcoord, ycoord-20))
        self.menusurface.blit(iteminformationname, (xcoord+50, ycoord-20))
        self.menusurface.blit(iteminformationdamage, (xcoord+200, ycoord-20))
        self.menusurface.blit(iteminformationhealth, (xcoord+300, ycoord-20))
        self.menusurface.blit(iteminformationtype, (xcoord+400, ycoord-20))
        for item in self.Player.inventory.items:
            #print(itemindex)
            itemnumber = fontObj.render(str(itemindex), True, self.WHITE, self.BLACK)
            itemname = fontObj.render(str(item.name), True, self.WHITE, self.BLACK)
            itemdamage = fontObj.render(str(item.damage), True, self.WHITE, self.BLACK)
            itemhealth = fontObj.render(str(item.health), True, self.WHITE, self.BLACK)
            itemtype = fontObj.render(str(item.type), True, self.WHITE, self.BLACK)
            itemindex += 1
            
            
            
            self.menusurface.blit(itemnumber, (xcoord, ycoord)) #Consider making the xcoordinate addition for subsequent values a ratio of screen size versus hardcoded
            self.menusurface.blit(itemname, (xcoord+50, ycoord))
            self.menusurface.blit(itemdamage, (xcoord+200,ycoord))
            self.menusurface.blit(itemhealth, (xcoord+300,ycoord))
            self.menusurface.blit(itemtype, (xcoord+400,ycoord))
            ycoord += 25
        return self.menusurface
        
    #def newInventory(self):
     
    def Character(self):
        self.menusurface = pygame.Surface((480,310))
        self.menusurface.fill(self.BLACK)
        
        fontObj = pygame.font.Font('freesansbold.ttf', 16) 
        
        namestring = str(self.Player.name)
        namerender = fontObj.render(namestring, True, self.WHITE, self.BLACK)
        
        levelstring = "Level: %s" % str(self.Player.level)
        levelrender = fontObj.render(levelstring, True, self.WHITE, self.BLACK)
        
        levelxpstring = "%s/%s" % (str(self.Player.XP), str(self.Player.levelXP))
        levelxprender = fontObj.render(levelxpstring, True, self.WHITE, self.BLACK)
        
        HPstring = "HP: %s/%s (%s+%s)" % (str(self.Player.current_health), str(self.Player.total_health), str(self.Player.base_health), str(self.Player.bonus_health))    
        hprender = fontObj.render(HPstring, True, self.WHITE, self.BLACK)
        
        goldstring = "Gold: %s" % (str(self.Player.gold))
        goldrender = fontObj.render(goldstring, True, self.WHITE, self.BLACK)
        
        damagestring = "Attack Damage: %s (%s+%s)" % (str(self.Player.total_damage), str(self.Player.base_damage),str(self.Player.bonus_damage))
        damagerender = fontObj.render(damagestring, True, self.WHITE, self.BLACK)
        
        inventorystring = "Inventory: %s/%s" % (len(self.Player.inventory.items),str(self.Player.inventory.maxNumberOfItems))
        inventoryrender = fontObj.render(inventorystring, True, self.WHITE, self.BLACK)
        
        
        
        self.menusurface.blit(namerender, (175, 20))
        self.menusurface.blit(levelrender, (170, 45))
        self.menusurface.blit(levelxprender, (170, 70))
        self.menusurface.blit(hprender,(15,150))
        self.menusurface.blit(damagerender,(225, 150))
        self.menusurface.blit(goldrender,(15,200))
        self.menusurface.blit(inventoryrender,(225,200))
        #print(self.Player.name)
        
        
        return self.menusurface

		
class StatsMenu(Menu):
 def __init__(self, Player):
  pygame.init()
  self.WHITE = (255, 255, 255)
  self.GREEN = (0, 255, 0)
  self.BLUE = (0, 0, 255)
  self.BLACK = (0,0,0)
  self.width=384
  self.height=160
  self.Player = Player
  #X,Y coordinates of the surface itself
  self.xcoord = 640
  self.ycoord = 800
  #X,Y location on the display
  pygame.font.init()  
  self.menusurface = pygame.Surface((self.width,self.height))
  self.menusurface.fill(self.BLACK)
  #fontObj = pygame.font.Font('freesansbold.ttf',16)
  self.font = pygame.font.SysFont("times new roman", 15)
  self.Update(self.Player)
  
 def Update(self, player):
 
 
   self.Player=player
   #Extract all of the current 
   self.playerName = self.font.render(self.Player.name, 1, (255,255,0))
   self.playerHealth = self.font.render("Health: " + str(self.Player.current_health) + " / " + str(self.Player.total_health), 1, (255,255,0))
   self.playerDamage = self.font.render("Damage: " + str(self.Player.total_damage), 1, (255,255,0))
   self.playerLevel = self.font.render("Level: " + str(self.Player.level), 1, (255,255,0))
   self.playerXP = self.font.render("Experience: " + str(self.Player.XP) + " / " + str(self.Player.levelXP), 1, (255,255,0))
   self.playerGold = self.font.render("Current Gold: " + str(self.Player.gold), 1, (255,255,0))
 
	#update all of the information on the menusurface
   self.menusurface.fill(self.BLACK)
   self.menusurface.blit(self.playerName, (150,0))
   self.menusurface.blit(self.playerLevel, (150,20))
   self.menusurface.blit(self.playerXP, (120,40))
   self.menusurface.blit(self.playerHealth, (20,60))
   self.menusurface.blit(self.playerDamage, (20,80))
   self.menusurface.blit(self.playerGold, (20,100))
 
  

  
class InventoryMenu(Menu):
 def __init__(self, Player,xloc,yloc):
  pygame.init()
  self.WHITE = (255, 255, 255)
  self.GREEN = (0, 255, 0)
  self.BLUE = (0, 0, 255)
  self.BLACK = (0,0,0)
  self.width=150
  self.height=100
  self.Player = Player
  #X,Y coordinates of the surface itself
  self.xcoord = 0
  self.ycoord = 0
  #X,Y location on the display
  self.xloc=xloc
  self.yloc=yloc   
  pygame.font.init()  
  self.menusurface = pygame.Surface((self.width,self.height))
  self.menusurface.fill(self.WHITE)
  self.menusurface.blit(pygame.image.load('images/inventoryGrid.png'), (0,0))
  fontObj = pygame.font.Font('freesansbold.ttf',16)
  self.menusurface.blit(fontObj.render('Inventory', True, self.WHITE,self.BLACK),(self.xcoord+45,self.ycoord))
  self.Update()
        
 def Update(self):  
  self.menusurface.blit(pygame.image.load('images/inventoryGrid.png'), (0,0)) 
  fontObj = pygame.font.Font('freesansbold.ttf',16)
  self.menusurface.blit(fontObj.render('Inventory', True, self.WHITE,self.BLACK),(self.xcoord+45,self.ycoord))
  tempx=10
  tempy=20
  for item in self.Player.inventory.items:
   self.menusurface.blit(item.image,(tempx,tempy))
   if tempx==110:
    tempx=10
    tempy=60
   else:
    tempx=tempx+50

    
class EquipmentMenu(Menu):

 def __init__(self, Player,xloc,yloc):
  pygame.init()
  self.WHITE = (255, 255, 255)
  self.GREEN = (0, 255, 0)
  self.BLUE = (0, 0, 255)
  self.BLACK = (0,0,0)
  self.width=200
  self.height=200
  self.Player = Player
  #X,Y coordinates of the surface itself
  self.xcoord = 0
  self.ycoord = 0
  #X,Y location on the display
  self.xloc=xloc
  self.yloc=yloc   
  pygame.font.init()  
  self.menusurface = pygame.Surface((self.width,self.height))
  self.menusurface.fill(self.WHITE)
  self.menusurface.blit(pygame.image.load('images/equipmentGrid.png'), (0,0))
  fontObj = pygame.font.Font('freesansbold.ttf',16)
  self.menusurface.blit(fontObj.render(self.Player.name, True, self.WHITE,self.BLACK),(self.xcoord+75,self.ycoord))
  self.Update()
 
 def Update(self):    
  self.menusurface.blit(pygame.image.load('images/equipmentGrid.png'), (0,0))
  fontObj = pygame.font.Font('freesansbold.ttf',16)
  self.menusurface.blit(fontObj.render(self.Player.name, True, self.WHITE,self.BLACK),(self.xcoord+75,self.ycoord))
  for item in self.Player.equipment.items:
   if item.type=='head':
    self.menusurface.blit(item.image,(self.xcoord+10,self.ycoord+10))
   if item.type=='shoulders':
    self.menusurface.blit(item.image,(self.xcoord+150,self.ycoord+10))
   if item.type=='chest':
    self.menusurface.blit(item.image,(self.xcoord+10,self.ycoord+60))
   if item.type=='hands':
    self.menusurface.blit(item.image,(self.xcoord+150,self.ycoord+60))
   if item.type=='legs':
    self.menusurface.blit(item.image,(self.xcoord+10,self.ycoord+110))
   if item.type=='feet':
    self.menusurface.blit(item.image,(self.xcoord+150,self.ycoord+110))
   if item.type=='1h' or item.type=='2h':
    self.menusurface.blit(item.image,(self.xcoord+10,self.ycoord+160))
   if item.type=='shield':
    self.menusurface.blit(item.image,(self.xcoord+150,self.ycoord+160))

        
        
    def Equipment(self):
        self.menusurface = pygame.Surface((500,300))
        self.menusurface.fill(self.BLACK)
        
        fontObj = pygame.font.Font('freesansbold.ttf', 16) 
        
        iteminformationnumber = fontObj.render("No.", True, self.WHITE, self.BLACK)
        iteminformationname = fontObj.render("Name", True, self.WHITE,self.BLACK)
        iteminformationdamage = fontObj.render("Damage", True, self.WHITE, self.BLACK)
        iteminformationhealth = fontObj.render("Health", True, self.WHITE, self.BLACK)
        iteminformationtype = fontObj.render("Type", True, self.WHITE, self.BLACK)
        
        xcoord = 50
        ycoord = 30
        itemindex = 1
        
        self.menusurface.blit(iteminformationnumber, (xcoord, ycoord-20))
        self.menusurface.blit(iteminformationname, (xcoord+50, ycoord-20))
        self.menusurface.blit(iteminformationdamage, (xcoord+200, ycoord-20))
        self.menusurface.blit(iteminformationhealth, (xcoord+300, ycoord-20))
        self.menusurface.blit(iteminformationtype, (xcoord+400, ycoord-20))
        
        for item in self.Player.equipment.items:
            itemnumber = fontObj.render(str(itemindex), True, self.WHITE, self.BLACK)
            itemname = fontObj.render(str(item.name), True, self.WHITE, self.BLACK)
            itemdamage = fontObj.render(str(item.damage), True, self.WHITE, self.BLACK)
            itemhealth = fontObj.render(str(item.health), True, self.WHITE, self.BLACK)
            itemtype = fontObj.render(str(item.type), True, self.WHITE, self.BLACK)
            itemindex += 1
            
            self.menusurface.blit(itemnumber, (xcoord, ycoord)) #Consider making the xcoordinate addition for subsequent values a ratio of screen size versus hardcoded
            self.menusurface.blit(itemname, (xcoord+50, ycoord))
            self.menusurface.blit(itemdamage, (xcoord+200,ycoord))
            self.menusurface.blit(itemhealth, (xcoord+300,ycoord))
            self.menusurface.blit(itemtype, (xcoord+400,ycoord))
            ycoord += 25

            
 

        #print(self.Player.name)
        
        
        return self.menusurface
        
#WHITE = (255, 255, 255)

#pygame.init()
#DISPLAYSURF = pygame.display.set_mode((500,500), 0, 32)
#pygame.display.set_caption('Dev') #Window Title

#DISPLAYSURF.fill(WHITE) #Fill the screen area with white.

#player = Player(32,32,'images/player.png',"David",100,10)

#item1 = Item(0, "sword", 10, 10,'images/player.png',"1h")
#item2 = Item(1, "monkey dick", 5, 35,'images/player.png',"2h")
#item3 = Item(32, "monkey dick", 5, 35,'images/player.png',"2h")
#item4 = Item(5, "grawblewarble", 10, 15, 'images/player.png', "1h")

#player.inventory.add_item(item1)
#player.inventory.add_item(item2)
#player.inventory.add_item(item3)
#player.inventory.add_item(item4)


#menu = Menu(player)
#menu.Character()

#DISPLAYSURF.blit(menu.Character(), (25, 25))
#pygame.display.update()
