# Advent of Code #
#----- Day 4 ----- #

import re
raw_batch_file = [] #Batch file - still split

with open ("Passports AoC Day 4.txt") as f:
    data = f.read()
for line in data.splitlines():
    raw_batch_file.append(str(line))
   
raw_batch_file.append('')
passports = []
x = 0
for i in range(len(raw_batch_file)):
    if raw_batch_file[i] == '':
        data = ' '.join(raw_batch_file[x:i]) 
        passports.append(data)
        x = i + 1
        
passports.append(raw_batch_file[-1])
# combining the lists so all passport fields are together. 


## PART 1 ##
valid = 0
for j in passports:
    f_regex = re.compile(r'byr|iyr|eyr|hgt|hcl|ecl|pid')
    fields = f_regex.findall(j)                                                                  
    if len(fields) == 7:
        valid = valid + 1
# searching each passport for the valid fields
#if the field total counts to 7 it increases the number of valid passports by 1
print(valid)


## PART 2 ##

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

valid_two = 0 
keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'hcl', 'ecl', 'pid']

for line in passports: # seperating each passport from the whole list
    if all(key + ':' in line for key in keys): 
        passport_two = {k:v for part in line.split(' ') for k,v in [part.split(':')] }
        # seperaying and making each passport a dictionary with the tital being the key and the value as the value
        if (
            int(passport_two['byr']) >= 1920 and int(passport_two['byr']) <= 2002 and # validating the birth year
            int(passport_two['iyr']) >= 2010 and int(passport_two['iyr']) <= 2020 and # validating the issue yeat
            int(passport_two['eyr']) >= 2020 and int(passport_two['eyr']) <= 2030 and # validating the expiration year
            re.match('^(1([5-8][0-9]|9[0-3])cm|(59|[6][0-9]|[7][0-6])in)$', passport_two['hgt']) and # validating the height 
            re.match('#[0-9a-f]{6}', passport_two['hcl']) and # validating the hair colour
            re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', passport_two['ecl']) and # validating eye colour
            re.match('^\d{9}$', passport_two['pid']) # validating passport ID 
        ):
            
            valid_two += 1
            #if all the above passport infomation is valid, the counter will go up by one


print(valid_two)

