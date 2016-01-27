# winter-rogue

Developed as a hobby project over the winter break 2015 with a friend (Brennan Settles), Winter-Rogue is a 2D rogue-like. It's a fairly complete rogue-like framework that would be well suited to development of tile based RPGs or other rogue-likes for those willing to add to the Monster AI.
 
It's coded in Python and uses the Pygame library for graphics and mouse support. 

It features:

-Random map generation
-Random monster generation (with monsters having different graphics and dropping rarer loot with higher levels)
-A turn based combat system
-A level handler with support for persistent dungeons and multiple levels (only one level currently programmed in when run)
-Character stats such as HP, Attack, Level, and Gold
-A graphical inventory and equip system with mouse support
-54 different items over 8 equipment slots (and an item database where items can be easily added without touching code)
-Combat log showing damage taken, given, and loot received.
-Healer and Merchant NPCs


Coded but not implemented:

-A turn based system based on Monster speed (SpeedAlgorithm.py)
-State machines for monster AI (StateMachine.py), including  functions such as Line of Sight, and movement.


