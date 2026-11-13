"""#Beggining

message = "Hello Python World"
print(message)

message = "Hello World Of Python Crash course"
print(message)
print("hope everyone is doing great")
print("And to be told we are all good thanks")

# strings

#name = "shanny rosine"
##making name to start wit capital letters & lower letters
#print(name.title())
#print(name.lower())

name = "Eic"
message = f"Hello {name}, do you want to learn some python?"
print(message )



#Using Variales in Strings

first_name = "Shanny"
last_name = "Rosine"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello {full_name.title()}!")

message = f"Hello {full_name.title()}!"
print(message)

# adding white spaces(\t) and moving to a new line(\n)

print("Languages: \n\tJavaScript \n\tC++ \n\tPython")

# striping white spaces from right using (rstrip) and from the left side using (lstrip)

favourite_language = "Python "
#print(favourite_language)
print(favourite_language.rstrip())

country =  " Cameroon"
#print(country)
print(country.lstrip())

#exercise

persons_name = "khan nevis"
print(persons_name.title())
print(persons_name.upper())
print(persons_name.lower())

quot = 'Albert Einstein once said "A person who never made a mistake, never tried something new."'
print(quot)

famous_person = f"Isac Newton"
his_message = f"first law of motion states 'A body will reamian at rest until an extenal force acts on it.' this law was stated by {famous_person} the great physicist"
print(his_message)

#Numbers

x, y, z = 2, 4, 16
sum = y + y
print(sum)
product = x * y
print(product)
division = z / x
print(division)   #answer will still be a float take note
print(5+3)

favorite_number = f"20"
my_message = f"My favourie number is {favorite_number} :)"
print(my_message)

#comments

#The Zen of Python
import this #Rules to follow and apply when writing our code
"""
"""
#LISTS (Allows you to store information in one place)

brands = ['BMW', 'GLE', 'Toyota', 'Dodge', 'Tesla']
print(brands)

#accessing elements (by position or index, which always starts from 0 )
print(brands[0]) #BMW
print(brands[3]) #Dodge
#Negative numbers can also be used to access elements in a list from the last(beginning form -1). EG
print(brands[-1]) #Tesla
print(brands[-2]) #Dodge

#using individual values from a list
message = f"My second car was a flying {brands[-1]}" #My second car was a flying Tesla
print(message)

#Exercise

names = ["Nevis", "Khan", "Faith", "Wisdom", "Rosynie"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

print(f"Hello {names[0]}! How are you doing?")
print(f"Hello {names[1]}! How are you doing?")
print(f"Hello {names[2]}! How are you doing?")
print(f"Hello {names[3]}! How are you doing?")
print(f"Hello {names[4]}! How are you doing?")

#Changing, Adding and Removing elements
motorcycles = ['Honda', 'yamaha', 'suzuki', 'Ellisam', 'Nanfang']
print(motorcycles)

#changing
motorcycles[2] = 'Lfancy'
print(motorcycles)

#adding
motorcycles.append('KEKE')
motorcycles.append('Short Gun') 
print(motorcycles)

#inserting
motorcycles.insert(0, 'High Jack') #exact position and item
print(motorcycles)

#removing(deleting)
#1) using the del method (which after item is removed, it can not be used again)
del motorcycles[0]
print(motorcycles)

#2) using the pop method (which after item is removed, it can be used after) (removes just the last item or element)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"the last motorcycle i owned was {last_owned.title()}")

#popping by position
first_owned = motorcycles.pop(0)
print(f"The first car i owned was a {first_owned.title()}")


#exercise under lists

guest = ['Fabiola', 'Rosynie', 'Bright']
first_guest = guest[0]
print(f"We Highly invite you {first_guest} to our dinner to night")
second_guest = guest[1]
print(f"We Highly invite you {second_guest} to our dinner to night")
third_guest = guest[2]
print(f"We Highly invite you {third_guest} to our dinner to night")

print(f"{second_guest} is not able to attend the dinner")

guest[1] = 'Rosine'
print(f"We Highly invite you {first_guest} to our dinner to night")
second_guest = guest[1]
print(f"We Highly invite you {second_guest} to our dinner to night")
third_guest = guest[2]
print(f"We Highly invite you {third_guest} to our dinner to night")

print("Hello guys i just found a bigger table!")

guest.insert(0, 'Fabiola')
guest.insert(2, 'Nevis')
guest.append('Angelo')
print(guest)

#...........

print(f"We Highly invite you {first_guest} to our dinner to night")
print(f"We Highly invite you {second_guest} to our dinner to night")
print(f"We Highly invite you {third_guest} to our dinner to night")
print(f"We Highly invite you {guest[0]} to our dinner to night")
print(f"We Highly invite you {guest[2]} to our dinner to night")
print(f"We Highly invite you {guest[-1]} to our dinner to night")

print(f"im inviting {len(guest)} friends for the dinner") 

print("Oh sory guys the dinner will be delaid and i can invite just 2 people :(")

guest.pop(0)
guest.pop(1)
guest.pop(2)
guest.pop(3)

print(guest)

 

 #AVOIDING INDEX ERRORS WHEN WORKING WITH LIST

"""


#WORKING WITH LISTS USING LOOPS
"""
magicians = ['Nevis', 'Khan', 'Paul', 'Jack', 'Peter']

for magician in magicians:
    #print(magician)
    print(f"{magician.title()}, that was a great trick")
    print(f"I can't wait to see your next trick {magician.title()}")
#Stoping the loop
print("Thank you every one that was a great magic show!")

#Making Numerical Lists
#1) Using range()
for number in range(1, 5):
    print(number)

#using range() to make a list of numbers
numbers = list(range(1, 6))
print(numbers)

#using range to skip numbers in a range
even_numbers = list(range(2, 11, 2))
print(even_numbers)


""
squares = [] #first we create our empty list
for values in range(1, 11):  #next we loop though our given number of range
    square = values ** 2 #we square each value from the range
    squares.append(square) #Then we add te square numbers to the empty list we created
print(squares) #and lastly we print tfe list :)
""

#list comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)

# working with part of a list
# slicing a list
players = ['Ronaldo', 'Mbape', 'Neymah', 'Olise', 'Foden', 'Bruno']
print(players[0:4])
print(players[:3])
print(players[4:])
print(players[-3:]) #this prints the last three elements on the list

#looping through a slice
for player in players[-3:]:
    print(player)

#looping through a loop
print("Here are the first players in my team")
for player in players[:3]:
    print(player.title())

#copying a list
my_food = ['Garri', 'Rice', 'Beef', 'Pork', 'Pie']
friend_food = my_food[:]

print("My favourite foods are:")
my_food.append('Ice Scream')
print(my_food)

print("My friends favourite foods are:")
friend_food.append('Plum')
print(friend_food)

#TUPLES
my_t = (3, 10, 40 )
print(my_t)

#writing over a tuple
#assigning new values to a variable that exist as a tuple
dimensions = (500, 20)
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)

#STYLING MY CODE
"""

"""
# IF STATEMENTS

cars = ['tesla', 'bmw', 'audi', 'toyota', 'benz']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#Ignoring case when cheching conditions
car_brand = 'Tesla'
if car_brand == 'tesla':
    print(car_brand)
else:
    print("Check the brand well!")

#checking multiple conditions with the use of (and) and (or)
#AND
age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 >=21:   #both conditions must be true for it to be true
    print("True")
else:
    print("False")

#OR
age_0 = 22
age_1 = 18
if age_0 >= 21 or age_1 >=21:   #only one condition must be true for it to be true
    print("True")
else:
    print("False")

#checking if a value  is (in) or (not in) a lists
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user in banned_users:
    print("Invalid User, you have been banned!")
else:
    print(f"{user}, you can proceed")


#DICTIONARIES {}
#Acollection of key-value pairs

alien_0 = {'color' : 'green', 'point' : 5} 
print(alien_0)
print(alien_0['color'].title())
print(alien_0['point'])

#accessing iether the color or the point of the alien
new_point = alien_0['point']
print(f"you just earned {new_point} points")

#adding a key-value pair in a dictonary
alien_0['x-position'] =  0
alien_0['y-position'] = 25
print(alien_0)

#Starting with an empty dictionary
alien_0 = {}
alien_0['color'] = 'yellow'
alien_0['points'] = 5
print(alien_0)
print(f"the alien color is {alien_0['color'].title()}")
#Modifying values in a dictionary
alien_0['color'] = 'blue'
print(f"the new color is {alien_0['color'].title()}")

#mor examples

alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print(f"Original position: {alien_0['x_position']}")

#moving the alien to the right
#determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else: 
    #this must be a fast alien
    x_increment = 3

#now position is the old position + the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

#deleting a key value using the del statement
alien_0 = {'color' : 'Green', 'points' : 5}
print(alien_0)
del alien_0['points']
print(alien_0)

#dictionary of similar objects
favourite_languages = {
    'norbet' : 'R',
    'khan' : 'python',
    'faith' : 'c',
    'sarah' : 'rubby'
}
print(favourite_languages)

#using a dictionary
favourite = favourite_languages['khan'].title()
print(f"The favourite language of Khan is {favourite}")

#using get() to access a value
alien_0 = {'color' : 'brown', 'speed' : 'fast'}
point_value = alien_0.get('point', 'No points exist')
print(point_value)

favourite_languages = {
    'nevis' : 'python',
    'norbet' : 'xbet',
    'mba' : 'woman',
    'faith' : 'game'
}
print("\tNAMES:")
for name in favourite_languages.keys():
    print(name.title())
print("\tLANGUAGE:")
for language in favourite_languages.values():
    print(language.title())
for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}")

friends = ['angela', 'angelo', 'nevis', 'averson']

for name in favourite_languages.keys():
    print(f"Hi {name}")
    if name in friends:
         language = favourite_languages[name].title()
         print(f"{name.title()}, your favourite language is {language}")
if 'erin' not in favourite_languages.keys():
    print("Erin pleace take our poll")



#NESTING

#A list of dictionaries
alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'yellow', 'points' : 10}
alien_2 = {'color' : 'red', 'points' : 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

#making a many aliens without writing different dictionaries using range()
#making an empty list to store the aliens
aliens = []

#creating 30 aliens
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print(f"The number of aliens: {len(aliens)}")

#modifying each aliens using the for loop and if statment
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    #expanding the loop
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[:5]:
    print(alien)
"""
#Chapter_7