# Mariam Raheem
#Unless otherwise noted, try solving these using class content and without searching online

#1
#Modify this code so that when i is 5 it doesn't print anything (including Finished!)
#and instead moves directly onto 6, while leaving it unchanged for other values of i
i = 0
while i < 10:
    if i < 5:
        print('little')
    #   print('Finished!')
    elif i > 5:
        print('big')
    #    print('Finished!')
    i += 1

#2
#Write a for loop that prints this pattern:
#HINT: you can write a for-loop inside of a for-loop

#1
#1 2
#1 2 3
#1 2 3 4

my_list = [1, 2, 3, 4]
for i in my_list:
    for j in range(1, i+1):
        print(j, sep='', end=' ')
    print()
    
#3
start_list = [[2, 3, 4], [6, 8, 9]]
#turn it into [1,    2,   3, 4   ]  
#NOTE:  The spacing is just to show which numbers are converted to which
#HINTS: There are three steps here: mapping, filtering, and flattening the nested lists
#       Try doing this in a for-loop, then try doing it in a list comprehension
#       You may need to check StackOverflow for how to flatten a nested list

# 3.1) Mapping to new list (dividing by 2)
list_mapping = []
for sublist in start_list:
    temp_mapping = [num/2 for num in sublist]
    list_mapping.append(temp_mapping)
print(list_mapping)

# 3.2) Filtering relevant values only
list_filter = []
for sublist in list_mapping:
    temp_filter = [int(num) for num in sublist if num not in [1.5,4.5]]
    list_filter.append(temp_filter)
print(list_filter)

# 3.3a) Flattening using for loop
list_flat_1 = []
for sublist in list_filter:
    for num in sublist:
        list_flat_1.append(num)
print(list_flat_1)

# 3.3b) Flattening using StackOverflow method
list_flat_2 = [
    x
    for y in list_filter
    for x in y
]
print(list_flat_2)


#4
import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime.datetime(1999, 2, 23),
#              'Sarah': datetime.datetime(2001, 9, 1),
#              'Zach': datetime.datetime(2005, 8, 8)}
#HINTS: The datetime library has a function that turns strings of the right format into dates
#       Again, start with a for-loop, but make a dictionary comprehension in the end

# Note: Tried to figure this out using hints from ChatGPT and StackOverflow to split date strings
new_dict = {}
for name in start_dict.keys(): 
    date = start_dict[name]
    proper_name = name.capitalize()
    month, day, year = map(int, date.split('/'))
    new_date = datetime.date(year, month, day)
    new_dict[proper_name] = new_date

print(new_dict)
