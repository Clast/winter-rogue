#COMMIT DAMN YOU
import random, sys, pygame
from Item_Database import *
from Map_Object import *
from Menu import *
from Log import *
from StateMachine import *
from LevelHandler import levelhandler

#from Dungeon import *

global log
log = Log()
class Actor(Map_Object):#Actor inherits from Map_Object to be able to post to the map

    def __init__(self, name, health, attackdamage, level):#These stats are shared between the Player and Monster Classes
        self.name=name
        self.base_health=health
        self.base_damage=attackdamage
        self.level=level
        self.speed = 100
        self.name = "Actor"

class Player(Actor):#This class is for only the user-created player
    def __init__(self, x, y, imgpath, name, health, attackdamage):
        self.type = 'Player'
    #X and Y coordinates are set for the map
        self.xcoordinate = x
        self.ycoordinate = y
    #The image associated with the player is attached this instance of the class
        self.imgpath = imgpath
        self.Img = pygame.image.load(imgpath)
    #Basic Player attributes are assigned
        self.name=name
        self.base_health=health
        self.base_damage=attackdamage
        self.bonus_health=0
        self.bonus_damage=0
        self.total_health=self.base_health+self.bonus_health
        self.total_damage=self.base_damage+self.bonus_damage
        self.current_health=self.total_health
        self.level=1
        self.XP=0
        self.levelXP=100
        self.gold=0
        self.speed = 110
    #A player needs an inventory in order to house all items and an equipment list for items that modify the
    #players bonus attributes
        self.equipment=Equipment()
        self.inventory=Inventory()
        self.charactermenu = EquipmentMenu(self,32*32/2-100,25*32/2-100)
        print 32*32/2,25*32/2
        self.charactersheet=self.charactermenu.menusurface
        self.charactermenu.Update()
        self.inventorymenu=InventoryMenu(self,32*32/2-75,25*32/2-45)
        self.inventorysheet=self.inventorymenu.menusurface

    def equip_item(self, index):#This function moves an item from the player's inventory into the equipment
        Item=self.inventory.items[index]
        if self.equipment.check_slot(Item.type):#Check to see an item of the same type is already equipped
            self.equipment.add_item(Item)
            self.inventory.remove_item(Item)
        else:#If the item type is already equipped, you must swap out the item that is equipped with the item from the inventory
        #A special case occurs with weapons, For example if you equip a 2hander, you must unequip both your shield and 1hander
            if Item.type=='1h':
                for item in self.equipment.items:
                    if item.type=='1h' or item.type=='2h':
                        self.inventory.add_item(item)
                        self.equipment.remove_item(item)
                self.equipment.add_item(Item)
                self.inventory.remove_item(Item)
            elif Item.type=='2h':
                for item in self.equipment.items:
                    if item.type=='1h' or item.type=='2h' or item.type=='shield':
                        self.inventory.add_item(item)
                        self.equipment.remove_item(item)
                for item in self.equipment.items:
                    if item.type=='1h' or item.type=='2h' or item.type=='shield':
                        self.inventory.add_item(item)
                        self.equipment.remove_item(item)
                self.equipment.add_item(Item)
                self.inventory.remove_item(Item)
            elif Item.type=='shield':
                for item in self.equipment.items:
                    if item.type=='2h' or item.type=='shield':
                        self.inventory.add_item(item)
                        self.equipment.remove_item(item)
                self.equipment.add_item(Item)
                self.inventory.remove_item(Item)
            else:
                for item in self.equipment.items:
                    if Item.type==item.type:
                        self.inventory.add_item(item)
                        self.equipment.remove_item(item)
                self.equipment.add_item(Item)
                self.inventory.remove_item(Item)
        self.update_stats()
        self.charactermenu.Update()

    def unequip_item(self,index):#This function removes an item from the player's equipment
        Item=self.equipment.items[index]
        if len(self.inventory.items)!=self.inventory.maxNumberOfItems:  
            for item in self.equipment.items:
                if Item==item:
                    self.inventory.add_item(item)
                    self.equipment.remove_item(item)
        self.update_stats()
        self.charactermenu.Update()


    def update_menu(self):
        self.equipmenu.blit(pygame.image.load('images/equipmentGrid.png'), (self.equipmenu.xcoord,self.equipmenu.ycoord))
        fontObj = pygame.font.Font('freesansbold.ttf',16)
        self.equipmenu.blit(fontObj.render(self.Player.name, True, self.WHITE,self.BLACK),(self.equipmenu.xcoord+75,self.equipmenu.ycoord))
        for item in self.Player.equipment.items:
            if item.type=='head':
                self.equipmenu.blit(item.image,(self.xcoord+10,self.ycoord+10))
            if item.type=='shoulders':
                self.equipmenu.blit(item.image,(self.xcoord+150,self.ycoord+10))
            if item.type=='chest':
                self.equipmenu.blit(item.image,(self.xcoord+10,self.ycoord+60))
            if item.type=='hands':
                self.equipmenu.blit(item.image,(self.xcoord+150,self.ycoord+60))
            if item.type=='legs':
                self.equipmenu.blit(item.image,(self.xcoord+10,self.ycoord+110))
            if item.type=='feet':
                self.equipmenu.blit(item.image,(self.xcoord+150,self.ycoord+110))
            if item.type=='1h' or item.type=='2h':
                self.equipmenu.blit(item.image,(self.xcoord+10,self.ycoord+160))
            if item.type=='shield':
                self.equipmenu.blit(item.image,(self.xcoord+150,self.ycoord+160))

    def update_stats(self):#This function updates the bonuses that the player gets from items in their inventory
        self.bonus_health=0
        self.bonus_damage=0
        for item in self.equipment.items:

            self.bonus_health=self.bonus_health+int(item.health)
            self.bonus_damage=self.bonus_damage+int(item.damage)
        self.current_health=self.total_health-self.current_health
        self.total_health=self.bonus_health+self.base_health
        self.total_damage=self.bonus_damage+self.base_damage
        self.current_health=self.total_health-self.current_health

    def display_stats(self):#This function prints out the player's stats
        self.update_stats()

        print "Player Stats: "
        print "***********************"
        print "Current Level: %d" % self.level
        print "Experience: %d/%d" % (self.XP,self.levelXP)
        print "Total health: %d/%d" % (self.current_health,self.total_health)
        print "Total damage: %d" % self.total_damage
        print "***********************"


    def levelUp(self):#This changes the level based on the experience that the player has
        self.XP=self.XP-self.levelXP
        self.level=self.level+1
        self.levelXP=100+self.level*125
        self.base_health=self.base_health+10
        self.base_damage=self.base_damage+4
        self.update_stats()

    def battleWin(self,Monster):#This function is accessed when the player defeats a monster in battle
        self.XP=self.XP+(Monster.level*Monster.XP)/self.level#If the experience is high enough to go to the next level, it carries over the remaining XP
        if self.XP>=self.levelXP:
            self.levelUp()
        self.gold=self.gold+Monster.gold

        for items in Monster.loot.items:
            log.addEvent((1,"You looted " + items.name))
            self.inventory.add_item(items)

    def battleLose(self):
        print "GAME OVER"
        sys.exit(0)

    def move(self, dx, dy):

    #The move function is special in that it accepts the map and objectlist on which you are moving (along with the change in x and y). It follows the following basic structure:
    #1) Determine if anything exists at the destination, tile or object.
    #2) If something exists, perform the associated action (whether denying movement or attacking a monster)
    #3) If nothing exists, move to that tile and set the player coordinates to the target.

        tiletarget = None
        target = None
        newx = self.xcoordinate + dx
        newy = self.ycoordinate + dy
        mapincrement = 0 
        map = levelhandler.activelevel().map
        objectlist = levelhandler.activelevel().objectlist

        for row in map:
            for tile in row:#Check to see if the tile exists at new location, if so, assign the tile to tiletarget
                if tile.xcoordinate == newx and tile.ycoordinate == newy:
                    tiletarget = tile
                    break


        for object in objectlist: #Check to see if anything exists at target location, if so, assign the object to target
            if object.xcoordinate == newx and object.ycoordinate == newy:
                target = object
                break

    # print target.__class__.__name__
        if tiletarget is None: #Does the tile exist?
            log.addEvent((1,"You are attempting to move outside the map!"))
        elif tiletarget.isPassable != 1: #Is the tile passable?
            log.addEvent((1,"The tile you are attempting to move into is not passable!"))
        elif target is not None: #If there is a monster, attack it
            if target.__class__.__name__=='Monster':
                log.addEvent((1,"You attack %s, dealing %s damage." % (target.name,self.total_damage)))
                target.current_health=target.current_health-self.total_damage
                if target.current_health<=0:
                    self.battleWin(target)
                    objectlist.remove(target)
                else:
                    log.addEvent((1,"%s attacks you back, dealing %s damage." % (target.name,target.damage)))
                    self.current_health=self.current_health-target.damage
                    if self.current_health<=0:
                        self.battleLose()
            elif target.__class__.__name__=='NPC':
                target.engage_dialogue(self)


        elif target is None: #Otherwise move
            #print("You successfully move!")
            self.xcoordinate += dx
            self.ycoordinate += dy

class Monster(Actor):#This class contains standard stats and location variables along with a loot list that contains items that the player can loot
    def __init__(self, xcoord,ycoord, name, health, attackdamage, level,imgpath, Rarity_Database, Item_Database):
        self.name=name
        self.type='monster'
        self.health=health
        self.current_health=health
        self.damage=attackdamage
        self.level=level
        self.loot=Loot()
        self.XP=level*60
        self.imgpath = imgpath
        self.xcoordinate=xcoord
        self.ycoordinate=ycoord
        self.tilecoordinatex = xcoord/32
        self.tilecoordinatey = ycoord/32
        self.Img = pygame.image.load(imgpath)
        self.AI = StateMachine(self)
        self.target = None
        index=0
        self.speed = 100
        self.canSee = {}
        
        
        #print self.xcoordinate,self.ycoordinate
        
        self.AI.states['Attack'] = Attack()
        self.AI.states['Flee'] = Flee()
        self.AI.states['Rest'] = Rest()
        self.AI.transitions["toAttack"] = Transition("Attack")
        self.AI.transitions["toFlee"] = Transition('Flee')
        self.AI.transitions["toRest"] = Transition('Rest')
        
        self.AI.SetState("Rest")

        for item in Rarity_Database[self.level]:#Populate randomly generated loot based on rarity
            item=int(item.rstrip())
            chance=random.randint(1,10000)
            if chance <= item:
                self.loot.add_item(Item_Database.items[index])
            chance= random.randint(1,100)
            if chance <=80:
                self.gold=chance*self.level*30/80
            index=index+1
    def display_stats(self):#This function prints out the player's stats
        print "Monster Stats: "
        print "Monster Name: ", self.name
        print "Monster Level: ", self.level
        print "Total health: %d" % self.health
        print "Total damage: %d" % self.damage
        print "Gold from killing", self.gold
    
    def look(self):
        sensedistance = 4 #Sight range is this value - 1
        target = None
        tiletarget = None
        dungeon = levelhandler.activelevel()
        
        ##THIS IS THE UGLIEST CODE I HAVE EVER WRITTEN, WARNING
        ##Look up
        for x in range(1,sensedistance):
            x+1
            newx = self.tilecoordinatex 
            newy = self.tilecoordinatey - x
            try:
                if target == None:
                    tiletarget = dungeon.map[newx][newy] ##Does the tile exist?
                    for object in dungeon.objectlist: ##If so, is there an object on it?
                        if object.xcoordinate == newx*32 and object.ycoordinate == newy*32:
                            target = object
                            print "I see: %s, at %s, %s" %(target, newx, newy)
                            break
                        else: 
                            break                    
           
            except IndexError:
                tiletarget = None
                print "I generate index errors"
                break
        
        ##Look down
        for x in range(1,sensedistance):
            x+1
            newx = self.tilecoordinatex 
            newy = self.tilecoordinatey + x
            try:
                if target == None:
                    tiletarget = dungeon.map[newx][newy] ##Does the tile exist?
                    for object in dungeon.objectlist: ##If so, is there an object on it?
                        if object.xcoordinate == newx*32 and object.ycoordinate == newy*32:
                            target = object
                            print "I see: %s, at %s, %s" %(target, newx, newy)
                            break
                        else: 
                            break                       
            except IndexError:
                tiletarget = None
                print "I generate index errors"
                break
            
            ##Look east
        for x in range(1,sensedistance):
            x+1
            newx = self.tilecoordinatex + x
            newy = self.tilecoordinatey 
            try:
                if target == None:
                    tiletarget = dungeon.map[newx][newy] ##Does the tile exist?
                    for object in dungeon.objectlist: ##If so, is there an object on it?
                        if object.xcoordinate == newx*32 and object.ycoordinate == newy*32:
                            target = object
                            print "I see: %s, at %s, %s" %(target, newx, newy)
                            break
                        else: 
                            break
           
            except IndexError:
                tiletarget = None
                print "I generate index errors"
                break
            
            #Look West
        for x in range(1,sensedistance):
            x+1
            newx = self.tilecoordinatex - x
            newy = self.tilecoordinatey 
            try:
                if target == None:
                    tiletarget = dungeon.map[newx][newy] ##Does the tile exist?
                    for object in dungeon.objectlist: ##If so, is there an object on it?
                        if object.xcoordinate == newx*32 and object.ycoordinate == newy*32:
                            target = object
                            print "I see: %s, at %s, %s" %(target, newx, newy)
                            break
                        else: 
                            break
                        
            except IndexError:
                tiletarget = None
                print "I generate index errors"
                break
                    
                #Look NorthEast
        for x in range(1,sensedistance):
            x+1
            newx = self.tilecoordinatex + x
            newy = self.tilecoordinatey + x
            try:
                if target == None:
                    tiletarget = dungeon.map[newx][newy] ##Does the tile exist?
                    for object in dungeon.objectlist: ##If so, is there an object on it?
                        if object.xcoordinate == newx*32 and object.ycoordinate == newy*32:
                            target = object
                            print "I see: %s, at %s, %s" %(target, newx, newy)
                            break
                        else: 
                            break
           
            except IndexError:
                tiletarget = None
                print "I generate index errors"
                break
                
                #Look NorthWest
        for x in range(1,sensedistance):
            x+1
            newx = self.tilecoordinatex - x
            newy = self.tilecoordinatey + x
            try:
                if target == None:
                    tiletarget = dungeon.map[newx][newy] ##Does the tile exist?
                    for object in dungeon.objectlist: ##If so, is there an object on it?
                        if object.xcoordinate == newx*32 and object.ycoordinate == newy*32:
                            target = object
                            print "I see: %s, at %s, %s" %(target, newx, newy)
                            break
                        else: 
                            break
           
            except IndexError:
                tiletarget = None
                print "I generate index errors"
                break
                #Look SouthEast
        for x in range(1,sensedistance):
            x+1
            newx = self.tilecoordinatex + x
            newy = self.tilecoordinatey - x
            try:
                if target == None:
                    tiletarget = dungeon.map[newx][newy] ##Does the tile exist?
                    for object in dungeon.objectlist: ##If so, is there an object on it?
                        if object.xcoordinate == newx*32 and object.ycoordinate == newy*32:
                            target = object
                            print "I see: %s, at %s, %s" %(target, newx, newy)
                            break
                        else: 
                            break
           
            except IndexError:
                tiletarget = None
                print "I generate index errors"
                break
                
                #Look SouthWest
        for x in range(1,sensedistance):
            x+1
            newx = self.tilecoordinatex - x
            newy = self.tilecoordinatey - x
            try:
                if target == None:
                    tiletarget = dungeon.map[newx][newy] ##Does the tile exist?
                    for object in dungeon.objectlist: ##If so, is there an object on it?
                        if object.xcoordinate == newx*32 and object.ycoordinate == newy*32:
                            target = object
                            print "I see: %s, at %s, %s" %(target, newx, newy)
                            break
                        else: 
                            break
           
            except IndexError:
                tiletarget = None
                print "I generate index errors"
                break
                    
        if target != None and target not in self.canSee:
            self.canSee[target.type] = (target.xcoordinate,target.ycoordinate)
            print self.canSee
        if len(self.canSee) > 0:
            print self.canSee
        
    def move(self, dx, dy):

    #The move function is special in that it accepts the map and objectlist on which you are moving (along with the change in x and y). It follows the following basic structure:
    #1) Determine if anything exists at the destination, tile or object.
    #2) If something exists, perform the associated action (whether denying movement or attacking a monster)
    #3) If nothing exists, move to that tile and set the player coordinates to the target.

        tiletarget = None
        target = None
        newx = self.xcoordinate + dx
        newy = self.ycoordinate + dy
        mapincrement = 0 
        map = levelhandler.activelevel().map
        objectlist = levelhandler.activelevel().objectlist

        for row in map:
            for tile in row:#Check to see if the tile exists at new location, if so, assign the tile to tiletarget
                if tile.xcoordinate == newx and tile.ycoordinate == newy:
                    tiletarget = tile
                    break


        for object in objectlist: #Check to see if anything exists at target location, if so, assign the object to target
            if object.xcoordinate == newx and object.ycoordinate == newy:
                target = object
                break

    # print target.__class__.__name__
        if tiletarget is None: #Does the tile exist?
            log.addEvent((1,"A monster is attempting to move outside the map!"))
        elif tiletarget.isPassable != 1: #Is the tile passable?
            log.addEvent((1,"A monster is trying to move into an impassable tile!"))
        elif target is not None: #If there is a monster, attack it
            if target.__class__.__name__=='Player':
                log.addEvent((1,"A monster attacks %s, dealing %s damage." % (target.name,self.damage)))
                target.current_health=target.current_health-self.damage
                #if target.current_health<=0:
                 #   self.battleWin(target)
                  #  objectlist.remove(target)
                #else:
                 #   log.addEvent((1,"%s attacks you back, dealing %s damage." % (target.name,target.damage)))
                  #  self.current_health=self.current_health-target.damage
                   # if self.current_health<=0:
                    #    self.battleLose()
            #elif target.__class__.__name__=='NPC':
             #   target.engage_dialogue(self)


        elif target is None: #Otherwise move
            #print("A monster moves")
            self.xcoordinate += dx
            self.ycoordinate += dy

class NPC(Actor):
    def __init__(self, x, y, health, level, type, Rarity_Database, Item_Database):

        self.xcoordinate=x
        self.ycoordinate=y
        self.health=health
        self.level=level
        self.inventory=Inventory()
        self.gold=0
        self.imagepath='images/' + type + '.png'
        self.Img = pygame.image.load(self.imagepath)
        self.type=type
        index=0
        self.speed = 0
        self.name = "NPC"
        if type == 'shopkeeper':
            for item in Rarity_Database[self.level]:#Populate randomly generated loot based on rarity
                #print item
                item=int(item.rstrip())
                chance=random.randint(1,10000)
                if chance <= item*5:
                    self.inventory.add_item(Item_Database.items[index])
                index=index+1

    def engage_dialogue(self, Player):
        if self.type=='healer':
            print "Please enter the amount of health that you would like me to heal you for."
            print ">",
            heal=int(raw_input()) 
            while heal*1.5>=Player.gold or heal>Player.total_health-Player.current_health:
                if heal*1.5>=Player.gold:
                    print "You do not have enough money!"
                    print "Please enter a lower amount."
                    print ">",
                    heal=int(raw_input())
                else:
                    print "I cannot heal you for more than your maximum health"
                    print "Please enter a lower amount."
                    print ">",
                    heal=int(raw_input())
            print "In order to heal you for %s HP, you will need to pay %s gold. Will this be OK? (Y/N)" % (heal,heal*1.5)
            print ">",
            answer=raw_input()
            while (answer != 'Y' and answer != 'y' and answer != 'N' and answer != 'n'):
                print "Invalid entry, please try again."
                print "In order to heal you for %s HP, you will need to pay %s gold. Will this be OK? (Y/N)" % (heal,heal*1.5)
                print ">",
                answer=raw_input()
            if answer=='Y' or answer=='y':
                Player.gold=Player.gold-heal*1.5
                Player.current_health=Player.current_health+heal
        elif self.type=='shopkeeper':
            chatting = True
            while chatting == True:
                print "What would you like to do?"
                print "1. Buy"
                print "2. Sell"
                print "3. Leave"
                print ">",
                answer = int(raw_input())
                while (answer!= 1 and answer!= 2 and answer != 3):
                    print "Invalid Entry!"
                    print "What would you like to do?"
                    print "1. Buy"
                    print "2. Sell"
                    print "3. Leave"
                    print ">",
                    answer = int(raw_input())
                if answer == 1:
                    print "Select the item that you are interested in purchasing"
                    print "Please view what I currently have to sell below:"
                    self.inventory.display()
                    print ">",
                    item = int(raw_input())
                    while item>=len(self.inventory.items) or len(Player.inventory.items) == Player.inventory.maxNumberOfItems or int(self.inventory.items[item].buygold)>Player.gold:
                        if item>=len(self.inventory.items):
                            print "Invalid Entry!"
                            print "Select the item that you are interested in purchasing"
                            print ">",
                            item = int(raw_input()) 
                        elif len(Player.inventory.items) == Player.inventory.maxNumberOfItems:
                            print "You do not have room in your inventory to hold any more items!"
                            print "Please sell an item before attempting to purchase more."
                            break
                        elif int(self.inventory.items[item].buygold)>Player.gold:
                            print self.inventory.items[item].buygold
                            print Player.gold
                            print "You do not have enough gold to purchase this item!"
                            print "Please select a different item"
                            print ">",
                            item = int(raw_input()) 
                    print "The item you have selected costs %s gold pieces." % self.inventory.items[item].buygold
                    print " Would you like to purchase this item? (Y/N)"
                    print ">",
                    answer = raw_input()
                    while (answer != 'Y' and answer != 'y' and answer != 'N' and answer != 'n'):
                        print "Invalid Entry!"
                        print "Please enter either Y or N."
                        print ">"
                        answer = raw_input()
                    if answer == 'Y' or answer == 'y':
                        Player.inventory.add_item(self.inventory.items[item])
                        Player.gold=Player.gold-int(self.inventory.items[item].buygold)
                        self.inventory.remove_item(self.inventory.items[item])
                elif answer == 2:
                    print "select an item that you would like to sell:"
                    Player.inventory.display()
                    print ">",
                    item = int(raw_input())
                    while item >= len(Player.inventory.items):
                        print "Invalid Entry!"
                        print "Select an item that you would like to sell."
                        print ">"
                        item = int(raw_input())
                    print "Would you like to sell %s for %s gold pieces? (Y/N)" % (Player.inventory.items[item].name,Player.inventory.items[item].sellgold)
                    print ">"
                    answer = raw_input()
                    while (answer != 'Y' and answer != 'y' and answer != 'N' and answer != 'n'):
                        print "Invalid Entry!"
                        print "Please enter either Y or N."
                        print ">"
                        answer = raw_input()
                    if answer == 'Y' or answer == 'y':
                        Player.gold=Player.gold+int(Player.inventory.items[item].sellgold)
                        Player.inventory.remove_item(Player.inventory.items[item])
                else:
                    chatting = False
        else:
            pass


