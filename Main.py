#COMMIT DAMN YOU
import pygame, sys, random
from pygame.locals import *
from Tile import *
from Dungeon import *
from Actor import *
from Menu import *
from Log import *
from LevelHandler import *

#Database importing for Item_Database and Rarity Database
database=Item_Database()
database.import_database()
Rarity_Database= [[int for i in range(8)] for j in range(54)]
increment=0
for line in open("LootRarity.csv"):
    Rarity_Database[increment]=line.split(",")
    increment=increment+1



#Set the width and height of the board. For pixel size, multiply each variable by 32.
boardWidth = 32
boardHeight = 25
dungeonLevel = 0

#Set Colors - Colors in pyGame are in RGB format. This is out of convenience.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Here we initialize the pygame surface and create the Displaysurface which will hold our main screen, passing along the board size variables*32 for actual pixel size.
pygame.init()
DISPLAYSURF = pygame.display.set_mode((boardWidth*32,boardHeight*32+160), 0, 32)
pygame.display.set_caption('Dev') #Window Title
DISPLAYSURF.fill(WHITE) #Fill the screen area with white.

#Create LevelHandler to keep track of dungeons and current floor
levelhandler = LevelHandler()
#Create new dungeon with the width and height specified.
dungeon = Dungeon(boardWidth, boardHeight)



#All elements in the object list will be printed when drawObjects are called.
#dungeon.objectlist = []
#Code to generate a monster a random location
dungeon.room_Generation(boardWidth,boardHeight)


#Append some items to the dungeon.objectlist
healer= NPC(64,0,200,1,'healer', Rarity_Database, database)
shopkeeper= NPC(0,64,200,1,'shopkeeper', Rarity_Database, database)
player = Player(32,32,'images/player.png',"Name",5000,50)
dungeon.objectlist.append(player)
dungeon.objectlist.append(healer)
dungeon.objectlist.append(shopkeeper)
dungeon.spawn_Monsters(boardWidth,boardHeight,Rarity_Database,database,dungeon.objectlist)

#Append the map to the LevelHandler and set it as the current level
levelhandler.dungeonlist.append(dungeon)
levelhandler.move_floor(1)

newdungeon = Dungeon(boardWidth,boardHeight)
newdungeon.testing_Generation(boardWidth,boardHeight)
newdungeon.testing_Monsters(boardWidth,boardHeight,Rarity_Database,database,newdungeon.objectlist)
#Append the map to the LevelHandler
levelhandler.dungeonlist.append(newdungeon)


stats=StatsMenu(player)
#global log
#log = Log()
#Function to draw the map to the board.
def drawMap(boardWidth, boardHeight):

    for y in xrange(boardHeight):
        for x in xrange(boardWidth):
            DISPLAYSURF.blit(levelhandler.dungeonlist[levelhandler.currentlevel].map[x][y].Img, (levelhandler.dungeonlist[levelhandler.currentlevel].map[x][y].xcoordinate,levelhandler.dungeonlist[levelhandler.currentlevel].map[x][y].ycoordinate)) #Surface.Blit takes an image and a coordinate and then draws to that location.

    #Function to draw the objects to the board
def drawObjects():
    for object in levelhandler.dungeonlist[levelhandler.currentlevel].objectlist:
        DISPLAYSURF.blit(object.Img, (object.xcoordinate, object.ycoordinate))

def redrawScreen():
    drawMap(boardWidth, boardHeight)
    drawObjects()
    redrawStats() #Updates the current player stats at the end of each turn
    redrawLog() #Updates the log after each player turn
    pygame.display.update()


def playersTurn(): #Pauses the game and allows the player to take a turn
    playersturn = True
    while playersturn == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if (event.key == K_o):
                    levelhandler.move_floor(-1)
                    levelhandler.dungeonlist[levelhandler.currentlevel].objectlist.append(player)
                    redrawScreen()

                if (event.key == K_p):
                    levelhandler.move_floor(1)
                    levelhandler.dungeonlist[levelhandler.currentlevel].objectlist.append(player)
                    redrawScreen()
                if (event.key == K_d):
                    player.move(32,0,levelhandler.dungeonlist[levelhandler.currentlevel].map,levelhandler.dungeonlist[levelhandler.currentlevel].objectlist) #Modify the game state when some action is entered. The move function takes target coordinates, the map[] list of a Dungeon object (see Dungeon.py), and the object list.
                    playersturn = False
                if (event.key == K_a):
                    player.move(-32,0,levelhandler.dungeonlist[levelhandler.currentlevel].map,levelhandler.dungeonlist[levelhandler.currentlevel].objectlist)
                    playersturn = False
                if (event.key == K_w):
                    player.move(0,-32,levelhandler.dungeonlist[levelhandler.currentlevel].map,levelhandler.dungeonlist[levelhandler.currentlevel].objectlist)
                    playersturn = False
                if (event.key == K_s):
                    player.move(0,32,levelhandler.dungeonlist[levelhandler.currentlevel].map,levelhandler.dungeonlist[levelhandler.currentlevel].objectlist)
                    playersturn = False
                if (event.key == K_h):
                    print ('Some Bullshit')




                if (event.key == K_i): #inventory
                    paused = 1
                    while (paused == 1):
                        drawMap(boardWidth, boardHeight)
                        drawObjects()
                        boolean = False
                        invmenu=player.inventorymenu
                        invmenu.Update()
                        invscreen=player.inventorysheet
                        DISPLAYSURF.blit(invscreen, (invmenu.xloc,invmenu.yloc ))
                        pygame.display.update()

                        for event in pygame.event.get():
                            if event.type==MOUSEBUTTONDOWN and event.button == 1 :
                                cursx,cursy=event.pos
                                if cursx>invmenu.xloc and cursx<invmenu.xloc+200 and cursy >invmenu.yloc and cursy < invmenu.yloc+10:
                                    boolean=True
                                while(boolean):
                                    for event in pygame.event.get():
                                        if event.type==MOUSEBUTTONUP and event.button == 1 :
                                            boolean=False
                                            relx, rely = event.pos
                                            invmenu.xloc=invmenu.xloc+(relx-cursx)
                                            invmenu.yloc=invmenu.yloc+(rely-cursy)
                            elif event.type==MOUSEBUTTONDOWN and event.button == 3:
                                cursx,cursy=event.pos
                                if(cursx>invmenu.xloc+10 and cursx<invmenu.xloc+42 and cursy>invmenu.yloc+20 and cursy<invmenu.yloc+52):
                                    player.equip_item(0)
                                if(cursx>invmenu.xloc+60 and cursx<invmenu.xloc+92 and cursy>invmenu.yloc+20 and cursy<invmenu.yloc+52):
                                    player.equip_item(1)
                                if(cursx>invmenu.xloc+110 and cursx<invmenu.xloc+142 and cursy>invmenu.yloc+20 and cursy<invmenu.yloc+52):
                                    player.equip_item(2)
                                if(cursx>invmenu.xloc+10 and cursx<invmenu.xloc+42 and cursy>invmenu.yloc+60 and cursy<invmenu.yloc+92):
                                    player.equip_item(3)
                                if(cursx>invmenu.xloc+60 and cursx<invmenu.xloc+92 and cursy>invmenu.yloc+60 and cursy<invmenu.yloc+92):
                                    player.equip_item(4)
                                if(cursx>invmenu.xloc+110 and cursx<invmenu.xloc+142 and cursy>invmenu.yloc+60 and cursy<invmenu.yloc+92):
                                    player.equip_item(5)

                            if event.type == KEYDOWN:
                                if event.key == K_p:
                                    redrawScreen()
                                    paused = 0

                if (event.key == K_e): #equipment
                    paused = 1
                    while (paused == 1):
                        drawMap(boardWidth, boardHeight)
                        drawObjects()
                        equipmenu=player.charactermenu
                        equipscreen=player.charactersheet
                        print player.charactermenu.xloc,player.charactermenu.yloc
                        DISPLAYSURF.blit(equipscreen, (player.charactermenu.xloc,player.charactermenu.yloc))
                        pygame.display.update()

                        for event in pygame.event.get():
                            if event.type==MOUSEBUTTONDOWN and event.button == 1 :
                                cursx,cursy=event.pos
                                if cursx>player.charactermenu.xloc and cursx<player.charactermenu.xloc+200 and cursy >player.charactermenu.yloc and cursy < player.charactermenu.yloc+10:
                                    boolean=True
                                    while(boolean):
                                        for event in pygame.event.get():
                                            if event.type==MOUSEBUTTONUP and event.button == 1 :
                                                boolean=False
                                                relx, rely = event.pos
                                                player.charactermenu.xloc=player.charactermenu.xloc+(relx-cursx)
                                                player.charactermenu.yloc=player.charactermenu.yloc+(rely-cursy)
                            elif event.type==MOUSEBUTTONDOWN and event.button == 3:
                                cursx,cursy=event.pos
                                if(cursx>player.charactermenu.xloc+10 and cursx<player.charactermenu.xloc+42 and cursy>player.charactermenu.yloc+10 and cursy<player.charactermenu.yloc+42 and player.equipment.check_slot('head') == False):
                                    index = 0
                                    for item in player.equipment.items:
                                        if item.type=='head':
                                            break
                                        else:
                                            index=index+1
                                    player.unequip_item(index)

                                if(cursx>player.charactermenu.xloc+150 and cursx<player.charactermenu.xloc+182 and cursy>player.charactermenu.yloc+10 and cursy<player.charactermenu.yloc+42 and player.equipment.check_slot('shoulders') == False):
                                    index = 0
                                    for item in player.equipment.items:
                                        if item.type=='shoulders':
                                            break
                                        else:
                                            index=index+1
                                    player.unequip_item(index)

                                if(cursx>player.charactermenu.xloc+10 and cursx<player.charactermenu.xloc+42 and cursy>player.charactermenu.yloc+60 and cursy<player.charactermenu.yloc+92 and player.equipment.check_slot('chest') == False):
                                    index = 0
                                    for item in player.equipment.items:
                                        if item.type=='chest':
                                            break
                                        else:
                                            index=index+1
                                    player.unequip_item(index)

                                if(cursx>player.charactermenu.xloc+150 and cursx<player.charactermenu.xloc+182 and cursy>player.charactermenu.yloc+60 and cursy<player.charactermenu.yloc+92 and player.equipment.check_slot('hands') == False):
                                    index = 0
                                    for item in player.equipment.items:
                                        if item.type=='hands':
                                            break
                                        else:
                                            index=index+1
                                    player.unequip_item(index)

                                if(cursx>player.charactermenu.xloc+10 and cursx<player.charactermenu.xloc+42 and cursy>player.charactermenu.yloc+110 and cursy<player.charactermenu.yloc+142 and player.equipment.check_slot('legs') == False):
                                    index = 0
                                    for item in player.equipment.items:
                                        if item.type=='legs':
                                            break
                                        else:
                                            index=index+1
                                    player.unequip_item(index)

                                if(cursx>player.charactermenu.xloc+150 and cursx<player.charactermenu.xloc+182 and cursy>player.charactermenu.yloc+110 and cursy<player.charactermenu.yloc+142 and player.equipment.check_slot('feet') == False):
                                    index = 0
                                    for item in player.equipment.items:
                                        if item.type=='feet':
                                            break
                                        else:
                                            index=index+1
                                    player.unequip_item(index)

                                if(cursx>player.charactermenu.xloc+10 and cursx<player.charactermenu.xloc+42 and cursy>player.charactermenu.yloc+160 and cursy<player.charactermenu.yloc+192 and (player.equipment.check_slot('1h') == False or player.equipment.check_slot('2h') == False)):
                                    index = 0
                                    for item in player.equipment.items:
                                        if item.type=='1h' or item.type=='2h':
                                            break
                                        else:
                                            index=index+1
                                    player.unequip_item(index)

                                if(cursx>player.charactermenu.xloc+150 and cursx<player.charactermenu.xloc+182 and cursy>player.charactermenu.yloc+160 and cursy<player.charactermenu.yloc+192 and player.equipment.check_slot('shield') == False):
                                    index = 0
                                    for item in player.equipment.items:
                                        if item.type=='shield':
                                            break
                                        else:
                                            index=index+1
                                    player.unequip_item(index)
                            if event.type == KEYDOWN:
                                if event.key == K_p:
                                    redrawScreen()
                                    paused = 0

def speedAdjust(objectlist):
    objectlist = sorted(levelhandler.dungeonlist[levelhandler.currentlevel].objectlist, key=lambda object:object.speed, reverse = True)
    return objectlist

def redrawStats():
    stats.Update(player)
    DISPLAYSURF.blit(stats.menusurface, (stats.xcoord, stats.ycoord))

def redrawLog():
    DISPLAYSURF.blit(log.menusurface, (log.xcoord, log.ycoord))

#The game structure is as follows:
#1) Draw the map and allow the player to take his first turn.
#2) After the player takes his first turn, enter the game loop.
                #3a) Re order the list of actors depending on speed. Higher speed = earlier turn order
                #3b) Iterate through the list of actors, allowing each to take his respective turn.
                #3c) When you get to the player, pause the game and allow him to take his turn.
                #3d) After everyone has taken their turns, refresh the screen with the new game state.

levelhandler.dungeonlist[levelhandler.currentlevel].objectlist = speedAdjust(levelhandler.dungeonlist[levelhandler.currentlevel].objectlist) #Adjust the objects according to speed
redrawScreen() #First draw the screen
redrawLog() #Updates the log after each player turn
playersTurn() #Player ALWAYS gets first turn. This is to avoid a monster attacking you when you enter the level before you have a chance to respond or receiving an attack before the screen is drawn.
redrawScreen() #Update the screen after the player takes the first turn, and then begin game loop.
redrawLog() #Updates the log after each player turn

while True:

    levelhandler.dungeonlist[levelhandler.currentlevel].objectlist = speedAdjust(levelhandler.dungeonlist[levelhandler.currentlevel].objectlist)

    for object in levelhandler.dungeonlist[levelhandler.currentlevel].objectlist:
        if object == player:
            playersTurn()
            redrawStats() #Updates the current player stats at the end of each turn
            redrawLog() #Updates the log after each player turn
        else:
            pass
            print(object.name + " growls") #Here, the monster will take their turn



    redrawScreen()
    redrawStats() #Updates the current player stats at the end of each turn
    redrawLog() #Updates the log after each player turn