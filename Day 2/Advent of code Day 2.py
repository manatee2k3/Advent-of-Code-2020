# Advent of code
#----- Day 2 ----- #

# The tobogan store is having trouble with their password system and need your help
# each line gives the password policy and then the password
# the policy indicates the lowest and highest number of times a given letter must appear
# eg. 1-3 a : abcde
#     the password must contain a at least 1 and at most 3 times
#     abcde is valid as a is there once


import re #importing regular expressions
with open('Passwords AoC Day 2.txt') as f:
    data = f.read()
#importing the data from the AoC page as a .txt file saved on my pc
    
passw = []
for line in data.splitlines():
    passw.append(str(line))
# manipulating data into a string 

f_count_one = 0
f_count_two = 0
#final counts one = part one, two = part two of the questions.

for lst in passw: #creating a function that will go through each password in the list
    number_regex = re.compile(r'\d+')
    lyst = number_regex.findall(lst[0:8])
    min_n = lyst[0] #pullng minimum number into its own variable
    min_n = int(min_n) #making sure the minimum number is formatted as an integer
    max_n = lyst[1] # pulling maximum number into its own variable 
    max_n = int(max_n) #making sure the maximum number is formatted as an integer
# Using Regular expressions to pull out the minimum and maximum numbers from each string
    letter_regex = re.compile(r'[abcdefghijklmnopqrstuvwxyz]')
    let = letter_regex.findall(lst[0:8])
    letter = let[0] #pulling the letter into its own variable
# Using regualr expressions to pull the specific letter we will use

    count = 0 # assuring the count is re-set after each iteration

    for i in lst[7:]: # going though each letter in the password individualy 
        if i == letter: #if the letter is found 
            count = count + 1 #add a counter 
    if count >= int(min_n) and count <= int(max_n):
        #if after going through the password the number of letters found is between the min and max
                f_count_one = f_count_one + 1 #add a count to our final count

    password_regex = re.compile(r'\w+') #using another regular expression to isolate just the password
    passw = password_regex.findall(lst[7:])
    password = passw[0] #pulling password into a variable
    min_n = min_n - 1 #removing a number so they work in the index
    max_n = max_n - 1 #removing a number so they work in the index
    
    if password[min_n] == letter and password[max_n] != letter or password[max_n] == letter and password[min_n] != letter::
        f_count_two = f_count_two + 1

    
print(f_count_one)
print(f_count_two)





