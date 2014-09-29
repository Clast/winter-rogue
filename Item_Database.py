#COMMIT DAMN YOU
from Item import *
from Map_Object import *
import csv
class Item_Database(Map_Object):

    def __init__(self):#This class is used to house all items that will be accessible in the game
        self.items=[]
        self.numberOfItems=0

    def add_item(self,Item):#This function adds an item to the database and then increments the counter
        self.items.append(Item)
        self.numberOfItems=self.numberOfItems+1

    def remove_item(self, Item):#This function locates an item to delete in the database and removes it while decrementing the counter
        find=Item.number
        for item in self.items:
            if item.get_number() == find:
                self.items.remove(item)
                break
        self.numberOfItems=self.numberOfItems-1

    def display(self):#Prints all of the stats for every item in the database
        number=0
        for item in self.items:
            print "Item Number: %d" % number
            print "Item Name: %s" % item.get_name()
            print "Item Health: %s" % item.get_health()
            print "Item Damage: %s" % item.get_damage()
            print "Item Type: %s" % item.get_type()
            number=number+1

    def import_database(self):#This function imports all items from the Item_Database CSV file in order for easy access
        for line in open("Item_Database.csv"):
            number,name,health,damage,image,type,buygold,sellgold = line.split(",")
            sellgold=int(sellgold.rstrip())
            dir='images/' + type + '.png'
            newItem=Item(number,name,health,damage,dir,type,buygold,sellgold)

            self.add_item(newItem)

class Inventory(Item_Database):#This class is will be used by the Player and NPC class to store all picked up items and tradeable items

    def __init__(self):#Sets a max number of items that a player/NPC can hold and keeps track of the items 
        self.items=[]
        self.numberOfItems=0
        self.maxNumberOfItems=6

    def add_item(self,Item):#This function adds an item to the current list of items
        if self.numberOfItems!=self.maxNumberOfItems:#checks to see if the inventory is full
            self.items.append(Item)
            self.numberOfItems=self.numberOfItems+1
        else:#Return an error if the inventory is full
            print "Maximum number of items reached, remove an item and try again."

class Loot(Item_Database):#This class is used by monsters and will allow the player to obtain items
    def remove_item(self, Item):#This function locates an item to delete in the database and removes it while decrementing the counter

        for item in self.items:
            if item==Item:
                self.items.remove(item)
        self.numberOfItems=self.numberOfItems-1

    pass

class Equipment(Item_Database):#This class is used by the Player class to add the bonuses for the player stats
#Boolean variables are used to keep track of which slot is currently occupied
    hasHead=False
    hasShoulder=False
    hasChest=False
    hasHands=False
    hasLegs=False 
    hasFeet=False
    has1h=False
    hasShield=False
    has2h=False

    def check_slot(self,slot):#This function returns true if a slot is currently occupied and false otherwise
        slot=slot.rstrip()
        for item in self.items:
            if slot == '1h' and (self.has1h or self.has2h):
                return False
            elif slot == '2h' and (self.has1h or self.has2h or self.hasShield):
                return False
            elif slot == 'shield' and (self.hasShield or self.has2h):
                return False
            elif (slot == 'head' and self.hasHead) or (slot == 'shoulders' and self.hasShoulder) or (slot== 'chest' and self.hasChest) or (slot=='hands' and self.hasHands) or (slot=='legs' and self.hasLegs) or (slot=='feet' and self.hasFeet):
                return False
        return True

    def remove_item(self,Item):#This function removes an item from the equipment

        type=Item.type
    #Before the item is removed, update the slot that it occupied to read as empty
        if type=='head':
            self.hasHead=False
        elif type=='shoulder':
            self.hasShoulder=False
        elif type=='chest':
            self.hasChest=False
        elif type=='hands':
            self.hasHands=False
        elif type=='legs':
            self.hasLegs=False
        elif type=='feet':
            self.hasFeet=False
        elif type=='1h':
            self.has1h=False
        elif type=='shield':
            self.hasShield=False
        elif type=='2h':
            self.has2h=False
    #Search through the item list and remove the item from the inventory
        for item in self.items:
            if item==Item:
                self.items.remove(item)
                break

    def add_item(self,Item):#Adds an item to the item list and updates the occupancy of the slot type
        slot=Item.type
        self.items.append(Item)
        if slot=='head':
            self.hasHead=True
        elif slot=='shoulders':
            self.hasShoulder=True
        elif slot=='chest':
            self.hasChest=True
        elif slot=='hands':
            self.hasHands=True
        elif slot=='legs':
            self.hasLegs=True
        elif slot=='feet':
            self.hasFeet=True
        elif slot=='1h':
            self.has1h=True
        elif slot=='shield':
            self.hasShield=True
        elif slot=='2h':
            self.has2h=True
