objectlist = speedAdjust(objectlist)

if objectlist[0].current_speed:
 if objectlist[0] == player
  playersTurn()
 else
  monstersTurn()
 objectlist[0].current_speed=objectlist[0].current_speed-1.0
 if objectlist[0].current_speed<0
  objectlist[0].current_speed=0
 objectlist = speedAdjust(objectlist)
else
 for object in objectlist
  object.current_speed=object.speed
 