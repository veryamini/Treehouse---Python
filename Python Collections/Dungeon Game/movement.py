#if move_x == -1:
#        x -= 1
 #   elif move_x == 1:
#        x += 1
 #   elif move_y == -1:
#        y -= 1
#    elif move_y == 1:
 #       y += 1

#ROOT
 #ROOT123

 # if move_x < 0 and x == 0 hp decreases
# move_x > 0 and x ==9
#or x == 9 or y == 0 or y == 9
def move(player, direction):
    x, y, hp = player
    move_x, move_y = direction
    print("move_x : {}, move_y : {}".format(move_x, move_y))
    
    if (move_x == -1 and x == 0) or (move_x == 1 and x == 9) :
        hp -= 5
    else:
        x += move_x
    if (move_y == -1 and y == 0) or (move_y == 1 and y == 9):
        hp -= 5
    else:
        y += move_y
    print ("x : {} , y : {}".format(x, y))
    return x, y, hp

print(move((0, 9, 10), (1, 1)))
