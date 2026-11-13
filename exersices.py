#Exercise on looping through a list

"""
#food
favourite_food = ['Rice', 'Achu', 'Eru', 'Equang', 'Kati-kati']
for food in favourite_food:
    print(food)
    print(f"I like {food.title()} so much")
print("I'm a foodie i love food so much.")

#animal
animals = ['Dog', 'Cat', 'Rat']
for animal in animals:
    print(animal)
    print(f"A {animal} will make a creat pet")
print("Any of the above animals will make a greate pet")

#Exersice on making numerical lists
for numbers in range(1, 21):
    print(numbers)

""
one_milion = []
#for values in range(1, 1000001):
    one_milion.append(values)
    print(one_milion)
""

#odd numbers
odd_numbers = []
for numbers in range(1, 10):
    value = 2 * numbers + 1
    odd_numbers.append(value)
print(odd_numbers)

#multiple of three
multiple_of_3 = []
for numbers in range (3, 31, 3):
    multiple_of_3.append(numbers)
print(multiple_of_3)

#cubes
cubes = []
for cube in range(1, 11):
    value = cube ** 3
    cubes.append(value)
print(cubes)

#cube comprehension
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

#Exercise on slicing lists
my_fruits = ['Mango', 'Pear', 'Apple', 'Banana', 'Guava', 'Orange']
print("The first 3 items of the list are: ")
print(my_fruits[0:3])
print("Three items from the middle of the list are: ")
print(my_fruits[2:4])
print("The last 3 items on the list are: ")
print(my_fruits[-3:])
friend_friuts = my_fruits[:]
my_fruits.append("Grapes")
print(my_fruits)
friend_friuts.append("Achu")
print(friend_friuts)


#Exercise on Tuple
food_stuffs = ('Fried Rice', 'Kati Kati', 'Cornchaff', 'Gari and Eru', 'Achu')
print("The menu of today: ")
for food in food_stuffs:
    print(food)
#food_stuffs[0] = "Iris" #type Error
#print (food_stuffs)

#rewriting the tuple
food_stuffs = ('Fried Rice', 'Kati Kati', 'Ndole', 'Pork Meat', 'Achu')
print("Modified Menu: ")
for food in food_stuffs:
    print(food)

"""

#EXERCISES ON IF Statements
car = 'tesla'
print("is car == 'tesla'? maybe")
print(car == 'tesla')

print("is car == 'audi'? sure its False")
print(car == 'audi') 

#testfor equality and inequality
age_0 = 20
age_1 = 12
print(age_0 >=19 and age_1 >= 19) 
print(age_0 >= 19 or age_1 <= 19)

#Test using the lower method
food = 'ACHU'
print(food == 'achu')
print(food.lower() == 'achu')

#Testing whether an item is in a list
menu = ['achu', 'rice', 'corn', 'eru']
favourite_food = 'achu'
if favourite_food not in menu:
    print(f"{favourite_food.title()} is not in that resto dont go there")
else:
    print(f"{favourite_food.title()} is there you can go there")


alien_color = 'green'
if alien_color == 'green':
    print("you just earned 10 points!")

"""
age = int(input("Enter your age: \n"))
if age < 2:
    print("you are still a baby")
elif age == 2 or age < 4:
    print("You are a todler")
elif age == 4 or age < 13:
    print("You are a kid")
elif age == 13 or age < 20:
    print("You are a teenager")
elif age == 20 or age < 65:
    print("you are an adult")
elif age == 65 or age >  65:
    print("You are Old!")
else:
    print("Enter a valid age")
"""

#exercises on dictionaries
#storing information about a person
person = {
    'first_name' : 'khan',
    'last_name' : 'nevis',
    'age' : 22,
    'city' : 'bamenda'
}
print(person)

#storing peoples favourite numbers
favourite_numbers = {
    'khan' : 22,
    'nevis' : 40,
    'faith' : 10,
    'norbet' : 3,
    'collins' : 20
}
print(favourite_numbers)

#printing the favourite number of each persons name
#first person
favourite_1 = favourite_numbers['khan']
print(f"The favourite number of khan is {favourite_1}")
#second person
favourite_2 = favourite_numbers['nevis']
print(f"The favourite number of khan is {favourite_2}")
#third person
favourite_3 = favourite_numbers['faith']
print(f"The favourite number of khan is {favourite_3}")
#forth person 
favourite_4 = favourite_numbers['norbet']
print(f"The favourite number of khan is {favourite_4}")
#fifth person
favourite_5 = favourite_numbers['collins']
print(f"The favourite number of khan is {favourite_5}")

#words and thire meaning
"""glossary = {
    'list' : 'Used to make a list of things/items []',
    'tuple' : 'used to make list of things/items that can not be edited ()',
    'dictionary' : 'Acollection of key-value pairs { }',
    'loops' : 'used to loop through things',
    'if statements' : 'used for conditions',
}
#list
words_meaning = glossary['list']
print(f"List: {words_meaning}")
#tuple
words_meaning = glossary['tuple']
print(f"Tuple: {words_meaning}")
#dictionary
words_meaning = glossary['dictionary']
print(f"Dictionary: {words_meaning}")
#loops
words_meaning = glossary['loops']
print(f"Loops: {words_meaning}")
#if conditions
words_meaning = glossary['if statements']
print(f"If- statements: {words_meaning}")
"""

#exercise 6.4   

glossary_2 = {
    'list' : 'Used to make a list of things/items []',
    'tuple' : 'used to make list of things/items that can not be edited ()',
    'dictionary' : 'Acollection of key-value pairs { }',
    'loops' : 'used to loop through things',
    'if statements' : 'used for conditions',
}
#making the above code clean
for key, value in glossary_2.items():
    print(f"{key}: {value}")

#6.5
rivers = {
    'nile' : 'egypt',
    'wouri' : 'cameroon',
    'khan' : 'nevis',
}
for river, country in rivers.items():
    print(f"The river {river.title()} passes through {country.title()}")
print("the rivers mentioned includes:")
for river in rivers.keys():
    print(river.title())
print("the countries mentioned include:")
for country in rivers.values():
    print(country.title())

#6.6 polling
favourite_languages = {
    'nevis' : 'python',
    'norbet' : 'xbet',
    'mba' : 'woman',
    'faith' : 'game'
    }
people = ['fabiola', 'rosine',   'nevis', 'mba']

for person in people:
    if person in favourite_languages:
        print(f"{person.title()}, your favourite language is  {favourite_languages[person].title()}")
    else:
        print(f"{person.title()}, you need to take a poll!")
