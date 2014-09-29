#For the duration of the game
while True:
#Initialize objectlist array in speed order
    objectlist = speedAdjust(objectlist)
    #While the first object in the objectlist has a speed greater than 0, commence turn of object.
    #Decrement the object's current speed by 1 and then resort the list
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
    #If the first object has a speed of 0, reassign adjusted object speeds to initial object speed
        for object in objectlist
            object.current_speed=object.speed
