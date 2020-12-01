# Advent of code
#----- DAY 1 ---- #
# the elves need you to go through your expense report and do some calculations
# you must import the expense report which has been downloaded as a .txt folder then
# find the 2/3 entries that sum up to 2020 and multiply them together.

#---------------------------------------------------------------#
#this first part is a test with a small ammount of data
test = [1721,979,366,299,675,1456] #small expense report

for x in range(len(test)): #making the code go through the list one by one
    for y in range(len(test)): #making the code go through again one by one
        if test[x] + test[y] == 2020: # checking if the singular items in each list search adds to 2020
            print(test[x],test[y]) # if it does we print both numbers.
            
#---------------------------------------------------------------#

## extracting the data from a txt file into a list ##  
data = [int(w) for w in open("Expenses.txt").read().splitlines()]
# Splitlines() removes new lines andthe int makes sure it reads as an integer. 

## find two entries in the expense report that sum 2020 ##
# the code for this is the same as commented on in the test
for a in range (len(data)):
    for b in range (len(data)):
        if data[a] + data[b] == 2020:
            print(data[a], data[b])
            print(data[a] * data[b]) # times both numbers together to get their sum
            
## find 3 entries in the expense report that sum 2020 ##
#this is the same line of code, but with a third line to go through the code a third time
for a in range (len(data)):
    for b in range (len(data)):
        for c in range (len(data)): 
            if data[a] + data[b] + data[c] == 2020: 
                print(data[a], data[b], data [c])
                print(data[a] * data[b] * data[c])
