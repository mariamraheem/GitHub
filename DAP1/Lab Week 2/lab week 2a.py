# Mariam Raheem

#### fix the following errors!
#### do not use any web-based resources to figure them out

#1
x = 10
y = 20
print(x + y)

#2
my_list = [40, 50, 60, 70, 80, 100, 200, 400]
my_list_len = len(my_list)
print(my_list_len)

#3
my_string = 'hello world'
print(my_string.upper())

#4
z = ['a', 'b', 'c']
z[2] = 'd'
print(z[2])

#5 run all these lines at once. why does the x not display 10, 
#followed by the 200?  Fix it so it does.
x = 10
print(x)
y = 20
print(x * y)

#6
name = 'blue'
color = 'My favorite color is %s, what is yours?' % name
print(color)

#7
name = 'yellow'
color = 'My favorite color is {}, what is yours?'.format(name)
print(color)

#8
name = 'red'
color = f'My favorite color is {name}, what is yours?'
print(color)

#### answer the following questions by adding lines, but without changing the code given

#9 make the entries in this list unique
schools = ['harris', 'booth', 'crown', 'harris', 'harris']
schools[3] = 'law'
schools[4] = 'divinity'
print(schools)

#10 change the 'dog' entry to 'cat'
animals = tuple(['bird', 'horse', 'dog', 'fish'])
animals = tuple(['bird', 'horse', 'cat', 'fish'])

#11 separate the words in this string into entries in a list, with only lower-case
#letters, e.g. ['i', 'love', 'how', ...
my_sent = 'All that snow we had this winter sure was fun!'
my_sent_lower = my_sent.lower()
my_sent_list = my_sent_lower.split()
my_sent_list
