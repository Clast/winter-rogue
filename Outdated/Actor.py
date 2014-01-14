from Item_Database import *


class Actor:

 def __init__(self, name, health, attackdamage):
  self.name=name
  self.base_health=health
  self.base_damage=attackdamage

 def get_name(self):
  return self.name
  
 def get_health(self):
  return self.total_health
  
 def get_damage(self):
  return self.total_damage
  
class Player(Actor):
 def __init__(self, name, health, attackdamage):
  self.name=name
  self.base_health=health
  self.base_damage=attackdamage
  self.equipment=Equipment()
  self.inventory=Inventory()
  self.bonus_health=0
  self.bonus_damage=0
  
 def equip_item(self, Item):
  if self.equipment.check_slot(Item):
   self.equipment.add_item(Item)
   self.inventory.remove_item(Item)
  else:
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
      
   
 
 def update_stats(self):
  self.bonus_health=0
  self.bonus_damage=0
  for item in self.equipment.items:
   self.bonus_health=self.bonus_health+item.health
   self.bonus_damage=self.bonus_damage+item.damage
  self.total_health=self.bonus_health+self.base_health
  self.total_damage=self.bonus_damage+self.base_damage
  
 def display_stats(self):
  self.update_stats()
  print "Player Stats: "
  print "Total health: %d" % self.total_health
  print "Total damage: %d" % self.total_damage
 
class Monster(Actor):
 
 def __init__(self, name, health, attackdamage, level)
  self.name=name
  self.base_health=health
  self.base_damage=attackdamage
  self.loot=Loot()
