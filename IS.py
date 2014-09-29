import sys, pygame
from Actor import *

pygame.init()

#print "Enter a player name: ",
#name=raw_input()
#print "Enter your starting health: ",
#health=int(raw_input())
#print "Enter your starting damage: ",
#damage=int(raw_input())
player=Player(0,0,'images/player.png','Brennan',100,10)
database=Item_Database()
database.import_database()
#database.display()
Rarity_Database= [[int for i in range(8)] for j in range(54)]
increment=0
for line in open("LootRarity.csv"):
    Rarity_Database[increment]=line.split(",")
    #print Rarity_Database[increment]
    #number,name,health,damage,image,type = line.split(",")
    increment=increment+1

David = Monster(0,0,'David', 1000, 10, 2,'images/monster.png', Rarity_Database, database)
David.display_stats()
David.loot.display()



player.inventory.add_item(database.items[0])
player.inventory.add_item(database.items[1])
player.inventory.add_item(database.items[2])



while 1:

    print "What would you like to do?"
    print "A.)Add an item B.)Remove an item C.)Move an item from inventory to equipment "
    print "D.)Print inventory E.) Print equipment F.) See player stats "
    decision=raw_input()
    if decision=="A":
        print "Enter a name for the item:",
        name=raw_input()
        print "Enter the item's damage: ",
        damage=int(raw_input())
        print "Enter the item's health: ",
        health=int(raw_input())
        print "Enter type of weapon: ",
        type=raw_input()
        player.inventory.add_item(Item(player.inventory.numberOfItems+1,name,health,damage,'temp2.png',type))
    elif decision=="B":
        print "Enter a number of an item to remove it:",
        number=int(raw_input())
        player.inventory.remove_item(player.inventory.items[number])
    elif decision=="C":
        print"Which of the following items would you like to equip?"
        player.inventory.display()
        print "------------------"
        print ">",
        itemNumber=int(raw_input())
        player.equip_item(player.inventory.items[itemNumber])
    elif decision=="D":
        print "Inventory:"
        print "------------------"
        player.inventory.display()
        print "------------------"
    elif decision=="E":
        print "Equipment:"
        print "------------------"
        player.equipment.display()
        print "------------------"
    elif decision=="F":
        player.display_stats()
        print "------------------"
    else:
        print "Invalid selection"