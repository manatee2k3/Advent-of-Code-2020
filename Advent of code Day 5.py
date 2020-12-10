

with open('Boarding Passes Aoc Day 5.txt') as f:
    data = f.read()
boarding_passes = []
# Importing the boarding passes

for line in data.splitlines():
    boarding_passes.append((line))
# formatting the boarding passes into a list of strings. 


def row_finder (boarding_pass, front, back): # Definition to look through the boarding pass and find the seat
    if boarding_pass[0] == 'F':
    # Looks at index 1 on the string.
        front = front
        back = (back - front) /2 + front
    # If loop will look for 'F', if it finds it it leaves the FRONT the same as before
    # and cuts down the BACK by the difference between the front and back, divided by 2 and added to the front number.
 
    else:
        front = (back - front) /2 + front
        back = back
    # If loop finds a 'B', it cuts down the FRONT by the difference between the front and back, divided by 2 and added to the front number. 
    # It also leaves the BACK the same as before.

    
    if boarding_pass[1] == 'F':
        front = front
        back = (back - front) /2 + front
 
    else:
        front = (back - front) /2 + front 
        back = back
    # Same as above but for index 2


    if boarding_pass[2] == 'F':
        front = front
        back = (back - front) /2 + front 
    else:
        front = (back - front) /2 + front 
        back = back
    # Same as above but for index 2

    
    if boarding_pass[3] == 'F':
        front = front
        back = (back - front) /2 + front
    else:
        front = (back - front) /2 + front 
        back = back
    # Same as above but for index 3

    
    if boarding_pass[4] == 'F':
        front = front
        back = (back - front) /2 + front 
    else:
        front =(back - front) /2 + front 
        back = back
    # Same as above but for index 4

    
    if boarding_pass[5] == 'F':
        front = front
        back = (back - front) /2 + front 
    else:
        front = (back - front) /2 + front 
        back = back
    # Same as above but for index 5

    
    if boarding_pass[6] == 'F':
        front = front
        back = (back - front) /2 + front 
    else:
        front = (back - front) /2 + front 
        back = back
    # Same as above but for index 6

    seats_row.append(int(back))
    # adds seat row to a list before reetting the values and looping to a new string. 

seats_row = []
seats_column = []
# lists ready to be filled with values.

front = 0
back = 127
# Starting values

for boarding_pass in boarding_passes: # Going through each boarding pass in the list of boarding passes 
    row_finder(boarding_pass, front, back) # Activating the 'ROW_FINDER' function
    

for boarding_pass in boarding_passes: # Going through again but only looking at the last 3 indexes for the column 
    left = 0
    right = 7
    if boarding_pass[7] == 'R':
        left = (right - left) /2 + left
        right = right
        if boarding_pass[8] == 'R':
            left = (right - left) /2 + left
            right = right
        else:
            left = left
            right = (right - left) /2 + left

        if boarding_pass[9] == 'R':
            left = (right - left) /2 + left
            right = right
        else:
            left = left
            right = (right - left) /2 + left

    
    else:
        left = left
        right = (right - left) /2 + left
        if boarding_pass[8] == 'R':
            left = (right - left) /2 + left
            right = right
        else:
            left = left
            right = (right - left) /2 + left

        if boarding_pass[9] == 'R':
            left = (right - left) /2 + left
            right = right
        else:
            left = left
            right = (right - left) /2 + left

    
    seats_column.append(int(right))
    # adds seat column to a list before reetting the values and looping to a new string. 



seat_ID = []
# list ready to be filled with values.
x = 0
# starting value for index number.
while x < 867: # making a loop using x as the loop and the index 
    seat = (seats_row[x] * 8) + seats_column[x]
    # formula to find the seat ID
    seat_ID.append(seat)
    # adding value into new seat_ID list.
    x += 1
    # increasing x by 1 to go to the nexr string in each list
    
seat_ID.sort() # sorting the list to find the largest number.
print(seat_ID)


###   PART 2     ###

#now you need to find the empty seat. the plane is full so shoudnt be difficult. 

for i in range(len(seat_ID)): # looping a list the length of the seat_ID list
    if seat_ID[i] + 1 != seat_ID[i+1]: # if the seat id matches the loop then its ok
        print('Your seat is: ',  seat_ID[i] + 1) # if it dosent match then you have found the missing seat
        break




