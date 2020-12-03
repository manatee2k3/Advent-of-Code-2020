# Advent of Code #
#----- Day 3 ----- #
# you are now on your way to the airport, however the toboggan is hard to steer
# there is a map of the area showing where there are trees that might be in your way.
# make a function that will calculate how many trees you will collide with.
# the toboggan can only move 3 accross, 1 down.

with open('Tree map AoC Day 3.txt') as f:
    data = f.read()
Map = []
for line in data.splitlines():
    Map.append(str(line))
# Importing the Map and turning it into a list

def toboggan_route(Map,slope): 
    total = 0
    Tree = 0
    
    width = len(Map[0])
    height = len(Map)
    #The width and height of the map will help your code stay within the area. 
    x = 0
    y = 0
    
    while y < height:    #this will only run while the toboggan is in the map
        if Map[y][x%width] == '#':   #this marks the location on the map and asks if thats ontop of a tree 
            Tree = Tree +1  #if it is the Tree counter goes up

        x = x + slope[0]  # a counter will then update the location of the toboggan
        y = y + slope[1]
    
    print(Tree) #printing the final total of trees

# Part 2 #
#trying out the function with other movements 
toboggan_route(Map,slope = (1,1))
toboggan_route(Map,slope = (3,1))
toboggan_route(Map,slope = (5,1))
toboggan_route(Map,slope = (7,1))
toboggan_route(Map,slope = (1,2))


total = 90 * 274 * 82 * 68 * 44 # only way I could see to multiply these. will need to learn this.
print(total)

